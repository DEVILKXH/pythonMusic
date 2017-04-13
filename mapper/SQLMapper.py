# -*- coding: UTF-8 -*-
# -*- author: kexiaohong -*-
import MySQLdb
from pythonMusic.properties import jdbc
from pythonMusic.properties import const


class SQLMapper(object):
    __db__ = None

    def __init__(self):
        pass

#   连接数据库
    def execute(self,sql):
        if sql is None:
            return
        self.__db__ = self.getconnection()
        try:
            cursor = self.__db__.cursor()
            cursor.execute(sql)
            self.__db__.commit()
        except:
            print  const.ERROR + sql
            self.__db__.rollback()
        self.closedb()


#   设置参数
    def getsql(self,sql,params = None):
        if params is None:
            return sql
        try:
            paramStr = "("
            for index in range(len(params)):
                param = params[index]
                if param is None:
                    param = ""
                paramStr += ("'" + param + "',")
            paramStr = paramStr[0:len(paramStr) -1]
            paramStr += ")"
            return sql + paramStr
        except:
            print "----getsql error----"


#   关闭数据库
    def closedb(self):
        if self.__db__:
            self.__db__.close()
        return


#   获取数据库连接
    def getconnection(self):
        host = jdbc.host
        username = jdbc.username
        password = jdbc.password
        database = jdbc.database
        db = MySQLdb.connect(host=host,user=username,passwd=password,db=database,charset='utf8')
        return db

######################################对外接口###################################################
#   获取数据
def getdata(sql):
    sqlmapper = SQLMapper()
    sqlmapper.__db__ = sqlmapper.getconnection()
    cursor = sqlmapper.__db__.cursor()
    results = None
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
    except BaseException,e:
        print e.message
        sqlmapper.__db__.rollback()
    sqlmapper.closedb()
    return results


#   插入数据
def insert(sql,params = None):
    print const.INSERT
    sqlmapper = SQLMapper()
    SQL = sqlmapper.getsql(sql,params)
    sqlmapper.execute(SQL)


#   更新
def update(sql,params = None):
    print const.UPDATE
    sqlmapper = SQLMapper()
    SQL = sqlmapper.getsql(sql, params)
    sqlmapper.execute(SQL)


#   测试主函数
# if __name__ == "__main__":
#     sql = "insert into music_record(UUID,music_name,music_singer,music_url_online) values"
#     name = unicode('柯晓鸿','utf-8').encode('utf-8')
#     singer = unicode('肖丽虹','utf-8').encode('utf-8')
#     params = [UUIDUtil.getuuid(),name,singer,"asdf"]
#     insert(sql,params)