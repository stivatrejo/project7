import pandas as pd
import plotly.express as px
import streamlit as st

# Lee los datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado principal
st.header('Dashboard interactivo: Análisis de vehículos')

# Casilla de verificación para gráficos
if st.checkbox('Histograma del Kilometraje'):
    fig_odometer = px.histogram(car_data, x='odometer',  
                                title='Distribución del Kilometraje (Odometer)', 
                                labels={'odometer': 'Kilometraje (millas)'}, 
                                nbins=50)
    st.plotly_chart(fig_odometer, use_container_width=True)

if st.checkbox('Histograma del Precio'):
    fig_price = px.histogram(car_data, x='price',  
                             title='Distribución del Precio de los Vehículos', 
                             labels={'price': 'Precio (USD)'}, 
                             nbins=50)
    st.plotly_chart(fig_price, use_container_width=True)

if st.checkbox('Histograma Precio según Condición'):
    fig_price_condition = px.histogram(car_data, x='price', color='condition',
                                       title='Distribución del Precio según la Condición',
                                       labels={'price': 'Precio (USD)', 'condition': 'Condición'},
                                       barmode='overlay',
                                       opacity=0.7)
    st.plotly_chart(fig_price_condition, use_container_width=True)

if st.checkbox('Histograma Año del Modelo'):
    fig_model_year = px.histogram(car_data, x='model_year',
                                  title='Distribución del Año del Modelo',
                                  labels={'model_year': 'Año del modelo'},
                                  nbins=30)
    st.plotly_chart(fig_model_year, use_container_width=True)

if st.checkbox('Dispersión Año vs Precio'):
    fig_year_price = px.scatter(car_data, x='model_year', y='price',
                                title='Año del Modelo vs Precio',
                                labels={'model_year': 'Año del modelo', 'price': 'Precio (USD)'},
                                color='condition',
                                opacity=0.7)
    st.plotly_chart(fig_year_price, use_container_width=True)

if st.checkbox('Dispersión Año vs Kilometraje'):
    fig_year_odometer = px.scatter(car_data, x='model_year', y='odometer',
                                   title='Año del Modelo vs Kilometraje',
                                   labels={'model_year': 'Año del modelo', 'odometer': 'Kilometraje (millas)'},
                                   color='condition',
                                   opacity=0.7)
    st.plotly_chart(fig_year_odometer, use_container_width=True)

