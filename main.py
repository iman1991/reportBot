import telebot
from getfromDB import *
from intoDB import *

bot = telebot.TeleBot("345809401:AAGUZlD5UdJ0iE7Xd2l2Tygn2mZRjWgCl2I")

@bot.message_handler(commands=['start'])
def handle_start(message):
	if(userinDB("SELECT id FROM users WHERE id = %i", message)):
		print(0)
	else:
		addUserID("INSERT INTO users (id, username) values (%i, '%s')", message)


bot.polling(none_stop=True, interval = 0)