import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
empire_movie = response.text
soup = BeautifulSoup(empire_movie, 'html.parser')

all_movies = soup.find_all(name="h3", class_="title")
movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]


with open("movies.txt", mode="w", encoding="utf-8") as data:
    for movie in movies:
        data.write(f"{movie}\n")

