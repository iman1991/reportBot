from connection import *


def start(request, message):
	connect = connection.connect()
	cursor = connect.cursor()
	cursor.execute(request % (message.from_user.id, message.from_user.first_name))
	connect.commit()
	result = cursor.fetchone()
	cursor.close()
	connect.close()


def addUserID(request, message):
	res = start(request, message)
	return res