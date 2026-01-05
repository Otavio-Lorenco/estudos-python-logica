nome = input('qual é seu nome? ')
por = float(input('qual a sua nota em Portugues? '))
mat = float(input('qual a sua nota em Matematica? '))
ing = float(input('qual a sua nota em Ingles? '))
art = float(input('qual a sua nota em Artes? '))
his = float(input('qual a sua nota em Historia? '))
geo = float(input('qual a sua nota em Geografia? '))

media = (por + mat + ing + art + his + geo) /6

print (f'a media do/a {nome} é {media}')

if media < 6:
    print(f'{nome} esta abaixo da media')

elif media <=7:
    print(f'{nome} esta abaixo da media')

else:
    print(f'{nome} esta acima da media')    