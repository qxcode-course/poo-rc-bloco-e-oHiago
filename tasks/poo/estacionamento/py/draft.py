from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, id: str,entrada:float):
        self.id = id
        self.entrada = entrada

    @abstractmethod
    def calcularValor(self, horaSaida:float):
        pass
    @abstractmethod
    def getTipo(self) -> str:
        pass
    def __str__(self):
        tipo = self.getTipo()
        return f"{tipo:_>10} : {self.id:_>10} : {self.entrada}"

class Bike(Veiculo):
    def __init__(self, id: str, entrada: float):
        super().__init__(id,entrada)
    
    def calcularValor(self,horaSaida:float):
        return 3.0
    def getTipo(self) -> str:
        return "Bike"
    
class Moto(Veiculo):
    def __init__(self, id: str, entrada: float):
        super().__init__(id,entrada)
    
    def calcularValor(self,horaSaida:float):
        tempo = horaSaida- self.entrada
        return tempo/20
    def getTipo(self) -> str:
        return "Moto"
class Carro(Veiculo):
    def __init__(self, id: str, entrada: float):
        super().__init__(id,entrada)
    
    def calcularValor(self,horaSaida:float):
        tempo = horaSaida- self.entrada
        valor = tempo/10
        return max(valor, 5.00)
        
    def getTipo(self) -> str:
        return "Carro"
class Estacionamento:
    def __init__(self):
        self.veiculos: dict [str, Veiculo] = {}
        self.tempo = 0
    def tempoAtual(self, time: int):
        self.tempo += time
    def entrar (self, tipo: str, id: str):
        if tipo == "bike":
            veiculo = Bike(id,self.tempo)
        elif tipo == "moto":
            veiculo = Moto(id,self.tempo)
        elif tipo == "carro":
            veiculo = Carro(id,self.tempo)

        self.veiculos[id] = veiculo
    def listar(self):
        for i in self.veiculos.values():
            print(i)
        print(f"Hora atual: {self.tempo}")
    def pagar(self, id: str):
        veiculo = self.veiculos[id]
        entrada = veiculo.entrada
        saida = self.tempo

        valor = veiculo.calcularValor(saida)

        print(f"{veiculo.getTipo()} chegou {entrada} saiu {saida}. Pagar R$ {valor:.2f}")

        del self.veiculos[id]
def main():

    estacionamento = Estacionamento ()
    while True:
         line = input()
         print("$" + line)
         args = line.split()
         try:
            if args[0] == "end":
                 break
            elif args[0] =="show":
                 estacionamento.listar()
            elif args[0] == "tempo":
                estacionamento.tempoAtual(int(args[1]))
            elif args[0] == "estacionar":
                tipo = args[1]
                id = args[2]
                estacionamento.entrar(tipo,id)
            elif args[0] == "pagar":
                id = args[1]
                estacionamento.pagar(id)
            else:
                print("Fail: comando invalido")
         except Exception as e:
          print(e)
if __name__ == "__main__":
    main()

        