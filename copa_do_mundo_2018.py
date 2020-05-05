from math import e
from random import randint, shuffle
from time import sleep, time

while True:
    a = input("Qual modo deseja jogar? [COPA DO MUNDO] = 0 | [SIMULACOES] = 1\n")
    if a == '0' or a == '1':
        break
    else:
        print("Valor invalido! Tente novamente...")
a = int(a)
lightSpeed = False
if a:
    lightSpeed = True
gols = 0
jogos = 0

times =     ['URUGUAI', 'RUSSIA',   'ARABIA SAUDITA',   'EGITO',    'ESPANHA',  'PORTUGAL', 'IRAN', 'MARROCOS', 'FRANCA',   'DINAMARCA',    'PERU', 'AUSTRALIA',    'CROACIA',  'ARGENTINA',    'NIGERIA',  'ISLANDIA', 'BRASIL',   'SUICA',    'SERVIA',   'COSTA RICA',   'SUECIA',   'MEXICO',   'COREIA DO SUL',    'ALEMANHA', 'BELGICA',  'INGLATERRA',   'TUNISIA',  'PANAMA',   'COLOMBIA', 'JAPAO',    'SENEGAL',  'POLONIA'   ]
atk =       [ 2.02,      1.56,       0.69,               0.71,       1.56,       1.63,       0.6,    0.87,       1.82,       1.5,            1.17,   0.81,           1.5,        1.69,           1.1,        0.67,       2.12,       1.32,       1.56,       1.06,           1.57,       1.05,       0.97,               2.07,       1.13,       1.32,           0.87,       0.67,       1.45,       0.95,       1.25,       1.35       ]
defense =   [ 1.09,      1.33,       2.44,               1.71,       1.14,       1.17,       1.6,    1.38,       1.23,       1.25,           1.83,   1.94,           1,          1.1,            1.43,       1.67,       1.06,       1.84,       1.33,       1.56,           1.43,       1.7,        2.03,               1.15,       1.8,        1.03,           1.67,       3.67,       1.36,       1.38,       1.13,       1.38       ]
vogal =     [ 'o',       'a',        'a',                'o',        'a',        'a',        'o',    'o',        'a',        'a',            'o',    'a',            'a',        'a',            'a',        'a',        'o',        'a',        'a',        'a',            'a',        'o',        'a',                'a',        'a',        'a',            'a',        'o',        'a',        'o',        'o',        'a'        ]

gramaticaCampeao = []
for letra in vogal:
    if letra == 'a':
        gramaticaCampeao.append('')
    else:
        gramaticaCampeao.append('o')

vezesCampeao = []
for num in times:
    vezesCampeao.append(0)

pontos = []
for i in times:
    pontos.append(0)

grupoA, grupoB, grupoC, grupoD, grupoE, grupoF, grupoG, grupoH, eliminatorias = [], [], [], [], [], [], [], [], []
grupos = [grupoA, grupoB, grupoC, grupoD, grupoE, grupoF, grupoG, grupoH]
nomeGrupos = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

for i in range(0,len(times),4):
    grupos[i//4].append(times[i])
    grupos[i//4].append(times[i+1])
    grupos[i//4].append(times[i+2])
    grupos[i//4].append(times[i+3])
    
golsMedios = 2 * sum(atk)/len(atk) * sum(defense)/len(defense) / 2.64

while True:
    if lightSpeed:
        gameMode = 1
        break
    else:
        gameMode = input("Escolha modo de jogo: [PADRAO] = 0 | [TURBO] = 1\n")
        if gameMode == '0' or gameMode == '1':
            break
        else:
            print("Valor invalido! Tente novamente...\n")
gameMode = int(gameMode)

def order_map(key, value, x = 2):
  if len(key) != len(value):
    return "Error in length of key and value"
  while x != 0 and x != 1:
    x = int(input("Ordem crescente -> 0 | decrescente -> 1:\n"))
    if (x > 1 or x < 0):
      print("Try again:")
  ordenator = []
  copia = []
  for i in range(len(value)):
    copia.append(value[i])
  menor = value[0]
  for i in range(1,len(value)):
    if menor > value[i]:
      menor = value[i]
  for j in range(len(key)):
    maior = menor
    for i in range(len(value)):
      if maior <= value[i]:
        maior = value[i]
        index = i
    ordenator.append(index)
    value[index] = menor-1
  for i in range(len(copia)):
    value[i] = copia[i]
  k = []
  v = []
  for i in range(len(key)):
    k.append(key[ordenator[i]])
    v.append(value[ordenator[i]])
  for i in range(len(k)):
    if x == 0:
      key[i] = k[len(k)-i-1]
      value[i] = v[len(v)-i-1]
    else:
      key[i] = k[i]
      value[i] = v[i]

def fat(y):
    if y == 0:
        return 1
    num = 1
    dec = y
    while dec-1:
        num *= dec
        dec -= 1
    return num

def findIndex(x):
    for i in range(len(times)):
        if times[i] == x.upper():
            return i
    return -1

def findLambda(A, B, extraTime = False):
    indexA = findIndex(A)
    indexB = findIndex(B)
    lambdaA = atk[indexA] * defense[indexB] / golsMedios
    lambdaB = atk[indexB] * defense[indexA] / golsMedios
    if extraTime:
        lambdaA = lambdaA / 3.0
        lambdaB = lambdaB / 3.0
    return lambdaA, lambdaB

def draftGoal(lista):
    newList = []
    for i in range(len(lista)):
        for j in range(int(lista[i])):
            newList.append(i)
    rnd = randint(0,len(newList)-1)
    return newList[rnd]

def poisson(A, B, extraTime = False):
    lambdaA, lambdaB = findLambda(A, B, extraTime)
    P1 = []
    P2 = []
    for i in range(9):
        result = (e**(-1*lambdaA) * lambdaA**i) / (fat(i)*1.0)
        P1.append(1000*result)
        result = (e**(-1*lambdaB) * lambdaB**i) / (fat(i)*1.0)
        P2.append(1000*result)
    golsA = draftGoal(P1)
    golsB = draftGoal(P2)
    return golsA, golsB

def match(A, B, knockOut = True, grupo = []):
    if not lightSpeed:
        print("\n========================================================================================================================\n")
        print("\nPARTIDA:", A.upper(), "x", B.upper())
        print()
    if not gameMode:
        sleep(1.5)
    golsA, golsB = poisson(A, B)
    goalStamps = []
    sideScoring = []
    for i in range(golsA):
        sideScoring.append(0)
    for i in range(golsB):
        sideScoring.append(1)
    for i in range(golsA + golsB):
        while True:
            stamp = randint(1,90)
            if stamp not in goalStamps:
                goalStamps.append(stamp)
                break
    shuffle(sideScoring)
    count = 0
    placarA = 0
    placarB = 0
    for tempo in range(1, 91):
        if tempo in goalStamps:
            if sideScoring[count]:
                placarB += 1
            else:
                placarA += 1
            if not lightSpeed:
                goalEvent(A, B, sideScoring[count], placarA, placarB, tempo)
            count += 1
        else:
            if not lightSpeed:
                otherEvents(A, B, tempo)
        if not gameMode:
            sleep(0.1)
    if not knockOut:
        indexA = findIndex(A)
        indexB = findIndex(B)
        if golsA > golsB:
            pontos[indexA] = pontos[indexA] + 3 + 0.01*(golsA-golsB) + 0.0001*golsA
            pontos[indexB] = pontos[indexB] + 0.25 + 0.01*(golsB-golsA) + 0.0001*golsB
        elif golsB > golsA:
            pontos[indexB] = pontos[indexB] + 3 + 0.01*(golsB-golsA) + 0.0001*golsB
            pontos[indexA] = pontos[indexA] + 0.25 + 0.01*(golsA-golsB) + 0.0001*golsA
        else:
            pontos[indexA] = pontos[indexA] + 1 + 0.0001*golsA
            pontos[indexB] = pontos[indexB] + 1 + 0.0001*golsB

    else:
        if golsA > golsB:
            if len(eliminatorias) > 29:
                index = findIndex(A)
                if not lightSpeed:
                    print(A,"EH {} CAMPEA{} DA COPA DO MUNDO!".format(vogal[index].upper(), gramaticaCampeao[index].upper()))
                else:
                    vezesCampeao[index] += 1
            else:
                eliminatorias.append(A)
                if not lightSpeed:
                    print(A,"SE CLASSIFICOU PARA A PROXIMA FASE!")
        elif golsB > golsA:
            if len(eliminatorias) > 29:
                index = findIndex(B)
                if not lightSpeed:
                    print(B,"EH {} CAMPEA{} DA COPA DO MUNDO!".format(vogal[index].upper(), gramaticaCampeao[index].upper()))
                else:
                    vezesCampeao[index] += 1
            else:
                eliminatorias.append(B)
                if not lightSpeed:
                    print(B,"SE CLASSIFICOU PARA A PROXIMA FASE!")
        else:
            if not lightSpeed:
                print("FIM DO TEMPO REGULAMENTAR! VAMOS PARA A PRORROGACAO!\n")
            prorrogacao(A, B, placarA, placarB)
    
    if not lightSpeed:
        print("FINAL DE PARTIDA:",A.upper(),golsA,'x',golsB,B.upper())
    else:
        global jogos, gols
        jogos += 1
        gols = gols + golsA + golsB
    if not knockOut:
        showTable(grupo)
    if not gameMode:
        input("\nPartida terminada. Pressione ENTER para continuar...")
    if not lightSpeed:
        print()

def prorrogacao(A, B, placarA, placarB):
    if not lightSpeed:
        print("PRORROGACAO!\n")
    if not gameMode:
        sleep(1.5)
    golsA, golsB = poisson(A, B, True)
    goalStamps = []
    sideScoring = []
    for i in range(golsA):
        sideScoring.append(0)
    for i in range(golsB):
        sideScoring.append(1)
    for i in range(golsA + golsB):
        while True:
            stamp = randint(91,120)
            if stamp not in goalStamps:
                goalStamps.append(stamp)
                break
    shuffle(sideScoring)
    count = 0
    for tempo in range(91, 121):
        if tempo in goalStamps:
            if sideScoring[count]:
                placarB += 1
            else:
                placarA += 1
            if not lightSpeed:
                goalEvent(A, B, sideScoring[count], placarA, placarB, tempo)
            count += 1
        else:
            if not lightSpeed:
                otherEvents(A, B, tempo)
        if not gameMode:
            sleep(0.1)
    if golsA > golsB:
        if len(eliminatorias) > 29:
            index = findIndex(A)
            if not lightSpeed:
                print(A,"EH {} CAMPEA{} DA COPA DO MUNDO!".format(vogal[index].upper(), gramaticaCampeao[index].upper()))
            else:
                vezesCampeao[index] += 1
        else:
            eliminatorias.append(A)
            if not lightSpeed:
                print(A,"SE CLASSIFICOU PARA A PROXIMA FASE!")
    elif golsB > golsA:
        if len(eliminatorias) > 29:
            index = findIndex(B)
            if not lightSpeed:
                print(B,"EH {} CAMPEA{} DA COPA DO MUNDO!".format(vogal[index].upper(), gramaticaCampeao[index].upper()))
            else:
                vezesCampeao[index] += 1
        else:
            eliminatorias.append(B)
            if not lightSpeed:
                print(B,"SE CLASSIFICOU PARA A PROXIMA FASE!")
    else:
        if not lightSpeed:
            print("FIM DA PRORROGACAO! O JOGO SERA DECIDIDO NOS PENALTIS! HAJA CORACAO!\n")
        penaltis(A, B)

def penaltis(A, B):
    vez = True
    placarPenaltiA = 0
    placarPenaltiB = 0
    contaCobrancas = 0
    while True:
        if vez:
            if cobraPenalti(A):
                placarPenaltiA += 1
            vez = False
        else:
            if cobraPenalti(B):
                placarPenaltiB += 1
            vez = True
        contaCobrancas += 1
        if (contaCobrancas >= 10 and vez and placarPenaltiA != placarPenaltiB) or ((contaCobrancas == 8 or contaCobrancas == 9) and abs(placarPenaltiA - placarPenaltiB) >= 2) or ((contaCobrancas == 6 or contaCobrancas == 7) and abs(placarPenaltiA - placarPenaltiB) >= 3):
            break
    if placarPenaltiA > placarPenaltiB:
        if len(eliminatorias) > 29:
            index = findIndex(A)
            if not lightSpeed:
                print(A,"EH {} CAMPEA{} DA COPA DO MUNDO!".format(vogal[index].upper(), gramaticaCampeao[index].upper()))
            else:
                vezesCampeao[index] += 1
        else:
            eliminatorias.append(A)
            if not lightSpeed:
                print(A,"SE CLASSIFICOU PARA A PROXIMA FASE!")
    else:
        if len(eliminatorias) > 29:
            index = findIndex(B)
            if not lightSpeed:
                print(B,"EH {} CAMPEA{} DA COPA DO MUNDO!".format(vogal[index].upper(), gramaticaCampeao[index].upper()))
            else:
                vezesCampeao[index] += 1
        else:
            eliminatorias.append(B)
            if not lightSpeed:
                print(B,"SE CLASSIFICOU PARA A PROXIMA FASE!")

def cobraPenalti(time):
    if not lightSpeed:
        print("{} VAI COBRAR O PENALTI...".format(time.upper()))
    if not gameMode:
        sleep(1)
    rnd = randint(1,10)
    if rnd < 4:
        if not lightSpeed:
            print("PERDEU!\n")
        return False
    if not lightSpeed:
        print("GOOOOL!\n")
    return True

def otherEvents(A, B, tempo):
    rnd = randint(0,1)
    if rnd:
        randomTeam = B.upper()
        index = findIndex(B)
    else:
        randomTeam = A.upper()
        index = findIndex(A)
    event = randint(1, 1350)
    if event == 1:
        print("Que situacao! Torcedor revoltado entra em campo pra protestar aos", tempo, "minutos, mas eh detido a tempo!\n")
    elif event < 4:
        print("Bandeirinha atento! {}".format(vogal[index].upper()), randomTeam, "ja ia marcando um gol aos", tempo, "minutos, mas o artilheiro tava na banheira.\n")
    elif event < 56:
        print("Falta pr{}".format(vogal[index]), randomTeam, "cobrar. Jogador adversario tomou o amarelo aos", tempo, "minutos de jogo.\n")
    elif event < 61:
        print("Expulso o defensor d{}".format(vogal[index]), randomTeam, "depois de uma falta dura aos", tempo, "minutos!\n")

def goalEvent(A, B, side, placarA, placarB, tempo):
    if not side:
        timeGol = A.upper()
        index = findIndex(A)
    else:
        timeGol = B.upper()
        index = findIndex(B)
    tipo = randint(0,100)
    if tipo == 0:
        print("Ih rapaz... O goleirao falhou! Entregou pr{}".format(vogal[index]), timeGol, "marcar aos", tempo, "minutos!")
    elif tipo < 21:
        print("Gol de escanteio d{}".format(vogal[index]), timeGol, "aos", tempo, "minutos!")
    elif tipo < 41:
        print("Gol de cabeca d{}".format(vogal[index]), timeGol, "aos", tempo, "minutos!")
    elif tipo < 56:
        print("Golaco de longe d{}".format(vogal[index]), timeGol, "aos", tempo, "minutos!")
    elif tipo < 81:
        print("Golaco! Jogada trabalhada d{}".format(vogal[index]), timeGol, "aos", tempo, "minutos!")
    elif tipo < 91:
        print("Gol de puro talento em jogada individual d{}".format(vogal[index]), timeGol, "aos", tempo, "minutos!")
    elif tipo < 96:
        print("Golaco de falta d{}".format(vogal[index]), timeGol, "aos", tempo, "minutos!")
    else:
        print("Gol de penalti d{}".format(vogal[index]), timeGol, "aos", tempo, "minutos!")
    print(A.upper(), placarA, "x", placarB, B.upper())
    print()

def showTable(grupo):
    try:
        indexInicial = findIndex(grupo[0])
        timesGrupo = [grupo[0], grupo[1], grupo[2], grupo[3]]
        pontosGrupo = [pontos[indexInicial], pontos[indexInicial+1], pontos[indexInicial+2], pontos[indexInicial+3]]
        order_map(timesGrupo, pontosGrupo, 1)
        if not lightSpeed:
            print()
            for i in range(4):
                print("{}: {:.0f} pts ->\t{}".format(i+1,pontosGrupo[i],timesGrupo[i]))
    except:
        pass

def avanco(grupo):
    indexInicial = findIndex(grupo[0])
    timesGrupo = [grupo[0], grupo[1], grupo[2], grupo[3]]
    pontosGrupo = [pontos[indexInicial], pontos[indexInicial+1], pontos[indexInicial+2], pontos[indexInicial+3]]
    order_map(timesGrupo, pontosGrupo, 1)
    eliminatorias.append(timesGrupo[0])
    eliminatorias.append(timesGrupo[1])
    if not lightSpeed:
        print("{} e {} avancaram pras oitavas de final!".format(timesGrupo[0], timesGrupo[1]))
    if not gameMode:
        input("\nPressione ENTER para continuar...")
    if not lightSpeed:
        print()

def playGrupo(grupo):
    match(grupo[0], grupo[1], False, grupo)
    match(grupo[2], grupo[3], False, grupo)
    match(grupo[0], grupo[2], False, grupo)
    match(grupo[1], grupo[3], False, grupo)
    match(grupo[0], grupo[3], False, grupo)
    match(grupo[1], grupo[2], False, grupo)
    avanco(grupo)

def playOitavas(grupo):
    match(grupo[0], grupo[3])
    match(grupo[1], grupo[2])
    match(grupo[4], grupo[7])
    match(grupo[5], grupo[6])
    match(grupo[8], grupo[11])
    match(grupo[9], grupo[10])
    match(grupo[12], grupo[15])
    match(grupo[13], grupo[14])
    if not lightSpeed:
        print("AVANCAM PARA AS QUARTAS:")
        for i in range(16,24):
            print(grupo[i])
        print("\n\n\n")

def playQuartas(grupo):
    match(grupo[16], grupo[17])
    match(grupo[18], grupo[19])
    match(grupo[20], grupo[21])
    match(grupo[22], grupo[23])
    if not lightSpeed:
        print("AVANCAM PARA A SEMI:")
        for i in range(24,28):
            print(grupo[i])
        print("\n\n\n")

def playSemi(grupo):
    match(grupo[24], grupo[25])
    match(grupo[26], grupo[27])
    if not lightSpeed:
        print("AVANCAM PARA A GRANDE FINAL:")
        for i in range(28,30):
            print(grupo[i])
        print("\n\n\n")

def playFinal(grupo):
    match(grupo[28], grupo[29])

if lightSpeed:
    while True:
        numSimuls = input("Quantas simulacoes rodar? ")
        try:
            numSimuls = int(numSimuls)
            if numSimuls > 0:
                inicio = time()
                break
            else:
                print("Valor invalido! Tente novamente...")
        except:
            print("Valor invalido! Tente novamente...")
    
else:
    numSimuls = 1

for i in range(numSimuls):
    pontos = []
    for i in times:
        pontos.append(0)
    eliminatorias = []

    if not lightSpeed:
        print("Comeca a COPA DO MUNDO!\n")
    contaGrupo = 0
    for grupo in grupos:
        if not lightSpeed:
            print("\nINICIO DO GRUPO {}!\n".format(nomeGrupos[contaGrupo]))
        playGrupo(grupo)
        contaGrupo += 1

    if not lightSpeed:
        print("\nCOMECAM AS OITAVAS DE FINAL!\n")
    playOitavas(eliminatorias)
    if not lightSpeed:
        print("\nCOMECAM AS QUARTAS DE FINAL!\n")
    playQuartas(eliminatorias)
    if not lightSpeed:
        print("\nCOMECA A SEMI FINAL!\n")
    playSemi(eliminatorias)
    if not lightSpeed:
        print("\nCOMECA A FINAL!\n")
    playFinal(eliminatorias)

if lightSpeed:
    order_map(times, vezesCampeao, 1)
    print("Numero de Simulacoes realizadas: {}\nTempo de execucao: {:.2f} segundos".format(numSimuls, time() - inicio))
    print("Media de gols por jogo: {:.2f}".format(gols/(jogos*1.0)))
    for i in range(len(times)):
        print("{}:\t{}x campeao ->\t{}".format(i+1, vezesCampeao[i], times[i]))
