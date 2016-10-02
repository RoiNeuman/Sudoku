from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def Home():
    return jsonify({'message': 'Welcome!'})


if __name__ == '__main__':
    app.run(port=8080)
