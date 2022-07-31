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
            msg = input("Qual mensagem deve ser criptografada? (Apenas letras de A a Z e espaços serão aceitos): ")
        else:
            msg = input("Qual mensagem deve ser decriptografada? (Apenas letras de A a Z e espaços serão aceitos): ")
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


# Funcao usada para apresentar as probabilidades de cada letra na msg
def print_probabilidades(probabilidade_1, probabilidade_2, probabilidade_3, total=10, maximo=10, letra_estudo='A', letra_base='A', suffix='', decimals=2, length=25, fill='█'):
    percent_1 = ("{0:." + str(decimals) + "f}").format(100 * (probabilidade_1 / float(total)))
    percent_2 = ("{0:." + str(decimals) + "f}").format(100 * (probabilidade_2 / float(total)))
    percent_3 = ("{0:." + str(decimals) + "f}").format(100 * (probabilidade_3 / float(total)))
    filled_length_1 = int(length * probabilidade_1 // maximo)
    filled_length_2 = int(length * probabilidade_2 // maximo)
    filled_length_3 = int(length * probabilidade_3 // maximo)
    bar_1 = fill * filled_length_1 + '-' * (length - filled_length_1)
    bar_2 = fill * filled_length_2 + '-' * (length - filled_length_2)
    bar_3 = fill * filled_length_3 + '-' * (length - filled_length_3)
    print('\r+ %s |%s| %s%% %s  +  %s |%s| %s%% %s + |%s| %s%% %s +' % (letra_estudo, bar_1, percent_1, suffix, letra_base, bar_2, percent_2, suffix, bar_3, percent_3, suffix))


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

    # Apresenta o resultado para o usuario escolher o tamanho da chave
    total_repeticoes = 0
    for repeticao in tamanhos_esperados:
        total_repeticoes += repeticao[1]
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
    for x in range(tam_senha_escolhido):
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
        for j in range(len(freq_segmentos[0])):
            freq_segmentos[i][j] = segmento_msg[i].count(chr(ord('A')+j))/len(segmento_msg[i]) * 100

    # Vamos permitir ao usuario ver as probabilidades calculadas e alinhar a chave
    frequencia_maxima_lista = list()
    frequencia_maxima_lista.append(max(prob_por))
    frequencia_maxima_lista.append(max(prob_ing))
    for i in range(tam_senha_escolhido):
        frequencia_maxima_lista.append(max(freq_segmentos[i]))
    frequencia_maxima = max(frequencia_maxima_lista)
    senha = list()
    for i in range(tam_senha_escolhido):
        senha.append(0)
    for j in range(tam_senha_escolhido):
        while True:
            senha_letras = ''
            for i in range(tam_senha_escolhido):
                senha_letras += chr(ord('A') + senha[i])
            print(f"Senha atual: {senha_letras}")
            seta = "             " + (' ' * j) + "^"
            print(seta)
            print(f"Posicao atual: {j}")
            print()
            print(f"+---------------------------------------+---------------------------------------+-------------------------------------+")
            print(f"+   Frequência msg                      +   Frequência por                      +   Frequência ing                    +")
            print(f"+---------------------------------------+---------------------------------------+-------------------------------------+")
            for i in range(len(freq_segmentos[0])):
                posicao = i + int(senha[j])
                if posicao >= 26:
                    posicao -= 26
                # print_probabilidades(probabilidade_1, probabilidade_2, probabilidade_3, total=10, maximo=10, letra_estudo='A', letra_base='A', suffix='', decimals=2, length=25, fill='█')
                print_probabilidades(freq_segmentos[j][posicao], prob_por[i], prob_ing[i], 100, frequencia_maxima, chr(ord('A')+posicao), chr(ord('A')+i))
            print(f"+---------------------------------------+---------------------------------------+-------------------------------------+")
            entrada = input("Digite 'S' para seguir ou um numero inteiro positivo para mover a roda? ")
            if entrada == 'S':
                break
            if entrada.isalnum():
                senha[j] = int(entrada) + senha[j]
                if int(senha[j]) >= 26:
                    senha[j] -= 26
                elif int(senha[j]) < 0:
                    senha[j] += 26
    senha_letras = ''
    for i in range(tam_senha_escolhido):
        senha_letras += chr(ord('A') + senha[i])
    print(f"Senha encontrada: {senha_letras}")
    print(f"Criptograma de entrada: {msg}")
    criptografar(msg, senha_letras, 2)


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
