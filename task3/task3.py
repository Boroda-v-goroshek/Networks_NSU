import csv
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from bs4 import BeautifulSoup


# Настройка
options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--start-maximized")
driver = webdriver.Edge(options=options)
driver.get('https://hempforlife.ru/login/')


# Авторизация
driver.find_element(By.XPATH, "//input[@title='Логин']").send_keys("n.shestakov@g.nsu.ru")
driver.find_element(By.XPATH, "//input[@type='password']").send_keys("RAlf2005")
driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(1)


# Поиск страницы
driver.find_element(By.XPATH, "//div[@class='f-cookies__button']").click()
driver.find_element(By.XPATH, "//div[@data-id='83']").click()
driver.find_element(By.XPATH, "//div[@class='b-catalog__button']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//a[@href='/category/postelnye-prinadlezhnosti/']").click()
time.sleep(1)


# Сбор данных
driver.find_element(By.XPATH, "//button[@class='h-yet__show']").click()
title = driver.find_element(By.PARTIAL_LINK_TEXT, "Одеяла и подушки").text
data_list = driver.find_elements(By.XPATH, "//div[@class='products__item products__item-flying']")

# Запись в таблицу
with open("output.csv", 'w', encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter = ',')


    for data in data_list:
        text = data.text.split('\n')
        file_writer.writerow(text)

#river.quit()
input()