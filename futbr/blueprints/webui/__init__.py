from flask import Blueprint

from .views import index, campeonato

bp = Blueprint("webui", __name__, template_folder="templates")

bp.add_url_rule("/", view_func=index, endpoint="index")
bp.add_url_rule(
    "/campeonato/<ano>", view_func=campeonato, endpoint="campeonatoview"
)


def init_app(app):
    app.register_blueprint(bp)
