import pytest
import os
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeRegressor

from src.utilidades.utils import cargarAlgoritmo, obtenerPrediccion

def test_cargar_algoritmo_error():

	ruta_relativa=os.path.abspath("..")

	assert cargarAlgoritmo(ruta_relativa) is None

def test_cargar_algoritmo():

	modelo, encoder1, encoder2=cargarAlgoritmo(os.path.abspath("..")+"/src")

	assert isinstance(modelo, DecisionTreeRegressor)
	assert isinstance(encoder1, LabelEncoder)
	assert isinstance(encoder2, LabelEncoder)

def test_obtener_prediccion():

	modelo, encoder1, encoder2=cargarAlgoritmo(os.path.abspath("..")+"/src")

	prediccion=obtenerPrediccion(modelo, encoder1, encoder2, "United States", "Titulacion universitaria", 3)

	assert prediccion==96952.69