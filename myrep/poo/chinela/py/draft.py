class Chinela:
    def __init__(self):
        self.__tamanho = 0

    def setTamanho(self, valor: int) -> None:
        if valor % 2 == 0 and 20 <= valor <= 50:
            self.__tamanho = valor
            return self.__tamanho

    def getTamanho(self): 
        return self.__tamanho

def main():
    chinela = Chinela()
    while chinela.getTamanho() == 0: 
        print("Digite seu tamanho de chinela")
        tamanho = int(input()) 
        if chinela.setTamanho(tamanho):
            print("Parabens, você comprou uma chinela tamanho", chinela.getTamanho())
        else:
            print(f"Não existe esse tamanho")
main()