'''
Contador de opinião da satisfação de um filme!
'''

contador_otimo = 0
contador_bom = 0
contador_regular = 0

for x in range(10):
    opiniao =  int(input('Digite aqui sua opinião com relação ao filme: 1 para regular, 2 para bom ou 3 para ótimo: '))
    if opiniao == 1:
        contador_regular = contador_regular + 1
        print('Regular')
    elif opiniao == 2:
        contador_bom = contador_bom + 1
        print('Bom')
    elif opiniao == 3:
        contador_otimo = contador_otimo + 1
        print('Ótimo')
    else:
        print('Opção inválida.')
print('a) %i pessoa(s) que respondeu(ram) ótimo.' % contador_otimo)
print('b) %i pessoa(s) que respondeu(ram) bom.' % contador_bom)
print('c) %i pessoa(s) que respondeu(ram) regular.' % contador_regular)