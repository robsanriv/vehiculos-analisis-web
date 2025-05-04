# Se importan librerias

import streamlit as st
import pandas as pd
import plotly.express as px

# Leer archivo

car_data = pd.read_csv("vehicles_us.csv")

# Crear contenido de aplicacion

# Encabezado

st.header("Análisis de Anuncios de Venta de Coches")

# Boton para el histograma

build_histogram = st.checkbox('Mostrar histograma de odómetro')
build_scatter = st.checkbox(
    'Mostrar gráfico de dispersión de precio vs odómetro')

if build_histogram:
    st.write('Creando un histograma para la columna "odometer"')
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

if build_scatter:
    st.write('Creando un gráfico de dispersión para "odometer" vs "price"')
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig_scatter, use_container_width=True)
