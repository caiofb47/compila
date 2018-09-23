from Token import Token
from Tag import Tag

class TS:
    # Lista 
    # Variavies
    tabelaSimbolos = []
    word = Token('', '', 0, 0)
    
    # Construtor
    def __init__(self):
        self.__tabelaSimbolo = []
        self.__word = Token('', '', 0, 0)

    # Nessa classe vao ficar os Tokens de Key Words :D
    # def TS(self):
        
    word = Token(Tag['KW'], 'algoritmo', 0, 0)
    tabelaSimbolos.append(['algoritmo', word])
        
    word = Token(Tag['KW'], 'declare', 0, 0)
    tabelaSimbolos.append(['declare', word])
        
    word = Token(Tag['KW'], 'fim', 0, 0)
    tabelaSimbolos.append(['fim', word])
        
    word = Token(Tag['KW'], 'subrotina', 0, 0)
    tabelaSimbolos.append(['subrotina', word])
        
    word = Token(Tag['KW'], 'retorne', 0, 0)
    tabelaSimbolos.append(['retorne', word])
        
    word = Token(Tag['KW'], 'logico', 0, 0)
    tabelaSimbolos.append(['logico', word])
        
    word = Token(Tag['KW'], 'numerico', 0, 0)
    tabelaSimbolos.append(['numerico', word])
        
    word = Token(Tag['KW'], 'literal', 0, 0)
    tabelaSimbolos.append(['literal', word])
        
    word = Token(Tag['KW'], 'nao', 0, 0)
    tabelaSimbolos.append(['nao', word])
        
    word = Token(Tag['KW'], 'se', 0, 0)
    tabelaSimbolos.append(['se', word])
        
    word = Token(Tag['KW'], 'inicio', 0, 0)
    tabelaSimbolos.append(['inicio', word])
        
    word = Token(Tag['KW'], 'senao', 0, 0)
    tabelaSimbolos.append(['senao', word])
        
    word = Token(Tag['KW'], 'enquanto', 0, 0)
    tabelaSimbolos.append(['enquanto', word])
        
    word = Token(Tag['KW'], 'para', 0, 0)
    tabelaSimbolos.append(['para', word])
        
    word = Token(Tag['KW'], 'faca', 0, 0)
    tabelaSimbolos.append(['faca', word])
        
    word = Token(Tag['KW'], 'ate', 0, 0)
    tabelaSimbolos.append(['ate', word])
        
    word = Token(Tag['KW'], 'repita', 0, 0)
    tabelaSimbolos.append(['repita', word])
        
    word = Token(Tag['KW'], 'escreva', 0, 0)
    tabelaSimbolos.append(['escreva', word])
        
    word = Token(Tag['KW'], 'leia', 0, 0)
    tabelaSimbolos.append(['leia', word])
        
    word = Token(Tag['KW'], 'verdadeiro', 0, 0)
    tabelaSimbolos.append(['verdadeiro', word])
        
    word = Token(Tag['KW'], 'falso', 0, 0)
    tabelaSimbolos.append(['falso', word])
        
    word = Token(Tag['KW'], 'ou', 0, 0)
    tabelaSimbolos.append(['ou', word])
        
    word = Token(Tag['KW'], 'e', 0, 0)
    tabelaSimbolos.append(['e', word])
    
    def __srt__(self):
        # return self.tabelaSimbolos
        cont = 0
        for i in self.tabelaSimbolos:
            print 'posicao %i' % cont, '<"KW", "%s">' % self.tabelaSimbolos[cont][0]  # Acessando a variavel na posicao i/count, imprimindo o primeiro elemento da lista
            #Dentro de outra lista
            cont += 1
