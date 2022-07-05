# Cifra de Vigenère
# Trabalho 1 de Segurança Computacional
# Alunos:
# * Gabriel Rodrigues Pacheco - 17/0058280
# * Theo
# TODO: Colocar o nome e matricula do Theo

import re


# Funcao chamada ao se selecionar a funcao de criptografar (modo 1) ou decriptografar (modo 2). Ela e responsavel por
# solicitar e validar os dados
# Recebe um int como entrada que indica o modo de operacao
def lista_criptografar(modo):
    msg = ""
    key = ""
    while msg == "":
        if modo == 1:
            msg = input("Qual mensagem deve ser criptografada?: ")
        else:
            msg = input("Qual mensagem deve ser decriptografada?: ")
        msg = msg.upper()
        regex = re.compile('[^A-Z ]')
        msg = regex.sub('', msg)
    while key == "":
        key = input("Qual a senha? (Apenas letras): ")
        key = key.upper()
        regex = re.compile('[^A-Z]')
        key = regex.sub('', key)
    if modo == 1:
        criptografar(msg, key, 1)
    else:
        criptografar(msg, key, 2)


# Funcao que realiza a criptografia. Modo 1 significa criotografar e modo 2 descriptografar
# Recebe duas strings de entrada, correspondentes a mensagem e a senha, e um int referente ao modo de operacao
def criptografar(msg, key, modo):
    count_key = 0
    resultado = ''
    # Percorre letra por letra realizando a cifracao ou decifracao e ignora os espacos
    for letra in msg:
        if letra == ' ':
            # Se a letra for um espaco, ela e apenas copiada
            letra_crip = ord(letra)
        else:
            # Realiza a soma entre a letra da msg e da chave
            if modo == 1:
                letra_crip = ord(letra) + (ord(key[count_key]) - ord('A'))
            else:
                letra_crip = ord(letra) - (ord(key[count_key]) - ord('A'))
            # Se sair dos limites desejados, ele regride ao alfabeto
            if letra_crip > ord('Z'):
                letra_crip -= 26
            if letra_crip < ord('A'):
                letra_crip += 26
        # Percorre a chave ate seu fim, ao chegar ao fim recomeca
        count_key += 1
        if count_key == len(key):
            count_key = 0
        # Adiciona o resultado a string de saida
        resultado += chr(letra_crip)
    if modo == 1:
        print("Criptograma: ")
    else:
        print("Mensagem: ")
    print(resultado)


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
        lista_criptografar(1)
    elif resposta == '2':
        lista_criptografar(2)
    else:
        pass
