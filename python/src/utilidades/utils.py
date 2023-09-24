import pickle
import os
from typing import Optional
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeRegressor
import numpy as np

# Funcion para cargar el algoritmo
def cargarAlgoritmo(ruta:str)->Optional[tuple]:

    try:

        ruta_algoritmo=os.path.join(ruta, r"algoritmo/algoritmo.pkl")

        with open(ruta_algoritmo, "rb") as archivo:

            algoritmo=pickle.load(archivo)

        return algoritmo["Modelo"], algoritmo["Encoder Pais"], algoritmo["Encoder Estudios"]

    except FileNotFoundError as e:

        return None

# Funcion para obtener la prediccion del salario
def obtenerPrediccion(modelo:DecisionTreeRegressor, encoder_pais:LabelEncoder, encoder_estudios:LabelEncoder,
                        pais:str, estudios:str, experiencia:str)->float:

    data=np.array([[pais, estudios, int(experiencia)]])

    data_transf=np.array([[encoder_pais.transform(data[:,0])[0], 
                            encoder_estudios.transform(data[:,1])[0],
                            data[:,2][0]]]).astype(float)

    prediccion=modelo.predict(data_transf)

    return round(prediccion[0],2)