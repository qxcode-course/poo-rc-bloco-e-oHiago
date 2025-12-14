from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, valor: float, descricao: str):
        self.valor: float = valor 
        self.descricao: str = descricao

    def validar_valor(self):
        if self.valor <=0:
            raise Exception("Valor negativo")
        
    def resumo(self):
        print(f"pagamento de R$ {self.valor}:{self.descricao}")
    
    @abstractmethod
    def processar(self):
        pass

class Pix(Pagamento):
    def __init__(self, valor: float, descricao: str, chave: str, banco: str):
        super().__init__(valor, descricao)
        self.chave = chave
        self.banco = banco

    def processar(self):
        print(f"Pagando pix produto {self.descricao} para {self.chave} do banco {self.banco} no valor de {self.valor}")
    

class CartaoCredito(Pagamento):
    def __init__(self, valor: float, descricao: str, numero: float, nome_titular: str, limite_disponivel: float):
        super().__init__(valor,descricao)
        self.numero = numero
        self.nome_titular = nome_titular
        self.limite_disponivel = limite_disponivel

    def processar(self):
        if self.valor > self.limite_disponivel:
            raise Exception(f"Erro: Limite insuficiente no cartão {self.numero}")
        else:
            self.limite_disponivel -= self.valor
            print(f"Pagamento aprovado no cartão Cliente {self.nome_titular}. Limite restante: {self.limite_disponivel}")
class Boleto(Pagamento):
    def __init__(self, valor: float, descricao: str, codigo_barras: int, vencimento: str):
        super().__init__(valor,descricao)
        self.codigo_barras = codigo_barras
        self.vencimento = vencimento

    def processar(self):
        print("Boleto gerado. Aguardando pagamento...")

def processar_pagamento(pagamento: Pagamento):
    pagamento.validar_valor()
    pagamento.resumo()
    pagamento.processar()
def main():

    pagamentos = [
        Pix(150, "Camisa esportiva","seila@email.com","Banco XPTO"),
        CartaoCredito(400, "Tenis", "1234 5678 9101", "Cliente X", 500),
        Boleto(80.90, "Livro de Python", "1234567890", "2025-01-10"),
        CartaoCredito(800,"Notebook","1111 2222 3333 4444", "cliente y", 700)
    ]
    for pagamento in pagamentos:
        try:
            processar_pagamento(pagamento)
        except Exception as e:
            print(e)
if __name__ == "__main__":
    main()
