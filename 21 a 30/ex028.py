#aqui é a famosa formula para puxar o numero maximo e minimo que esta na lista

numero = ('22', '20', '31', '48', '52' ,'94', '55', '24', '61', '75')

print (f'aqui ele mostra o valor maximo da lista {max(numero)}')

print (f'aqui ele mostra o valor minimo da lista {min(numero)}')


# aqui o (sum) é usado com os mesmos numeros da lista de cima porem tem uma coisa que eu reparei só depois que é:
# para usarmos a forma (sum) temos que ter uma lista com o numero verdadeiro sem a famosa sting que é a aspas em volta do numero

sem_aspas = (25, 20, 31, 48, 52 ,94, 55, 24, 61, 75)

print(f'aqui ele mostra a soma de todos os numeros que tem na lista {sum(sem_aspas)}')