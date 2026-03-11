import streamlit as st
import pandas as pd

st.set_page_config(page_title="Movie Recommendation System", page_icon="🎬")

# Movie Class
class Movie:
    def __init__(self, name, genre, rating):
        self.name = name
        self.genre = genre
        self.rating = rating


# Store movies
if "movies" not in st.session_state:
    st.session_state.movies = []


st.title("🎬 Movie Recommendation System")

menu = st.sidebar.selectbox(
    "Menu",
    ["Add Movie", "View Movies", "Search Movie", "Top Rated Movies"],
    key="menu"
)

# -------- Add Movie --------
if menu == "Add Movie":

    st.subheader("➕ Add New Movie")

    name = st.text_input("Movie Name", key="movie_name")
    genre = st.text_input("Genre", key="genre")
    rating = st.slider("Rating", 1, 10, key="rating")

    if st.button("Add Movie", key="add_movie_btn"):
        movie = Movie(name, genre, rating)
        st.session_state.movies.append(movie)
        st.success("Movie added successfully 🎉")


# -------- View Movies --------
elif menu == "View Movies":

    st.subheader("📋 Movie List")

    if st.session_state.movies:

        data = {
            "Movie": [m.name for m in st.session_state.movies],
            "Genre": [m.genre for m in st.session_state.movies],
            "Rating": [m.rating for m in st.session_state.movies],
        }

        df = pd.DataFrame(data)

        st.dataframe(df)

    else:
        st.warning("No movies added yet")


# -------- Search Movie --------
elif menu == "Search Movie":

    st.subheader("🔍 Search Movie")

    search_name = st.text_input("Enter Movie Name", key="search_movie")

    if st.button("Search", key="search_btn"):

        found = False

        for movie in st.session_state.movies:
            if movie.name.lower() == search_name.lower():
                st.success("Movie Found")
                st.write("🎬 Name:", movie.name)
                st.write("🎭 Genre:", movie.genre)
                st.write("⭐ Rating:", movie.rating)
                found = True

        if not found:
            st.error("Movie not found")


# -------- Top Rated Movies --------
elif menu == "Top Rated Movies":

    st.subheader("🏆 Top Rated Movies")

    if st.session_state.movies:

        data = {
            "Movie": [m.name for m in st.session_state.movies],
            "Genre": [m.genre for m in st.session_state.movies],
            "Rating": [m.rating for m in st.session_state.movies],
        }

        df = pd.DataFrame(data)

        top_movies = df.sort_values(by="Rating", ascending=False)

        st.dataframe(top_movies)

        st.bar_chart(top_movies.set_index("Movie")["Rating"])

    else:
        st.warning("No movies available")