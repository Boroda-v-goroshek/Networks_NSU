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
driver.get("https://qwind.ru/")



# Поиск страниц
with open("free/output.csv", 'w', encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter = ',')

    # раздел 1
    driver.find_element(By.XPATH, "//a[@href='https://qwind.ru/podgotovka-vozduha/']").click()
    file_writer.writerow("Блоки подготовки воздуха")
    for page in range(1, 91):
        xpath_string = f"//a[@href='https://qwind.ru/podgotovka-vozduha/?page={page}']"

        if page != 1:
            driver.find_element(By.XPATH, xpath_string).click()

        time.sleep(1)
        data = driver.find_element(By.XPATH, "//ul[@class='catalogue__products-list']")
        text = data.text.split('\n')
        
        text_list = []

        for i in range(0, len(text), 2):
            text_list.append(text[i:i+2])

        for text in text_list:
            xpath_image = f"//img[@alt='{text[0]}']"
            img = driver.find_element(By.XPATH, xpath_image)
            img_link = img.get_attribute("src")
            if img_link:
                text.append(img_link)
            file_writer.writerow(text)






input()
driver.quit()