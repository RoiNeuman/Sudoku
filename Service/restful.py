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


@app.route('/grid/create/<num>', methods=['GET'])
def createMaps(num):
    grids = mongo.db.grids
    newGrids = []
    for _ in range(int(num)):
        grid = createGrid()
        grid_id = grids.insert({'grid': grid})
        newGrids.append(grids.find_one({'_id': grid_id}))
    return jsonify({'maps': grid})


if __name__ == '__main__':
    app.run(port=8080)
