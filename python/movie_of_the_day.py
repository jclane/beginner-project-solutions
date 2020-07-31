import requests
from bs4 import BeautifulSoup
from random import choice as rchoice


def get_random_movie():
    addr = r"https://www.themoviedb.org/movie"
    resp = requests.get(addr)
    soup = BeautifulSoup(resp.content, "html.parser")
    titles = []
    for header in soup.find_all("h2"):
        for link in header.find_all("a"):
            titles.append(link.get("title"))
    
    return rchoice(titles)

print(get_random_movie())
