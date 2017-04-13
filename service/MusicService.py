# -*- coding: UTF-8 -*-
# -*- author: kexiaohong -*-
from pythonMusic.mapper import UrlMapper
from pythonMusic.entity import MusicRecords
from pythonMusic.properties import tagattr
from pythonMusic.utils import TagUtils
from pythonMusic.properties import Music


class MusicService(object):

    def __insert__(self):
        pass


#   插入分类推荐信息
def insertRankList(ranknode,musictype):
    for node in ranknode:
        MusicRecords.clear()
        aSong = node.a
        url = TagUtils.gethtmlcontent(aSong, tagattr.__HREF__)
        if UrlMapper.isused(url) != 0:
            continue
        UrlMapper.insert(url, Music.MUSIC_RANK)
        MusicRecords.setmusicname(TagUtils.gethtmlcontent(aSong, tagattr.__TITLE__))
        MusicRecords.setmusiconline(url)
        author = node.find_all('span', class_='author_list')[0]
        aAuthorList = author.find_all('a')
        MusicRecords.setmusicsinger(TagUtils.gethtmlcontent(aAuthorList, tagattr.__CONTENT__))
        #     # 插入mysql
        #     params = [UUIDUtil.getuuid(),
        #               StringUtil.replace(music_name, "'", " "),
        #               StringUtil.replace(music_singer, "'", " "),
        #               StringUtil.replace(music_url, "'", " ")]
        #     sql = """insert into music_record(UUID,music_name,music_singer,music_url_online) values"""
        #     SQLUtil.insert(sql, params)
        # 插入mongodb
        # MongoDBUtil.insert(musicName=music_name, musicSinger=music_singer, musicUrlOnline=music_url)
        # print music_name,music_singer,music_url