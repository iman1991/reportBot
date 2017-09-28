#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import telebot

token = telebot.TeleBot("345809401:AAGUZlD5UdJ0iE7Xd2l2Tygn2mZRjWgCl2I")

welcome = """
	Здравствуйте!\n
	Я бот для отчетов, каждый день нещадно с 9 утра спамить вас
	запросами об отчетах покуда вы не ответите. Вы сами на это подписались!\n
	Надеюсь наша работа с вами будет успешной.
"""

selectKWhereID = "SELECT id FROM users WHERE id = %i"
insertUser = "INSERT INTO users (id, username) values (%i, '%s')"
selectUser = "SELECT id FROM users"
request4 = """
	INSERT INTO `report`.`report` (`id`) VALUES ('21312');
	INSERT INTO `report`.`report` (`id`) VALUES ('12312');
"""


askPlans = "Какие планы на сегодня?\n\nНапишите:"
askDone = "Что сделанно?\n\nНапишите:"
askDoneAsDay = "Что сделал за день?\n\nНапишите:"
