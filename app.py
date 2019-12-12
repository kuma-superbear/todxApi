import os
import io
import time
import numpy as np
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, session, jsonify, abort
from flask_cors import CORS
from werkzeug import secure_filename
import json
# call other api
import callApi
import get_spot

app = Flask(__name__)
CORS(app)
app.config["JSON_AS_ASCII"] = False

# for test
@app.route('/')
def index():
  return 'Hello World!'


# get spot recommend
@app.route('/get/recommend', methods=['GET'])
def get_spot_information():
  latitude = request.args.get("latitude")
  longitude = request.args.get("longitude")
  # ms
  seconds = request.args.get("seconds")
  depature_time = request.args.get("departure_time")
  response = get_spot.recommend_spot(latitude, longitude, seconds, depature_time)
  
  if not response:
    abort(404, {'code': 'Not Found', 'message': 'spot not found'})
  return jsonify(response)


# get route
@app.route('/get/route', methods=['GET'])
def get_spot_route():
  
  if not response:
    abort(404, {'code': 'Not Found', 'message': 'spot not found'})
  return jsonify(response)


# error
@app.errorhandler(400)
@app.errorhandler(404)
def error_handler(error):
    # error.code: HTTPステータスコード
    return jsonify({'error': {
        'code': error.description['code'],
        'message': error.description['message']
    }}), error.code


# main
if __name__ == '__main__':
  app.run(debug = True)