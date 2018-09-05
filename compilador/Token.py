class Token:
    
    # Variaveis
    nome = ''
    lexema = ''
    linha = 0
    coluna = 0

    # Construtor
    def __init__(self):
        self.__nome
        self.__lexema
        self.__linha
        self.__coluna

    # Construtor Cheios
    def Token(self, nome, lexema, linha, coluna):
        self.__nome = nome
        self.__lexema = lexema
        self.__linha = linha
        self.__coluna = coluna

    # Gets e Sets :D
    def nomeGet(self):
        return self.__nome

    def nomeSet(self, nome):
        self.__nome = nome

    def lexemaGet(self):
        return self.__lexema

    def lexemaSet(self, lexema):
        self.__lexema = lexema

    def linhaGet(self):
        return self.__linha

    def linhaSet(self, linha):
        self.__linha = linha

    def colunaGet(self):
        return self.__coluna

    def colunaSet(self, coluna):
        self.__coluna = coluna

    def __srt__(self):
        return '<', self.__nome, ', \"', self.__lexema, '\">'
