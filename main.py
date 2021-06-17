import PySimpleGUI as sg
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import requests

run = True

while run:
    layoutInit = [[sg.T('O que você deseja obter?')],
              [sg.I()],
              [sg.Ok(), sg.Cancel()]]

    search_url = 'https://bing.com/images/search'

    first_window = sg.Window('Checker V1', layoutInit)
    event, keyword = first_window.read(close=True)

    params = {'q': '+' + str(keyword[0])}

    r = requests.get(search_url, params)

    soap = BeautifulSoup(r.text, 'html.parser')

    images = soap.find_all('img', {'class': 'mimg'})
    numpery = len(images)

    layoutMid = [[sg.T("Obtendo " + str(numpery) + " " + str(keyword[0]) + "...")]]
    mid_window = sg.Window('Checker V1', layoutMid, size=(250, 50))
    mid = mid_window.read()

    count = 1
    for img in images:
        src = img['src']
        img_obj = requests.get(src)
        print("Obtendo " + str(keyword[0] + " " + str(count)))
        img = Image.open(BytesIO(img_obj.content))
        format4 = img.format
        img.save(f'images/{keyword[0]}{count}.{format4.lower()}', img.format)
        count += 1

    layoutEnd = [[sg.T('Finalizado, verifique a pasta imagens!')],
                 [sg.T('Repetir processo?')],
                 [sg.Ok(), sg.Cancel()]]
    window = sg.Window('Checker V1', layoutEnd)
    final = window.read()
    if final[0] == 'Ok':
        window.close()
        continue
    else:
        window.close()
        break
