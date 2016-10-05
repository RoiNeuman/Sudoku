#!/usr/bin/env python3
from flask import Flask, jsonify
from flask_pymongo import PyMongo

from Service.grid import createGrid

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'Sudoku'

mongo = PyMongo(app)


@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Welcome!'})


@app.route('/grid/add/<num>', methods=['GET'])
def createMaps(num):
    newGrids = []
    for _ in range(int(num)):
        newGrids.append(createGrid())
    return jsonify({'maps': newGrids})


if __name__ == '__main__':
    app.run(port=8080)
