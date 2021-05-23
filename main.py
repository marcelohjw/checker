import requests
from bs4 import BeautifulSoup


"""
import cv2
import numpy as np
"""


# This is how i can capture video from the webcam.
# cap = cv2.VideoCapture(0)

search = input('You want to create a database of?: ')
params = {"q": search}

r = requests.get("http://www.bing.com/search", params=params)
print("Status: ", r.status_code)
soup = BeautifulSoup(r.text, "html.parser")
print(soup.prettify())

'''
while True:
    success, img = cap.read()

    cv2.imshow('Cam', img)
    cv2.waitKey(1)
'''