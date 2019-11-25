def menu():
    """
    Função responsável por criar um menu inicial para o usuário e por verificar se o usuário tem permissão para operar
    o sistema.
    :return: Retorna a senha para confirmar se a pessoa tem permissão.
    """
    print()
    print(f'\033[1m{"SISTEMA DE CRIPTOGRAFIA":^102}')
    print('\033[92m')
    print("Acesso restrito a área contaminada ambientalmente, contendo riscos a saúde pública.\nSomente"
          " é possível utilizar o sistema pessoas que tenham permissão para tal, de forma a\nserem"
          " responsáveis para não permitir que a situação piore ainda mais.\n")
    confirma = str(input('Digite a senha que se encontra no arquivo \'senha.txt.enc\', que está criptografado,\n'
                         'para verificar se você tem permissão de utilizar o sistema: '))
    print('\033[m')
    return confirma


def menu2():
    print()
    print(f'\033[1m{"SISTEMA DE CRIPTOGRAFIA":^102}')
    print('\033[92m')
    print("Acesso restrito a área contaminada ambientalmente, contendo riscos a saúde pública.\nSomente"
          " é possível utilizar o sistema pessoas que tenham permissão para tal, de forma a\nserem"
          " responsáveis para não permitir que a situação piore ainda mais.\n")
    print('Por ser a primeira execução do programa, será necessário gerar uma senha ...\033[m\n')
    while True:
        senha = str(input("Configurando os dados... Por favor, digite uma senha que será usada "
                          "nas próximas execuções do programa: "))
        senha_novamente = str(input("Confirme a senha: "))
        if senha == senha_novamente:
            break
        else:
            print('\033[31mSenhas diferentes! Por favor, preencha os dados novamente.\033[m')
    return senha
