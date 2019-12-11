import urllib.parse
import urllib.request
import json
import sys
import codecs
import json


def api_get(latitude, longitude, category, distance):

  apikey = 'Vu5iede1ahziequ3Ang1Asailahhez9D'
  url = 'https://api.ottop.org/tourist/spots?'
  param = {
      'latitude' : latitude,
      'longitude' : longitude,
      'category' : category,
      'distance' : distance,
      'apiKey' : apikey
  }
  param_str = urllib.parse.urlencode(param)
  read_obj = urllib.request.urlopen(url + param_str)
  raw_data = read_obj.read()
  json_data = json.loads(raw_data)

  dic = extract_ottop(json_data)
#  json_file = open('spot.json', 'w')
#  json.dump(json_data, indent=2, ensure_ascii=False)

  return dic

def extract_ottop(json_data):
  i = 0
  lis = []
  ottop_dic = {}
  while i < len(json_data):
    name = json_data[i]['name']
    url = json_data[i]['url']
    latitude = json_data[i]['geo']['latitude']
    longitude = json_data[i]['geo']['longitude']
    ottop_dic[i] = {"name" : name, "url" : url, "latitude" : latitude, "longitude" : longitude}
#    lis.append(ottop_dic[i])
    i += 1
  return ottop_dic