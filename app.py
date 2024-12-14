import streamlit as st
import pandas as pd
import random

# Function to fetch Spotify link (modify based on your data source)
def fetch_spotify_link(song_id):
    return f"https://open.spotify.com/track/{song_id}"  # Modify according to your source if needed

# Load music data (replace with actual CSV path)
songs = pd.read_csv(r"C:\Users\dell\OneDrive\clutterfolder\music system\expanded_songs_dataset.csv")

# Streamlit Header with Spotify-inspired theme
st.markdown(
    """
    <style>
        body {
            background-color: #121212; /* Dark background */
            color: white; /* Light text */
            font-family: 'Arial', sans-serif;
        }
        .stButton>button {
            background-color: #1DB954; /* Green background for the button */
            color: black; /* Black text inside the button */
            border: none;
            padding: 12px 24px;
            font-size: 18px;
            font-weight: bold;
            border-radius: 30px;
            cursor: pointer;
            transition: transform 0.2s ease, background-color 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #1aa34a; /* Lighter green on hover */
            transform: scale(1.05); /* Slight zoom effect */
        }
        .stSelectbox>label {
            font-size: 18px;
            color: white;
        }
        h1 {
            color: white;  /* Set the header color to white */
            text-align: center;
            font-size: 36px;
            font-weight: bold;
        }
        .song-card {
            background-color: #1E1E1E; /* Card background */
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 10px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.3);
        }
        .song-name {
            font-size: 20px;
            font-weight: bold;
            color: white;
        }
        .artist-name {
            font-size: 16px;
            color: #bbbbbb;
        }
        .spotify-link {
            font-size: 14px;
            color: #1DB954;
            text-decoration: none;
        }
        .spotify-link:hover {
            text-decoration: underline;
        }
    </style>
    """, unsafe_allow_html=True
)

st.header("Mood-based Music Recommender")

# Dropdown for mood selection
mood_list = ['romantic', 'lofi', 'sad', 'happy', 'upbeat']
mood = st.selectbox("Select your mood", mood_list)

# Function to recommend random songs based on mood
def recommend_random_songs(mood, num_songs=5):
    filtered_songs = songs[songs['mood'] == mood]
    if len(filtered_songs) < num_songs:
        num_songs = len(filtered_songs)  # Avoid errors if there are fewer songs than requested
    recommended_songs = filtered_songs.sample(num_songs)  # Randomly select songs
    return recommended_songs[['name', 'artist', 'id']].values

# Check if the "Show Recommendations" button is clicked
if st.button("🎵 Show Recommendations",key='recommendations_button', help="Click to view the recommendations"):
    recommended_songs = recommend_random_songs(mood)

    for song in recommended_songs:
        song_name, artist_name, song_id = song
        spotify_link = fetch_spotify_link(song_id)

        # Display each song as a card
        st.markdown(
            f"""
            <div class="song-card">
                <div class="song-name">{song_name}</div>
                <div class="artist-name">by {artist_name}</div>
                <a href="{spotify_link}" target="_blank" class="spotify-link">Listen on Spotify</a>
            </div>
            """, unsafe_allow_html=True
        )









           

            



























                

















