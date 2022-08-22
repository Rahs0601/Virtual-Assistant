import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    try:
        url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=ecc38c6fcc39ea373b36609c896c544c'
        response = requests.get(url)
        data = response.json()
        print(data)
        poster_path = data['poster_path']
        print(poster_path)
        return "https://image.tmdb.org/t/p/w185" + poster_path
    except:
        pass


def recommend(title):
    idx = movies[movies['title'] == title].index[0]
    sim_scores = list(enumerate(similarity[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]

    recd_movies = []
    recd_movies_poster = []
    for i in sim_scores:
        movie_id = movies.iloc[i[0]].id
        recd_movies.append(movies.iloc[i[0]].title)
        recd_movies_poster.append(fetch_poster(movie_id))
    return recd_movies, recd_movies_poster


movies_dict = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("Movie Recommendation System By Rah's")

option = st.selectbox(
    'select a movie you like', movies['title'].values)

st.write('You selected:', option)

if st.button('Recommend'):
    recommend_movies, recommend_movies_poster = recommend(option)

    col0, col1, col2, col3, col4 = st.columns(5)
    with col0:
        st.text(recommend_movies[0])
        st.image(recommend_movies_poster[0])

    with col1:
        st.text(recommend_movies[1])
        st.image(recommend_movies_poster[1])

    with col2:
        st.text(recommend_movies[2])
        st.image(recommend_movies_poster[2])

    with col3:
        st.text(recommend_movies[3])
        st.image(recommend_movies_poster[3])

    with col4:
        st.text(recommend_movies[4])
        st.image(recommend_movies_poster[4])
    col5, col6, col7, col8, col9 = st.columns(5)

    with col5:
        st.text(recommend_movies[5])
        st.image(recommend_movies_poster[5])

    with col6:
        st.text(recommend_movies[6])
        st.image(recommend_movies_poster[6])

    with col7:
        st.text(recommend_movies[7])
        st.image(recommend_movies_poster[7])

    with col8:
        st.text(recommend_movies[8])
        st.image(recommend_movies_poster[8])

    with col9:
        st.text(recommend_movies[9])
        st.image(recommend_movies_poster[9])
