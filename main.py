# Cifra de Vigenère
# Trabalho 1 de Segurança Computacional
# Alunos:
# * Gabriel Rodrigues Pacheco - 17/0058280
# * Théo Henrique Gallo - 17/0080781

import re

# Lista de probabilidades em porcentagem
# A = 0, B = 1, ...
prob_por = [14.63, 1.04, 3.88, 4.99, 12.57, 1.02, 1.3, 1.28, 6.18, 0.4, 0.02, 2.78, 4.74, 5.05, 10.73, 2.52, 1.2, 6.53, 7.81, 4.34, 4.63, 1.67, 0.01, 0.21, 0.01, 0.47]
prob_ing = [8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153, 0.772, 4.025, 2.406, 6.749, 7.507, 1.929, 0.095, 5.987, 6.327, 9.056, 2.758, 0.978, 2.36, 0.15, 1.974, 0.074]


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
    msg = ""
    while msg == "":
        msg = input("Qual mensagem deve ser decriptografada mesmo sem a chave?: ")
        msg = msg.upper()
        regex = re.compile('[^A-Z ]')
        msg = regex.sub('', msg)


    # a = 0
    # for prob in prob_ing:
    #     print(chr(ord('A')+a))
    #     print(prob)
    #     a += 1

    # TODO: Criar funcao de quebrar


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
        lista_quebrar()
