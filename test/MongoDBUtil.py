# -*- coding: UTF-8 -*-
# -*- author: kexiaohong -*-
import UUIDUtil
# from pymongo import MongoClient


class MongoDBUtil(object):
    __client__ = None
    __db__ = None
    __table__ = None

    def __init__(self):
        print "start MongoDB"
        # self.__client__ = MongoClient("mongodb://127.0.0.1:27017")
        self.__db__ = self.__client__.music
        self.__table__ = self.__db__.music_record

    def __insert__(self,params):
        self.__table__.insert(params)


def insert(musicname, musicsinger="未知歌手", musicalbum="未知专辑", musicurlonline="", musicurldownload="", musicdesc=""):
    if musicname is None or musicname == "":
        print "musicName is not None"
        return
    mongodbutil = MongoDBUtil()
    params = {
        "uuid": UUIDUtil.getuuid(),
        "music_name": musicname,
        "music_singer": musicsinger,
        "music_album": musicalbum,
        "music_url_download": musicurldownload,
        "music_desc": musicdesc,
        "music_url_online": musicurlonline
    }
    mongodbutil.__insert__(params)