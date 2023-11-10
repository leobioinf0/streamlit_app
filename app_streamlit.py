import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder

st.set_page_config(page_title="Healthy Heart App",page_icon="⚕️",layout="centered",initial_sidebar_state="auto")
st.title("App de predicción de enfermedades cardíacas")
st.markdown("""Esta app predice la presencia de enfermedad cardíaca en base a los datos ingresados""") 
st.markdown("""---""")
logo = "imagen.png"
st.sidebar.image(logo, width=150)
st.sidebar.header("Datos ingresados por el usuario")
uploaded_file = st.sidebar.file_uploader("Cargue su CSV", type=["csv"])
if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)
else:
    def user_input_features():
        Age = st.sidebar.slider('age',29,77,29)
        Sex = st.sidebar.slider('Sex',0,1,0)
        ChestPain = st.sidebar.slider('ChestPain',0,3,0)
        RestBP = st.sidebar.slider('RestBP',94,200,94)
        Chol = st.sidebar.slider('Chol',126,564,126)
        Fbs = st.sidebar.slider('Fbs',0,1,0)
        RestECG = st.sidebar.slider('RestECG',0,2,0)
        MaxHR = st.sidebar.slider('MaxHR',71,202,71)
        ExAng = st.sidebar.slider('ExAng',0,1,0)
        Oldpeak = st.sidebar.slider('Oldpeak',0.0,6.2,0.0)
        Slope = st.sidebar.slider('Slope',1,3,1)
        Ca = st.sidebar.slider('Ca',0.0,3.0,0.0)
        Thal = st.sidebar.slider('Thal',0.0,2.0,0.0)

        data = {
            'Age':Age,
            'Sex':Sex,
            'ChestPain':ChestPain,
            'RestBP':RestBP,
            'Chol':Chol,
            'Fbs':Fbs,
            'RestECG':RestECG,
            'MaxHR':MaxHR,
            'ExAng':ExAng,
            'Oldpeak':Oldpeak,
            'Slope':Slope,
            'Ca':Ca,
            'Thal':Thal
            }
        features = pd.DataFrame(data, index=[0])
        return features
    input_df =  user_input_features()


input_df = input_df[:1]

st.subheader("Datos ingresados por el usuario")
if uploaded_file is not None:
    st.write(input_df)
else:
    st.write("A la espera de que se cargue el CSV. Actualmente usando parámetros de ejemplo.")
    st.write(input_df)

load_clf = pickle.load(open('heart.pkl','rb'))
prediction = load_clf.predict(input_df)
prediction_proba = load_clf.predict_proba(input_df)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Predicción")
    st.write(prediction)

with col2:
    st.subheader("Probabilidad de predicción")
    st.write(prediction_proba)

if prediction == 0:
    st.subheader("No tiene problemas cardíacos")
else:
    st.subheader("Sí tiene problemas cardíacos")
st.markdown("""---""")