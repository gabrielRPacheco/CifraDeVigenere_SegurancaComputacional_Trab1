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


def sort(sub, indice):
    return sorted(sub, key=lambda x: x[indice])


def lista_quebrar():
    # Recebe do usuario a msg a ser decifrada
    msg = ""
    while msg == "":
        msg = input("Qual mensagem deve ser decriptografada mesmo sem a chave?: ")
        msg = msg.upper()
        regex = re.compile('[^A-Z ]')
        msg = regex.sub('', msg)

    # Separa a msg em trios
    trios = []
    for i in range(len(msg)):
        if (i+3) <= len(msg):
            trios.append(msg[i]+msg[i+1]+msg[i+2])

    # Procura pela repeticao dos trios na msg, conta as ocorrencias
    distancia_trios = []
    ocorrencias_trios = []
    for i in range(len(trios)):
        count = trios.count(trios[i])
        if count > 1:
            ocorrencias_trios.append([trios[i], i])
    ocorrencias_trios = sort(ocorrencias_trios, 0)
    # Calcula a distancia entre as ocorrencias
    for i in range(len(ocorrencias_trios)):
        for j in range(len(ocorrencias_trios)):
            if i != j and ocorrencias_trios[i][0] == ocorrencias_trios[j][0]:
                distancia = ocorrencias_trios[j][1]-ocorrencias_trios[i][1]
                if distancia > 0:
                    distancia_trios.append(distancia)
    distancia_trios = sorted(distancia_trios)

    # Realiza a fatoracao
    # TODO: Isso esta certo?
    fatores = []
    for i in range(len(distancia_trios)):
        for j in range(distancia_trios[i]):
            if j > 0 and distancia_trios[i] % (j + 1) == 0:
                fatores.append(j+1)
    fatores = sorted(fatores)

    # Calcula a probabilidade de tamanho de chave
    tamanhos_esperados = []
    for numero in fatores:
        if [numero, fatores.count(numero)] not in tamanhos_esperados:
            tamanhos_esperados.append([numero, fatores.count(numero)])
    tamanhos_esperados = sort(tamanhos_esperados, 1)
    tamanhos_esperados = list(reversed(tamanhos_esperados))
    print(tamanhos_esperados)

    # Apresenta o resultado para o usuario escolher o tamanho da chave
    total_repeticoes = 0
    for repeticao in tamanhos_esperados:
        total_repeticoes += repeticao[1]
    print(total_repeticoes)
    print(f"+----------------+----------------+")
    print(f"+ Chave sugerida +      Chances   +")
    print(f"+----------------+----------------+")
    for repeticao in tamanhos_esperados:
        print(f"+          {'% 3.0f'%(repeticao[0])}   +        {'%0.3f'%(repeticao[1]/total_repeticoes)}   +")
    print(f"+----------------+----------------+")
    tam_senha_escolhido = 0
    valid = False
    while not valid:
        try:
            tam_senha_escolhido = int(input('Escolha um número: '))
            if tam_senha_escolhido > 0:
                valid = True
        except ValueError:
            print('Por favor, escolha um número válido')

    # Separar a msg em segmentos com base no tamanho de senha escolhido
    segmento_msg = []
    for x in range (tam_senha_escolhido):
        segmento_msg.append(list())
    count = 0
    for i in range(len(msg)):
        segmento_msg[count].append(msg[i])
        count += 1
        if count >= tam_senha_escolhido:
            count = 0

    # Calcula a frequencia de cada letra em cada segmento
    freq_segmentos = [[0] * 26 for i in range(tam_senha_escolhido)]
    for i in range(tam_senha_escolhido):
        for j in range (26):
            freq_segmentos[i][j] = segmento_msg[i].count(chr(ord('A')+j))/len(segmento_msg[i])
    print(freq_segmentos)


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
