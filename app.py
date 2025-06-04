import streamlit as st
import pandas as pd
import plotly.express as px

# Leer el archivo CSV (cambia 'datos.csv' por el nombre de tu archivo)
df = pd.read_csv('vehicles_us (2).csv')

# Encabezado de la aplicación
st.header("Cuadro de Mandos - Análisis del Conjunto de Datos")

# Opción con botones para construir gráficos
if st.button('Construir Histograma'):
    st.write('Creación de un histograma para la columna seleccionada')
    fig = px.histogram(df, x=df.columns[0])  # Aquí puedes cambiar la columna que quieres analizar
    st.plotly_chart(fig, use_container_width=True)

if st.button('Construir Gráfico de Dispersión'):
    st.write('Creación de un gráfico de dispersión para dos columnas')
    # Cambia las columnas para tu dataset o haz que el usuario las elija
    fig = px.scatter(df, x=df.columns[0], y=df.columns[1])
    st.plotly_chart(fig, use_container_width=True)