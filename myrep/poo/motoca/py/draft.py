class Pessoa:
    def __init__(self,nome : str, idade : int):
        self.__nome = nome
        self.__idade = idade

    def __str__(self):
        return f"({self.__nome}:{self.__idade})"

    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade

class Moto:
    def __init__(self, potencia : int = 1):
        self.potencia = potencia
        self.tempo = 0
        self.pessoa : Pessoa | None = None

    def __str__(self):
        person_str = "(empty)"
        if self.pessoa is not None:
            person_str = str(self.pessoa)

        return f"power:{self.potencia}, time:{self.tempo}, person:{person_str}"

    def inserir(self, pessoa : Pessoa):
        if self.pessoa is not None:
            print("fail: busy motorcycle")
            return 
        self.pessoa = pessoa

    def remover(self):
        if self.pessoa is None:
            print("fail: empty motorcycle")
            return
        print(f"{self.pessoa.get_nome()}:{self.pessoa.get_idade()}")
        self.pessoa = None

    def dirigir(self, tempo : int):
        if self.tempo == 0:
            print("fail: buy time first")
            return
        if self.pessoa is None:
            print("fail: empty motorcycle")
            return
        if self.pessoa.get_idade() > 10:
            print("fail: too old to drive")
            return
        if tempo > self.tempo:
            tempo_faltante = tempo - self.tempo
            print(f"fail: time finished after {tempo_faltante} minutes")
            self.tempo = 0
        else:
            self.tempo -= tempo

    def comprarTempo(self,valor : int):
        self.tempo += valor

    def buzinar(self):
        honk_str = "P" + "e" * self.potencia + "m"
        print(honk_str)

def main():
    moto = Moto()
    while True:
        try:
            line = input().strip()
        except EOFError:
            break

        print(f"${line}")
        args = line.split()

        if not args:
            continue

        cmd = args[0]

        if cmd== "end":
            break

        elif cmd == "init":
            moto = Moto(int(args[1]))

        elif cmd == "show":
            print(moto)

        elif cmd == "enter":
            nome = args[1]
            idade = int(args[2])
            moto.inserir(Pessoa(nome,idade))

        elif cmd == "leave":
            moto.remover()

        elif cmd == "buy":
            moto.comprarTempo(int(args[1]))

        elif cmd == "drive":
            moto.dirigir(int(args[1]))

        elif cmd == "honk":
            moto.buzinar()
main()