from app import app
from flask import render_template,request, jsonify
from datetime import datetime
from app.controller.controllerBrInterfaces import *
from app.controller.controllerComInterfaces import *
from app.controller.controllerContainerDNSMASQ import *
from app.controller.controllerPhysicEthernetInterfaces import *
from app.controller.controllerVlanInterfaces import *

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
        # print type(k),"=",k, type(v)
        if (k == "brInterfaces"):
            ctler = ControllerBrInterfaces(v,k)
            ctler.printController()
        elif (k == "comInterfaces"):
            ctler = ControllerComInterfaces(v,k)
            ctler.printController()
        elif (k == "physicEthernetInterfaces"):
            ctler = ControllerPhysicEthernetInterfaces(v,k)
            ctler.printController()
        elif (k == "vlanInterfaces"):
            ctler = ControllerVlanInterfaces(v,k)
            ctler.printController()
        elif (k == "containerDNSMASQ"):
            print "Container DNSMASQ is not supported"
        else:
            print "Not support type:",k

    return jsonify(status="success")


@app.route('/delete/<string:todo_id>')
def delete(todo_id):
    return jsonify(status="success")


@app.route('/update', methods=['POST',])
def update():
    print "here"
    return jsonify(status="success")

@app.route('/list')
def list():
    return jsonify(status="success")



