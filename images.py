from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os


def search():
    searchImage = input("Jakie obrazki chcesz pobrać:")
    params = {"q": searchImage}
    dir_name = searchImage.replace(" ", "_").lower()

    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)
    r = requests.get("https://www.bing.com/images/search", params=params)
    bs = BeautifulSoup(r.text, "html.parser")
    link = bs.findAll("a", {"class": "thumb"})

    for item in link:
        try:
            imgObj = requests.get(item.attrs["href"])
            print("Pobieram", item.attrs["href"])
            title = item.attrs["href"].split("/")[-1]
            try:
                img = Image.open(BytesIO(imgObj.content))
                img.save("./" + dir_name + "/" + title, img.format)
            except:
                print("Nie można zapisać obrazka")
        except:
            print("Nie można wczytać obrazka")
    search()


search()
