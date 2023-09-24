import pytest

def test_pagina_inicial_get(cliente):

	respuesta=cliente.get("/")

	contenido=respuesta.data.decode()

	respuesta.status_code==200
	assert "SalariApp" in contenido

@pytest.mark.parametrize(["datos"],
	[
		({"pais":"Spain", "estudios":"Titulacion universitaria", "experiencia":"3"},),
		({"pais":"United States", "estudios":"Titulacion universitaria", "experiencia":"8"},),
		({"pais":"Spain", "estudios":"Post grado", "experiencia":"0"},),
		({"pais":"Italy", "estudios":"Titulacion universitaria", "experiencia":"33"},),
		({"pais":"Spain", "estudios":"Titulacion de master", "experiencia":"1"},)
	]
)
def test_pagina_inicial_post(cliente, datos):

	respuesta=cliente.post("/", data=datos)

	contenido=respuesta.data.decode()

	respuesta.status_code==200
	assert "El salario estimado segun tus datos es de" in contenido