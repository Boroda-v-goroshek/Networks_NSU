import json

from flask import Flask, request, jsonify
import psycopg2

from my_pars import my_parser_func


app = Flask(__name__)

def write_in_bd(data_for_insert):
    connection = psycopg2.connect(
        dbname="parse_utf",
        user="Boroda-v-goroshek",
        password="RAlf2005",
        host="127.0.0.1",
        port="5432"
    )

    connection.autocommit = True
    cursor = connection.cursor()

    # SQL-запрос для вставки данных
    insert_query = "INSERT INTO dictionaries (title, other_info) VALUES (%s, %s)"

    # Выполнение вставки для каждого словаря в списке
    for item in data_for_insert:
        cursor.execute(insert_query, (item['title'], item['other_info']))

    if connection:
        cursor.close()
        connection.close()

@app.route('/parse', methods=['GET'])
def parse():
    url = request.args.get('url')
    if not url:
        return jsonify({'error': 'URL параметр обязателен'}), 400
    result = my_parser_func(url)

    # Запись в БД
    write_in_bd(result)

    # Запись в JSON
    with open('output.json', 'w', encoding='utf-8') as json_file:
        json.dump(result, json_file, ensure_ascii=False, indent=4)

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)