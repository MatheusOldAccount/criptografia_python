from random import randint
from datetime import datetime
data_atual = datetime.now()
val = randint(1, 200)


def arquivo(resultado, detalhe=False, publica1=0, publica2=0, privada1=0, privada2=0, privada3=0):
    data_formatada = data_atual.strftime('Programa executado em - \'Data: %d/%m/%Y Horário: %H:%M\'')
    archive = open('rsa.txt', 'a')
    archive.write('-=' * 30)
    archive.write(f'\n{data_formatada}\n')
    if detalhe:
        global val
        archive.write(f'Chaves públicas -> e = {publica1}, n = {publica2}\nChaves Privadas -> p = {privada1}, q = {privada2}, d = {privada3}')
        archive.write(f'\nValor de \'val\' utilizado para conta -> {val} ')
    archive.write(f'\n{resultado}\n')
    archive.write('-=' * 30)
    archive.write('\n')
    archive.close()
    print('\033[35mResultado adicionado ao arquivo!\033[m')


def escolha(decisao):
    if decisao == 'C':
        p = primo('p')
        q = primo('q')
        n = p * q
        phi = (p - 1) * (q - 1)
        while (((p == 2) and (q == 3)) or ((p == 3) and (q == 2))) or (((p == 5) and (q == 13)) or ((p == 13) and (q == 5))) or (((p == 7) and (q == 13)) or ((p == 13) and (q == 7))):
            print('\033[31mValores digitados muito baixos, não há valor para \'e\' que satisfaça a condição.\033[m')
            p = primo('p')
            q = primo('q')
        e = gerar_e(phi)
        d = inversao_modular(phi, e)
        mensagem = str(input('Mensagem que deseja criptografar: '))
        codificacao(mensagem, e, n, p, q, d)
    else:
        try:
            d = int(input('Valor da chave privada \'d\': '))
            n = int(input('Valor da chave pública \'n\': '))
            v = int(input('Valor de \'val\' utilizado para as operações: '))
            codificado = str(input('Texto codificado: '))
        except (ValueError, TypeError):
            print('\033[31mErro com os tipos de dados digitados !\033[m')
        except Exception as erro:
            print(f'\033[31mErro: {erro}\033[m')
        else:
            decodificado = decodificacao(codificado.split(), d, n, v)
            arquivo(f'Decodificação = {decodificado}')


def conversao(msg):
    global val
    convertido = ''
    tabelaconversao = '9,6y{êqíi[dlfg8únÂÃÊÀ7hu]jmâ5o)wbt1éóvKERZ-HMCTGIOBWUYAFQDSNVJPLXacx4s`(ã0*z?2à.r^ôk~}&p\'\" e3á'
    for caractere in msg:
        if caractere in tabelaconversao:
            convertido += f'{tabelaconversao.find(f"{caractere}") + val} '
        else:
            convertido += f'{caractere} '
    print(f'A conversão de {msg} é {convertido}')
    return convertido.split()


def desconversao(msg_cod, value):
    desconvertido = ''
    tabelaconversao = '9,6y{êqíi[dlfg8únÂÃÊÀ7hu]jmâ5o)wbt1éóvKERZ-HMCTGIOBWUYAFQDSNVJPLXacx4s`(ã0*z?2à.r^ôk~}&p\'\" e3á'
    for caractere in msg_cod:
        if caractere.isnumeric():
            if tabelaconversao[int(caractere) - value] == ' ':
                desconvertido += ' '
            else:
                desconvertido += f'{tabelaconversao[int(caractere) - value]}'
        else:
            desconvertido += f'{caractere}'
    # print(f'A conversão de \'{" ".join(msg_cod)}\' é {desconvertido}')
    return desconvertido


def primo(variavel):
    while True:
        try:
            tot = 0
            prim = int(input(f'Digite um número primo para \'{variavel}\': '))
        except (ValueError, TypeError):
            print(f'\033[31mErro ! Problema com os tipos de dados digitados !\033[m')
        except Exception as error:
            print(f'\033[31mErro ocorrido: {error}\033[m')
        else:
            for c in range(1, prim + 1):
                if prim % c == 0:
                    tot += 1
            if tot == 2:
                break
            else:
                print(f'\033[31mErro! Por favor, digite um número PRIMO.\033[m')
    return prim


def mdc(a, b):
    while b != 0:
        resto = a % b
        a = b
        b = resto
    return a


def gerar_e(totiente):
    total = 0
    while True:
        val = randint(2, totiente - 1)
        if mdc(totiente, val) == 1:
            total += 1
        if total > 0:
            break
    return val


def inversao_modular(func_totiente, num):
    for c in range(2, func_totiente):
        if ((c * num) % func_totiente) == 1:
            return c


def codificacao(mensage, ev, nv, pv, qv, dv):
    texto_codificado = ''
    texto_convertido = conversao(mensage)
    for txt in texto_convertido:
        if txt.isnumeric():
            texto_codificado += f'{(int(txt) ** ev) % nv} '
        else:
            texto_codificado += f'{txt} '
    arquivo(f'A codificação de {mensage} é -> {texto_codificado}', True, ev, nv, pv, qv, dv)
    # return texto_codificado


def decodificacao(mensage_codificada, dv, nv, valor):
    texto_claro = ''
    for caractere in mensage_codificada:
        if caractere.isnumeric():
            texto_claro += f'{(int(caractere) ** dv) % nv} '
        else:
            texto_claro += f'{caractere} '
    resp = desconversao(texto_claro.split(), valor)
    return resp
