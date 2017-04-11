# -*- coding: UTF-8 -*-
# -*- author: kexiaohong -*-
import UUIDUtil
import SQLUtil
import ConstData
import UrlUtil
import Trampline
import MongoDBUtil
from bs4 import BeautifulSoup


class SongUtil(object):
    __urlList__ = []
    __usedList__ = []
    __HREF__ = 'href'
    __TITLE__ = 'title'
    __CONTENT__ = 'content'
    __CLASSIFY__ = 'classify'
    TYPE = ""

    def __init__(self):
        print "----song----"

#   获得内容
    def __getcontent__(self,obj,attr):
        try:
            if attr == self.__CONTENT__:
                return obj.string.strip()
            if obj.has_attr(attr) and obj[attr] is not None and obj[attr] != "":
                if attr == self.__HREF__ and obj[attr].find(ConstData.hostUrl, 0, 20) == -1:
                    return ConstData.baseBaiduUrl + "/" + obj[attr].strip()
                return obj[attr].strip()
            else:
                if attr == self.__TITLE__ and type(obj.string.strip()) != 'bs4.element.Comment' and obj.string is not None and obj.string != "":
                    return obj.string.strip()
                else:
                    return ""
        except:
            try:
                return obj.string.strip()
            except:
                return ""
        return

#   获取url
    def __getUrls__(self,soup,tag,classname):
        aNodes = soup.find_all(tag, class_=classname)
        if aNodes is None and len(aNodes) == 0:
            return
        for node in aNodes:
            aANodes = node.find_all('a')
            if aANodes is None and len(aANodes) == 0:
                continue
            for aNode in aANodes:
                url = self.__getcontent__(aNode,self.__HREF__)
                if self.__urlList__.count(url) == 0 and self.__usedList__.count(url) == 0:
                    self.__urlList__.append(url)
        return

#   获取页码的url
    def __getPageNum__(self,soup):
        aNodes = soup.find_all('a',class_='page-navigator-number')
        if aNodes is None and len(aNodes) == 0:
            return
        for node in aNodes:
            url = self.__getcontent__(node,'href')
            if self.__urlList__.count(url) == 0 and self.__usedList__.count(url) == 0:
                self.__urlList__.append(url)
        return

#   按照音乐分类
    def __classifyByMusic__(self,soup):
        self.__getUrls__(soup,'ul','clearfix tags-1220')
        self.__getUrls__(soup,'ul','clearfix tags-980')
        return

#   按照歌手分类
    def __classifyBySinger__(self,soup):
        self.__getUrls__(soup,'ul','cate-list-height-112')
        return

#   获得分类的信息
    def __getClassifyMusic__(self,soup):
        for node in soup.find_all('div', class_='song-item'):
            music_album = ""
            music_singer = ""
            songTitle = node.find_all('span', class_='song-title')[0].find('a')
            music_name = self.__getcontent__(songTitle,self.__CONTENT__)
            music_desc = self.__getcontent__(songTitle,self.__TITLE__)
            music_url = self.__getcontent__(songTitle,self.__HREF__)
            asongSinger = node.find_all('span', class_='singer')
            if asongSinger is not None and len(asongSinger) > 0:
                songSinger = asongSinger[0].find('a')
                if songSinger is not None and len(songSinger) > 0:
                    music_singer = self.__getcontent__(songSinger,self.__TITLE__)
            asongAlbum = node.find_all('span', class_='album-title')
            if asongAlbum is not None and len(asongAlbum) > 0:
                songAlbum = asongAlbum[0].find('a')
                if songAlbum is not None and len(songAlbum) > 0:
                    music_album = self.__getcontent__(songAlbum,self.__TITLE__)
            #插入mysql数据库
            # sql = "insert into music_record(UUID,music_name,music_singer,music_album,music_url_online) values"
            # params = [UUIDUtil.getuuid(),music_name,music_singer,music_album,music_url]
            # SQLUtil.insert(sql,params)
            #插入mongodb数据库
            MongoDBUtil.insert(musicName=music_name,musicSinger=music_singer,musicAlbum=music_album,musicUrlOnline=music_url,musicDesc=music_desc)
            print music_name,music_singer,music_album,music_url,music_desc
        self.__getPageNum__(soup)
        yield self.__getSongs__()

#   获取url中的歌曲
    def __getSongs__(self):
        print "----getSongs----"
        url = self.__urlList__.pop()
        if self.__usedList__.count(url) == 0:
            self.__usedList__.append(url)
            html = UrlUtil.get_content(url)
            if html is None:
                yield  self.__getSongs__(self.TYPE)
            else:
                soup = BeautifulSoup(html, 'html5lib')
                print url
                if self.TYPE == self.__CLASSIFY__:
                    yield self.__getClassifyMusic__(soup)
        return


#   获得首页歌曲数据
def getindexsongs(soup):
    songUtil = SongUtil()
    aNodes =  soup.find_all('div', class_='song')
    if aNodes is not None:
        for node in aNodes:
            aSong = node.a
            music_name = songUtil.__getcontent__(aSong, songUtil.__TITLE__)
            music_url = songUtil.__getcontent__(aSong, songUtil.__HREF__)
            if songUtil.__usedList__.count(music_url) == 0:
                songUtil.__usedList__.append(music_url)
                author = node.find_all('span', class_='author_list')[0]
                aAuthorList = author.find_all('a')
                singer = ""
                for authorlist in aAuthorList:
                    print authorlist
                    singer += (songUtil.__getcontent__(authorlist, songUtil.__TITLE__) + ',')
                music_singer = singer[0:len(singer) - 1]
                # 插入mysql
                # params = [UUIDUtil.getuuid(), music_name, music_singer, music_url]
                # sql = """insert into music_record(UUID,music_name,music_singer,music_url_online) values"""
                # SQLUtil.insert(sql, params)
                # 插入mongodb
                MongoDBUtil.insert(musicName=music_name, musicSinger=music_singer, musicUrlOnline=music_url)
                print music_name,music_singer,music_url

#   获取分类数据
def gettypesongs(soup):
    songUtil = SongUtil()
    songUtil.__classifyByMusic__(soup)
    # songUtil.__classifyBySinger__(soup)
    songUtil.TYPE = songUtil.__CLASSIFY__
    Trampline.tramp(songUtil.__getSongs__)
    return
