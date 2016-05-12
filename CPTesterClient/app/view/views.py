from app import app
from flask import render_template,request, jsonify
from datetime import datetime
from app.controller.controllerBrInterfaces import *

@app.route('/')
def index():
    return jsonify(status="success")


class TestControllerBrInterfaces:
    def __init__(self):
        print("Controller Bridge Interfaces Init")

#    def sayHello(self):
#        print("Test Hello")


# add delete update list

@app.route('/add', methods=['POST',])
def add():
    jsondata = request.json
    # print type(jsondata)
    for(k,v) in jsondata.items():
        print type(k),"=",k, type(v)
        if (k == "brInterfaces"):
            ctlbrintfs = ControllerBrInterfaces()
            ctlbrintfs.initBridgeInterfaces(v)
            ctlbrintfs.printBridgeInterfaces()
    return jsonify(status="success")


@app.route('/delete/<string:todo_id>')
def delete(todo_id):
    return jsonify(status="success")


@app.route('/update', methods=['POST',])
def update():
    print "here"
    ctlbrintf = ControllerBrInterfaces()
    ctlbrintf.sayHello()
#    print ctlbrintf
    return jsonify(status="success")

@app.route('/list')
def list():
    return jsonify(status="success")



