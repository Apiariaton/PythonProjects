from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
website_content = response.text

soup = BeautifulSoup(website_content,"html.parser")

scraped_movie_titles = soup.select(selector="h3.title")
movie_titles = []

for scraped_movie_title in scraped_movie_titles:
    movie_titles.append(scraped_movie_title.text)

movie_titles.reverse()

with open("top_100_movies.txt", encoding="utf-8",mode="w") as movie_list:
    for movie_title in movie_titles:
        movie_list.write(movie_title + "\n")

print(movie_titles)