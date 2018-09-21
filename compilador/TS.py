from Token import Token
from Tag import Tag

class TS:
    # Dicionario vai servir como o HASH MAP do JAVA
    # Variavies
    tabelaSimbolos = dict()
    word = Token('','',0,0)
    
    # Construtor
    def __init__(self):
        self.__tabelaSimbolos = dict()

    # Nessa classe vao ficar os Tokens de Key Words :D
    def TS(self):
        self.__word = Token()

        # Inserindo Palavras reservadas
        # Cria um token
        # Rever se falta algum
        word = Token(Tag['KW'], 'algoritmo', 0, 0)
        self.__tabelaSimbolos('algoritmo',word)
        
        word = Token(Tag['KW','declare',0, 0])
        self.__tabelaSimbolos('declare',word)
        
        word = Token(Tag['KW','fim',0, 0])
        self.__tabelaSimbolos('fim',word)
        
        word = Token(Tag['KW','subrotina',0, 0])
        self.__tabelaSimbolos('subrotina',word)
        
        word = Token(Tag['KW','retorne',0, 0])
        self.__tabelaSimbolos('retorne',word)
        
        word = Token(Tag['KW','logico',0, 0])
        self.__tabelaSimbolos('logico',word)
        
        word = Token(Tag['KW','numerico',0, 0])
        self.__tabelaSimbolos('numerico',word)
        
        word = Token(Tag['KW','literal',0, 0])
        self.__tabelaSimbolos('literal',word)
        
        word = Token(Tag['KW','nao',0, 0])
        self.__tabelaSimbolos('nao',word)
        
        word = Token(Tag['KW','se',0, 0])
        self.__tabelaSimbolos('se',word)
        
        word = Token(Tag['KW','inicio',0, 0])
        self.__tabelaSimbolos('inicio',word)
        
        word = Token(Tag['KW','senao',0, 0])
        self.__tabelaSimbolos('senao',word)
        
        word = Token(Tag['KW','enquanto',0, 0])
        self.__tabelaSimbolos('enquanto',word)
        
        word = Token(Tag['KW','para',0, 0])
        self.__tabelaSimbolos('para',word)
        
        word = Token(Tag['KW','faca',0, 0])
        self.__tabelaSimbolos('faca',word)
        
        word = Token(Tag['KW','ate',0, 0])
        self.__tabelaSimbolos('ate',word)
        
        word = Token(Tag['KW','repita',0, 0])
        self.__tabelaSimbolos('repita',word)
        
        word = Token(Tag['KW','escreva',0, 0])
        self.__tabelaSimbolos('escreva',word)
        
        word = Token(Tag['KW','leia',0, 0])
        self.__tabelaSimbolos('leia',word)
        
        word = Token(Tag['KW','verdadeiro',0, 0])
        self.__tabelaSimbolos('verdadeiro',word)
        
        word = Token(Tag['KW','falso',0, 0])
        self.__tabelaSimbolos('falso',word)
        
        word = Token(Tag['KW','ou',0, 0])
        self.__tabelaSimbolos('ou',word)
        
        word = Token(Tag['KW','e',0, 0])
        self.__tabelaSimbolos('e',word)
        
    
        
        


