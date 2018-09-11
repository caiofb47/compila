from _ast import TryExcept
from Token import Token
from Tag import Tag


# Procurar pela tag "Rever"


# Variaveis GLOBAIS
END_OF_FILE = 0 # TEM Q SER |Constante| para fim do arquivo
lookahead = 0 # Armazena o ultimo caractere lido no arquivo
n_line = 1 # Contador de linhas
n_column = 1 # Contador de colunas
instance_file = '' # Referencia para o arquivo

class Lexer:
	
	# Lendo arquivo
	@staticmethod # https://stackoverflow.com/questions/4473184/unbound-method-f-must-be-called-with-fibo-instance-as-first-argument-got-cla
	def abrirArq(self, input_data):
		try:
			instance_file = open(input_data,'r')
		
		# Excecao de "No such file or directory"
		except IOError as e:
			print('Erro de abertura do arquivo', e)
			exit(1)
		
	# Metodo que simula o AUTOMATO FD
	def proxToken(self):
		
		# Variaveis do AUTOMATO FD
		lexema = ''
		estado = 1
		c = ''
		END_OF_FILE = instance_file.len() - 1 # Definindo o tamanho do arquivo
		
		while(True):
			
			# Avanca caractere ou retorna um token
			try:
				# Como python le direto o arquivo, n precisa converter
				if (lookahead != END_OF_FILE):
					c = instance_file[lookahead] # Le um caractere
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
	
	# Variaveis # /home/caiofb47/text
	token = Token()
	lexer = Lexer.abrirArq(self, input_data)
	
	
		
	# Enquanto nao houver erros ou nao for o fim do arquivo:
	while(True):
		token = lexer.proxToken()
		
		# Imprimindo TOKEN
		if(token != None):
			print('Token: ', token.__srt__, '\t Linha: ', n_line, '\t Coluna', n_column)
	
	

	
	# Imprimir a tabela de simbolos
	print('')
	print('Tabela de simbolos: ')
	
	
	

