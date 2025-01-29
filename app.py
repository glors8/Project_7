import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')        
show_histogram = st.checkbox('Mostrar histograma')  # Casilla para el histograma
show_scatter = st.checkbox('Mostrar gráfico de dispersión')  # Casilla para el gráfico de dispersión

# Si el usuario selecciona la casilla para el histograma
if show_histogram:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Si el usuario selecciona la casilla para el gráfico de dispersión
if show_scatter:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True) # crear un botón

