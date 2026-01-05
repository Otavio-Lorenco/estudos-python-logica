def par_ou_impar (numero):
    if numero % 2 == 0:
        return 'par'
    else:
        return 'impar'

num = int(input('Digite um numero: '))
print (f'o numero {num} é {par_ou_impar (num)}')