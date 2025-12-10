from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, id: str,entrada:int,tipo:str):
        self.id = id
        self.entrada = entrada
        self.tipo = tipo
    
    def __str__(self):
        return f"{self.tipo}:{self.id}:{self.entrada}"

    @abstractmethod
    def calcularValor():
        pass
class Bike(Veiculo):
    def __init__(self, id: str, entrada: int, tipo: str):
        super().__init__(id,entrada,tipo)
    
    def calcularValor(self,horaSaida:float):
        return 3
    
class Moto(Veiculo):
    def __init__(self, id: str, entrada: int, tipo: str):
        super().__init__(id,entrada,tipo)
    
    def calcularValor(self,horaSaida:float,entrada):
        tempo = horaSaida- entrada
        return tempo/20
def main():
    veiculo = Veiculo ()
    while True:
         line = input()
         print("$" + line)
         args = line.split()
         try:
             if args[0] == "end":
                 break
             elif args[0] =="show":
                 print(veiculo)
             else:
                print("Fail: comando invalido")
         except Exception as e:
          print(e)
if __name__ == "__main__":
    main()

        