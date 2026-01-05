Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

Q1 = int(input('voce gosta do (1) amanhecer ou do (2) anoitecer? \n'))
if Q1 == 1:
  Gryffindor += 1
elif Q1 == 2:
  Hufflepuff += 1
else:
  print('Nenhuma casa ganha pontos!')  

Q2 = int(input('''Quando eu morrer, Eu quero que as pessoas se lembrem de mim como?
1) O Bom
2) O Legal
3) O Sabio
4) O Audacioso
> '''))
if Q2 == 1:
  Hufflepuff += 2
elif Q2 == 2:
  Slytherin += 2
elif Q2 == 3:
  Ravenclaw += 2
elif Q2 == 4:
  Gryffindor += 2
else:
  print('Nenhuma casa ganha pontos!')  

Q3 = int(input('''qual desses tipos de instrumentos mais agrada sua orelha?
1) O violino
2) O trompete
3) O piano
4) A bateria
'''))
if Q3 == 1:
  Slytherin += 4
elif Q3 == 2:
  Hufflepuff += 4
elif Q3 == 3:
  Ravenclaw += 4
elif Q3 == 4:
  Gryffindor += 4       

resultados = {
    'Gryffindor': Gryffindor,
    'Ravenclaw': Ravenclaw,
    'Hufflepuff': Hufflepuff,
    'Slytherin': Slytherin
}


vencedora = max(resultados, key=resultados.get)

print(f'\nSua casa é: {vencedora}!')