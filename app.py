import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    response=requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US=en-US')
    data=response.json()
    print(data)
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies=[]
    recommended_movies_poster=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster

movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name=st.selectbox(
        'Movies',
        movies['title'].values)

if st.button('Recommend'):
    names,posters=recommend(selected_movie_name)

    movie1,movie2,movie3,movie4,movie5=st.columns(5)
    with movie1:
        st.text(names[0])
        st.image(posters[0])
    with movie2:
        st.text(names[1])
        st.image(posters[1])
    with movie3:
        st.text(names[2])
        st.image(posters[2])
    with movie4:
        st.text(names[3])
        st.image(posters[3])
    with movie5:
        st.text(names[4])
        st.image(posters[4])
