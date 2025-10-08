class Camisa:
    def __init__(self): 
        self.__tamanho: str = ""

    def setTamanho(self, valor: str) -> None:
        if valor == "PP":
            self.__tamanho = valor
        if valor == "P": 
            self.__tamanho = valor
        if valor == "M": 
            self.__tamanho = valor
        if valor == "G": 
            self.__tamanho = valor
        if valor == "GG": 
            self.__tamanho = valor
        if valor == "XG": 
            self.__tamanho = valor
        return self.__tamanho

    def getTamanho(self):
        return self.__tamanho

def main():
    roupa = Camisa()
    while roupa.getTamanho() == "":  
        print("Digite seu tamanho de roupa")
        tamanho = str(input())
        if roupa.setTamanho(tamanho):
            print("Parabens, você comprou uma roupa tamanho", roupa.getTamanho())
        else:
            print(f"Tamanho não identificado. Escolha um destes tamanhos: P, PP, M, G, GG, XG.")
main()


