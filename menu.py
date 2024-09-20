from operacao import Operacao


class Menu:
    def __init__(self):
        self.opcao = -1
        self.exer = Operacao()
        self.num = 0
        self.num1 = 0
        self.num2 = 0

    def mostrarMenu(self):        print("\n ---Menu---\n\n" +
              "Escolha uma das opções abaixo:" +
              "\n0. Sair" +
              "\n1.Somar" +
              "\n2.Subtrair" +
              "\n3.Dividir" +
              "\n4.Multiplicar" +
              "\n5.Potência" +
              "\n6.Raiz" +
              "\n7.Tabuada" +
              "\n8 potencia" +
              "\n9 exercicio -1" +
              "\n10 exercicio 2" +
              "\n11 exercicio 3" +
              "\n12 exercicio 4" +
              "\n13 exercicio 5" +
              "\n14 exercicio 6" +
              "\n15 exercicio 7" +
              "\n16 exercicio 8" +
              "\n17 exercicio 9" +
              "\n18 exercicio 10"  +
              "\n19 exercicio 11"  +
              "\n20 exercicio 12" +
              '\n21 Exercício 13' +
              "\n22 Exercicio 14" +
              "\n23 Exercicio 15" +
              "\n24 Exercicio 16" +
              "\n25 Exercicio 17" +
              "\n26 Exercicio 18" +
              "\n27 Exercicio 19" +
              "\n28 Exercicio 20" +
              "\n29 Exercicio 21" +
              "\n30 Exercicio 22" +
              "\n31 Exercicio 23" +
              "\n32 Exercicio 24" +
              "\n33 Exercicio 25" +
              "\n34 Exercicio 26" +
              "\n35 Exercicio 27" +
              "\n36 Exercicio 28" +
              "\n37 Exercicio 29" +
              "\n38 Exercicio 30" +
              "\n39 Exercicio 31" +
              "\n40 Exercicio 32" )









    def coletar(self):
        self.num1 = int(input('Informe o primeiro número:'))
        self.num2 = int(input('Informe o segundo número:'))

    def operacao(self):
        while self.opcao != 0:
            self.mostrarMenu()
            self.opcao = int(input('Escolha uma das opções acima: '))
            if self.opcao == 0:
                print("Obrigado!")
            if self.opcao == 1:
                self.coletar()  # chamando o input
                print(f'A soma dos números é: {self.exer.somar(self.num1, self.num2)}')

            elif self.opcao == 2:
                self.coletar()  # chamando o input
                print(f'A subtração dos números digitados é: {self.exer.subtrair(self.num1, self.num2)}')

            elif self.opcao == 3:
                self.coletar()  # chamando o input
                print(f'A divisão dos números digitados é: {self.exer.dividir(self.num1, self.num2)}')

            elif self.opcao == 4:
                self.coletar()  # chamando o input
                print(f'A multiplicação dos números digitados é: {self.exer.multiplicar(self.num1, self.num2)}')

            elif self.opcao == 5:
                self.coletar()  # chamando o input
                print(f'A potência dos números digitados é: {self.exer.potencia(self.num1, self.num2)}')

            elif self.opcao == 6:
                self.coletar()  # chamando o input
                print(f'A raiz de {self.num1} digitado é: {self.exer.raiz(self.num1)}')

            elif self.opcao == 7:
                self.coletar()  # chamando o input
                print(f'A tabuada de {self.num1} digitado é: {self.exer.tabuada(self.num1)}')

            elif (self.opcao == 8):
                print(self.exer.potencia(base,expoente))

            elif (self.opcao == 9):
                print(self.exer.exercicio1())

            elif (self.opcao == 10):
                print(self.exer.exercicio2())

            elif(self.opcao == 11):
                print(self.exer.exercicio3())

            elif(self.opcao == 12):
                print(self.exer.exercicio4())

            elif (self.opcao == 13):
                num = int(input("Informe o primeiro número: "))
                print(self.exer.exercicio5(num))

            elif(self.opcao == 14):
                num = int(input("informe o primeiro número"))
                print(self.exer.exercicio6(num))

            elif(self.opcao == 15):
                num = int(input("informe o número")) #falta acabar
                print(self.exer.exercicio7(num))

            elif(self.opcao == 16):
                num = int(input("informe um número"))
                print(f'a número escolhido é {self.num} digitado é {self.exer.exercicio8(num)}')

            elif(self.opcao == 17):
                num = int(input("informe um numero"))
                print(f' a soma dos é {self.num} digitado é {self.exer.exercicio9(num)}')

            elif(self.opcao == 18):
                num = int(input("informe um número primo"))
                print(f'o impressão é {self.num} é {self.exer.exercicio10(num)}')

            elif(self.opcao == 19):
                num = int(input("informe um número"))
                print(f'seu número é {self.exer.exercicio11(num)}')

            elif (self.opcao == 20):
                num = int(input("informe um número"))
                print(self.exer.exercicio12(num))

            elif(self.opcao == 21):
                num = int(input("informe um número: "))
                print(self.exer.exercicio13(num))

            elif (self.opcao == 23):
                num = int(input("informe um número:"))
                print(f'a soma dos digitos  {self.num} é {self.exer.exercicio15(self.num)}')

            elif (self.opcao == 24):
                num = int(input("informe um número"))
                print(f'os numeros pares e impares {self} é {self.exer.exercicio16(self)}')

            elif (self.opcao == 25):
                num = int(input("informe um número"))
                print(f' a sequência dos número  {self} é {self.exer.exercicio17(self)}')

            elif (self.opcao == 26):
                num = int(input("informe um número"))
                print(f'a formula de Collatz{self.num} é {self.exer.exercicio18(num)}')

            elif (self.opcao == 27):
                num = int(input("Informe um número: "))
                resultado = self.exer.exercicio19(num)
                print(resultado)

            elif (self.opcao == 28):
                num = int(input("Informe um número:"))
                print(f'o número perfeito{self.num} é {self.exer.exercicio20(num)}')

            elif (self.opcao == 29):
                num = int(input("informe um número:"))
                print(f'o vice versa é {num}  ')

            elif (self.opcao == 30): #EXERCICIO 22
                self.coletar()
                print(f'  {self.exer.exercicio21(self.num1, self.num2)}')

            elif (self.opcao == 31):
                num = int(input('a Área do Retângulo é'))
                print(f'{self.exer.exercicio23()}')

            elif (self.opcao == 32):
                num = int(input("a digite o ano de nascimento"))
                print(f'sua idade em dias {self.num} digitado é {self.exer.exercicio24(num)}')

            elif (self.opcao == 33):
                num = int(input())
                print(f'o total de votos{self.num} é {self.exer.exercicio25(self.num)}')

            elif (self.opcao == 34):
                num = int(input())
                print(f'o Reajuste {self.num}  é  {self.exer.exercicio26(self.num)}')

            elif (self.opcao == 35):
                num = int(input("o custo final é "))
                print(f'o custo final {self.num} é {self.exer.exercicio27(num)}')

            elif(self.opcao == 36):
                print(f'a nota final {self.num} é {self.exer.exercicio28(self.num)}')

            elif(self.opcao == 37):
                print(self.exer.exercicio29(self.num))

            elif(self.opcao == 38):
               num1 = int(input("A sua sequência é: "))
               print(f'a sequência {self.num1} é {self.exer.exercicio30(self.num1)}')

            elif (self.opcao == 39):
                num = self.exer.exercicio31(self.num)
                print(f'A nota final {self.num} é {self.exer.exercicio31(self.num)}')

            elif (self.opcao == 40):
                num = int(input("Digite o número: "))
                print(f'O seu saldo  {self.num} é {self.exer.exercicio32(self.num)}')






























