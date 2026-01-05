#aqui criamos um arquivo txt
arquivo = open('ex044.txt', 'w')

arquivo.write('aqui vai criar um arquivo de texto dentro da nossa pasta \n ')
arquivo.close()

#agora vamo fazer a maquina ler
leitura = open('ex044.txt', 'r')
print (leitura.read())
leitura.close