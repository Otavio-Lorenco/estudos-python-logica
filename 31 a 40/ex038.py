while True:
    nome = input('Qual seu nome? ')
    idade = int(input('Qual sua idade? '))
    opn = int(input('Dê uma nota de 0 a 3 para o filme: '))

    if opn == 1:
        print(f'{nome} deu uma nota regular para o filme')
    elif opn == 2:
        print(f'{nome} deu uma nota boa para o filme')
    elif opn == 3:
        print(f'{nome} deu uma nota ótima para o filme')
    else:
        print('Nota inválida!')

    continuar = input('Deseja avaliar novamente? (s/n): ').lower()
    if continuar == 'n':
        print('Programa encerrado. Obrigado!')
        break
