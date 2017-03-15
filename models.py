class Client():
    def __init__(self):
        self.nome = None
        self.endereco = None
        self.cpf = None
        self.idade = None

class Gerente():
    def __init__(self):
        self.nome = None
        self.email = None

class Equipamento():
    def __init__(self):
        self.modelo = None
        self.marca = None
        self.consumo = None

class Consumo():
    def __init__(self):
        self.horas = None
        self.consumo = None

class Agencia():
    def __init__(self):
        self.cidade = None
        self.endereco = None
        self.gerente = None

class Suporte():
    def __init__(self):
        self.chamado = None
        self.protocolo = None
