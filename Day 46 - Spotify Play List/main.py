import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth


SPOTIPY_CLIENT_ID = ''
SPOTIPY_CLIENT_SECRET = ''
SPOTIPY_REDIRECT_URI = 'https://example.com'

year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

URL = f"https://www.billboard.com/charts/hot-100/{year}/"

response = requests.get(url=URL)
song_response = response.text
soup = BeautifulSoup(song_response, 'html.parser')

song_names_html = soup.select("li ul li h3")
song_name = [song.getText().strip() for song in song_names_html]

print(song_name)