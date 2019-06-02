class Jogo:
    def __init__(self, nome, categoria, console, usuario_id, id=None):
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.console = console
        self.usuario_id = usuario_id


class Usuario:
    def __init__(self, id, nome, senha):
        self.id = id
        self.nome = nome
        self.senha = senha