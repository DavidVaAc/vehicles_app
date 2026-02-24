import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')
car_data['manufacturer'] = car_data['model'].str.split().str[0]
car_data['model'] = car_data['model'].str.split().str[1:].str.join(' ')
car_data = car_data[['price', 'model_year', 'manufacturer', 'model', 'condition', 'cylinders', 'fuel',
       'odometer', 'transmission', 'type', 'paint_color', 'is_4wd',
       'date_posted', 'days_listed']]
car_data['condition'] = pd.Categorical(car_data['condition'], categories=['new', 'like new', 'excellent', 'good', 'fair', 'salvage'], ordered=True)
manufacturers = car_data['manufacturer'].value_counts()[car_data['manufacturer'].value_counts() > 1000].index

# Título de la aplicación
st.title('Análisis de Coches en Venta en Estados Unidos')

# Barra lateral para la configuración de la aplicación
with st.sidebar:
    st.header("Configuración")
    st.write("Selecciona opciones de visualización:")

    # Crear una casilla de verificación para mostrar el DataFrame completo
    df_button = st.checkbox('Desplegar tabla de datos')

    # Crear una casilla de verificación para el histograma
    hist_button = st.checkbox('Construir un histograma')

    # Crear una casilla de verificación para el gráfico de dispersión
    dist_button = st.checkbox('Distribución de precios por fabricante')

    # Crear una casilla de verificación para la correlación entre precio y condición
    disp_button = st.checkbox('Matriz de dispersión')

if df_button or hist_button or disp_button:
    st.success("¡Disfruta la Aplicación!")

# Lógica a ejecutar cuando se hace clic en la casilla de verificación del DataFrame
if df_button:
    # Escribir un mensaje en la aplicación
    st.subheader('Catalogo de coches en venta en Estados Unidos')
    st.write("Selecciona las condiciones de los coches que deseas visualizar:")

    # Opciones de visualización del DataFrame
    conditions = []

    col1, col2 = st.columns(2)
    with col1:
        if st.checkbox('New'):
            conditions.append('new')
        if st.checkbox('Like New'):
            conditions.append('like new')
        if st.checkbox('Excellent'):
            conditions.append('excellent')
    with col2:
        if st.checkbox('Good'):
            conditions.append('good')
        if st.checkbox('Fair'):
            conditions.append('fair')
        if st.checkbox('Salvage'):
            conditions.append('salvage')
        conditions = set(conditions)
    
    st.dataframe(car_data.query('condition in @conditions'))
    st.write(f"{len(car_data.query('condition in @conditions'))} resultados encontrados.")

# Lógica a ejecutar cuando se hace clic en el botón
if hist_button:
    # Escribir un mensaje en la aplicación
    st.subheader('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma
    # Se crea una figura vacía y luego se añade un rastro de histograma
    paleta = {'new':'purple', 'like new':"red", 'excellent':'blue', 'good':'green', 'fair':'rgb(39,125,245)', 'salvage':'rgb(220,172,15)'}
    fig = px.histogram(car_data.rename(columns={'condition': 'Condición'}),
                       x='model_year',
                       title='Distribución de los años de los coches en venta',
                       labels={'model_year': 'Año del modelo'},                       
                       color='Condición',
                       barmode='group',
                       category_orders={'Condición': ['new', 'like new', 'excellent', 'good', 'fair', 'salvage']},
                       color_discrete_map=paleta)

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Distribución por año del modelo y condición')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)

# Lógica a ejecutar cuando se hace clic en el botón
if dist_button:
    # Escribir un mensaje en la aplicación
    st.subheader('Comparando Precios de Fabricantes')

    # Crear un histograma
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = px.histogram(car_data,
                       x='price',
                       title='Distribución de precios por Fabricante'.title(),
                       labels={'price': 'Precio'},                       
                       color='type',
                       barmode='group')

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Distribución de precios por Fabricante'.title())

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)

if disp_button:
    # Escribir un mensaje en la aplicación
    st.subheader('Matriz de dispersión para analizar la relación entre precio, kilometraje y año del modelo')

    # Crear un histograma
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = px.scatter_matrix(car_data,
                            dimensions=['odometer', 'price', 'model_year'],
                            color='condition',
                            category_orders={'Condición': ['new', 'like new', 'excellent', 'good', 'fair', 'salvage']})

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Gráficos de Dispersión'.title())

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)

# Si no se ha seleccionado ninguna opción, mostrar un mensaje informativo
elif not df_button and not hist_button and not disp_button:
    st.info("Abra la barra lateral izquierda empezar a desplegar datos.")