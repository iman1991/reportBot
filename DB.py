import pymysql.cursors

def connect():
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='7087',
                                 db='reportBot',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection


class connection:
    def __init__(self, request, message):
        self.request = request
        self.message = message

    def start(self):
        self.conn = connect()
        self.cursor = self.conn.cursor()
        return True

    def res(self):
    	self.cursor.execute(self.request % (self.message.from_user.id))
    	result = self.cursor.fetchone()
    	return result

    def add(self):
    	self.cursor.execute(self.request % (self.message.from_user.id, self.message.from_user.first_name))
    	self.conn.commit()
    	result = self.cursor.fetchone()
    	return result

    def stop(self):
    	self.cursor.close()
    	self.conn.close()
    	return True

def userinDB(request, message):
	obj = connection(request, message)
	obj.start()
	res = obj.res()
	obj.stop()
	del obj
	return res

def addUserID(request, message):
	obj = connection(request, message)
	obj.start()
	res = obj.add()
	obj.stop()
	del obj
	return res


















