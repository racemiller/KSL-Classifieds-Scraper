from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

# Set up headless options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")  # Necessary for some Linux environments
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
chrome_options.add_argument("--remote-debugging-port=9222")  # Debugging
chrome_options.add_argument("--disable-gpu")  # Disable GPU Hardware acceleration
chrome_options.add_argument("window-size=1920x1080")  # Set a window size

# Set up the WebDriver
service = Service('/home/race/ksl/chromedriver-linux64/chromedriver')  # Path to your chromedriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the target webpage
driver.get("https://cars.ksl.com/v2/search/make/Chevrolet%3BGMC/model/2500%3BSilverado+2500HD%3BSilverado+2500%3BC%7CK+2500+Series%3BC%7CK+2500%3BSierra+2500+Classic%3BSierra/yearFrom/1999/yearTo/2006/numberDoors/4/drive/4-Wheel+Drive/fuel/Gasoline/productStatus/frontline")

# Initialize scrolling logic
last_height = driver.execute_script("return document.body.scrollHeight")
scroll_pause_time = 2  # Pause time for loading content
new_content_loaded = True

while new_content_loaded:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(scroll_pause_time)
    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height == last_height:
        new_content_loaded = False
    last_height = new_height

# Scrape content, e.g., links
links = driver.find_elements(By.TAG_NAME, 'a')
for link in links:
    print(link.text)

# Close the browser
driver.quit()
