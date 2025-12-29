from flask import Flask, request
from datetime import datetime as dt
from executequery import executeQuery

server = Flask(__name__)

@server.route('/', methods=['GET'])
def homepage():
    return "This is a homepage"

@server.route('/humidity', methods=['POST'])
def create_temperature():
    flag=1
    if(flag):
        query = f"""
INSERT INTO  feild_information (id,moisture_lvl, date_time)
VALUES (1,0, '{dt.now()}');
"""

        executeQuery(query=query)
        flag=0

    humidity = request.get_json().get('humidity')
    query=f"update feild_information SET moisture_lvl={humidity} where id=1;"
    executeQuery(query=query)
    print(f"humidity = {humidity}")

    return "humidity is received"

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=4000, debug=True)