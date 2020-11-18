class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def mul(self):
        return  self.a * self.b
    def sub(self):
        return  self.a - self.b
    def div(self):
        return self.a / self.b

if __name__ == '__main__':
        a = int(input("Entre com o primeiro numero: "))
        b = int(input("Entre com o segundo numero: "))

        obj = Calculator(a,b)

        choice = 1

        while choice !=0:
            print("1. adição")
            print("2. multiplicação")
            print("3. subtração")
            print("4. divisão")
            print("0. sair")
            choice = int(input("Escolha sua opção: "))
            if choice == 1:
                print("Resultado: ",obj.add())
            elif choice == 2:
                print("Resultado: ", obj.mul())
            elif choice == 3:
                print("Resultado: ", obj.sub())
            elif choice == 4:
                print("Resultado: ", round(obj.div()))
            elif choice == 0:
                print("Saindo...")
            else:
                print("Opção Invalida")


