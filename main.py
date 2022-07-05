# Cifra de Vigenère
# Trabalho 1 de Segurança Computacional
# Alunos:
# * Gabriel Rodrigues Pacheco - 17/0058280
# * Theo

import re


# Funcao chamada ao se selecionar a funcao de criptografar. Ela e responsavel por solicitar e validar os dados
def lista_criptografar():
    msg = ""
    key = ""
    while msg == "":
        msg = input("Qual mensagem deve ser criptografada?: ")
        msg = msg.upper()
        regex = re.compile('[^A-Z ]')
        msg = regex.sub('', msg)
    while key == "":
        key = input("Qual a senha? (Apenas letras): ")
        key = key.upper()
        regex = re.compile('[^A-Z]')
        key = regex.sub('', key)
    print(msg)
    print(key)


def lista_descriptografar():
    # TODO: Criar funcao de descriptografar
    print("Oi, ainda em construção")


def lista_quebrar():
    # TODO: Criar funcao de quebrar
    print("Oi, ainda em construção")


# Usamos o comeco do codigo para que o usuario escolha qual operacao deve ser feita: Cifrar, decifrar ou quebrar a cifra
if __name__ == '__main__':
    print("Seja bem-vindo!")
    print("Selecione a opção:")
    print("1 - Cifrar uma mensagem")
    print("2 - Decifrar uma mensagem")
    print("3 - Quebrar cifra")
    resposta = '0'
    while resposta != '1' and resposta != '2' and resposta != '3':
        resposta = input("Escolha: ")
    if resposta == '1':
        lista_criptografar()
    elif resposta == '2':
        pass
    else:
        pass
