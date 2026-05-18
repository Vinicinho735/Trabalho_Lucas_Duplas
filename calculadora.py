class Calculadora:
    def __init__(self):
        self.historico = []

    def adicionar_ao_historico(self, operacao):
        self.historico.append(operacao)

    def soma(self, a, b):
        res = a + b
        self.adicionar_ao_historico(f"{a} + {b} = {res}")
        return res

    def subtracao(self, a, b):
        res = a - b
        self.adicionar_ao_historico(f"{a} - {b} = {res}")
        return res

    def multiplicacao(self, a, b):
        res = a * b
        self.adicionar_ao_historico(f"{a} * {b} = {res}")
        return res

    def divisao(self, a, b):
        if b == 0:
            raise ValueError("O divisor não pode ser zero.")
        res = a / b
        self.adicionar_ao_historico(f"{a} / {b} = {res}")
        return res

    def potencia(self, a, b):
        res = a ** b
        self.adicionar_ao_historico(f"{a} ^ {b} = {res}")
        return res