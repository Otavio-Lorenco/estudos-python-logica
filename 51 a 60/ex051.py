def criar_contato():
    nome = input('Digite o seu nome aqui: ')
    idade = input('Digite a sua idade aqui: ')
    email = input('digite o seu email aqui: ')
    telefone = input('Digite seu numero de telefone aqui: ')

    contato = {
        "nome": nome,
        "idade": idade,
        "email": email,
        "telefone": telefone
    }

    return contato

def mostrar_contato (contato):
    print('nome: ', contato["nome"])
    print('idade: ', contato["idade"])
    print('email: ', contato["email"])
    print('telefone: ', contato["telefone"])

c = criar_contato()
mostrar_contato(c)