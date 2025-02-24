import streamlit as st
import pandas as pd
import plotly.express as px  # Importar plotly para los gráficos interactivos

# Leer datos
oferta = pd.read_csv("dash.csv", encoding='latin-1', index_col='propuesta')
demanda = pd.read_csv("board.csv", encoding='latin-1', index_col='partida')

# Variables
prop = oferta['clave'].nunique()
of = len(oferta[oferta['estatus'] != 'no procedente'])
efect = len(oferta[oferta['estatus'] != 'no procedente'])

adj = len(demanda[demanda['estatus'].isin(['único', 'simultáneo'])])
des = len(demanda[demanda['estatus'] == 'desierta'])
so = len(demanda[demanda['estatus'] == 'sin oferta'])
absim = len(demanda[demanda['estatus'] == 'simultáneo'])

# Crear un gráfico con Plotly (por ejemplo, un gráfico de barras de la adjudicación)
fig = px.histogram(oferta, x="adjudicación (%)")

# Configuración de la página
st.set_page_config(page_title="Dashboard", layout="wide")

# Pestañas
tab1, tab2, tab3 = st.tabs(["Resumen de licitación", "Oferta", "Demanda"])

# Pestaña 1
with tab1:
    st.header("Resumen de licitación")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("TOTAL DE PROPUESTAS", f"{prop}")
    col2.metric("OFERTAS PARA ANÁLISIS", f"{of}")
    col3.metric("ADJUDICADAS", f"{adj}")
    col4.metric("DESIERTAS", f"{des}")
        
    col5, col6, col7 = st.columns(3)
    col5.metric("PROPUESTAS EFECTIVAS", f"{efect}")
    col6.metric("SIN OFERTA%", f"{so}")
    col7.metric("SIMULTÁNEAS", f"{absim}")

# Pestaña 2
with tab2:
    st.write(oferta.head())  # Usamos st.write() para mostrar el DataFrame
    st.write(oferta.info())  # Usamos st.write() para mostrar el resumen
    
    # Mostrar el gráfico interactivo en Streamlit
    st.plotly_chart(fig)

# Pestaña 3
with tab3:
    st.write(demanda.head())  # Usamos st.write() para mostrar el DataFrame
    st.write(demanda.info())  # Usamos st.write() para mostrar el resumen
    st.plotly_chart(fig)
