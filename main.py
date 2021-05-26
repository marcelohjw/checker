from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import requests

search_url = 'https://bing.com/images/search'
keywords = ['cars']
params = {'q': '+'.join(keywords)}

r = requests.get(search_url, params)

soap = BeautifulSoup(r.text, 'html.parser')

images = soap.find_all('img', {'class': 'mimg'})
numbery = len(images)
print("Getting " + str(numbery) + " images...")

count = 1
for img in images:
    src = img['src']
    img_obj = requests.get(src)

    img = Image.open(BytesIO(img_obj.content))
    format4 = img.format
    img.save(f'{count}.{format4.lower()}', img.format)
    count += 1
