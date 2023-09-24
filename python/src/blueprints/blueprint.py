from flask import Blueprint, render_template, request
import os

from src.utilidades.utils import cargarAlgoritmo, obtenerPrediccion
from .config import PAISES, ESTUDIOS

bp=Blueprint("blueprint", __name__)

@bp.route("/", methods=["GET"])
def inicio():

	return render_template("inicio.html", paises=PAISES, estudios=ESTUDIOS)

@bp.route("/", methods=["POST"])
def predecir():

	pais=request.form.get("pais")
	estudios=request.form.get("estudios")
	experiencia=request.form.get("experiencia")

	ruta=os.path.dirname(os.path.join(os.path.dirname(__file__)))

	modelo, encoder_pais, encoder_estudios=cargarAlgoritmo(ruta)

	resultado=obtenerPrediccion(modelo, encoder_pais, encoder_estudios, pais, estudios, experiencia)

	return render_template("inicio.html", paises=PAISES, estudios=ESTUDIOS, prediccion=resultado)