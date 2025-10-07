class Camisa:
    def __init__(self): 
        self.__tamanho: str = ""
        
    def getTamanho(self) -> str: # métodos em python tem self como primeiro atributo
        return self.__tamanho

    def setTamanho(self, valor: str):
       if valor == "P" or "PP" or "M" or "G" or "GG" or "XG":
        valor = self.__tamanho
        return self.__tamanho

def main():
    roupa = Camisa()
    while roupa.getTamanho() == "":  
        print("Digite seu tamanho de roupa")
        tamanho = str(input())
        if roupa.setTamanho(tamanho):
            print("Parabens, você comprou uma roupa tamanho", roupa.getTamanho())
        else:
            print("Tamanho não identificado. Escolha um destes tamanhos: P, PP, M, G, GG, XG.")
main()

