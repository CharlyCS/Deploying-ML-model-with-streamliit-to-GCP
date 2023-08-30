import numpy as np
from flask import Flask, request, jsonify, render_template, url_for
import pickle
from sklearn import svm
import streamlit as st


# Path del modelo preentrenado
MODEL_PATH = 'models/pickle_model.pkl'


# Se recibe la imagen y el modelo, devuelve la predicción
def model_prediction(x_in, model):

    x = np.asarray(x_in).reshape(1,-1)
    preds=model.predict(x)

    return preds


def main():
    
    model=''

    # Se carga el modelo
    if model=='':
        with open(MODEL_PATH, 'rb') as file:
            model = pickle.load(file)
    
    # Título
    html_temp = """
    <h1 style="color:#181082;text-align:center;">CANTIDAD DE CONCENTRADO DE SILICA </h1>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)

    # Lecctura de datos
    #Datos = st.text_input("Ingrese los valores : N P K Temp Hum pH lluvia:")
    Feb = st.text_input("% Hierro bruto:")
    Sib = st.text_input("% Silicie bruto:")
    Al = st.text_input("Fluido de Almidon:")
    Am = st.text_input("Fluido de Amina:")
    Pulpau = st.text_input("Fluido de pulpa deL mineral:")
    phau = st.text_input("ph de pulpa de mineral:")
    densidad = st.text_input("Densidad de la pulpa del mineral:")
    columnaire1 = st.text_input("Flujo de aire de la columna de flotacion 1:")
    columnaire2 = st.text_input("Flujo de aire de la columna de flotacion 2:")
    columnaire3 = st.text_input("Flujo de aire de la columna de flotacion 3:")
    columnaire4 = st.text_input("Flujo de aire de la columna de flotacion 4:")
    columnaire6 = st.text_input("Flujo de aire de la columna de flotacion 6:")
    columna1 = st.text_input("Nivel de la columna de flotacion 1:")
    columna2 = st.text_input("Nivel de la columna de flotacion 2:")
    columna3 = st.text_input("Nivel de la columna de flotacion 3:")
    columna4 = st.text_input("Nivel de la columna de flotacion 4:")
    columna6 = st.text_input("Nivel de la columna de flotacion 6:")
    columna7 = st.text_input("Nivel de la columna de flotacion 7:")
    Fec = st.text_input("% Hierro concentrado:")

    # El botón predicción se usa para iniciar el procesamiento
    if st.button("Predicción :"): 
        #x_in = list(np.float_((Datos.title().split('\t'))))
        x_in =[np.float_(Feb.title()),
                    np.float_(Sib.title()),
                    np.float_(Al.title()),
                    np.float_(Am.title()),
                    np.float_(Pulpau.title()),
                    np.float_(phau.title()),
                    np.float_(densidad.title()),
                    np.float_(columnaire1.title()),
                    np.float_(columnaire2.title()),
                    np.float_(columnaire3.title()),
                    np.float_(columnaire4.title()),
                    np.float_(columnaire6.title()),
                    np.float_(columna1.title()),
                    np.float_(columna2.title()),
                    np.float_(columna3.title()),
                    np.float_(columna4.title()),
                    np.float_(columna6.title()),
                    np.float_(columna7.title()),
                    np.float_(Fec.title())
                    ]
        predicts = model_prediction(x_in, model)
        st.success('EL porcentaje de silicie concentrado es: {}'.format(predicts[0]).upper())

if __name__ == '__main__':
    main()
