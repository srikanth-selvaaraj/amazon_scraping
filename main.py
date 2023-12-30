import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# old method
# os.environ['PATH'] = r"/home/srikanth/Downloads/chromedriver-linux64"
# driver = webdriver.Chrome()

# new method
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# open the browser in background
options = webdriver.ChromeOptions()
options.add_argument('--headless')

# Base URL
driver.get('https://www.amazon.in/')

# fields to search
search_input_field = driver.find_element(By.ID, 'twotabsearchtextbox')
search_button = driver.find_element(By.ID, 'nav-search-submit-button')

# enter the product name in search field
search_input_field.send_keys('redmi note 8')
driver.save_screenshot('screenshots/search_field.png')

# click the search button
action = ActionChains(driver)
action.click(on_element=search_button)
action.perform()
driver.save_screenshot('screenshots/searched.png')

items = driver.find_elements(By.XPATH, '//div[@class="sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16"]')

product_names = []
product_asins = []

for item in items:
    name = item.find_element(By.XPATH, './/span[@class="a-size-medium a-color-base a-text-normal"]')
    asins = item.get_attribute('data-asin')
    product_asins.append(asins)
    product_names.append(name.text)

# saving data
# product names
file = open('product_names.txt', 'w')
file.writelines('\n'.join(product_names))

# asis
file = open('product_asins.txt', 'w')
file.writelines('\n'.join(product_asins))

# quit the driver
driver.quit()
