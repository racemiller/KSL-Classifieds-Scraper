# import module 
import requests 
from bs4 import BeautifulSoup 
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

url = "https://cars.ksl.com/v2/search/make/Chevrolet%3BGMC/model/2500%3BSilverado+2500HD%3BSilverado+2500%3BC%7CK+2500+Series%3BC%7CK+2500%3BSierra+2500+Classic%3BSierra/yearFrom/1999/yearTo/2006/numberDoors/4/drive/4-Wheel+Drive/fuel/Gasoline/productStatus/frontline"
# url = "https://classifieds.ksl.com/v2/search/cat/Appliances"
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
# names = [a.get_text() for a in soup.find_all('a') if a.get_text()]
# df = pd.DataFrame(names, columns=['Names'])

# df.to_csv('names.csv', index=False, header=False, encoding='utf-8')

# link to extract html data 
# def getdata(url): 
#     r = requests.get(url) 
#     return r.text 

with open('test-1.html', 'w', encoding='utf-8') as f:
    f.write(soup.prettify())

# for data in soup.find_all('a'):
#     print(data.get_text(separator=' '))

# for data in soup.find_all('a'):
#     with open('test.csv', 'a', encoding='utf-8') as f:
#         f.write(data.get_text(' '))

# data = '' 
# for data in soup.find_all('p'): 
#     print(data.get_text())