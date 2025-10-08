class Roupa:
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
    roupa : Roupa = None
    while True:
        line:str=input()
        print("$"+line)
        args:list[str]=line.split(" ")
        if args[0]=="end":
            break
        if args[0]=="size":
            valor: str = str(args[1])
            roupa = valor
        else:
            print("fail: Valor inválido, tente PP, P, M, G, GG ou XG")
        if args[0]=="show":
            print(roupa)
main()