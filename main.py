"""
import cv2
import numpy as np
"""
import requests


# This is how i can capture video from the webcam.
# cap = cv2.VideoCapture(0)

r = requests.get('https://google.com.br')
print("Status: ", r.status_code)

'''
while True:
    success, img = cap.read()

    cv2.imshow('Cam', img)
    cv2.waitKey(1)
'''