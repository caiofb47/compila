# Imports
from Tag import Tag
from Token import Token
from TS import TS

class Lexer:
	
	# Construtor/Inicializador da classe LEXER
	def __init__(self):
		self.instance_file = ''  # Referencia para o arquivo
		self.END_OF_FILE = 0  # TEM Q SER |Constante| para fim do arquivo
		self.n_line = 1
		self.n_column = 1
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
			self.END_OF_FILE = len(self.instance_file) - 1
		
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
					if(c == '\n' or c == '\r'):
						self.n_line += 1  # Mudanca de linha
						self.n_column = 1  # Volta o apontamento pra 1
					elif (c == ' '):
						self.n_column += 1
					elif (c == '\t'):
						self.n_column += 3
						
			except IOError as e:
				print("Erro na leitura do caractere")
				
			# Movimentacao do AFD
			# Inicio
			# Estado 0
			if (estado == 0):
				
				if(self.lookahead == self.END_OF_FILE):
					# Retorna um novo token Tag['END_OF_FILE'], 'EOF', self.n_line, self.n_column
					return Token(Tag['EOF'], 'EOF', self.n_line, self.n_column)

				
					estado = 0
						
				# Estados principais
					
				elif (c == '+'):
					return Token(Tag['+'], '+', self.n_line, self.n_column)
				
				elif (c == '-'):
					return Token(Tag['-'], '-', self.n_line, self.n_column)
				
				elif (c == '*'):
					return Token(Tag['*', '*', self.n_line, self.n_column])
				
				# Estado 4 vai pra 5,6
				elif (c == '/'):
					estado = 4
					
				# Estado 11 || ID - Letras A-Z || a-z
			# 	elif ((c >= 65 or c <= 95) and (c >= 97 or c <= 122)):
				elif (c.isalpha()):
					estado = 11
				
				# Estado 13 ||Digitos 0-9
				elif (c.isdigit()):
					estado = 13
				
				# Estado 18 || String
				elif (c == '"'):
					estado = 18
				
				# Estado 21	
				elif (c == ';'):
					return Token(Tag[';'], ';', self.n_line, self.n_column)
				
				# Estado 22
				elif (c == ','):
					return Token(Tag[','], ',', self.n_line, self.n_column)	

				# Estado 23
				elif (c == ')'):
					return Token(Tag[')'], ')', self.n_line, self.n_column)
				
				# Estado 24
				elif (c == '('):
					return Token(Tag['('], '(', self.n_line, self.n_column)
				
				# Estado 25
				elif (c == '='):
					return Token(Tag['='], '=', self.n_line, self.n_column)
				
				# Estado 26
				elif (c == '>'):
					estado = 26
				
				# Estado 29
				elif (c == '<'):
					estado = 29
				
						
				# FIM # Estados principais		
			
			if (estado == 4):
				if(c == '/'):
					estado = 9
				# Outro = else :D
				else:
					return Token(Tag['/'], '/', self.n_line, self.n_column)
			
			# Mini Loop
			if (estado == 6):
				if (c == '*'):
					estado = 7
					
			if (estado == 7):
				if (c == '/'):
					estado = 8
			
			# Comentario de mais de uma linha		
			if (estado == 8):
				return Token(Tag['/**/'], '/**/', self.n_line, self.n_column)

			# Comentario de uma unica linha com parada no \n		
			if (estado == 9):
				# Identificou um comentario
				if (c == '*'):
					estado = 6
					
				if (c == '\n'):
					return Token(Tag['//'], '//', self.n_line, self.n_column)
			
			# Estado 11		
			# Identificou um ID A-Z a-z 0-9		
			if (estado == 11):
				if (c.isalpha() or c.isdigit()):
					lexema.append(c)
					self.n_column += 1
					# permanece no estado = 11
				else:
					# Estado 12
					con_lisString = ''.join(lexema)
					return Token(Tag['ID'], con_lisString, self.n_line, self.n_column)  # Rever lexema - toString || __srt__(self)
			
			# Estado 13			
			if (estado == 13):
				if (c.isdigit()):
					lexema.append(c)  # permanece no estado 13
					self.n_column += 1
				elif(c == '.'):
					estado = 15
				else:
					# Estado 14
					con_lisString = ''.join(lexema)
					return Token(Tag['INTEGER'], con_lisString, self.n_line, self.n_column)
				
			# Estado 15						
			if (estado == 15):  # Tratar os erros de n vir numero
				if (c.isdigit() or c == '.'):
					lexema.append(c)  # permanece no estado 16
					self.n_column += 1
				else:
					# Estado 17
					# self.retornaPonteiro()
					con_lisString = ''.join(lexema)
					return Token(Tag['DOUBLE'], con_lisString, self.n_line, self.n_column)
			
			# Estado 18 || Sinais graficos (imprimiveis) 32 a 126 Rever
			if (estado == 18):
				if (c == '"'):
					print('[Erro Lexico]: String deve conter pelo menos um caractere. Erro na linha %d \t coluna %d' % (self.n_line, self.n_column))
					return None
				elif (c == 'Padrao para [ConstString] invalido na linha '):
					print('[Erro Lexico]: String deve conter pelo menos um caractere. Erro na linha %d \t coluna %d' % (self.n_line, self.n_column))
					return None
				elif (self.lookahead == self.END_OF_FILE):
					print('[Erro Lexico]: String deve ser fechada com \" antes do fim de arquivo')
					return None
				else:
					lexema.append(c)
					self.n_column += 1
					estado = 19
			
			# Estado 19
			if (estado == 19):
				if (c == '"'):
					# Estado = 20
					con_lisString = ''.joim(lexema)
					return Token(Tag['String'], con_lisString, self.n_line, self.n_column)  # Rever toString do lexer
				elif (c == 'Padrao para [ConstString] invalido na linha '):
					print('[Erro Lexico]: String deve conter pelo menos um caractere. Erro na linha ', self.n_line, ' coluna ', self.n_column)
					return None
				elif (self.lookahead == self.END_OF_FILE):
					print('[Erro Lexico]: String deve ser fechada com \" antes do fim de arquivo')
					return None
				else:
					# Permanece no 19
					lexema.append(c)
					self.n_column += 1
			
			# Estado 26
			if (estado == 26):
				if(c == '='):
					# Estado 28
					return Token(Tag['>='], '>=', self.n_line, self.n_column)
				else:
					# Estado 27
					return Token(Tag['>'], '>', self.n_line, self.n_column)
			
			# Estado 29
			if (estado == 29):
				# Estado 30
				if (c == '>'):
					return Token(Tag['<>'], '<>', self.n_line, self.n_column)
				# Estado 31
				elif(c == '='):
					return Token(Tag[''], '', self.n_line, self.n_column)
				elif(c == '-'):
					estado = 33
				# Estado 32
				else:
					return Token(Tag['<'], '<', self.n_line, self.n_column)
			
			# Estado 33
			if (estado == 33):
				# Estado 34
				if (c == '-'):
					return Token(Tag['<--'], '<--', self.n_line, self.n_column)

			
# Main :D
if __name__ == '__main__':
	
	# Variaveis Rever Deixar mais bonito

	token = Token('', '', 0, 0)
	lexer = Lexer()
	# Endereco do arquivo
	lexer.Lexer('/home/caiofb47/text')
	
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

