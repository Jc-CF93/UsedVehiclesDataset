# Importar paquetes
import streamlit as st
import pandas as pd
import plotly.express as px

# Leer el dataframe
df_cars = pd.read_csv('vehicles_us.csv')


st.header("Venta de vehículos usados")
st.subheader("DataFrame")
st.dataframe(df_cars)


st.subheader("Histográma")
hist_checkbox = st.checkbox('Construir histográma')

if hist_checkbox:
    st.write('Histográma de cantidad de vehículos por año del modelo')

    # crear un histograma
    fig = px.histogram(df_cars, x="model_year", labels={
                       "model_year": "Año del modelo", "count": "Cantidad de vehículos"})

    fig.update_layout(yaxis_title="Cantidad de vehículos")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


st.subheader('Gráfico de dispersión')
df_year_price = df_cars.groupby('model_year')['price'].mean()
df_year_price = df_year_price.reset_index()
df_year_price['model_year'] = df_year_price['model_year'].astype(int)
df_year_price['price'] = df_year_price['price'].astype(int)

disp_button = st.button('Crear gráfico de dispersión')

if disp_button:
    st.write(
        'Gráfico de dispersión del precio promedio por año del modelo')

    fig_disp = px.scatter(
        x=df_year_price['model_year'],
        y=df_year_price['price'],
        labels={"x": "Año del modelo", "y": "Precio"})
    st.plotly_chart(fig_disp, use_container_width=True)
