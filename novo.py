
numero = 1
max = int(input("digite um inteiro maior que 1: "))


countAlunos = 0
countalunos = 5

comeco = "começo"

print("Numeros pares entre 1 e", max, ":")

while numero <= max:
    if numero%2==0:
        print(numero, end=" ")
    numero+=1