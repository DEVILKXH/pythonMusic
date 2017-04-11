# -*- coding: UTF-8 -*-
import SQLUtil
import UUIDUtil

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    db = client.music
    table = db.music_record
    i = 0
    for item in table.find():
        i = i + 1
        print i
        print item
    music_name = "kxh"
    music_url_download = ""
    music_singer = "xlh"
    music_album = "kxh loves xlh"
    music_url_online = ""
    music_desc = "this is a love song"
    post = {
        "music_name" : music_name,
        "music_singer" : music_singer,
        "music_album" : music_album,
        "music_url_doanload" : music_url_download,
        "music_desc" : music_desc,
        "music_url_online":music_url_online
    }
    # table.insert(post)
    print '---- end sql ----'