qnt_laranja_pedro = 10
#perguntas pro usuário
print("pedro tem 10 laranjas, pegue algumas para você.")
qnt_laranja_usuario = int(input("quantas laranjas você quer retirar? "))
#retira do valor de pedro o que o usuário pegar
qnt_laranja_pedro = qnt_laranja_pedro-qnt_laranja_usuario
#caso sobre mais ou igual a 5, mostre que pedro está feliz
if qnt_laranja_pedro >= 5:
    print("pedro ficou feliz, qntd laranjas restantes: ",qnt_laranja_pedro)
elif qnt_laranja_pedro < 5:
    print("pedro ficou triste, qntd laranjas restantes: ",qnt_laranja_pedro)


