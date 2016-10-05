#!/usr/bin/env python3
from flask import Flask, jsonify
from flask_pymongo import PyMongo

from Service.grid import createGrid
from Service.grid import levelGrid

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'Sudoku'

mongo = PyMongo(app)


@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Welcome!'})


@app.route('/grid/create/<num>', methods=['GET'])
def createMaps(num):
    """Generate new sudoku grid, insert it into the DB and returned it."""
    grids = mongo.db.grids
    newGrids = []
    for _ in range(int(num)):
        grid = createGrid()
        grid_id = grids.insert({'grid': grid})
        newGrids.append(grids.find_one({'_id': grid_id}))
    return jsonify({'maps': grid})


@app.route('/game/start/<level>', methods=['GET'])
def getMap(level):
    """Return a random sudoku grid with a given number of elements on the grid.
    The level parameter stand for the wanted number of elements in the map.
    A 0 on the grid represent no-parameter.
    """
    grids = mongo.db.grids
    grid = [d for d in grids.aggregate([{'$sample': {'size': 1}}])][0]
    return jsonify({'_id': str(grid['_id']), 'grid': levelGrid(grid, level)})


if __name__ == '__main__':
    app.run(port=8080)
