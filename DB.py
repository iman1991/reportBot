import pymysql.cursors
from datetime import datetime


def connect():
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='7087',
                                 db='report',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection


class DB:
    def __init__(self, request = "", message = ""):
        self.request = request
        self.message = message

    def start(self):
        self.conn = connect()
        self.cursor = self.conn.cursor()
        return True

    def stop(self):
        self.cursor.close()
        self.conn.close()
        return True

    def addUser(self):
        self.cursor.execute(self.request % (self.message.from_user.id, self.message.from_user.first_name))
        self.conn.commit()
        result = self.cursor.fetchone()
        return result

    def getUser(self):
        self.cursor.execute(self.request % (self.message.from_user.id))
        result = self.cursor.fetchone()
        return result

    def getUserID(self):
        self.cursor.execute(self.request)
        result = self.cursor.fetchall()
        return result

    def addReportMorninig(self):
        now = datetime.now()
        nowtime = now.time()
        self.cursor.execute("UPDATE report SET morning='%s', come='%s' WHERE id='%i' and upload = '%s'" % (self.request.text, nowtime, self.request.from_user.id, now.date()))
        self.conn.commit()
        return True

    def addReportDinner(self):
        now = datetime.now()
        self.cursor.execute("UPDATE report SET dinner='%s' WHERE id='%i' and upload = '%s'" % (self.request.text, self.request.from_user.id, now.date()))
        self.conn.commit()
        return True

    def addReportEveninig(self):
        now = datetime.now()
        nowtime = now.time()
        self.cursor.execute("UPDATE report SET evening='%s', gone='%s' WHERE id='%i' and upload = '%s'" % (self.request.text, nowtime, elf.request.from_user.id, now.date()))
        self.conn.commit()
        return True

    def addNull(self, users, date): 
        for item in users:
            self.cursor.execute("INSERT INTO report (id, upload) values (%i, '%s')" % (item, date))
        self.conn.commit()
        return True

def getuserDB(request, message):
    obj = DB(request, message)
    obj.start()

    res = obj.getUser()

    obj.stop()
    del obj
    return res

def addUserDB(request, message):
    obj = DB(request, message)
    obj.start()

    res = obj.addUser()

    obj.stop()
    del obj
    return res

def getUserIDDB(request):
    obj = DB(request)
    obj.start()

    res = obj.getUserID()

    obj.stop()
    del obj

    arr = []

    for item in res:
        arr.append(item["id"])
        
    return arr

def addReportMorningDB(message):
    obj = DB(message)
    obj.start()

    res = obj.addReportMorninig()

    obj.stop()
    del obj
    return res


def addReportDinnerDB(message):
    obj = DB(message)
    obj.start()

    res = obj.addReportDinner()

    obj.stop()
    del obj
    return res


def addReportEveninigDB(message):
    obj = DB(message)
    obj.start()

    res = obj.addReportEveninig()

    obj.stop()
    del obj
    return res


def addNullDB(users, upload):
    obj = DB()
    obj.start()

    res = obj.addNull(users, upload)

    obj.stop()
    del obj
    return res