"""
vogais = 'a' ,'e' ,'i' ,'o' ,'u'
o = 'otavio'
for o in vogais:
    print (o)
"""
"""
nome = 'otavio'
vogais = 'aeiou'
contador_vogais = 0

for letras in nome:
    if nome in vogais:
        contador_vogais += 1


print (f'o nome {nome} tem {contador_vogais} vogais')         
"""

palavra = "otavio"
vogais = "aeiou"
contador_vogais = 0

for letra in palavra:
    if letra in vogais:
        contador_vogais += 1

print(f"A palavra '{palavra}' tem {contador_vogais} vogais.")