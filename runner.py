# coding: UTF-8

from models import Client

c = []

def cadastrar():
	cliente = Client()
	print 'Entre com os dados:'
	cliente.nome = raw_input('Nome:')
	cliente.idade = raw_input('Idade:')
	cliente.cpf = raw_input('CPF:')
	cliente.endereco = raw_input('Endereço: ')
	print 'Cadastrado com Sucesso!'
	c.append(cliente)
	
def editar():
	nome = raw_input('Nome do cliente para editar:')
	flag = 0
	for cliente in c:
		if nome == cliente.nome:
			print 'Entre com os novos dados do cliente:'
			cliente.nome = raw_input('Nome:')
			cliente.idade = raw_input('Idade:')
			cliente.cpf = raw_input('CPF:')
			cliente.endereco = raw_input('Endereço: ')
			print 'Editado com Sucesso!'
			flag = 1
	if flag == 0:
		print 'Cliente não encontrado!'

def remover():
	nome = raw_input('Nome do cliente para remover:')
	flag = 0
	for cliente in c:
		if nome == cliente.nome:
			c.remove(cliente)
			flag = 1
	if flag == 0:
		print 'Cliente não encontrado!'

def consultar():
	nome = raw_input('Nome do cliente para consultar:')
	flag = 0
	for cliente in c:
		if nome == cliente.nome:
			print cliente.__dict__
			flag = 1
	if flag == 0:
		print 'Cliente não encontrado!'

def listar():
	if c is not None:
		for cliente in c:
			print cliente.__dict__
			
	else:
		print 'Nao tem nenhum cliente cadastrado'
		
if __name__ == '__main__':
	
	while True:
		menu = 'Escolha o cadastro\n1- Cadastrar\n2- Editar\n3- Consultar\n4- Excluir\n5 - Listar\n0 - Sair\n'
		opt = raw_input(menu)
		if opt == '1':
			cadastrar()
		elif opt == '2':
			editar()
		elif opt == '3':
			consultar()
		elif opt == '4':
			remover()
		elif opt == '5':
			listar()
		elif opt == '0':
			print 'Saindo...'
		else:
			print 'Opção invalida!'

