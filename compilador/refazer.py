# Estado 11 || ID - Letras A-Z || a-z
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
				
			
			if (estado == 5):
				if(c == '/'):
					estado = 6
				
			# Comentario de uma unica linha com parada no \n 		
			if (estado == 6):
				# Identificou um comentario
				if (c == '*' or '/'):
					estado = 7
					
				elif (c != '/' and c.isdigit()):
					return Token(Tag['/'], '/', self.n_line, self.n_column)
			# Mini Loop
			if (estado == 7):
				if (c == '*'):
					estado = 8
				if (c == '/'):
					return Token(Tag['//'], '//', self.n_line, self.n_column)
					
			if (estado == 8):
				if (c == '/'):
					estado = 9
			
			# Comentario de mais de uma linha		
			if (estado == 9):
				return Token(Tag['/**/'], '/**/', self.n_line, self.n_column)

			# Estado 11		
			# Identificou um ID 
			if (estado == 11):
				if (c.isalpha() or c.isdigit()):
					lexema.append(c)
					self.n_column += 1
					# permanece no estado = 11
				else:
					if (lexema[0]== 'e'):
						estado = 36
					elif(lexema[0] == 'o' and lexema[1]== 'u'):
						estado = 39
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
				if(c.isalpha() or c.isdigit()):
					estado = 19
			
			# Estado 19
			if (estado == 19):
				if (c == '"'):
					# Estado = 20
					con_lisString = ''.join(lexema)
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
				
			if (estado == 36):
				return Token(Tag['e'], 'e', self.n_line, self.n_column)
			
			if (estado == 39):
				return Token(Tag['ou'], 'ou', self.n_line, self.n_column)