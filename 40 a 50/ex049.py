print("Contador de vogais e consoantes")

frase = input("Digite sua frase aqui: ")

vogais = "aeiou"
cont_vogais = 0
cont_consoantes = 0

for letra in frase: #laço de repetição que percorre cada letra da frase
    letra = letra.lower() #garante que a letra seja minúscula para comparação

    if letra.isalpha(): #verifica se a letra é uma letra do alfabeto para evitar contar espaços e pontuações
        if letra in vogais:
            cont_vogais += 1
        else:
            cont_consoantes += 1

print(f"Vogais: {cont_vogais}")
print(f"Consoantes: {cont_consoantes}")