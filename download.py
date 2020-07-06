from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys, json

json_open = open('conf.json','r')
json_load = json.load(json_open)

# APIキーの情報
key = json_load['flickr']['key']
secret = json_load['flickr']['secret']
wait_time = 1

# 保存フォルダの指定
animalname = sys.argv[1]
savedir = "./" + animalname

flickr = FlickrAPI(key, secret, format='parsed-json')
result = flickr.photos.search(
    text = animalname,
    per_page = 400,
    media = 'photos',
    sort = 'relevance',
    safe_search = 1,
    extras = 'url_q, licence'
)

photos = result['photos']
pprint(photos)
