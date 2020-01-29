from flask import Flask
from flask_cors import CORS
from database.connect import connect

app = Flask(__name__)
app.register_blueprint("book_blueprint")
CORS(app)

session = connect()


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4996)
