#!/usr/bin/env python3
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

from Service.grid import createGrid
from Service.grid import levelGrid

# Initialize the Flask application
app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'Sudoku'

mongo = PyMongo(app)


# Define a route for the default URL
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
        newGrids.append(dumps(grids.find_one({'_id': grid_id}, projection={'_id': False})))
    return jsonify({'maps': newGrids})


@app.route('/game/start/<level>', methods=['GET'])
def getMap(level):
    """Return a random sudoku grid with a given number of elements on the grid.
    The level parameter stand for the wanted number of elements in the map.
    A 0 on the grid represent no-parameter.
    """
    grids = mongo.db.grids
    grid = [d for d in grids.aggregate([{'$sample': {'size': 1}}])][0]
    return jsonify({'_id': str(grid['_id']), 'grid': levelGrid(grid, level)})


@app.route('/game/check', methods=['POST'])
def checkNumber():
    """Checks if a given number match the number in a given coordinate in a given grid.
    The request contain the _id of the grid.
    The id is used for making the query to the DB.
    the DB returned the wanted grid."""
    grids = mongo.db.grids
    content = request.get_json(force=True)
    grid = grids.find_one({'_id': ObjectId(content['id'])})['grid']
    if grid[content['row']][content['column']] == content['number']:
        return jsonify({'success': True})
    else:
        return jsonify({'success': False})

# Run the app.
if __name__ == '__main__':
    app.run(port=8080, debug=False)
