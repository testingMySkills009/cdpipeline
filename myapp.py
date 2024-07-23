from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message='Welcome to my Flask app!')

@app.route('/hello/<name>')
def hello(name):
    return jsonify(message=f'Hello, {name}!')

if __name__ == '__main__':
    app.run(debug=True)
