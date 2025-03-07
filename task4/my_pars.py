import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options


def my_parser_func(url):
    # Настройка
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--start-maximized")
    driver = webdriver.Edge(options=options)
    driver.get(url)


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
    data_list = driver.find_elements(By.XPATH, "//div[@class='products__item products__item-flying']")

    products_data = []

    for data in data_list:
        product_info = data.text.split('\n')

        product_info.remove(product_info[-1])
        if (len(product_info[0]) <= 3):
            product_info.remove(product_info[0])
            product_info.remove(product_info[0])

        if (len(product_info[0]) <= 4):
            product_info.remove(product_info[0])
        
        products_data.append({
            'title': product_info[0], 
            'other_info': product_info[1:],
        })
   
    driver.quit()
    return(products_data)