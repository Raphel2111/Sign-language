import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/201001 Firefox/24.0'}


res = requests.get('https://spreadthesign.com/es.es/alphabet/22/', headers=headers)


if res.status_code == 200:
   
    soup_data = BeautifulSoup(res.text, 'html.parser')
    

    main_div = soup_data.find('div', class_='main')
    if main_div:
    
        directory = 'abecedario2'
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        
        images = main_div.find_all('img')
        for image in images:
            img_url = urljoin('https://www.fundacioncnse.org/educa/bancolse/', image['src'])
            img_name = img_url.split('/')[-1]
            img_path = os.path.join(directory, img_name)
            with open(img_path, 'wb') as img_file:
                img_file.write(requests.get(img_url, headers=headers).content)
                print(f"Imagen guardada: {img_path}")
    else:
        print("No se encontró ningún div con la clase 'main'.")
else:
    print("Error al obtener la página:", res.status_code)

