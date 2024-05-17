from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Specify the path to the ChromeDriver executable
chrome_driver_path = '/path/to/chromedriver'

# Set up Chrome options (optional)
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run in headless mode (no GUI)

# Set up the WebDriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open a webpage
driver.get('https://www.example.com')

# Print the title of the page
print(driver.title)

# Close the browser
driver.quit()
