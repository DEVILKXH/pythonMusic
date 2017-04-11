# -*- coding: UTF-8 -*-
# -*- author: kexiaohong -*-
import UUIDUtil
from pymongo import MongoClient

class MongoDBUtil(object):
    __client__ = None
    __db__ = None
    __table__ = None

    def __init__(self):
        print "start MongoDB"
        self.__client__ = MongoClient("mongodb://127.0.0.1:27017")
        self.__db__ = self.__client__.music
        self.__table__ = self.__db__.music_record

    def __insert__(self,params):
        self.__table__.insert(params)


def insert(musicName,musicSinger="未知歌手",musicAlbum="未知专辑",musicUrlOnline="",musicUrlDownLoad="",musicDesc=""):
    if musicName is None or musicName == "":
        print "musicName is not None"
        return
    mongoDBUtil = MongoDBUtil();
    params = {
        "uuid": UUIDUtil.getuuid(),
        "music_name": musicName,
        "music_singer": musicSinger,
        "music_album": musicAlbum,
        "music_url_doanload": musicUrlDownLoad,
        "music_desc": musicDesc,
        "music_url_online": musicUrlOnline
    }
    mongoDBUtil.__insert__(params)