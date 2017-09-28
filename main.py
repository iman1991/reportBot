#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import telebot
from DB import *
from settings import *
import threading
from datetime import datetime


bot = token


@bot.message_handler(commands=['start'])
def handle_start(message):
    if(getuserDB(request1, message)):
        pass
    else:
        addUserDB(request2, message)
        bot.send_message(message.from_user.id, welcome)


def cycle():
	Morning = 9
	Dinner = 13
	Evening = 18
	while True:
		now = datetime.now()
		if (now.hour == Morning):
			Morning = 0
			Evening = 18
			addNullDB(getUserIDDB(request3), now.date())
			handlerMorning(request3)

		if (now.hour == Dinner):
			Morning = 9
			Dinner = 0
			handlerDinner(request3)

		if (now.hour == Evening):
			Dinner = 13
			Evening = 0
			handlerEvening(request3)



def handlerMorning(request):
	users = getUserIDDB(request)
	for item in users:
		sent = bot.send_message(item, question1)
		bot.register_next_step_handler(sent, handle_messageMorning)


def handlerDinner(request):
	users = getUserIDDB(request)
	for item in users:
		sent = bot.send_message(item, question2)
		bot.register_next_step_handler(sent, handle_messageDinner)

def handlerEvening(request):
	users = getUserIDDB(request)
	for item in users:
		sent = bot.send_message(item, question3)
		bot.register_next_step_handler(sent, handle_messageEvening)


def handle_messageMorning(message):
	addReportMorningDB(message)

def handle_messageDinner(message):
	addReportDinnerDB(message)

def handle_messageEvening(message):
	addReportEveninigDB(message)


if __name__ == "__main__":
	thraed = threading.Thread(target=cycle)
	thraed.start()
	bot.polling(none_stop=True, interval = 0)


 





