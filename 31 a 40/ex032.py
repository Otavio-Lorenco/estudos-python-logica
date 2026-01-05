# Cria uma lista vazia para guardar os números
numeros = []

# Pede para o usuário digitar 5 números
for i in range(5):
    while True:
        try:
            num = int(input(f'Digite o {i+1}º número: '))
            numeros.append(num)
            break
        except ValueError:
            print('Entrada inválida. Por favor, digite um número inteiro.')

# Encontra o maior e o menor número na lista
maior_numero = max(numeros)
menor_numero = min(numeros)

# Mostra os resultados
print(f'Os números que você digitou foram: {numeros}')
print(f'O maior número é: {maior_numero}')
print(f'O menor número é: {menor_numero}')