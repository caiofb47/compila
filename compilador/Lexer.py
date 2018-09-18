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
		self.n_line = 1
		self.n_column = 1
		
		
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
					return Token(Tag['EOF'], 'EOF', self.n_line, self.n_column)
				
				# Estado 1
				elif(c == ' ' or c == '\t' or c =='\n' or c =='\r'):
					# Permanece no estado 1
					if(c == '\n' or c == '\r'):
						self.n_line += 1 # Mudanca de linha
						self.n_column = 1 # Volta o apontamento pra 1
					elif (c == ' '):
						self.n_column += 1
					elif (c == '\t'):
						self.n_column += 3 # Rever: nao tenho certeza se sao 3
				
					estado = 1
				# Nivel 1	
				# Estado 2
				elif (c == '+'):
					estado = 2
				
				# Estado 3
				elif (c == '-'):
					estado = 3
				
				# Estado 4
				elif (c == '*'):
					estado = 4
					
				# Estado 5 (Pode tomar mais de um caminho :D)
				elif (c == '/'):
					estado = 5
				
				# Rever Falta o Q9(10) e o Q10(11)
				
				# Letras
				
				
				
				# FIM Nivel 1	
				
				# RAMOS do Estado 5		
			if (estado == 5):
				
				if (c == '/'):
					return Token(Tag['/'], '/', self.n_line, self.n_column)
				# Identificou um comentario
				elif (c == '*'):
					estado = 7
			
			if (estado == 7): # Ramo do 7
				if (c == '*'):
					estado = 8
					
			if (estado == 8):
				if (c == '*'):
					estado = 9
					
			if (estado == 9):
				if (c == '/'):
					return Token(Tag['Coment'], '/**/', self.n_line, self.n_column)
					
					
					
				
				
					
						
			
			
					
			
# Main :D
if __name__ == '__main__':
	
	# Variaveis Rever Deixar mais bonito
	token = Token('','',1,1)
	lexer = Lexer()
	lexer.Lexer('/home/caiofb47/text2')
	
	# Enquanto nao houver erros
	while(True):
		token = lexer.proxToken()

		if(token != None):
			print('Token: ', token.__srt__())
		# Test se a funcao .proxToken() retorna
		#else:
			#print('N retorna')
			
		# Break caso fim de arquivo
		if(token != None and token.nomeGet() == Tag['EOF']):
			break
	
	
	# Imprimir a tabela de simbolos
	print('')
	print('Tabela de simbolos: ')
	
	
	

