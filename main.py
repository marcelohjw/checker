import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO


"""
import cv2
import numpy as np
"""


# This is how i can capture video from the webcam.
# cap = cv2.VideoCapture(0)

search = input('You want to create a database of?: ')
params = {"q": search}

r = requests.get("https://www.bing.com/images/search", params)
print("Status: ", r.status_code)

soup = BeautifulSoup(r.text, "html.parser")
links = soup.find_all("a", {"class": "iusc"})
print("Results:", len(links))

for item in links:
    img_obj = requests.get(item.attrs["href"])
    print("Getting", item.attrs["href"])
    title = item.attrs["href"].split("/")[-1]
    img = Image.open(BytesIO(img_obj.content))
    img.save("./sets/" + title, img.format)

'''
while True:
    success, img = cap.read()

    cv2.imshow('Cam', img)
    cv2.waitKey(1)
'''