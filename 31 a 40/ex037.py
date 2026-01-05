'''
Cada espectador de um cinema respondeu a um questionário no qual constava
sua idade e a sua opinião em relação ao filme: ótimo - 3, bom - 2, regular - 1.
Faça uma Programa que receba a idade e a opinião de N espectadores, calcule e
imprima:
• a média das idades das pessoas que responderam ótimo;
• a quantidade de pessoas que responderam regular;
'''
while True:
    nome = input('qual seu nome? ')
    idade = int(input('qual sua idade? '))
    opn = int(input('De uma nota de 0 a 3 para o filme '))

    if opn == 1:
        print(f'{nome} deu uma nota regular para o filme')
    elif opn == 2:
        print(f'{nome} deu uma nota Boa para o filme')    
    elif opn == 3:
        print(f'{nome} deu uma nota otima para o filme')
    else:
        print('nota invalida')


    continuar = input('Deseja continuar?  S/N').lower()

    if continuar == 'n':
        print('o programa sera interronpido!')
        break