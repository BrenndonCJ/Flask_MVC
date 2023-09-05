from flask import abort, render_template
from futbr.models import Futbrdata


def index():
    campeonatos = Futbrdata.query.all()
    return render_template("index.html", campeonatos=campeonatos)


def campeonato(ano):
    campeonato = Futbrdata.query.filter_by(ano=ano).first() or abort(
        404, "Campeonato nao encontrado"
    )
    return render_template("campeonato.html", campeonato=campeonato)
