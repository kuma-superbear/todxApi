import os
import io
import time
import numpy as np
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, session, jsonify
from werkzeug import secure_filename
import json
# call other api
import callApi
import get_spot
app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

# for test
@app.route('/')
def index():
  return 'Hello World!'

# get spot information
@app.route('/get/spot', methods=['GET'])
def get_spot_information():
  latitude = request.args.get("latitude")
  longitude = request.args.get("longitude")
  category = request.args.get("category")
  distance = request.args.get("distance")

  response = get_spot.api_get(latitude, longitude, category, distance)

  return jsonify(response)


if __name__ == '__main__':
  app.run(debug = True)