import requests
import csv
import os.path
from time import sleep


class Fact:
    def __init__(self, data):
        self.post = data['data']['children'][0]['data']
        self.id = self.post['id']
        self.title = self.post['title'].replace("TIL", "").strip()
        self.url = self.post['url']
        
        if self.title.startswith("about"):
            self.title = self.title.replace("about", "", 1).strip()

        if self.title.startswith("that"):
            self.title = self.title.replace("that", "", 1).strip()
            
        if self.title.startswith(","):
            self.title = self.title.replace(",", "", 1).strip()
            
        if self.title.startswith("of"):
            self.title = self.title.replace("of", "", 1).strip()
            
        if not self.title.endswith("."):
            self.title = self.title + "."
            
        self.title = self.title[0].upper() + self.title[1:]
        
    def show(self):
        print("\nFACT:")
        print("\n" + self.title)
        print("\n" + self.url + "\n")


def save_fact(data):
    file_path = "facts.csv"

    if os.path.exists(file_path):
        with open(file_path, "a", newline='', encoding="UTF8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(data)
    else:
        with open(file_path, "w", newline='', encoding="UTF8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(data)


def check_for_duplicates(title):
    file_path = "facts.csv"

    if os.path.exists(file_path):
        with open(file_path, "r", encoding="UTF8") as csvfile:
            reader = csv.reader(csvfile, quotechar='"')
            for row in reader:
                if title == row[0]:
                    return True
                else:
                    continue
    else:
        return False
        

def get_fact():
    url = "https://www.reddit.com/r/todayilearned/new/.json"
    resp = requests.get(url, headers={'User-agent': 'Simple Test'})
    data = resp.json()
    
    if 'error' not in data.keys():
        return data
    else:
        print("Error fetching fact.")


while True:
    fact = Fact(get_fact())
        
    if not check_for_duplicates(fact.title):
        fact.show()
        save_fact([fact.title, fact.url])
        
    sleep(60)
