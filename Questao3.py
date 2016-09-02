'''
Média de notas.
'''
nome = input('Nome:')
n1 = float(input('1ª Nota:'))
n2 = float(input('2ª Nota:'))
n3 = float(input('3ª Nota:'))

media = (n1 + n2 + n3)/3
print('Média = %.2f' %(media))
if media >= 7:
    print('%s você está APROVADO' %(nome))
elif media >= 4 and media < 7.0:
    print('%s você está NA FINAL' % (nome))
else:
    print('%s você está REPROVADO' % (nome))