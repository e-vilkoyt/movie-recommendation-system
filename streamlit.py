import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from ast import literal_eval
import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")  # Obtén tu API Key desde el archivo .env

# Cachear la carga de datos
@st.cache_data  
def load_data():
    new_df = pd.read_csv('new_df_with_embeddings.csv')
    new_df['embedding'] = new_df['embedding'].apply(literal_eval)  # Convertir la columna de embeddings
    return new_df

new_df = load_data()

# Calcular y cachear la matriz de similitud 
@st.cache_data  
def compute_similarity_matrix(df):
    similarity_matrix = cosine_similarity(list(df['embedding'].apply(np.array)))
    return pd.DataFrame(similarity_matrix, index=df['title'], columns=df['title'])

similarity_df = compute_similarity_matrix(new_df)

# Función para obtener recomendaciones
def get_similar_movies(movie_title, n=5):
    if movie_title not in similarity_df.index:
        return f"La película '{movie_title}' no se encuentra en la base de datos."
    return similarity_df[movie_title].sort_values(ascending=False).index[1:n + 1]

# Función para obtener el poster de la película
def get_movie_poster(movie_title):
    search_url = f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_title}'
    response = requests.get(search_url)

    if response.status_code == 200:
        data = response.json()
        if data['results']:
            return f'https://image.tmdb.org/t/p/w500{data["results"][0]["poster_path"]}'
    return None

# Mostrar la imagen en la parte superior
st.image('wp1945939.jpg', use_column_width=True)

# Establecer el estilo para el fondo
st.markdown(
    """
    <style>
    body {
        background-color: #f0f8ff;  /* Color de fondo suave (Alice Blue) */
        margin: 0;
        padding: 0;
        overflow-x: hidden;  /* Evita el desbordamiento horizontal */
    }
    .main {
        background-color: rgba(255, 255, 255, 0.8);  /* Fondo blanco semi-transparente para los elementos */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título de la aplicación
st.title("El Sabio del Cine: recomendaciones de películas que no puedes ignorar")

# Selector para elegir o escribir el título de la película
movie_title = st.selectbox(
    "Escribe o selecciona el título de la película:",
    options=[""] + list(new_df['title']),
    format_func=lambda x: "" if x == "" else x
)

# Botón para obtener recomendaciones
if st.button("Obtener recomendaciones"):
    if movie_title and movie_title in new_df['title'].values:
        recommendations = get_similar_movies(movie_title)
        st.write("Películas recomendadas:")

        # Crear columnas para mostrar los posters en fila
        cols = st.columns(len(recommendations))
        for col, movie in zip(cols, recommendations):
            poster_url = get_movie_poster(movie)
            if poster_url:
                col.image(poster_url, caption=movie, use_column_width='auto')
            else:
                col.write(f"No se encontró el poster para {movie}")
    else:
        st.error("Por favor, selecciona o ingresa un título de película válido.")
