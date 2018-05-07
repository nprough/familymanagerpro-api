#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import os

app = Flask(__name__)

app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME', None)
app.config['MONGO_URI'] = os.environ.get('MONGO_URI', None)

mongo = PyMongo(app)

# Shopping List
@app.route('/shoppinglist', methods=['GET'])
def get_items():
    items = mongo.db.shoppinglist
    output = []
    for i in items.find():
        output.append({'name': i['name'],'_id':str(i['_id'])})
    return jsonify({'items': output})

@app.route('/shoppinglist/<item_id>', methods=['GET'])
def get_item(item_id):
    items = mongo.db.shoppinglist
    output = ""
    for i in items.find():
        if str(i['_id']) == item_id:
            output = i
    if (output == ""):
        abort(404)
    return jsonify({'item': {'name': output['name'],'_id':str(output['_id'])}})

@app.route('/shoppinglist', methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        abort(400)
    newitem = {'name': request.json['name']}
    mongo.db.shoppinglist.insert_one(newitem)
    return jsonify({'new_item': {'name': request.json['name']}}), 201

@app.route('/shoppinglist', methods=['PUT'])
def update_item():
    items = mongo.db.shoppinglist
    if not request.json or not 'name' in request.json:
        abort(400)
    mongo.db.shoppinglist.update_one({'_id': ObjectId(request.json['id'])},{"$set": {'name': request.json['name']}}, True)
    return jsonify({'item': {'_id': request.json['id'], 'name': request.json['name']}})

@app.route('/shoppinglist/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    mongo.db.shoppinglist.delete_one({'_id': ObjectId(task_id)})
    return jsonify({'deleted': True})

# Task List
@app.route('/tasklist', methods=['GET'])
def get_tasks():
    items = mongo.db.tasklist
    output = []
    for i in items.find():
        output.append({'name': i['name'],'_id':str(i['_id'])})
    return jsonify({'tasks': output})

@app.route('/tasklist/<task_id>', methods=['GET'])
def get_tasks(task_id):
    tasks = mongo.db.tasklist
    output = ""
    for i in tasks.find():
        if str(i['_id']) == task_id:
            output = i
    if (output == ""):
        abort(404)
    return jsonify({'task': {'name': output['name'],'_id':str(output['_id'])}})

@app.route('/tasklist', methods=['POST'])
def create_task():
    if not request.json or not 'name' in request.json:
        abort(400)
    newtask = {'name': request.json['name']}
    mongo.db.tasklist.insert_one(newtask)
    return jsonify({'new_task': {'name': request.json['name']}}), 201

@app.route('/tasklist', methods=['PUT'])
def update_task():
    tasks = mongo.db.tasklist
    if not request.json or not 'name' in request.json:
        abort(400)
    mongo.db.tasklist.update_one({'_id': ObjectId(request.json['id'])},{"$set": {'name': request.json['name']}}, True)
    return jsonify({'task': {'_id': request.json['id'], 'name': request.json['name']}})

@app.route('/tasklist/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    mongo.db.tasklist.delete_one({'_id': ObjectId(task_id)})
    return jsonify({'deleted': True})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    # app.run(debug=True)
