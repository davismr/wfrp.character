import colander
import deform
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.models.experience import ExperienceGain
from wfrp.character.views.base_view import BaseView


@view_defaults(renderer="wfrp.character:templates/forms/experience.pt")
class ExperienceGainViews(BaseView):
    def schema(self):
        schema = colander.SchemaNode(colander.Mapping(), title="Give Experience")
        experience_schema = colander.SchemaNode(
            colander.Mapping(),
            name="experience_gain",
        )
        experience_schema.add(
            colander.SchemaNode(
                colander.Integer(),
                title="Amount",
                widget=deform.widget.TextInputWidget(),
                name="amount",
            )
        )
        experience_schema.add(
            colander.SchemaNode(
                colander.String(),
                title="Reason",
                validator=colander.Length(max=100),
                widget=deform.widget.TextInputWidget(),
                name="reason",
            )
        )
        schema.add(experience_schema)
        return schema

    @view_config(route_name="experience-add")
    def form_view(self):
        schema = self.schema()
        form = deform.Form(
            schema,
            buttons=("Give Experience",),
        )
        if "Give_Experience" in self.request.POST:
            try:
                captured = form.validate(self.request.POST.items())
            except deform.ValidationFailure as error:
                html = error.render()
            else:
                experience = ExperienceGain(
                    character_id=self.character.id,
                    amount=captured["experience_gain"]["amount"],
                    reason=captured["experience_gain"]["reason"],
                )
                self.request.dbsession.add(experience)
                url = self.request.route_url("character_summary", id=self.character.id)
                return HTTPFound(location=url)
        else:
            html = form.render()
        static_assets = self.get_widget_resources(form)
        return {
            "form": html,
            "character": self.character,
            "css_links": static_assets["css"],
            "js_links": static_assets["js"],
        }
