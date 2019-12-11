import urllib.parse
import urllib.request
import json
import sys
import codecs
import json
import math


def recommend_spot(latitude, longitude, seconds, departure_time):
  recommend_list = []
  distance = caluculate_distance(float(seconds))

  # get ottop api
  ottop_list = get_ottop_api(latitude, longitude, distance)
  # get yahoo api
  # N/A
  # get gurunabi api
  gurunabi_list = get_gurunabi_api(latitude, longitude, distance)

  recommend_list = ottop_list + gurunabi_list

  return recommend_list


def caluculate_distance(seconds):
  # 係数(km/ms)
  coefficient  = 30/360000
  distance = math.floor(seconds * coefficient)
  return distance


def get_gurunabi_api(latitude, longitude, distance):
  apikey = '21d4e3248fb7645bb26293edd8f81beb'
  url = 'https://api.gnavi.co.jp/RestSearchAPI/v3/?'

  if distance < (0.3 + 0.5)/2:
    dis_range = 1
  elif distance >= (0.3 +0.5)/2 and distance < (0.5 + 1)/2:
    dis_range = 2
  elif distance >= (0.5 + 1)/2 and distance < (1 + 2)/2:
    dis_range = 3
  elif distance >= (1 + 2)/2 and distance < (2 + 3)/2:
    dis_range = 4
  elif distance >= 3:
    dis_range = 5

  param = {
      'keyid' : apikey,
      'latitude' : latitude,
      'longitude' : longitude,
      'range' : dis_range
  }

  param_str = urllib.parse.urlencode(param)
  read_obj = urllib.request.urlopen(url + param_str)
  raw_data = read_obj.read()
  json_data = json.loads(raw_data)
  gurunabi_list = extract_gurunabi(json_data)

  return gurunabi_list


def extract_gurunabi(json_data):
  i = 0
  gurunabi_dic = {}
  gurunabi_list = []

  while i < len(json_data):
    name = json_data['rest'][i]['name'] 
    url = json_data['rest'][i]['url']
    latitude = json_data['rest'][i]['latitude']
    longitude = json_data['rest'][i]['longitude']
    # mili second
    stay_time = '360000'
    description = ''
    category = '飲食店'
    gurunabi_dic[i] = {"name" : name, "url" : url, "latitude" : latitude, "longitude" : longitude, 
    "category" : category, "stay_time" : stay_time, "description" : description }
    gurunabi_list.append(gurunabi_dic[i])
    i += 1
  
  return gurunabi_list


def get_ottop_api(latitude, longitude, distance):
  apikey = 'Vu5iede1ahziequ3Ang1Asailahhez9D'

  url = 'https://api.ottop.org/tourist/spots?'
  param = {
      'latitude' : latitude,
      'longitude' : longitude,
      'category' : ' ',
      'distance' : distance,
      'apiKey' : apikey
  }

  param_str = urllib.parse.urlencode(param)
  read_obj = urllib.request.urlopen(url + param_str)
  raw_data = read_obj.read()
  json_data = json.loads(raw_data)
  ottop_list = extract_ottop(json_data)

  return ottop_list


def extract_ottop(json_data):
  i = 0
  ottop_dic = {}
  ottop_list = []

  while i < len(json_data):
    name = json_data[i]['name']
    url = json_data[i]['url']
    latitude = json_data[i]['geo']['latitude']
    longitude = json_data[i]['geo']['longitude']
    # mili second
    stay_time = '360000'
    description = ''
    category = '観光地'
    ottop_dic[i] = {"name" : name, "url" : url, "latitude" : latitude, "longitude" : longitude,
    "category" : category, "stay_time" : stay_time, "description" : description }
    ottop_list.append(ottop_dic[i])
    i += 1
  
  return ottop_list