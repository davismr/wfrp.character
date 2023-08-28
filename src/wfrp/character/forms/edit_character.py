import colander
import deform
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.data.careers import CAREER_DATA
from wfrp.character.data.species import SPECIES_LIST
from wfrp.character.forms.create.attributes import ATTRIBUTES
from wfrp.character.views.base_view import BaseView


@view_defaults(route_name="character_edit")
class CharacterEditViews(BaseView):
    def schema(self):
        schema = colander.SchemaNode(
            colander.Mapping(), title=f"Edit {self.character.get_display_title()}"
        )
        name_schema = colander.SchemaNode(
            colander.Mapping(),
            name="name",
        )
        name_schema.add(
            colander.SchemaNode(
                colander.String(),
                name="character_name",
                widget=deform.widget.TextInputWidget(),
                validator=colander.Length(max=100),
                default=self.character.name,
            )
        )
        schema.add(name_schema)
        species_schema = colander.SchemaNode(
            colander.Mapping(),
            name="species",
        )
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
        schema.add(species_schema)
        career_schema = colander.SchemaNode(
            colander.Mapping(),
            name="career",
        )
        career_schema.add(
            colander.SchemaNode(
                colander.String(),
                name="career",
                widget=deform.widget.SelectWidget(
                    values=[(x, x) for x in list(CAREER_DATA.keys())]
                ),
                validator=colander.OneOf(list(CAREER_DATA.keys())),
                default=self.character.career,
            )
        )
        schema.add(career_schema)
        attributes_schema = colander.SchemaNode(
            colander.Mapping(),
            name="attributes",
        )
        for attribute in ATTRIBUTES:
            attributes_schema.add(
                colander.SchemaNode(
                    colander.Integer(),
                    name=attribute,
                    widget=deform.widget.TextInputWidget(),
                    default=getattr(
                        self.character, attribute.lower().replace(" ", "_")
                    ),
                )
            )
        schema.add(attributes_schema)
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
                colander.String(),
                name="height",
                widget=deform.widget.TextInputWidget(),
                default=self.character.height,
            )
        )
        details_schema.add(
            colander.SchemaNode(
                colander.String(),
                name="age",
                widget=deform.widget.TextInputWidget(),
                default=self.character.age,
            )
        )
        schema.add(details_schema)
        talents_schema = colander.SchemaNode(
            colander.Mapping(),
            name="talents",
        )
        schema.add(talents_schema)
        skills_schema = colander.SchemaNode(
            colander.Mapping(),
            name="skills",
        )
        schema.add(skills_schema)
        trappings_schema = colander.SchemaNode(
            colander.Mapping(),
            name="trappings",
        )
        schema.add(trappings_schema)
        return schema

    @view_config(renderer="wfrp.character:templates/form.pt")
    def form_view(self):
        schema = self.schema()
        form = deform.Form(schema, buttons=("Select Name",))
        if "Save" in self.request.POST:
            try:
                captured = form.validate(self.request.POST.items())  # noqa
            except deform.ValidationFailure as error:
                html = error.render()
            else:
                url = self.request.route_url(
                    "character_summary", uuid=self.character.uuid
                )
                return HTTPFound(location=url)
        else:
            html = form.render()

        static_assets = form.get_widget_resources()
        return {
            "form": html,
            "css_links": static_assets["css"],
            "js_links": static_assets["js"],
        }
