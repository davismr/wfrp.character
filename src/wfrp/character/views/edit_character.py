import uuid

import colander
import deform
from pyramid.httpexceptions import HTTPFound
from pyramid.httpexceptions import HTTPUnauthorized
from pyramid.security import forget
from pyramid.view import view_config
from pyramid.view import view_defaults
from sqlalchemy.exc import NoResultFound

from wfrp.character.data.careers.careers import ALL_CAREER_DATA
from wfrp.character.data.careers.careers import ALL_CAREER_DATA_WITH_SEAFARER
from wfrp.character.data.careers.careers import CAREER_BY_CLASS
from wfrp.character.data.careers.careers import CAREER_BY_CLASS_WITH_SEAFARER
from wfrp.character.data.expansions import EXPANSIONS
from wfrp.character.data.magic.chanty import CHANTY_DATA
from wfrp.character.data.magic.miracles import get_miracles
from wfrp.character.data.magic.petty import PETTY_MAGIC_DATA
from wfrp.character.data.magic.spells import get_arcane_spells
from wfrp.character.data.magic.spells import get_colour_spells
from wfrp.character.data.skills import SKILL_DATA
from wfrp.character.data.species import SPECIES_LIST
from wfrp.character.data.talents import TALENT_DATA
from wfrp.character.models.character import Character
from wfrp.character.models.user import User
from wfrp.character.views.base_view import BaseView
from wfrp.character.views.create_character.attributes import ATTRIBUTES


@view_defaults(route_name="new-manual-character", permission="edit_character")
class CharacterManualViews:
    def __init__(self, request):
        self.request = request
        if self.request.registry.settings.get("wfrp.character.enable_auth"):
            try:
                self.logged_in = request.session["googleauth.userid"]
            except KeyError:
                raise HTTPUnauthorized

    @view_config(request_method="GET")
    def get_view(self):
        new_id = uuid.uuid4()
        character = Character(id=new_id)
        if self.request.registry.settings.get("wfrp.character.enable_auth"):
            try:
                character.user_id = (
                    self.request.dbsession.query(User)
                    .filter(User.email == self.logged_in)
                    .one()
                    .id
                )
            except NoResultFound:
                forget(self.request)
                raise HTTPUnauthorized
        character.status = "complete"
        self.request.dbsession.add(character)
        url = self.request.route_url("character-edit", id=new_id)
        return HTTPFound(location=url)


@view_defaults(route_name="character-edit", permission="edit_character")
class CharacterEditViews(BaseView):

    def expansions_schema(self):
        schema = colander.SchemaNode(
            colander.Mapping(),
            title=f"Edit Expansions for {self.character.get_display_title()}",
        )
        expansions_schema = colander.SchemaNode(
            colander.Mapping(),
            name="expansions",
        )
        choices = [
            (expansion[0], expansion[1]["title"]) for expansion in EXPANSIONS.items()
        ]
        expansions_schema.add(
            colander.SchemaNode(
                colander.Set(),
                name="expansions",
                widget=deform.widget.CheckboxChoiceWidget(values=choices),
                default=self.character.expansions,
            )
        )
        schema.add(expansions_schema)
        return schema

    def character_schema(self):
        schema = colander.SchemaNode(
            colander.Mapping(),
            title=f"Edit {self.character.get_display_title()}",
        )
        character_schema = colander.SchemaNode(
            colander.Mapping(),
            name="character",
        )
        character_schema.add(
            colander.SchemaNode(
                colander.String(),
                name="character_name",
                widget=deform.widget.TextInputWidget(),
                validator=colander.Length(max=100),
                default=self.character.name,
            )
        )
        character_schema.add(
            colander.SchemaNode(
                colander.Integer(),
                name="experience",
                widget=deform.widget.TextInputWidget(),
                default=self.character.experience,
            )
        )
        character_schema.add(
            colander.SchemaNode(
                colander.Integer(),
                name="experience_spent",
                widget=deform.widget.TextInputWidget(),
                default=self.character.experience_spent,
            )
        )
        character_schema.add(
            colander.SchemaNode(
                colander.String(),
                name="psychology",
                widget=deform.widget.TextAreaWidget(),
                default=self.character.psychology,
            )
        )
        character_schema.add(
            colander.SchemaNode(
                colander.String(),
                name="corruption",
                widget=deform.widget.TextAreaWidget(),
                default=self.character.corruption,
            )
        )
        schema.add(character_schema)
        return schema

    def species_schema(self):
        schema = colander.SchemaNode(
            colander.Mapping(),
            title=f"Edit Species for {self.character.get_display_title()}",
        )
        species_schema = colander.SchemaNode(colander.Mapping(), name="species")
        species_schema.add(
            colander.SchemaNode(
                colander.String(),
                name="species",
                widget=deform.widget.RadioChoiceWidget(
                    values=[(x, x) for x in SPECIES_LIST]
                ),
                validator=colander.OneOf(SPECIES_LIST),
                default=self.character.species,
            )
        )
        species_schema.add(
            colander.SchemaNode(
                colander.Integer(),
                name="movement",
                widget=deform.widget.TextInputWidget(),
                default=self.character.movement,
            )
        )
        species_schema.add(
            colander.SchemaNode(
                colander.Integer(),
                name="fate",
                widget=deform.widget.TextInputWidget(),
                default=self.character.fate,
            )
        )
        species_schema.add(
            colander.SchemaNode(
                colander.Integer(),
                name="fortune",
                widget=deform.widget.TextInputWidget(),
                default=self.character.fortune,
            )
        )
        schema.add(species_schema)
        return schema

    def career_schema(self):
        schema = colander.SchemaNode(
            colander.Mapping(),
            title=f"Edit Career for {self.character.get_display_title()}",
        )
        career_schema = colander.SchemaNode(colander.Mapping(), name="career")
        if "sea_of_claws" in self.character.expansions:
            career_choices = ALL_CAREER_DATA_WITH_SEAFARER.keys()
        else:
            career_choices = ALL_CAREER_DATA.keys()
        career_schema.add(
            colander.SchemaNode(
                colander.String(),
                name="career",
                widget=deform.widget.SelectWidget(
                    values=[(x, x) for x in career_choices]
                ),
                validator=colander.OneOf(career_choices),
                default=self.character.career,
            )
        )
        if self.character.career:
            if "sea_of_claws" in self.character.expansions:
                career_title_choices = ALL_CAREER_DATA[self.character.career].keys()
            else:
                career_title_choices = ALL_CAREER_DATA[self.character.career].keys()
            career_schema.add(
                colander.SchemaNode(
                    colander.String(),
                    name="career_title",
                    description=(
                        "If you change the career above, you will need to select the "
                        "correct career title after you save the form."
                    ),
                    widget=deform.widget.RadioChoiceWidget(
                        values=[(x, x) for x in career_title_choices]
                    ),
                    validator=colander.OneOf(career_title_choices),
                    default=self.character.career_title,
                    missing="",
                )
            )
        schema.add(career_schema)
        return schema

    def characteristics_schema(self):
        schema = colander.SchemaNode(
            colander.Mapping(),
            title=f"Edit Characteristics for {self.character.get_display_title()}",
        )
        characteristics_schema = colander.SchemaNode(
            colander.Mapping(), name="characteristics"
        )
        for attribute in ATTRIBUTES:
            characteristics_schema.add(
                colander.SchemaNode(
                    colander.Integer(),
                    name=attribute + " Initial",
                    widget=deform.widget.TextInputWidget(),
                    default=getattr(
                        self.character, attribute.lower().replace(" ", "_") + "_initial"
                    ),
                )
            )
            characteristics_schema.add(
                colander.SchemaNode(
                    colander.Integer(),
                    name=attribute + " Advances",
                    widget=deform.widget.TextInputWidget(),
                    default=getattr(
                        self.character,
                        attribute.lower().replace(" ", "_") + "_advances",
                    ),
                )
            )
        schema.add(characteristics_schema)
        return schema

    def skills_schema(self):
        schema = colander.SchemaNode(
            colander.Mapping(),
            title=f"Edit Skills for {self.character.get_display_title()}",
        )
        skills_schema = colander.SchemaNode(
            colander.Mapping(),
            name="skills",
            description="Set a skill to zero if you want to remove it.",
        )
        for skill in self.character.skills:
            skills_schema.add(
                colander.SchemaNode(
                    colander.Integer(),
                    name=skill,
                    widget=deform.widget.TextInputWidget(),
                    default=self.character.skills[skill],
                )
            )
            if skill in SKILL_DATA and "specialisations" in SKILL_DATA[skill]:
                choices = [(x, x) for x in SKILL_DATA[skill]["specialisations"]]
                skills_schema.add(
                    colander.SchemaNode(
                        colander.String(),
                        name=f"{skill} specialisation",
                        validator=colander.OneOf([x[0] for x in choices]),
                        widget=deform.widget.RadioChoiceWidget(
                            values=choices, inline=True
                        ),
                    )
                )
        skill_choices = [("", "Add Skill")]
        for skill in SKILL_DATA:
            skill_choices.append((skill, skill))
        skills_schema.add(
            colander.SchemaNode(
                colander.String(),
                name="add_skill",
                validator=colander.OneOf(SKILL_DATA),
                widget=deform.widget.SelectWidget(values=skill_choices),
                missing="",
            )
        )
        schema.add(skills_schema)
        return schema

    def talents_schema(self):
        schema = colander.SchemaNode(
            colander.Mapping(),
            title=f"Edit Talents for {self.character.get_display_title()}",
        )
        talents_schema = colander.SchemaNode(
            colander.Mapping(),
            name="talents",
            description="Set a talent to zero if you want to remove it.",
        )
        for talent in self.character.talents:
            talents_schema.add(
                colander.SchemaNode(
                    colander.Integer(),
                    name=talent,
                    widget=deform.widget.TextInputWidget(),
                    default=self.character.talents[talent],
                )
            )
            if talent in TALENT_DATA and "specialisations" in TALENT_DATA[talent]:
                choices = [(x, x) for x in TALENT_DATA[talent]["specialisations"]]
                talents_schema.add(
                    colander.SchemaNode(
                        colander.String(),
                        name=f"{talent} specialisation",
                        validator=colander.OneOf([x[0] for x in choices]),
                        widget=deform.widget.RadioChoiceWidget(
                            values=choices, inline=True
                        ),
                    )
                )
        talent_choices = [("", "Add Talent")]
        for talent in TALENT_DATA:
            talent_choices.append((talent, talent))
        talents_schema.add(
            colander.SchemaNode(
                colander.String(),
                name="add_talent",
                validator=colander.OneOf(TALENT_DATA),
                widget=deform.widget.SelectWidget(values=talent_choices),
                missing="",
            )
        )
        schema.add(talents_schema)
        return schema

    def magic_schema(self):
        schema = colander.SchemaNode(
            colander.Mapping(),
            title=f"Edit Magic Spells for {self.character.get_display_title()}",
        )
        magic_schema = colander.SchemaNode(
            colander.Mapping(),
            name="magic",
        )
        if "Petty Magic" in self.character.talents:
            choices = [(x, x) for x in PETTY_MAGIC_DATA]
            magic_schema.add(
                colander.SchemaNode(
                    colander.Set(),
                    name="petty_magic",
                    widget=deform.widget.CheckboxChoiceWidget(values=choices),
                    default=self.character.petty_magic,
                )
            )
        lore_spells = []
        for talent in self.character.talents:
            if talent.startswith("Arcane Magic ("):
                lore_spells = get_colour_spells(
                    talent.split("(")[1].replace(")", ""), self.character.expansions
                )
        if lore_spells:
            choices = [(x, x) for x in get_arcane_spells(self.character.expansions)]
            magic_schema.add(
                colander.SchemaNode(
                    colander.Set(),
                    name="arcane_magic",
                    widget=deform.widget.CheckboxChoiceWidget(values=choices),
                    default=self.character.arcane_magic,
                )
            )
            choices = [(x, x) for x in lore_spells]
            magic_schema.add(
                colander.SchemaNode(
                    colander.Set(),
                    name="lore_magic",
                    widget=deform.widget.CheckboxChoiceWidget(values=choices),
                    default=self.character.lore_magic,
                )
            )
        schema.add(magic_schema)
        return schema

    def miracles_schema(self):
        schema = colander.SchemaNode(
            colander.Mapping(),
            title=f"Edit Miracles for {self.character.get_display_title()}",
        )
        miracles_schema = colander.SchemaNode(
            colander.Mapping(),
            name="miracles",
        )
        for talent in self.character.talents:
            if talent.startswith("Invoke ("):
                all_miracles = get_miracles(
                    talent.split("Invoke (")[1].replace(")", "")
                )
        choices = [(x, x) for x in all_miracles]
        miracles_schema.add(
            colander.SchemaNode(
                colander.Set(),
                name="miracle",
                widget=deform.widget.CheckboxChoiceWidget(values=choices),
                default=self.character.miracles,
            )
        )
        schema.add(miracles_schema)
        return schema

    def chanties_schema(self):
        schema = colander.SchemaNode(
            colander.Mapping(),
            title=f"Edit Chanties for {self.character.get_display_title()}",
        )
        chanties_schema = colander.SchemaNode(
            colander.Mapping(),
            name="chanties",
        )
        choices = [(x, x) for x in CHANTY_DATA]
        chanties_schema.add(
            colander.SchemaNode(
                colander.Set(),
                name="chanty",
                widget=deform.widget.CheckboxChoiceWidget(values=choices),
                default=self.character.chanties,
            )
        )
        schema.add(chanties_schema)
        return schema

    def trappings_schema(self):
        schema = colander.SchemaNode(
            colander.Mapping(),
            title=f"Edit Trappings for {self.character.get_display_title()}",
        )
        trappings_schema = colander.SchemaNode(
            colander.Mapping(),
            name="trappings",
        )
        schema.add(trappings_schema)
        wealth_schema = colander.SchemaNode(
            colander.Mapping(),
            name="wealth",
        )
        wealth_schema.add(
            colander.SchemaNode(
                colander.Integer(),
                name="gold_crowns",
                widget=deform.widget.TextInputWidget(style="width:100px;"),
                default=self.character.gold_crowns,
            )
        )
        wealth_schema.add(
            colander.SchemaNode(
                colander.Integer(),
                name="silver_shillings",
                widget=deform.widget.TextInputWidget(style="width:100px;"),
                default=self.character.silver_shillings,
            )
        )
        wealth_schema.add(
            colander.SchemaNode(
                colander.Integer(),
                name="brass_pennies",
                widget=deform.widget.TextInputWidget(style="width:100px;"),
                default=self.character.brass_pennies,
            )
        )
        schema.add(wealth_schema)
        return schema

    def details_schema(self):
        schema = colander.SchemaNode(
            colander.Mapping(),
            title=f"Edit Character Details for {self.character.get_display_title()}",
        )
        details_schema = colander.SchemaNode(
            colander.Mapping(),
            name="details",
        )
        details_schema.add(
            colander.SchemaNode(
                colander.String(),
                name="eye_colour",
                widget=deform.widget.TextInputWidget(),
                default=self.character.eyes,
            )
        )
        details_schema.add(
            colander.SchemaNode(
                colander.String(),
                name="hair_colour",
                widget=deform.widget.TextInputWidget(),
                default=self.character.hair,
            )
        )
        details_schema.add(
            colander.SchemaNode(
                colander.Integer(),
                name="height",
                widget=deform.widget.TextInputWidget(),
                default=self.character.height,
            )
        )
        details_schema.add(
            colander.SchemaNode(
                colander.Integer(),
                name="age",
                widget=deform.widget.TextInputWidget(),
                default=self.character.age,
            )
        )
        schema.add(details_schema)
        return schema

    def ambitions_schema(self):
        schema = colander.SchemaNode(
            colander.Mapping(),
            title=f"Edit Ambitions for {self.character.get_display_title()}",
        )
        ambitions_schema = colander.SchemaNode(
            colander.Mapping(),
            name="ambitions",
        )
        ambitions_schema.add(
            colander.SchemaNode(
                colander.String(),
                name="short_term_ambition",
                widget=deform.widget.TextAreaWidget(),
                validator=colander.Length(max=100),
                default=self.character.short_term_ambition,
            )
        )
        ambitions_schema.add(
            colander.SchemaNode(
                colander.String(),
                name="long_term_ambition",
                widget=deform.widget.TextAreaWidget(),
                validator=colander.Length(max=100),
                default=self.character.long_term_ambition,
            )
        )
        schema.add(ambitions_schema)
        return schema

    def party_schema(self):
        schema = colander.SchemaNode(
            colander.Mapping(),
            title=f"Edit Party Details for {self.character.get_display_title()}",
        )
        party_schema = colander.SchemaNode(
            colander.Mapping(),
            name="party",
        )
        schema.add(party_schema)
        return schema

    @view_config(renderer="wfrp.character:templates/forms/base_form.pt")
    def form_view(self):  # noqa: C901
        html = []
        all_forms = [
            "expansions",
            "character",
            "species",
            "career",
            "characteristics",
            "skills",
            "talents",
            "magic",
            "miracles",
            "chanties",
            "trappings",
            "details",
            "ambitions",
            "party",
        ]
        if "Chanty" not in self.character.talents:
            all_forms.remove("chanties")
        for talent in self.character.talents:
            if talent == "Petty Magic" or talent.startswith("Arcane Magic ("):
                break
        else:
            all_forms.remove("magic")
        for talent in self.character.talents:
            if talent.startswith("Invoke ("):
                break
        else:
            all_forms.remove("miracles")
        forms = {}
        for form in all_forms:
            schema = getattr(self, f"{form}_schema")()
            forms[f"{form}_form"] = deform.Form(
                schema,
                buttons=(f"Save {form}",),
                formid=f"{form}_form",
            )
        if "__formid__" in self.request.POST:
            form = forms[self.request.POST["__formid__"]]
            try:
                captured = form.validate(self.request.POST.items())
            except deform.ValidationFailure as error:
                for form in forms:
                    if form == self.request.POST["__formid__"]:
                        form_title = form.title().replace("_", " ")
                        message = f"{form_title} has an error"
                        self.request.session.flash(message, "error")
                        html.append(error.render())
                    else:
                        html.append(forms[form].render())
            else:
                self.update_character(form.formid, captured)
                url = self.request.route_url("character-edit", id=self.character.id)
                return HTTPFound(location=url)
        else:
            for form in forms:
                html.append(forms[form].render())
        static_assets = list(forms.values())[0].get_widget_resources()
        return {
            "form": "".join(html),
            "css_links": static_assets["css"],
            "js_links": static_assets["js"],
            "character": self.character,
        }

    def update_character(self, form_id, captured):  # noqa: C901
        if form_id == "expansions_form":
            self.character.expansions = list(captured["expansions"]["expansions"])
        elif form_id == "character_form":
            self.character.name = captured["character"]["character_name"]
            self.character.experience = captured["character"]["experience"]
            self.character.experience_spent = captured["character"]["experience_spent"]
            self.character.psychology = captured["character"]["psychology"]
            self.character.corruption = captured["character"]["corruption"]
        elif form_id == "species_form":
            self.character.species = captured["species"]["species"]
            self.character.movement = captured["species"]["movement"]
            self.character.fate = captured["species"]["fate"]
            self.character.fortune = captured["species"]["fortune"]
        elif form_id == "career_form":
            career = captured["career"]["career"]
            if self.character.career != career:
                self.character.career = career
                if "sea_of_claws" in self.character.expansions:
                    self.character.career_class = CAREER_BY_CLASS_WITH_SEAFARER[career]
                else:
                    self.character.career_class = CAREER_BY_CLASS[career]
                self.character.career_title = ""
                self.character.career_tier = ""
                self.character.career_standing = ""
            elif self.character.career_title == "":
                career_title = captured["career"]["career_title"]
                if "sea_of_claws" in self.character.expansions:
                    career_data = ALL_CAREER_DATA_WITH_SEAFARER[career][career_title]
                else:
                    career_data = ALL_CAREER_DATA[career][career_title]
                self.character.career_title = career_title
                self.character.career_tier = career_data["status"]["tier"]
                self.character.career_standing = career_data["status"]["standing"]
            # XXX career path
            # self.character.career_path.append(career_title)
        elif form_id == "characteristics_form":
            for attribute in ATTRIBUTES:
                attribute_lower = attribute.lower().replace(" ", "_")
                setattr(
                    self.character,
                    f"{attribute_lower}_initial",
                    captured["characteristics"][f"{attribute} Initial"],
                )
                setattr(
                    self.character,
                    f"{attribute_lower}_advances",
                    captured["characteristics"][f"{attribute} Advances"],
                )
        elif form_id == "skills_form":
            skills = {}
            captured_skills = captured["skills"]
            for skill in captured_skills:
                if skill.endswith("specialisation"):
                    continue
                if skill == "add_skill":
                    if captured_skills["add_skill"]:
                        skills[captured_skills["add_skill"]] = 0
                    continue
                if captured_skills[skill]:
                    if f"{skill} specialisation" in captured_skills:
                        specialisation = captured_skills[f"{skill} specialisation"]
                        skills[f"{skill} ({specialisation})"] = captured_skills[skill]
                    else:
                        skills[skill] = captured_skills[skill]
            self.character.skills = dict(sorted(skills.items()))
        elif form_id == "talents_form":
            talents = {}
            captured_talents = captured["talents"]
            for talent in captured_talents:
                if talent.endswith("specialisation"):
                    continue
                if talent == "add_talent":
                    if captured_talents["add_talent"]:
                        talents[captured_talents["add_talent"]] = 0
                    continue
                if captured_talents[talent]:
                    if f"{talent} specialisation" in captured_talents:
                        specialisation = captured_talents[f"{talent} specialisation"]
                        talents[f"{talent} ({specialisation})"] = captured_talents[
                            talent
                        ]
                    else:
                        talents[talent] = captured_talents[talent]
            self.character.talents = dict(sorted(talents.items()))
        elif form_id == "magic_form":
            if "petty_magic" in captured["magic"]:
                self.character.petty_magic = list(captured["magic"]["petty_magic"])
            if "arcane_magic" in captured["magic"]:
                self.character.arcane_magic = list(captured["magic"]["arcane_magic"])
            if "lore_magic" in captured["magic"]:
                self.character.lore_magic = list(captured["magic"]["lore_magic"])
        elif form_id == "miracles_form":
            self.character.miracles = list(captured["miracles"]["miracle"])
        elif form_id == "chanties_form":
            self.character.chanties = list(captured["chanties"]["chanty"])
        elif form_id == "trappings_form":
            # XXX trappings
            self.character.brass_pennies = captured["wealth"]["brass_pennies"]
            self.character.silver_shillings = captured["wealth"]["silver_shillings"]
            self.character.gold_crowns = captured["wealth"]["gold_crowns"]
        elif form_id == "details_form":
            self.character.eyes = captured["details"]["eye_colour"]
            self.character.hair = captured["details"]["hair_colour"]
            self.character.height = captured["details"]["height"]
            self.character.age = captured["details"]["age"]
        elif form_id == "ambitions_form":
            ambitions = captured["ambitions"]
            self.character.short_term_ambition = ambitions["short_term_ambition"]
            self.character.long_term_ambition = ambitions["long_term_ambition"]
        elif form_id == "party_form":
            pass
