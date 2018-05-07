#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import os, shoppinglist

app = Flask(__name__)

app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME', None)
app.config['MONGO_URI'] = os.environ.get('MONGO_URI', None)

mongo = PyMongo(app)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    # app.run(debug=True)
