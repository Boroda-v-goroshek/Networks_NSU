import csv
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from bs4 import BeautifulSoup


#object = "Носки"

options = Options()
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Edge(options=options)
driver.get('https://daitres.com')

# Авторизациz
time.sleep(1)
driver.find_element(By.XPATH, "//a[@href='https://daitres.com/my-account']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='nasa_username']").send_keys("n.shestakov@g.nsu.ru")
driver.find_element(By.XPATH, "//input[@id='nasa_password']").send_keys("RAlf2005")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(3)

# Переход к нужной странице
katalog = driver.find_element(By.XPATH, "//a[@href='https://daitres.com/muzhskie-trusy-skidki']").click()
time.sleep(3)
# Получение данных







input()
driver.quit()