import requests
from bs4 import BeautifulSoup
import spotipy
from pprint import pprint

URL = "https://www.billboard.com/charts/hot-100/"
SPOTIFY_ID = "enter_spotify_id"
SPOTIFY_KEY = "enter_spotify_token"

# test date
# date = "2020-07-22"
date = input("Which date you want to travel to? Type the date in this format YYYY-MM-DD:\n")

response = requests.get(URL + date + "/")

soup = BeautifulSoup(response.text, "html.parser")

top100_songs = [artist.getText().strip() for artist in soup.select(selector=".o-chart-results-list-row-container ul li ul li .c-title")]
soup.select(selector=".o-chart-results-list-row-container ul li ul li .c-label")
top100_artists_unfiltered = soup.select(selector=".o-chart-results-list-row-container ul li ul li .c-label")
top100_artists = [top100_artists_unfiltered[item].getText().strip() for item in range(0, len(top100_artists_unfiltered)-1,7)]

print("Connecting to spotify.")
sp = spotipy.Spotify(
        auth_manager = spotipy.oauth2.SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri="http://www.example.com/", 
            client_id=SPOTIFY_ID, 
            client_secret=SPOTIFY_KEY, 
            show_dialog=True,
            cache_path="token.txt"
        )
)

user_id = sp.current_user()["id"]
#print(sp.current_user())

print(f"Creating new playlist: {date} Billboard Hot 100.")
playlist_id = sp.user_playlist_create(user=user_id, name=f"{date} Billboard Hot 100", public=False)["id"]

print("Adding songs to playlist.")
song_list = []
for item in range(len(top100_artists)-1):
    song = sp.search(q=f"track: {top100_songs[item]} year: {date.split('-')[0]}", limit=1)
    # print(f"Adding {song['tracks']['items'][0]['name']}")
    try:
        song_list.append(song["tracks"]["items"][0]["id"])
    except KeyError:
        print(f"Song {top100_songs[item]} not found.")
        continue

sp.playlist_add_items(playlist_id=playlist_id, items=song_list)