from Tag import Tag
from Token import Token
from TS import TS

class Lexer:
	
	# Construtor/Inicializador da classe LEXER
	def __init__(self):
		self.instance_file = ''  # Referencia para o arquivo
		self.END_OF_FILE = 0  # TEM Q SER |Constante| para fim do arquivo
		self.n_line = 1
		self.n_column = 0
		self.lookahead = 0  # Armazena a posicao do ultimo caractere lido no arquivo	
		
	# Funcao para ler o arquivo
	def Lexer(self, input_data):
		# Tenta abrir e ler arquivo
		try:
			
			# Abrindo o arquivo
			lido = open(input_data, 'r')
			# Lendo o arquivo
			self.instance_file = lido.read()
			
			# Pegando o tamanho do arquivo com a funcao len para obter o EOF
			self.END_OF_FILE = len(self.instance_file)
		
		# Excecao de "No such file or directory"
		except IOError as e:
			print('Erro de abertura do arquivo:', e)
			exit(1)
		
	# Metodo que simula o AUTOMATO Finito Determinisitico
	def proxToken(self):
		
		# Variaveis do AUTOMATO FD
		lexema = []
		estado = 0
		c = ''

		while(True):
			# Avanca caractere ou retorna um token
			try:
				# Como python le direto o arquivo, n precisa converter
				if (self.lookahead != self.END_OF_FILE):
					c = self.instance_file[self.lookahead]  # Le um caractere
					self.lookahead += 1  # Muda o apontamento
					self.n_column += 1
				else:
					self.n_column += 1
			except IOError as e:
				print("Erro na leitura do caractere")
				
			# Movimentacao do AFD
			# Inicio
			# Estado 0

			if (c == '\n'):
				self.n_column =0
			if (estado == 0):
				
				if(self.lookahead == self.END_OF_FILE):
					# Retorna um novo token Tag['END_OF_FILE'], 'EOF', self.n_line, self.n_column
					return Token(Tag['EOF'], 'EOF', self.n_line, self.n_column)

						
				# Estado 0
				elif(c == ' ' or c == '\n' or c == '\t' or c == '\r'):
					estado = 0
					if (c == '\n' or c == '\t'):
						self.n_line += 1 # Avanca Linha
						self.n_column = 0 # Retorna coluna
					if (c == '\t'):
						self.n_column += 3
				
				# Estado 1
				elif (c == '+'):
					return Token(Tag['+'], '+', self.n_line, self.n_column)
				# Estado 2
				elif (c == '-'):
					return Token(Tag['-'], '-', self.n_line, self.n_column)
				# Estado 3
				elif (c == '*'):
					return Token(Tag['*'], '*', self.n_line, self.n_column)
				# Estado 4
				elif (c == '/'):
					estado = 5
				# Estado 10
				elif (c.isalpha()):
					estado = 10
				# Estado 14
				elif (c.isdigit()):
					estado = 14
				# Estado 19
				elif (c == '"'):
					estado = 19
				# Estado 22
				elif (c == ';'):
					return Token(Tag[';'], ';', self.n_line, self.n_column)
				# Estado 23
				elif (c == ','):
					return Token(Tag[','], ',', self.n_line, self.n_column)
				# Estado 24
				elif (c == ')'):
					return Token(Tag[')'], ')', self.n_line, self.n_column)
				# Estado 25
				elif (c == '('):
					return Token(Tag['('], '(', self.n_line, self.n_column)
				# Estado 26
				elif (c == '='):
					return Token(Tag['='], '=', self.n_line, self.n_column)
				# Estado 27
				elif (c == '>'):
					estado = 27
				# Estado 30
				elif (c == '<'):
					estado = 30

#$$$$$$$$$$$$$$$$$$$$$$$$ Ramo do estado 4 $$$$$$$$$ 5 ao 9 $$$$$$$$$$$$$$$$$$$$$$$$#
			# Estado 5
			if (estado == 5):
				if (c == '*'):
					estado = 6
				elif(c.isdigit()):
					return Token(Tag['/'],'/', self.n_line, self.n_column)
				# Estado 9
				elif(c == '\n'):
					return Token(Tag['//'], '//', self.n_line, self.n_column)
			if (estado == 6):

				if (c == '*'):
					estado = 7
				if (c == '/'):
					estado = 9

			if (estado == 7):
				if(c == '/'):
					estado = 8
			if (estado == 8):
				if (c == '/'):
					return Token(Tag['/**/'], '/**/', self.n_line, self.n_column)
#$$$$$$$$$$$$$$$$$$$$$$$$ Ramo do estado 4 $$$$$$$$$ 5 ao 9 $$$$$$$$$$$$$$$$$$$$$$$$#

#$$$$$$$$$$$$$$$$$$$$$$$$ Ramo do estado 10 $$$$$$$$$ 10 ao 13 $$$$$$$$$$$$$$$$$$$$$#
			if (estado == 10):
				if (c.isalpha() or c.isdigit()):
					lexema.append(c)
				else:
					# Estado 12
					if (lexema[0]== 'e'):
						return Token(Tag['e'], 'e', self.n_line, self.n_column)
					# Estado 13
					elif(lexema[0] == 'o' and lexema[1]== 'u'):
						return Token(Tag['ou'], 'ou', self.n_line, self.n_column)
					# Estado 11
					else:
						con_lisString = ''.join(lexema)
						return Token(Tag['ID'], con_lisString, self.n_line, self.n_column)  # Rever lexema - toString || __srt__(self)
#$$$$$$$$$$$$$$$$$$$$$$$$ Ramo do estado 10 $$$$$$$$$ 10 ao 13 $$$$$$$$$$$$$$$$$$$$$#

#$$$$$$$$$$$$$$$$$$$$$$$$ Ramo do estado 14 $$$$$$$$$ 14 ao 18 $$$$$$$$$$$$$$$$$$$$$#
			# Estado 14
			if (estado == 14):
				if (c.isdigit()):
					lexema.append(c)
					self.n_column += 1
				elif (c == '.'):
					estado = 16
				else:
					# Estado 15
					con_lisString = ''.join(lexema)
					return Token(Tag['INTEGER'], con_lisString, self.n_line, self.n_column)

			# Estado 16
			if (estado == 16):  # Tratar os erros de n vir numero
				if (c.isdigit() or c == '.'):
					lexema.append(c)  # permanece no estado 17
					self.n_column += 1
				else:
					# Estado 18
					# self.retornaPonteiro()
					con_lisString = ''.join(lexema)
					return Token(Tag['DOUBLE'], con_lisString, self.n_line, self.n_column)
#$$$$$$$$$$$$$$$$$$$$$$$$ Ramo do estado 14 $$$$$$$$$ 14 ao 18 $$$$$$$$$$$$$$$$$$$$$#

#$$$$$$$$$$$$$$$$$$$$$$$$ Ramo do estado 19 $$$$$$$$$ 19 ao 21 $$$$$$$$$$$$$$$$$$$$$#
			if (estado == 19):
				if (c.isalpha() or c.isdigit()):
					estado = 20

			# Estado 20
			if (estado == 20):
				# Estado = 21
				if (c == '"'):
					con_lisString = ''.join(lexema)
					return Token(Tag['String'], con_lisString, self.n_line, self.n_column)  # Rever toString do lexer
				elif (c == 'Padrao para [ConstString] invalido na linha '):
					print('[Erro Lexico]: String deve conter pelo menos um caractere. Erro na linha ', self.n_line,
						  ' coluna ', self.n_column)
					return None
				elif (self.lookahead == self.END_OF_FILE):
					print('[Erro Lexico]: String deve ser fechada com \" antes do fim de arquivo')
					return None
				# Permanece no 20
				else:
					lexema.append(c)
					self.n_column += 1
#$$$$$$$$$$$$$$$$$$$$$$$$ Ramo do estado 19 $$$$$$$$$ 19 ao 21 $$$$$$$$$$$$$$$$$$$$$#

#$$$$$$$$$$$$$$$$$$$$$$$$ Ramo do estado 27 $$$$$$$$$ 27 ao 29 $$$$$$$$$$$$$$$$$$$$$#
			if (estado == 27):
				# Estado 29
				if(c == '='):
					return Token(Tag['>='], '>=', self.n_line, self.n_column)
				# Estado 28
				elif(c.isdigit() or c.isalpha() or c == ' '):
					return Token(Tag['>'], '>', self.n_line, self.n_column)
#$$$$$$$$$$$$$$$$$$$$$$$$ Ramo do estado 27 $$$$$$$$$ 27 ao 29 $$$$$$$$$$$$$$$$$$$$$#

#$$$$$$$$$$$$$$$$$$$$$$$$ Ramo do estado 30 $$$$$$$$$ 30 ao 36 $$$$$$$$$$$$$$$$$$$$$#
			if (estado == 30):
				# Estado 32
				if(c == '='):
					return Token(Tag['<='], '<=', self.n_line, self.n_column)
				# Estado 34
				elif (c == '>'):
					return Token(Tag['<>'], '<>', self.n_line, self.n_column)
				# Estado 35
				elif (c == '-'):
					estado = 36
				elif(c.isdigit() or c.isalpha() or c == ' '):
					# Estado 31
					return Token(Tag['<'], '<', self.n_line, self.n_column)

			if (estado == 36):
				if (c.isalpha() or c.isdigit() or c == ' '):
					return Token(Tag['<--'], '<--', self.n_line, self.n_column)
#$$$$$$$$$$$$$$$$$$$$$$$$ Ramo do estado 30 $$$$$$$$$ 30 ao 36 $$$$$$$$$$$$$$$$$$$$$#

# Main :D
if __name__ == '__main__':
	
	# Variaveis Rever Deixar mais bonito
	token = Token('', '', 0, 0)
	lexer = Lexer()

	# Endereco do arquivo
	lexer.Lexer('C:/Users/caio-/oi.txt')
	
	# Enquanto nao houver erros
	while(True):
		token = lexer.proxToken()
		if(token != None):
			print(token.__srt__())
		# Break caso fim de arquivo
		if(token != None and token.nomeGet() == Tag['EOF']):
			break
	
	# Imprimir a tabela de simbolos
	print('')
	print('Tabela de simbolos: ')
	TS().__srt__()

