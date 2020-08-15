import requests
from bs4 import BeautifulSoup as bs
import os

def download_repository():
    name = input("Enter username: ")
    r = requests.get("https://www.github.com/{}?tab=repositories".format(name))
    soup = bs(r.text,"html.parser")
    h3 = soup.findAll("h3",{"class":"wb-break-all"})
    for i in h3:
        a = i.find("a")
        path = "https://www.github.com"+a.attrs["href"]
        os.system("git clone "+path)

if __name__== "__main__":
    download_repository()