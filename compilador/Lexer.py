from _ast import TryExcept
import Token
import Tag


# Procurar pela tag "Rever"





# Variaveis GLOBAIS
END_OF_FILE = 0 # TEM Q SER |Constante| para fim do arquivo
lookahead = 0 # Armazena o ultimo caractere lido no arquivo
n_line = 1 # Contador de linhas
n_column = 1 # Contador de colunas

class Lexer:


	# Metodo que simula o AUTOMATO FD
	def proxToken(self):
		
		# Variaveis do AUTOMATO FD
		lexema = ''
		estado = 1
		c = ''
		END_OF_FILE = lexer.len() - 1 # Definindo o tamanho do arquivo
		
		while(True):
			
			# Avanca caractere ou retorna um token
			try:
				# Como python le direto o arquivo, n precisa converter
				if (lookahead != END_OF_FILE):
					c = lexer[lookahead] # Le um caractere
					lookahead += 1 # Muda o apontamento
			# Rever essa exception
			except IOError as e:
				print("Erro na leitura do caractere")
				
			
			# Movimentacao do AFD
			if (estado == 1):
				if(lookahead == END_OF_FILE):
					return Token(Tag['END_OF_FILE'], 'EOF', n_line, n_column)
				
				
			
					
				
				
				


# Main :D
if __name__ == '__main__':
	# Lendo arquivo
	try:
		lexer = open('home/caiofb47/git/repository/compilador/text','r')
		
	# Excecao de "No such file or directory"
	except IOError as e:
		print('Erro de abertura do arquivo 1', e)
		exit()
		
	# Enquanto nao houver erros ou nao for o fim do arquivo:
	
	
	
	
	# Fechando arquivo
	lexer.close()
	
	# Imprimir a tabela de simbolos
	print('')
	print('Tabela de simbolos: ')
	
	
	

