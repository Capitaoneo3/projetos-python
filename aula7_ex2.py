print("este é um programa que lê 3 números e imprime eles em ordem decrescente.")

primeiro = int(input("digite o primeiro número: "))
segundo = int(input("digite o segundo número: "))
terceiro = int(input("digite o terceiro número: "))

if primeiro >= segundo >= terceiro :
    print(f"{primeiro} {segundo} {terceiro}")


elif primeiro >= terceiro >= segundo :
    print(f"{primeiro} {terceiro} {segundo}")


elif segundo >= primeiro >= terceiro :
    print(f"{segundo} {primeiro} {terceiro}")

elif segundo >= terceiro >= primeiro :
    print(f"{segundo} {terceiro} {primeiro}")

elif terceiro >= primeiro >= segundo :
    print(f"{terceiro} {primeiro} {segundo}")

elif terceiro >= segundo >= primeiro :
    print(f"{terceiro} {segundo} {primeiro}")
else:
    print("caso não caia nas outras alternativas acima.")
