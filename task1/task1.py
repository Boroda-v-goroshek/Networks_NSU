import subprocess
import csv


site_list = ['Google.com', 'Yandex.ru', 'dzen.ru', 'vk.com', 'youtube.com', 'mail.ru', 'ozon.ru', 'ok.ru', 'wildberries.ru', 'mangalib.me']

with open("output.csv", mode="w", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter = ",")
    file_writer.writerow(["Сайт", " Время"])
    
    for site in site_list:
        # С помощью subprocess.run() пингуем каждый из сайтов (в аргументах функции передана командная строка и параметры для ввода в нее)
        ping = subprocess.run(['cmd', '/c', 'ping ' + site], capture_output=True, text=True)

        text = str(ping)
        
        # Разбиваем весь текст по запятым, после чего берем нужную нам подстроку и разбиваем её по пробелам
        split_text = text.split(',')
        line_in_ping = (split_text[len(split_text) - 2]).split(' ')

        file_writer.writerow([site, line_in_ping[3]])
        print(site + ": " + line_in_ping[3])
