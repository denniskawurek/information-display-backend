# -*- coding: utf-8 -*-

import feedparser
import json
import config
from RequestHandler import *

flask_api_handler = RequestHandler()

def getFeedAndUpdate():
    rss = feedparser.parse(config.RSS_URL)
    entries = rss.entries[:config.RSS_READ_ENTRIES]
    
    data = {}
    index = 0
    for e in entries:
        obj = {'title': e.title, 'summary': e.summary}
        data[index] = obj
        index += 1

    updateDatabase(json.dumps(data))

def updateDatabase(jsonData):
    if config.INIT is True:
        flask_api_handler.post("news", jsonData)
    else:
        flask_api_handler.put("news", jsonData)

if __name__ == '__main__':
    getFeedAndUpdate()
