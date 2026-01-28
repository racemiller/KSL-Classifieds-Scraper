from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import logging
import sys
import requests

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("chrometest.log")
        # logging.StreamHandler(sys.stdout)
    ]
)

try:

    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    # url = "https://classifieds.ksl.com/v2/search/cat/Appliances"
    url = "https://cars.ksl.com/v2/search/make/Chevrolet%3BGMC/model/2500%3BSilverado+2500HD%3BSilverado+2500%3BC%7CK+2500+Series%3BC%7CK+2500%3BSierra+2500+Classic%3BSierra/yearFrom/1999/yearTo/2006/numberDoors/4/drive/4-Wheel+Drive/fuel/Gasoline/productStatus/frontline"

    response = requests.get(url, headers=headers)
    cookies_dict = response.cookies.get_dict()  # Get any session cookies
    # html_content = response.text
    # soup = BeautifulSoup(html_content, 'html.parser')

    # Set up headless options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--no-sandbox")  # Necessary for some Linux environments
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
    chrome_options.add_argument("--remote-debugging-port=9222")  # Debugging
    chrome_options.add_argument("--disable-gpu")  # Disable GPU Hardware acceleration
    chrome_options.add_argument("window-size=1920x1080")  # Set a window size
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36")  # Custom user-agent


    # Set up the WebDriver
    service = Service('/home/race/ksl/chromedriver-linux64/chromedriver')  # Path to your chromedriver
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Load the initially retrieved HTML into Selenium
    driver.get(url)

    for cookie_name, cookie_value in cookies_dict.items():
        driver.add_cookie({'name': cookie_name, 'value': cookie_value})

    driver.refresh()

    time.sleep(5)  # Wait for the page to load

    # Scroll down a few times to load content
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll to bottom of page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait for new content to load
        time.sleep(2) 
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Get the entire HTML of the page after scrolling
    final_html_content = driver.page_source

    # Output the HTML content
    # print(html_content)
    # with open('test-1.html', 'w', encoding='utf-8') as f:
    #     f.write(html_content)

    driver.quit()

    final_soup = BeautifulSoup(final_html_content, 'html.parser')
    
    # links = soup.find_all('a')
    # for link in links:
    #     print(link.text)

    # data = ''
    # for data in soup.find_all('a'):
    #     print(data.get_text())

    with open('test-1.html', 'w', encoding='utf-8') as f:
        f.write(final_soup.prettify())

except Exception as e:
    logging.error(f"An error occurred: {e}")