import urllib.parse
import urllib.request
import json
import sys
import codecs

def api_get():
  url = 'https://api.ottop.org/transit/routes?'

  param = {
      'origin_latitude' : '24.337612',
      'origin_longitude' : '124.154725',
      'dest_latitude' : '24.391161',
      'dest_longitude' : '124.246482',
      'arrival_time' : '2019-12-09T12:00'
  }

  # URIパラメータの文字列の作成
  param_str = urllib.parse.urlencode(param)
  # 読み込むオブジェクトの作成
  readObj = urllib.request.urlopen(url + paramStr)
  # webAPIからのJSONを取得
  response = readObj.read()

  return response


def convert_json(json_str):
  # webAPIから取得したJSONデータをpythonで使える形に変換する
  data = json.loads(json_str)
  return data


def search_date(data):
  # date
  search_date = data['date']
  return search_date