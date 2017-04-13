# -*- coding: UTF-8 -*-
# -*- author: kexiaohong -*-
#!/pythonMusic

from pythonMusic.utils import UUIDUtil


#   音乐记录类
#   extends  object
class MusicRecommend(object):
    #   uuid
    __uuid__ = None
    #   名称
    __musicName__ = None
    #   歌手
    __musicSinger__ = None
    #   在线地址
    __musicOnLine__ = None
    #   音乐分类
    __musicType__ = None
    #   音乐来源
    __musicSource__ = None


def getmusicname():
    if(MusicRecommend.__musicName__ is None):
        MusicRecommend.__musicName__ = ''
    return MusicRecommend.__musicName__


def setmusicname(musicNmae):
    MusicRecommend.__musicName__ = musicNmae


def getuuid():
    if(MusicRecommend.__uuid__ is None):
        MusicRecommend.__uuid__ = UUIDUtil.getuuid()
    return MusicRecommend.__uuid__


def getmusicsinger():
    if MusicRecommend.__musicSinger__ is None:
        MusicRecommend.__musicSinger__ = ""
    return MusicRecommend.__musicSinger__


def setmusicsinger(musicSinger):
    MusicRecommend.__musicSinger__ = musicSinger


def getmusiconline():
    if MusicRecommend.__musicOnLine__ is None:
        MusicRecommend.__musicOnLine__ = ""
    return MusicRecommend.__musicOnLine__


def setmusiconline(musicOnline):
    MusicRecommend.__musicOnLine__ = musicOnline


def getmusictype():
    if MusicRecommend.__musicType__ is None:
        MusicRecommend.__musicType__ = ""
    return MusicRecommend.__musicType__


def setmusictype(musicType):
    MusicRecommend.__musicType__ = musicType


def getmusicsource():
    if MusicRecommend.__musicSource__ is None:
        MusicRecommend.__musicSource__ = ""
    return MusicRecommend.__musicSource__


def setmusicsource(musicSource):
    MusicRecommend.__musicSource__ = musicSource


def clear():
    MusicRecommend.__uuid__ = None
    MusicRecommend.__musicName__ = None
    MusicRecommend.__musicSinger__ = None
    MusicRecommend.__musicAlbum__ = None
    MusicRecommend.__musicDesc__ = None
    MusicRecommend.__musicOnLine__ = None
    MusicRecommend. __musicDownLoad__ = None
    MusicRecommend. __musicType__ = None
    MusicRecommend.__musicSource__ = None


def tostring():
    return {
        "uuid": getuuid(),
        "music_name": getmusicname(),
        "music_singer": getmusicsinger(),
        "music_url_online": getmusiconline(),
        "music_type": getmusictype(),
        "music_source": getmusicsource()
    }