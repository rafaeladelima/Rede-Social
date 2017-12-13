from Models.Pessoa import Pessoa
def Cadastro():
	conn = sqlite3.connect('Rede_Social.db')
	conn.close()
	cursor = conn.cursor()
	nome = input("Nome:")
	email = input("E-mail:")
	senha = input("Senha:")
	nascimento = input("Nascimento:")
	profissao = input("Profissão:")
	pessoa = Pessoa(nome,email,senha,nascimento,profissao)
	cursor.execute(""" INSERT INTO Usuarios Values(nome,email,senha,nascimento,profissao);""")

	#enviar dados para o banco de dados