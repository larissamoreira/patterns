class Quarto:
    def __init__(self, tipo, preço):
        self.tipo = tipo
        self.preço = preço
        self.disponivel = True
    
    def __str__(self):
        return f'{self.tipo} - R${self.preço}'