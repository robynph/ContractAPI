# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 18:24:13 2018

@author: Monika Asawa
@edits by RH
"""
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run(debug=True)

@app.route("/test", methods=['GET'])
def test():

    if request.method == 'GET':
            return ("This is a test :) ")


@app.route("/transDetailGET", methods=['GET'])
def transDetailGET():

    if request.method == 'GET':
            return jsonify({"app_id" : "App id1","model_id" : "Model id1","Date" : "Sept. 16, 2018","order_id" : "2348858","trans_id" : "0xtransID","selected_product" : "sku1","bundled_products" : "order line item sku","Original Revenue" : "$####","Total Revenue" : "$####"})

@app.route("/regDetailGET", methods=['GET'])
def regDetailGET():

    if request.method == 'GET':
            return jsonify({"app_id":"appID", "walletID": {"0xwallet": [{"transID1" : "0xtransID1", "Total Revenue" : "$###,###", "Total Bundles Generated" : "$###,###"},{"transID2" : "0xtransID2", "Total Revenue" : "$###,###", "Total Bundles Generated" : "$###,###"}],}})
