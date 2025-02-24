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

# Crear un gráfico de barras con Plotly
fig_histogram = px.histogram(oferta, x="adjudicación (%)")

# Crear un gráfico de pastel con Plotly
fig_pie = px.pie(oferta, names='estatus', title='Distribución de Estatus de Oferta')

# Configuración de la página
st.set_page_config(page_title="Dashboard", layout="wide")

# Pestañas
tab1, tab2, tab3 = st.tabs(["Resumen de licitación", "Oferta", "Demanda"])

# Pestaña 1
with tab1:
    st.header("Resumen de licitación")

    # Crear un DataFrame con la información
    resumen_data = {
        "Métrica": ["TOTAL DE PROPUESTAS", "OFERTAS PARA ANÁLISIS", "ADJUDICADAS", "DESIERTAS", "PROPUESTAS EFECTIVAS", "SIN OFERTA%", "SIMULTÁNEAS"],
        "Valor": [prop, of, adj, des, efect, so, absim]
    }
    resumen_df = pd.DataFrame(resumen_data)

    # Estilizar el DataFrame
    st.dataframe(resumen_df.style.format({"Valor": "{:.0f}"}).highlight_max(axis=0, color='gray'))

# Pestaña 2
with tab2:
    st.write(oferta.head())  # Usamos st.write() para mostrar el DataFrame
    st.write(oferta.info())  # Usamos st.write() para mostrar el resumen
    
    # Mostrar el gráfico interactivo en Streamlit con un key único
    st.plotly_chart(fig_histogram, key="oferta_histogram")
    st.plotly_chart(fig_pie, key="oferta_pie")

# Pestaña 3
with tab3:
    st.write(demanda.head())  # Usamos st.write() para mostrar el DataFrame
    st.write(demanda.info())  # Usamos st.write() para mostrar el resumen
    
    # Mostrar el gráfico interactivo en Streamlit con un key único
    st.plotly_chart(fig_histogram, key="demanda_histogram")
    st.plotly_chart(fig_pie, key="demanda_pie")
