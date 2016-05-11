from app import app
from flask import render_template,request, jsonify
from datetime import datetime

@app.route('/')
def index():
    return jsonify(status="success")


# add delete update list

@app.route('/add', methods=['POST',])
def add():
    jsondata = request.json
    print type(jsondata)
    for(k,v) in jsondata.items():
        print type(k),"=",k, type(v)
    return jsonify(status="success")


@app.route('/delete/<string:todo_id>')
def delete(todo_id):
    return jsonify(status="success")


@app.route('/update', methods=['POST',])
def update():
    form = request.form
    return jsonify(status="success")

@app.route('/list')
def list():
    return jsonify(status="success")



