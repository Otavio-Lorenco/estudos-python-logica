salario = float(input('Qual é o seu salario ? '))

if salario > 2000:
    print (salario)
elif salario <= 1660:
    print (f'o seu salario com bonus fiica: {salario + salario * 0.20} ')    