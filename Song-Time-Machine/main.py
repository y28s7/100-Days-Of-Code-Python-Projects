import os

from bs4 import BeautifulSoup
import requests
import spotipy
from dotenv import load_dotenv
load_dotenv(dotenv_path=r"C:\Users\shahn\Python Code\Pycharm Env Vars\spotipy-keys.env")

SPOTIPY_CLIENT_ID = os.environ["SPOTIPY_CLIENT_ID"]
SPOTIPY_CLIENT_SECRET = os.environ["SPOTIPY_CLIENT_SECRET"]
SPOTIPY_REDIRECT_URI = "http://example.com"

date = input("What date would you like to travel back to? Enter the date in the input YYYY-MM-DD: ")
url = f"https://www.billboard.com/charts/hot-100/{date}"
html_code = requests.get(url).text
soup = BeautifulSoup(html_code, "html.parser")

song_names = [song.getText().strip() for song in soup.select("h3.c-title.a-no-trucate")]

# Creating the Spotipy Object
sp = spotipy.Spotify(
    auth_manager=spotipy.SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=SPOTIPY_REDIRECT_URI,  # Your URI
        client_id=SPOTIPY_CLIENT_ID,  # YOUR CLIENT ID
        client_secret=SPOTIPY_CLIENT_SECRET,  # Your Client Secret
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]

song_uris = []
date = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{date}", type="track")
    #print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
