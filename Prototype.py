'''
	Askarkhujaev Sarvarkhuja Zufarkhujaevich:
		autentification: 
			1. passed -> next
			2. failed -> login/password -> next
			+ finger scan
		enter academy: (time) -> next:
			enter x-room: (time) ->next:
				computer-work
			exit x-room: (time) -> next
		exit academy: (time)
'''	

import os
from datetime import datetime as dt
import json

class Student:
	def __init__(self, full_name, iden, date_of_birth, login, password, rating, semestr):
		self.full_name = full_name
		self.iden = iden
		self.login = login
		self.password = password
		self.date_of_birth = date_of_birth
		self.rating = rating
		self.semestr = semestr

class PersonAuten:
	def __init__(iden, time_iden):
		iden = iden
		time_iden = time_iden

# создание папок, файлов для чтения - база данных
months = ['none', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

now = dt.now()
current_year = now.year
current_month = now.month
current_day = now.day

current_path = os.getcwd();
current_path_tmp = os.getcwd() + "\\" + str(current_year)

if not(os.path.exists(current_path_tmp)) :
	os.mkdir(current_path_tmp)
current_path = current_path_tmp
current_path_tmp += ("\\" + months[current_month])

if not(os.path.exists(current_path_tmp)) :
	os.mkdir(current_path_tmp)
current_path = current_path_tmp
current_path_tmp += ("\\" + str(current_day))

if not(os.path.exists(current_path_tmp)) :
	os.mkdir(current_path_tmp)
current_path = current_path_tmp
# конец
#--------------------------------------------------------------------------------------------------------------
# создание студента (одного текущего/рассматриваемого)
person = PersonAuten
#конец
#--------------------------------------------------------------------------------------------------------------
# чтение значений передаваемых нейронной сетью

while (True):
	ex=False
	num=""
	with open("D:\Sarvar\Python\EnterAuth\\" + "enter.txt") as f:
		num=f.read()
		if (len(num)>0):
			ex=True
	if ex:
		f = open("D:\Sarvar\Python\EnterAuth\\" + "enter.txt","w")
		f.close()
		#number=int(num[0])
	#read_neuron_autentification = open(current_path + "\\" + "enter.txt", "r+")
	#read_neuron_autentification.read()
	if (len(num)>0):
		print(num)
		f = open(current_path + "\\" + str(num) + ".txt", "w+")
		f.write(str(dt.now().hour) + ":" + str(dt.now().minute) + ":" + str(dt.now().second)+" authentification passed")
#конц
#--------------------------------------------------------------------------------------------------------------
# запись действий после аутентификации

# конец
#--------------------------------------------------------------------------------------------------------------