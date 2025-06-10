inicio = int(input('digite um numero inicial: '))
final = int(input('digite o numero final: '))
passo = int(input('digite o intervalo:'))


for conta in range(inicio, final+1, passo):
    print('numero {}' .format(conta))
print ('fim contagem')
