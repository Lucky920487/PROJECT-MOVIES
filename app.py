import pickle
import streamlit as st
import requests
import time

# Function to fetch poster with fallback
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=4e82aa54a073d3f4f830b872e51d6d2f&language=en-US"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        poster_path = data.get("poster_path", "")
        if not poster_path:
            return None  # No poster available
        return f"https://image.tmdb.org/t/p/w500/{poster_path}"
    except:
        return None

# Recommend function with poster check
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    
    names, posters = [], []
    for i in distances[1:]:
        movie_id = movies.iloc[i[0]]['movie_id']
        poster = fetch_poster(movie_id)
        if poster:  # Only if poster fetched
            names.append(movies.iloc[i[0]].title)
            posters.append(poster)
        if len(names) == 5:  # Limit to 5
            break

    return names, posters

# Load assets
movies = pickle.load(open(r'C:\Users\lluuc\OneDrive\Desktop\PROJECT MOVIES\artifacts\movie_list.pkl', 'rb'))
similarity = pickle.load(open(r'C:\Users\lluuc\OneDrive\Desktop\PROJECT MOVIES\artifacts\similarity.pkl', 'rb'))

# UI
st.markdown("""
    <h2 style='text-align: center; font-size: 28px;'>
        🎬 Movies Recommendation System 
    </h2>
""", unsafe_allow_html=True)

movie_list = movies['title'].values
selected_movie = st.selectbox("Type or select a movie to get recommendations", movie_list)

if st.button('Show Recommendations'):
    names, posters = recommend(selected_movie)

    cols = st.columns(len(names))  # Dynamically create columns

    for idx, col in enumerate(cols):
        with col:
            st.markdown(f"""
<div style='text-align: center'>
    <img src="{posters[idx]}" style='width:100%; border-radius: 10px;'>
    <p style='font-weight: bold; margin-top: 10px;'>{names[idx]}</p>
</div>
""", unsafe_allow_html=True) 