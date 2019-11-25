from Crypto import Random
from Crypto.Cipher import AES
import os
import os.path


class Criptografia:
    def __init__(self, chave):
        self.chave = chave

    def bloco(self, s):
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

    def criptografar(self, mensagem, chave):
        mensagem = self.bloco(mensagem)
        valor_binario = Random.new().read(AES.block_size)
        cifra = AES.new(chave, AES.MODE_CBC, valor_binario)
        return valor_binario + cifra.encrypt(mensagem)

    def criptografar_file(self, nome_arquivo):
        with open(nome_arquivo, 'rb') as arquivo:
            texto_simples = arquivo.read()
        enc = self.criptografar(texto_simples, self.chave)
        with open(nome_arquivo + ".enc", 'wb') as arquivo:
            arquivo.write(enc)
        os.remove(nome_arquivo)

    def descriptografar(self, texto_cifrado, chave):
        valor_binario = texto_cifrado[:AES.block_size]
        cifra = AES.new(chave, AES.MODE_CBC, valor_binario)
        texto_simples = cifra.decrypt(texto_cifrado[AES.block_size:])
        return texto_simples.rstrip(b"\0")

    def descriptografar_file(self, nome_arquivo):
        with open(nome_arquivo, 'rb') as arquivo:
            texto_cifrado = arquivo.read()
        dec = self.descriptografar(texto_cifrado, self.chave)
        with open(nome_arquivo[:-4], 'wb') as arquivo:
            arquivo.write(dec)
        os.remove(nome_arquivo)

    def PegarTodosArquivos(self):
        diretorio = os.path.dirname(os.path.realpath(__file__))
        dirs = []
        for dirName, subdirList, fileList in os.walk(diretorio):
            for fname in fileList:
                if fname != 'main.py' and fname != 'senha.txt.enc':
                    dirs.append(dirName + "/" + fname) if os.name != 'nt' else dirs.append(dirName + "\\" + fname)
        return dirs

    def criptografar_todos_arquivos(self):
        dirs = self.PegarTodosArquivos()
        for nome_arquivo in dirs:
            self.criptografar_file(nome_arquivo)

    def descriptografar_todos_arquivos(self):
        dirs = self.PegarTodosArquivos()
        for nome_arquivo in dirs:
            self.descriptografar_file(nome_arquivo)


def limpa_tela(): os.system('cls' if os.name == 'nt' else 'clear')


def menu(chave):
    key = chave
    enc = Criptografia(key)
    while True:
        limpa_tela()
        try:
            opc = int(input(
                "1. Aperte '1' para criptografar um arquivo.\n2. Aperte '2' para descriptografar um arquivo.\n"
                "3. Aperte '3' para criptografar todos os arquivos no diretório.\n"
                "4. Aperte '4' para descriptografar todos os arquivos no diretório.\n5. Aperte '5' para sair.\n"))
        except (ValueError, TypeError):
            print('\033[31mErro com os tipos de dados digitados !\033[m')
        except Exception as erro:
            print(f'\033[31mErro: {erro}\033[m')
        else:
            limpa_tela()
            if opc == 1:
                try:
                    nome = str(input("Nome do arquivo que deseja criptografar: ")).strip()
                    enc.criptografar_file(nome)
                except FileNotFoundError:
                    print('\033[31mArquivo não encontrado !\033[m')
                except Exception as error:
                    print(f'\033[31mErro: {error}\033[m')
                else:
                    print(f'\033[34mArquivo \'{nome}\' Criptografado com Sucesso !\033[m')
            elif opc == 2:
                try:
                    nome2 = str(input("Nome do arquivo que deseja descriptografar: ")).strip()
                    enc.descriptografar_file(nome2)
                except FileNotFoundError:
                    print('\033[31mArquivo não encontrado !\033[m')
                except Exception as error:
                    print(f'\033[31mErro: {error}\033[m')
                else:
                    print(f'\033[34mArquivo \'{nome2}\' Descriptografado com Sucesso !\033[m')
            elif opc == 3:
                enc.criptografar_todos_arquivos()
            elif opc == 4:
                enc.descriptografar_todos_arquivos()
            elif opc == 5:
                break
            else:
                print('\033[31mPor favor, selecione uma opção válida!\033[m')

