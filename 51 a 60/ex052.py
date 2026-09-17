def varios_contatos():
    contatos = []
    while True:
        nome = input('Digite seu nome aqui: ')
        idade = int(input('Digite sua idade aqui: '))
        email = input('digite o seu email aqui: ')
        telefone = input('Digite seu numero de telefone aqui: ')

        while len(telefone) not in (9, 12): #veerificador de telefone 
                telefone = input('Telefone inválido. Digite novamente (com DDD): ')

        contato = {
            "nome": nome,
            "idade": idade,
            "email": email,
            "telefone": telefone
        }
        

        contatos.append(contato)   # 1º: salva o contato

        if input('Deseja adicionar outro contato? (s/n) ') != 's':
            break                   # 2º: só depois pergunta e decide sair

    return contatos   # fora do while — só roda quando o laço realmente termina

def mostrar_contatos(contatos):
    for contato in contatos:
        print('-----------------------------')
        print('nome: ', contato["nome"])
        print('idade: ', contato["idade"])
        print('email: ', contato["email"])
        print('telefone: ', contato["telefone"])
        print('-----------------------------')


def main():
    contatos = varios_contatos()
    mostrar_contatos(contatos)


if __name__ == "__main__":
    main()