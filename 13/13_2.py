"""Esimerkiksi EFHK-koodia vastaava GET-pyyntö annetaan muodossa:
 http://127.0.0.1:3000/kenttä/EFHK. Vastauksen on oltava muodossa:
  {"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}"""


import mysql.connector
from flask import Flask, Response
import json


connection = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user='root',
         password='tikape',
         collation='utf8mb4_general_ci',
         autocommit=True
         )

#icao for testing: zw-0039, FVCD, ZM-0041, VE-0200, WDA, NVVI, FAQR

app = Flask(__name__)
@app.route('/kenttä/<icao>')
def get_name_and_city(icao):
    try:
        sql = f"select name, municipality from airport where ident='{icao}'"
        cursor = connection.cursor()
        cursor.execute(sql)

        result = cursor.fetchall()

        status = 200
        response = {
            "status": status,
            "ICAO": icao,
            "Name": result[0][0],
            "Municipality": result[0][1]
        }

    except ValueError:
        status = 400
        response = {
            "status": status,
            "message": "Invalid ICAO"
        }

    json_resp = json.dumps(response)
    return Response(response=json_resp, status=status, mimetype="application/json")

@app.errorhandler(404)
def page_not_found(error_code):
    response = {
        "status" : "404",
        "message": "Invalid ICAO"
    }
    json_resp = json.dumps(response)
    return Response(response=json_resp, status=404, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)

