# -*- coding: UTF-8 -*-
# -*- author: kexiaohong -*-
import UrlUtil
import SongUtil
import ConstData
from bs4 import BeautifulSoup

if __name__ == '__main__':
    html = UrlUtil.get_content(ConstData.baseBaiduUrl)
    if html is not None:
        soup = BeautifulSoup(html,'html5lib')
        SongUtil.getindexsongs(soup)
        SongUtil.gettypesongs(soup)

