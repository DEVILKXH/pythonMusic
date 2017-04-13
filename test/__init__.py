# -*- coding: UTF-8 -*-
# -*- author: kexiaohong -*-

import Trampline
import re
import MusicRecord
import StringUtil

def classify(i):
    print i
    yield song(i+1)


def song(i):
    if(i % 2 ==0):
        yield song(i + 1)
    else:
        yield classify(i)


if __name__ == '__main__':
    # Trampline.tramp(song,0)
    string = '<font></font>可<font><!-- adasd --></font>可1<font></font>可2<font></font>'
    # reobj = re.compile("<[^<>]+>")
    str = re.sub("<[^<>]+>","",string)
    print str
    # str = string.replace("", "<[^<>]+>")
    # print str
    # result,number = reobj.subn("","<[^<>]+>")
    # print result,number
    # baseurl = str(raw_input('http://tieba.baidu.com/p/'))
    # print baseurl
    # string = ",，,asdfsadf,,"
    # reobj = re.compile()
    # result,number = re.sub(",|，","",string)
    # print result
    # MusicRecord.setMusicName("kxh")
    # print MusicRecord.getMusicName()
    # print MusicRecord.getUuid()
    # MusicRecord.clear()
    # print MusicRecord.getMusicName()
    # print MusicRecord.getUuid()
    # print StringUtil.replace("asdfasdf'asdfasdf'","'", " ")