from abc import ABC, abstractmethod

 
class Animal(ABC):
    def __init__(self, especie:str):
        self.especie = especie
    def apresentar_nome(self) -> str:
        return f"Eu sou um(a) {self.especie}"  
    @abstractmethod
    def fazer_som(self) -> str:
        pass
    @abstractmethod
    def mover (self) -> str:
        pass
class Cachorro(Animal):
    def __init__(self, especie:str):
        super().__init__(especie)
    
    def fazer_som(self) -> str:
        return "Au Au" 
    def mover(self) -> str:
        return "Au *passo* Au *Passo*"
class Cobra(Animal):
    def __init__(self, especie:str):
        super().__init__(especie)
    
    def fazer_som(self) -> str:
        return "Shhhhhhhhh" 
    def mover(self) -> str:
        return "*Rasteja*"

class Elefante(Animal):
    def __init__(self, especie:str):
        super().__init__(especie)
    
    def fazer_som(self) -> str:
        return "Pruuuuuuuuu" 
    def mover(self) -> str:
        return "*TUM* *TUM*"   
def apresentar(animal: Animal):
    print(animal.apresentar_nome())
    print(animal.fazer_som())
    print(animal.mover())

def main():
    animais = [
        Cachorro("cachorro"),
        Cobra("cobra"),
        Elefante("elefante")
    ]
    for animal in animais:
        apresentar(animal)

if __name__ == "__main__":
    main()