import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
time.sleep(5)
driver.get("https://stepik.org/lesson/25969/step/12")
time.sleep(5)
textarea = driver.find_element(By.XPATH,)
def test_open_project():
    driver.get("https://www.google.com/search?q=%D0%B2%D0%BA")
    driver.get("https://stepik.org/course/38218/syllabus")

driver.find_element(By.XPATH,'//li[@class="navbar__menu-item"]/a[@id="ember15"]').send_keys()
driver.implicitly_wait(60)
