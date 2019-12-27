import requests
from bs4 import BeautifulSoup
from random import choice as rchoice


def get_random_movie():
    addr = r"https://www.themoviedb.org/discover/movie?sort_by=popularity.desc"
    resp = requests.get(addr)
    soup = BeautifulSoup(resp.content, "html.parser")
    titles_soup = soup.find_all("a", class_="title result")
    titles = list(title.attrs["title"] for title in titles_soup)
    return rchoice(titles)

print(get_random_title())
