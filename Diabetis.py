# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 12:09:58 2022

@author: NRodriguezL
"""
import streamlit as st
import joblib
import numpy as np

model_filename = 'rf_model.pkl'
loaded_model = joblib.load(model_filename)
print("Modelo Cargado")

st.title('Herramienta de diagnostico para diabetologo')
st.header("Zero azucar")
st.subheader("Ingrese los datos del paciente")

with st.form(key='diabetes-pred-form'):
    col1, col2 = st.columns(2)
    
    Pregnancies = col2.text_input(label='Numero de embarazo:', value =0)
    PlasmaGlucose = col2.text_input(label='resultado de glucosa:', value =0)
    DiastolicBloodPressure = col2.text_input(label='Presion arterial:', value =0)
    TricepsThickness = col2.text_input(label='Medida del triceps:', value =0)
    SerumInsulin  = col2.text_input(label='Nivel de Insulina:', value =0)
    BMI  = col2.text_input(label='IMC:', value =0)
    DiabetesPedigree  = col2.text_input(label='Diabetis en la familia:', value =0)
    Age  = col2.text_input(label='Edad:', value =0)
    
    submit = st.form_submit_button(label='Check') 
    
    inputs = np.array([Pregnancies,PlasmaGlucose,DiastolicBloodPressure,TricepsThickness,SerumInsulin,BMI,DiabetesPedigree,Age]).reshape(-1, 1) 
    predicted_diabetico = loaded_model.predict(inputs)[0] 
     #st.write("El paciente es diabetico ",round(predicted_boot_size))

    if int(predicted_diabetico) == 1 :
     st.write('Paciente Diabetico')
    else:
     st.write('Paciente  No Diabetico')

   