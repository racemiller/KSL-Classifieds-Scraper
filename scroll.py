import requests
from bs4 import BeautifulSoup


headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

url = "https://classifieds.ksl.com/v2/search/cat/Appliances"
# url = "https://cars.ksl.com/v2/search/make/Chevrolet%3BGMC/model/2500%3BSilverado+2500HD%3BSilverado+2500%3BC%7CK+2500+Series%3BC%7CK+2500%3BSierra+2500+Classic%3BSierra/yearFrom/1999/yearTo/2006/numberDoors/4/drive/4-Wheel+Drive/fuel/Gasoline/productStatus/frontline"

response = requests.get(url, headers=headers)
html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')

with open('test-1.html', 'w', encoding='utf-8') as f:
    f.write(soup.prettify())