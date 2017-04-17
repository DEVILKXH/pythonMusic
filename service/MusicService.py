# -*- coding: UTF-8 -*-
# -*- author: kexiaohong -*-
from pythonMusic.mapper import UrlMapper
from pythonMusic.mapper import SQLMapper
from pythonMusic.properties import Music
from pythonMusic.properties import tagattr
from pythonMusic.properties import const
from pythonMusic.utils import TagUtils
from pythonMusic.utils import StringUtil
from pythonMusic.utils import UUIDUtil
from pythonMusic.utils import Trampline
from pythonMusic.entity import MusicRecords
from bs4 import BeautifulSoup


class MusicService(object):

    __urllist__ = []
    __urltype__ = []
    __urlused__ = []
    __baseurl__ = ""

    def __insert__(self):
        pass

    #   插入分类推荐信息
    def __insertranklist__(self,ranknode, musictype, baseurl):
        for node in TagUtils.gethtmlnodebyclass(ranknode, tagattr.__DIV__, Music.SONG):
            MusicRecords.clear()
            MusicRecords.setmusictype(musictype)
            aSong = node.a
            url = TagUtils.gethtmlcontent(aSong, tagattr.__HREF__, baseurl)
            if UrlMapper.isused(url,Music.MUSIC_URL_USED):
                continue
            UrlMapper.insert(url, Music.MUSIC_URL_USED)
            MusicRecords.setmusicname(TagUtils.gethtmlcontent(aSong, tagattr.__TITLE__, baseurl))
            MusicRecords.setmusiconline(url)
            author = node.find_all('span', class_='author_list')[0]
            MusicRecords.setmusicsinger(TagUtils.gethtmlcontent(author, tagattr.__CONTENT__, baseurl))
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
        return


    #   获取分类标签的url
    def __gettagurl__(self,soup,baseurl):
        self.__geturls__(soup, 'a', 'tag-item')
        return

    def __geturls__(self, soup, tag, classname, type="init"):
        aNodes = soup.find_all(tag, class_=classname)
        if aNodes is None and len(aNodes) == 0:
            return
        for node in aNodes:
            url = TagUtils.gethtmlcontent(node, tagattr.__HREF__,MusicService.__baseurl__)
            if UrlMapper.isused(url,Music.MUSIC_URL_UNUNSE) or UrlMapper.isused(url,Music.MUSIC_URL_USED):
                continue
            url_name = TagUtils.gethtmlcontent(node, tagattr.__CONTENT__,MusicService.__baseurl__)
            if type != "init":
                url_name = self.__type__
                self.__urllist__.append(url)
                self.__urltype__.append(url_name)
            sql = "insert into music_url_unuse (uuid,music_url,url_name) values"
            params = [UUIDUtil.getuuid(),url,url_name]
            SQLMapper.insert(sql,params)
        return

    #   获取页码的url
    def __getpagenum__(self, soup):
        self.__geturls__(soup,'a','page-navigator-number',"page")


    def __getmusic__(self):
        print const.GETMUSIC
        sql = "select * from music_url_unuse"
        result = SQLMapper.getdata(sql)
        if result is None:
            return
        for row in result:
            self.__urllist__.append(row[1])
            self.__urltype__.append(row[2])
        yield self.__getmusics__()

    def __getmusics__(self):
        print const.GETMUSICS
        url = self.__urllist__.pop()
        url_type = self.__urltype__.pop()
        self.__type__ = url_type
        if UrlMapper.isused(url,Music.MUSIC_URL_USED):
            yield self.__getmusics__()
        UrlMapper.delete(url,Music.MUSIC_URL_UNUNSE)
        UrlMapper.insert(url,Music.MUSIC_URL_USED)
        html = UrlMapper.get_content(url)
        if html is None:
            yield self.__getmusics__()
        else:
            soup = BeautifulSoup(html, 'html5lib')
            yield self.__getMusicInfos__(soup)

    def __getMusicInfos__(self,soup):
        for node in soup.find_all('div', class_='song-item'):
            MusicRecords.clear()
            songTitle = node.find_all('span', class_='song-title')[0].find('a')
            MusicRecords.setmusicname(TagUtils.gethtmlcontent(songTitle, tagattr.__CONTENT__,MusicService.__baseurl__))
            MusicRecords.setmusicdesc(TagUtils.gethtmlcontent(songTitle, tagattr.__TITLE__,MusicService.__baseurl__))
            MusicRecords.setmusiconline(TagUtils.gethtmlcontent(songTitle, tagattr.__HREF__,MusicService.__baseurl__))
            try:
                asongSinger = node.find_all('span', class_='singer')[0]
                MusicRecords.setmusicsinger(TagUtils.gethtmlcontent(asongSinger, tagattr.__CONTENT__, MusicService.__baseurl__))
            except:
                pass
            try:
                asongAlbum = node.find_all('span', class_='album-title')[0]
                MusicRecords.setmusicalbum(TagUtils.gethtmlcontent(asongAlbum, tagattr.__CONTENT__, MusicService.__baseurl__))
            except:
                pass
            # 插入mysql数据库
            sql = "insert into music_records" \
                  "(UUID,music_name,music_singer," \
                  "music_album,music_url_online,music_desc," \
                  "music_type,music_source) values"
            params = [UUIDUtil.getuuid(),
                      StringUtil.replace(MusicRecords.getmusicname().strip(), "'", " "),
                      StringUtil.replace(MusicRecords.getmusicsinger().strip(), "'", " "),
                      StringUtil.replace(MusicRecords.getmusicalbum().strip(), "'", " "),
                      StringUtil.replace(MusicRecords.getmusiconline().strip(), "'", " "),
                      StringUtil.replace(MusicRecords.getmusicdesc().strip(), "'", " "),
                      StringUtil.replace(self.__type__, "'", " "),
                      StringUtil.replace(MusicService.__baseurl__["url"], "'", " ")]
            SQLMapper.insert(sql, params)
            # 插入mongodb数据库
            # MongoDBUtil.insert(musicName=music_name,musicSinger=music_singer,musicAlbum=music_album,musicUrlOnline=music_url,musicDesc=music_desc)
            # print music_name,music_singer,music_album,music_url,music_desc
        self.__getpagenum__(soup)
        yield self.__getmusics__()


#   插入分类推荐信息
def insertranklist(ranknode,musictype,baseurl):
    musicservice = MusicService()
    musicservice.__insertranklist__(ranknode,musictype,baseurl)


def gettypemusic(soup,baseurl):
    MusicService.__baseurl__ = baseurl
    musicservice = MusicService()
    musicservice.__gettagurl__(soup,baseurl)
    Trampline.tramp(musicservice.__getmusic__)