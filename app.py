import streamlit as st
import pandas as pd
import plotly.express as px  # Importar plotly para los gráficos interactivos

# Leer datos
ofertas = pd.read_csv("dash.csv")
demanda = pd.read_csv("board.csv")

# Crear un gráfico con Plotly (por ejemplo, un gráfico de barras de la edad)
fig = px.histogram(titanic, x="age")

# Configuración de la página
st.set_page_config(page_title="Dashboard", layout="wide")
st.sidebar.title("Análisis de datos")
columna_input = st.sidebar.text_input("Ingrese los símbolos de las acciones separados por comas (por ejemplo: Edad):", "age")

# Pestañas
tab1, tab2 = st.tabs(["Cuadros de desglose", "Gráficas"])

# Pestaña 1
with tab1:
    st.header("Información general")
    st.write(titanic.head())  # Usamos st.write() para mostrar el DataFrame
    st.write(titanic.info())  # Usamos st.write() para mostrar el resumen

# Pestaña 2
with tab2:

    
    # Mostrar el gráfico interactivo en Streamlit
    st.plotly_chart(fig)
