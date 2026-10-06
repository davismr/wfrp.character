from flask import render_template
from flask.views import MethodView


class HomePageView(MethodView):

    def get(self):
        return render_template("home.html", title="Home")
