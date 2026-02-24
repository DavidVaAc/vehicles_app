import pandas as pd
import streamlit as st
import plotly.graph_objects as go

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')
models = car_data['model'].value_counts()[car_data['model'].value_counts() > 1000].index
short_data = car_data.query('model in @models')

# Título de la aplicación
st.title('Análisis de Coches en Venta en Estados Unidos')

# Barra lateral para la configuración de la aplicación
with st.sidebar:
    st.header("Configuración")
    st.write("Selecciona opciones de visualización:")

    # Crear una casilla de verificación para mostrar el DataFrame completo
    df_button = st.checkbox('Desplegar el DataFrame completo')

    # Crear una casilla de verificación para el histograma
    hist_button = st.checkbox('Construir un histograma')

    # Crear una casilla de verificación para el gráfico de dispersión
    disp_button = st.checkbox('Construir un gráfico de dispersión')

# Lógica a ejecutar cuando se hace clic en la casilla de verificación del DataFrame
if df_button:
    # Escribir un mensaje en la aplicación
    st.subheader('Mostrando el DataFrame completo de anuncios de venta de coches')

    # Opciones de visualización del DataFrame
    if st.checkbox('Mostrar solo modelos con más de 1000 anuncios'):
        st.dataframe(short_data, use_container_width=True)

    else:
        # Mostrar el DataFrame completo en la aplicación Streamlit
        st.dataframe(car_data, use_container_width=True)

# Lógica a ejecutar cuando se hace clic en el botón
if hist_button:
    # Escribir un mensaje en la aplicación
    st.subheader('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Distribución del Odómetro')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)

    # Lógica a ejecutar cuando se hace clic en el botón
if disp_button:
    # Escribir un mensaje en la aplicación
    st.subheader('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # Crear un gráfico de dispersión utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro del gráfico de dispersión
    fig = go.Figure(data=[go.Scatter(x=car_data['odometer'])])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Distribución del Odómetro')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)