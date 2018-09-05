import Token
import Tag

class Ts:
    # Dicionario vai servir como o HASH MAP do JAVA
    # Variavies
    tabelaSimbolos = dict()
    word = Token()
    
    # Construtor
    def __init__(self):
        self.__tabelaSimbolos = dict()

    # Nessa classe vao ficar os Tokens de Key Words :D
    def TS(self):
        self.__word = Token()

        # Inserindo Palavras reservadas
        # Cria um token
        word = Token(Tag['KeyWord'], 'public', 0, 0)
        self.__tabelaSimbolos('public',word)


