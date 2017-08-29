from connection import *


def start(request, message):
	connect = connection.connect()
	cursor = connect.cursor()
	cursor.execute(request % (message.from_user.id))
	result = cursor.fetchone()
	cursor.close()
	connect.close()
	if result is not None:
		return True
	else:
		return False


def userinDB(request, message):
	res = start(request, message)
	return res