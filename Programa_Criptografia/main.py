import Programa_Criptografia.chamadas
try:
    Programa_Criptografia.chamadas.processamento()
except IndexError:
    print(f'\033[31mErro: Algum(s) do(s) valor(es) foi(ram) digitado(s) incorretamente.\033[m')
except Exception as falhou:
    print(f'\033[31mErro: {falhou}\033[m')
print('\033[1;94mMuito Obrigado. Volte Sempre !\033[m')
