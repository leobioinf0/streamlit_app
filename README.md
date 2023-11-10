
---

# Streamlit App de predicción de enfermedades cardíacas

Esta es una aplicación web Streamlit sencilla que permite a los usuarios predecir la probabilidad de sufrir enfermedades cardíacas en función de las funciones de entrada. La predicción se realiza utilizando un modelo de aprendizaje automático que ha sido entrenado con datos de enfermedades cardíacas.

![logo](imagen.png)

[Website](https://heart-disease-predict.streamlit.app/)


## Tabla de contenido

- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Features de entrada](#features-de-entrada)
- [Salida](#salida)

## Requisitos

- Python (3.6 or later)
- Streamlit
- pandas
- pickle

## Instalación

1. Clonar este repositorio:

```bash
git clone https://github.com/leobioinf0/streamlit_app.git
```

2. Navegar al directorio de la app.:

```bash
cd streamlit_app
```

3. Instalar las dependencias requeridas:

```bash
pip install -r requirements.txt
```

## Uso

Ejecute la aplicación Streamlit ejecutando el siguiente comando en su terminal:

```bash
streamlit run app_streamlit.py
```

La aplicación web se abrirá en su navegador web predeterminado. Luego puede interactuar con la aplicación ingresando varias funciones y haciendo clic en el botón "Predecir" para obtener el resultado previsto.

## Features de entrada

Las siguientes features de entrada se pueden ajustar en la app:

- Age
- Sex
- ChestPain
- RestBP
- Chol
- Fbs
- RestECG
- MaxHR
- ExAng
- Oldpeak
- Slope
- Ca
- Thal

## Salida

Después de ajustar las funciones de entrada y hacer clic en "Predecir", la aplicación mostrará el resultado previsto, indicando si la predicción sugiere una probabilidad positiva o negativa de enfermedad cardíaca.

---