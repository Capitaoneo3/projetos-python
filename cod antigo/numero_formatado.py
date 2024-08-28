total = float(input('Premio total da Mega: '))

num = int(input('Número de ganhadores: '))



#print('O  premio total foi R$ %.2f  para %d ganhadores, onde cada um ficou com R$ %.2f' %(total,num,total/num))

print(f'O premio total foi R${total:.2f} para {num} ganhadores, onde cada um ficou com R${total/num:.2f}')

