import streamlit as st
import pandas as pd
import plotly.express as px  # Importar plotly para los gráficos interactivos

# Leer datos
oferta = pd.read_csv("dash.csv", encoding='latin-1', index_col = 'propuesta')
demanda = pd.read_csv("board.csv", encoding='latin-1', index_col = 'partida')

# Variable
prop = oferta['clave'].nunique()
of = len(oferta[oferta['estatus'] != 'no procedente'])
efect = len(oferta[oferta['estatus'] != 'no procedente'])

adj = len(demanda[demanda['estatus'].isin(['único','simultáneo'])])
des = len(demanda[demanda['estatus'] == 'desierta'])
so = len(demanda[demanda['estatus'] == 'sin oferta'])
absim = len(demanda[demanda['estatus'] == 'simultáneo'])

# Crear un gráfico con Plotly (por ejemplo, un gráfico de barras de la edad)
fig = px.histogram(oferta, x="adjudicación (%)")

# Configuración de la página
st.set_page_config(page_title="Dashboard", layout="wide")
#st.sidebar.title("Análisis de datos")
#columna_input = st.sidebar.text_input("Ingrese los símbolos de las acciones separados por comas (por ejemplo: Edad):", "age")

# Pestañas
tab1, tab2, tab3 = st.tabs(["Resumen de licitación", "Oferta", "Demanda"])

# Pestaña 1
with tab1:
    st.header("Resumen de licitación")

            col1, col2, col3, col4 = st.columns(4)
        col1.metric("TOTAL DE PROPUESTAS", f"{prop}")
        col2.metric("OFERTAS PARA ANÁLISIS", f"{calcular_sharpe_ratio(returns[selected_asset]):.2f}")
        col3.metric("ADJUDICADAS", f"{calcular_sortino_ratio(returns[selected_asset]):.2f}")
        col4.metric("DESIERTAS", f"{calcular_sortino_ratio(returns[selected_asset]):.2f}")
        
        col5, col6, col7 = st.columns(3)
        col5.metric("PROPUESTAS EFECTIVAS", f"{var_95:.2%}")
        col6.metric("SIN OFERTA%", f"{cvar_95:.2%}")
        col7.metric("ABASTECIMIENTO SIMULTÁNEO", f"{var_95:.2%}")


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
