class Client(Object):
    def __init__(self):
        self.nome = None
        self.endereco = None
        self.cpf = None
        self.idade = None

class Gerente(Object):
    def __init__(self):
        self.nome = None
        self.email = = None

class Equipamento(Object):
    def __init__(self):
        self.modelo = None
        self.marca = None
        self.consumo = None

class Consumo(Object):
    def __init__(self):
        self.horas = None
        self.consumo = None

class Agencia(Object):
    def __init__(self):
        self.cidade = None
        self.endereco = None
        self.gerente = None

class Suporte(Object):
    def __init__(self):
        self.chamado = None
        self.protocolo = None
