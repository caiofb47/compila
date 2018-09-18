# Imports
from Tag import Tag
from Token import Token




# Procurar pela tag "Rever"

# Caio Fabio Gomes Alves - caiofb47@gmail.com

class Lexer:
	
	
	# Construtor/Inicializador da classe LEXER
	def __init__(self):
		self.instance_file = '' # Referencia para o arquivo
		self.END_OF_FILE = 0 #TEM Q SER |Constante| para fim do arquivo
		self.n_line = 0
		self.n_column = 0
		
		
	# Funcao para ler o arquivo
	def Lexer(self, input_data):
		# Tentar abrir e ler arquivo
		try:
			
			# Abrindo o arquivo
			lido = open(input_data,'r')
			# Lendo o arquivo
			self.instance_file = lido.read()
			
			# Pegando o tamanho do arquivo com a funcao len
			self.END_OF_FILE = len(self.instance_file) - 1
		
		# Excecao de "No such file or directory"
		except IOError as e:
			print('Erro de abertura do arquivo:', e)
			exit(1)
		
	# Metodo que simula o AUTOMATO Finito Determinisitico
	def proxToken(self):
		
		# Variaveis do AUTOMATO FD
		lookahead = 0 # Armazena a posicao do ultimo caractere lido no arquivo	
		lexema = ''
		estado = 1
		c = ''

		
		while(True):
		
			# Avanca caractere ou retorna um token
			try:
				# Como python le direto o arquivo, n precisa converter
				if (lookahead != self.END_OF_FILE):
					c = self.instance_file[lookahead] # Le um caractere
					lookahead += 1 # Muda o apontamento
					
					
			# Rever essa exception, pq n e de entrada e saida :/
			except IOError as e:
				print("Erro na leitura do caractere")
				
			
			
			# Movimentacao do AFD
			if (estado == 1):
				
				if(lookahead == self.END_OF_FILE):
					# Retorna um novo token Tag['END_OF_FILE'], 'EOF', self.n_line, self.n_column
					return Token(Tag['END_OF_FILE'], 'EOF', self.n_line, self.n_column)
				elif(c == ' ' or c == '\t' or c =='\n' or c =='\r' or c == '7'):
					# Permanece no estado 1
					if(c == '\n' or c == '\r'):
						self.n_line += 1 # Mudanca de linha
			
					
			
# Main :D
if __name__ == '__main__':
	
	# Variaveis 
	token = Token('','',1,1)
	lexer = Lexer()
	lexer.Lexer('/home/caiofb47/text')
	
	# Enquanto nao houver erros
	while(True):
		token = lexer.proxToken()

		if(token != None):
			print('Token: ', token.__srt__())
		# Test se a funcao .proxToken() retorna
		#else:
			#print('N retorna')
			
		# Break caso fim de arquivo
		if(token != None and token.nomeGet() != Tag['END_OF_FILE']):
			break
	
	
	# Imprimir a tabela de simbolos
	print('')
	print('Tabela de simbolos: ')
	
	
	

