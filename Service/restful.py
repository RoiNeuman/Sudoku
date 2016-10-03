from flask import Flask, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'Sudoku'

mongo = PyMongo(app)


@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Welcome!'})


if __name__ == '__main__':
    app.run(port=8080)
