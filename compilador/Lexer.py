class Lexer:

	# Variaveis
	END_OF_FILE = -1
	lookhead = 0
	n_line = 1
	n_column = 1


# Main :D
if __name__ == '__main__':
	# Lendo arquivo
	try:
		lexer = open('/home/caiofb47/eclipse-workspace/compilador/text','r')
		
	# Excecao de "No such file or directory"
	except IOError as e:
		print('Erro de abertura do arquivo', e)
		exit()
	
	

