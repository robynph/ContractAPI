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
            return jsonify({"app_id” : “App id1”})

@app.route("/regDetailGET", methods=['GET'])
def regDetailGET():

    if request.method == 'GET':
            return jsonify({"app_id” : “App id1”})
