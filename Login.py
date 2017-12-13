import sqlite3
from Models.Rede_Social import Rede_Social

def Login():
	conn = sqlite3.connect('Rede_Social.db')
	conn.close()
	cursor = conn.cursor()
	email = input("Digite seu E-Email:")
	senha = input("Digite sua senha:")
	if email == cursor.execute("""SELECT email from Usuarios;"""):
		if senha == cursor.execute(""" SELECT senha from Usuarios;"""):
			Rede_Social.Rede_Social()
	#verificar no banco de dados e fazer um try except e chamar a rede social 

