import requests
from webbrowser import open as wbopen


def get_article():
    """Pulls JSON from wikipedia API using requests module"""
    url = ("https://en.wikipedia.org/w/api.php?action=query&list="
          "random&rnnamespace=0&rnlimit=10&format=json")
    resp = requests.get(url, headers={"User-agent": "Simple Test"})
    data = resp.json()

    if "error" not in data.keys():
        return data
    else:
        print("Error fecthing articles.")


while True:
    articles = get_article()
    for article in articles["query"]["random"]:
        resp = ""
        while resp.lower().strip() not in ("y", "yes", "n", "no"):
            resp = input("Would you like to read about " + article["title"] +
                         "? [y/n]\n>>")
        if resp.lower().strip() in ("y", "yes"):
            wbopen("https://en.wikipedia.org/wiki?curid=" +
                    str(article["id"]))
            input("Press the [enter] key to continue")
        elif resp.lower().strip() in ("n", "no"):
            continue
