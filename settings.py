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

request1 = "SELECT id FROM users WHERE id = %i"
request2 = "INSERT INTO users (id, username) values (%i, '%s')"
request3 = "SELECT id FROM users"
request4 = """
	INSERT INTO `report`.`report` (`id`) VALUES ('21312');
	INSERT INTO `report`.`report` (`id`) VALUES ('12312');
"""


question1 = "Какие планы на сегодня?\n\nНапишите:"
question2 = "Что сделанно?\n\nНапишите:"
question3 = "Что сделал за день?\n\nНапишите:"
