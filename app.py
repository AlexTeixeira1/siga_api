import os
from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/')
def app():
    if request.headers.get('Authorization') == '42':
        return jsonify({"42": "a resposta para a vida, o universo e tudo mais"})
    return jsonify({"message": "Não entre em pânico!"})

if __name__ == "__main__":
    app.run()
