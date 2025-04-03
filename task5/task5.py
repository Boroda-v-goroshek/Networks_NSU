import json

from flask import Flask, request, jsonify
import psycopg2


app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        dbname="task5",
        user="postgres",
        password="122122",
        host="task5-cont",
        port="5432"
    )

def write_in_bd(data_for_insert):
    connection = get_db_connection()
    connection.autocommit = True
    cursor = connection.cursor()
    insert_query = "INSERT INTO dictionaries (url) VALUES (%s)"
    cursor.execute(insert_query, (data_for_insert,))
    cursor.close()
    connection.close()

def get_all_urls():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT id, url, created_at FROM dictionaries ORDER BY created_at DESC")
    urls = cursor.fetchall()
    cursor.close()
    connection.close()
    return [{"id": row[0], "url": row[1], "created_at": row[2]} for row in urls]

@app.route('/parse', methods=['GET'])
def parse():
    url = request.args.get('url')
    if not url:
        return jsonify({'error': 'URL parameter is required'}), 123
    
    write_in_bd(url)
    
    with open('output.json', 'w', encoding='utf-8') as json_file:
        json.dump({"url": url}, json_file, ensure_ascii=False, indent=4)
    
    return jsonify({"status": "success", "url": url})

@app.route('/urls', methods=['GET'])
def get_urls():
    try:
        urls = get_all_urls()
        return jsonify({"urls": urls})
    except Exception as e:
        return jsonify({"error": str(e)}), 321

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=4000)