# -*- coding: UTF-8 -*-
# -*- author: kexiaohong -*-
from pythonMusic.mapper import UrlMapper
from pythonMusic.entity import MusicRecords
from pythonMusic.properties import tagattr
from pythonMusic.utils import TagUtils
from pythonMusic.properties import Music
from pythonMusic.utils import StringUtil
from pythonMusic.mapper import SQLMapper


class MusicService(object):

    def __insert__(self):
        pass


#   插入分类推荐信息
def insertranklist(ranknode,musictype):
    for node in TagUtils.gethtmlnodebyclass(ranknode,tagattr.__DIV__,Music.SONG):
        MusicRecords.clear()
        MusicRecords.setmusictype(musictype)
        aSong = node.a
        url = TagUtils.gethtmlcontent(aSong, tagattr.__HREF__)
        print url
        if UrlMapper.isused(url):
            continue
        UrlMapper.insert(url, Music.MUSIC_URL_USED)
        MusicRecords.setmusicname(TagUtils.gethtmlcontent(aSong, tagattr.__TITLE__))
        MusicRecords.setmusiconline(url)
        author = node.find_all('span', class_='author_list')[0]
        MusicRecords.setmusicsinger(TagUtils.gethtmlcontent(author, tagattr.__CONTENT__))
        # 插入mysql
        params = [MusicRecords.getuuid(),
                  StringUtil.replace(MusicRecords.getmusicname(), "'", " "),
                  StringUtil.replace(MusicRecords.getmusicsinger(), "'", " "),
                  StringUtil.replace(MusicRecords.getmusiconline(), "'", " "),
                  StringUtil.replace(MusicRecords.getmusictype(), "'", " "),
                  StringUtil.replace(MusicRecords.getmusicsource(), "'", " ")]
        sql = """insert into music_rank(UUID,music_name,music_singer,music_url_online,music_type,music_source) values"""
        SQLMapper.insert(sql, params)
        # 插入mongodb
        # MongoDBUtil.insert(musicName=music_name, musicSinger=music_singer, musicUrlOnline=music_url)
        # print music_name,music_singer,music_url