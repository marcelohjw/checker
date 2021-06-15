import PySimpleGUI as sg
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import requests

layoutInit = [[sg.T('What you want to get?')],
          [sg.I()],
          [sg.Ok(), sg.Cancel()]]

search_url = 'https://bing.com/images/search'

first_window = sg.Window('Checker V1', layoutInit)
event, keyword = first_window.read(close=True)

# keyword = sg.popup_get_text('What you want to get?', size=(100, 200))
params = {'q': '+' + str(keyword[0])}

r = requests.get(search_url, params)

soap = BeautifulSoup(r.text, 'html.parser')

images = soap.find_all('img', {'class': 'mimg'})
numpery = len(images)

layoutMid = [[sg.T("Getting " + str(numpery) + " " + str(keyword[0]) + " images...")]]
mid_window = sg.Window('Checker V1', layoutMid)
mid = mid_window.read()
# sg.popup("Getting " + str(numpery) + " " + str(keyword[0]) + " images...")

count = 1
for img in images:
    src = img['src']
    img_obj = requests.get(src)
    print("Getting the " + str(count) + " " + str(keyword[0]))
    img = Image.open(BytesIO(img_obj.content))
    format4 = img.format
    img.save(f'images/{keyword[0]}{count}.{format4.lower()}', img.format)
    count += 1
# sg.popup("Finished! Check the images folder!", background_color='Green')

layoutEnd = [[sg.T('Done! Check your images folder!')]]
window = sg.Window('Checker V1', layoutEnd)
final = window.read()
