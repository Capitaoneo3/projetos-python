
#1. Faça um programa que peça dois números inteiros e 
#armazene em duas variáveis. Em seguida, troque o valor das variáveis e exiba na tela



num1 = int(input("digite o primeiro número: "))#primeira atribuição de valor de num1
num2 = int(input("digite o segundo número: "))#segunda atribuição de valor de num2
aux = ""
aux = num2
num2 = num1#neste momento num2 está tendo seu valor re atribuido
num1 = aux#neste momento num1 está tendo seu valor re atribuido

print(f"o valor de num2 é: {num2} \ne o valor de num1 é {num1}")