from flask import Flask,jsonify,request
import json as js
import copy
import numpy as np
from screening import perform
from AHP import ahp
from ranking import ranking

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/screening', methods=['POST'])
def create_task():
    print(request.json)
    a=request.json
    data=a['data']
    print(type(data))
    
    # return("recieved")
    return js.dumps(perform(data)), 201

@app.route('/weightassessment',methods=['POST'])
def calc_weight():
    print(request)
    a=request.json
    print(a)
    a=a['pairwise']
    weights=ahp(a)
    print(weights)
    return jsonify({'weights':weights}), 201

@app.route('/ranking',methods=['POST'])
def calc_ranks():
    a=request.json
    ranks=ranking(a)
    return jsonify({'ranks':ranks}),201

if __name__ == '__main__':
    app.run(debug=True)
