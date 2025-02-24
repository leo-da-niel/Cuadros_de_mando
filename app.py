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

# Crear gráficos con Plotly
fig_histogram_oferta = px.histogram(oferta, x="adjudicación (%)", title="Distribución de Adjudicación (%)")
fig_pie_oferta = px.pie(oferta, names='estatus', title='Distribución de Estatus de Oferta')

# Ajustar la columna para el gráfico de demanda
fig_histogram_demanda = px.histogram(demanda, x="otra_columna_existente", title="Distribución de Otra Columna")
fig_pie_demanda = px.pie(demanda, names='estatus', title='Distribución de Estatus de Demanda')

# Configuración de la página
st.set_page_config(page_title="Dashboard", layout="wide")

# Pestañas
tab1, tab2, tab3 = st.tabs(["Resumen de licitación", "Oferta", "Demanda"])

# Pestaña 1: Resumen de licitación
with tab1:
    st.header("Resumen de licitación")

    # Crear un DataFrame con la información
    resumen_data = {
        "Métrica": ["TOTAL DE PROPUESTAS", "OFERTAS PARA ANÁLISIS", "ADJUDICADAS", "DESIERTAS", "PROPUESTAS EFECTIVAS", "SIN OFERTA%", "SIMULTÁNEAS"],
        "Valor": [prop, of, adj, des, efect, so, absim]
    }
    resumen_df = pd.DataFrame(resumen_data)

    # Mostrar la tabla en Streamlit
    st.dataframe(resumen_df.style.format({"Valor": "{:.0f}"}).highlight_max(axis=0, color='lightgreen'))

    # Mostrar gráficos mixtos
    st.plotly_chart(fig_histogram_oferta, key="resumen_histogram_oferta")
    st.plotly_chart(fig_pie_oferta, key="resumen_pie_oferta")
    st.plotly_chart(fig_histogram_demanda, key="resumen_histogram_demanda")
    st.plotly_chart(fig_pie_demanda, key="resumen_pie_demanda")

# Pestaña 2: Oferta
with tab2:
    st.header("Oferta")
    st.write(oferta.head())  # Mostrar el DataFrame
    st.write(oferta.info())  # Mostrar el resumen

    # Mostrar gráficos interactivos
    st.plotly_chart(fig_histogram_oferta, key="oferta_histogram")
    st.plotly_chart(fig_pie_oferta, key="oferta_pie")

# Pestaña 3: Demanda
with tab3:
    st.header("Demanda")
    st.write(demanda.head())  # Mostrar el DataFrame
    st.write(demanda.info())  # Mostrar el resumen

    # Mostrar gráficos interactivos
    st.plotly_chart(fig_histogram_demanda, key="demanda_histogram")
    st.plotly_chart(fig_pie_demanda, key="demanda_pie")
