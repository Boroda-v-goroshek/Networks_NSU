import psycopg2
from psycopg2 import sql


try:
    connection = psycopg2.connect(
        dbname="parse_db",
        user="Boroda-v-goroshek",
        password="RAlf2005",
        host="127.0.0.1",
        port="5432"
    )

    connection.autocommit = True
    cursor = connection.cursor()

    # SQL-запрос для вставки данных
    insert_query = "INSERT INTO your_table_name (title, other_info) VALUES (%s, %s)"

    # Выполнение вставки для каждого словаря в списке
    for item in data_to_insert:
        cursor.execute(insert_query, (item['title'], item['other_info']))

except Exception as error:
    print("Ошибка при создании базы данных:", error)
finally:
    if connection:
        cursor.close()
        connection.close()
