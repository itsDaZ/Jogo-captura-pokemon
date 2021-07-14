import math

DELTA_T = 0.1
GRAVIDADE = 2
def clona_matriz(A):
    C = []
    m = len(A)
    n = len(A[0])
    for i in range(m):
        C.append(A[i][:])
    return C
def distanciaPontos(x1, y1, x2, y2):
    '''
    Esta função calcula a distância entre dois pontos dados por
    (x1, y1) e (x2, y2).
    '''
    n = (x2-x1)**2 + (y2-y1)**2
    D = math.sqrt(n)
    return D

def arredonda_num(num):
    frac,inteir = math.modf(num)
    if frac > 0.5:
        inteir +=1
    return int(inteir)

def houveColisao(xpokebola, ypokebola, xpokemon, ypokemon, r):

    if distanciaPontos(xpokebola,ypokebola,xpokemon,ypokemon) <= r:
        return True
    else:
        return False

def simula_lancamento (matriz,pokemons,xtreinador):
    n = False
    vlancamento = int(input("Digite a velocidade de lancamento em m/s:  \n\n"))
    angulolancamento = int(input("Digite o angulo de lancamento em graus:  \n"))
    angulo = grau2Radiano(angulolancamento)
    vy = vlancamento*math.sin(angulo)
    vx = vlancamento*math.cos(angulo)
    xpokebola = xtreinador
    ypokebola = 0
    matriz2 = clona_matriz(matriz)
    while n == False and xpokebola >= 0 and ypokebola >=0 and xpokebola < len(matriz[0]) :
        xpokebola,ypokebola=atualizaPosicao(xpokebola,ypokebola,vx,vy,dt=DELTA_T)
        xpokebolaint,ypokebolaint = arredonda_num(xpokebola),arredonda_num(ypokebola)
        vx,vy = atualizaVelocidade(vx,vy,dt=DELTA_T)
        if 0<= xpokebolaint < len(matriz[0]) and 0<= ypokebolaint < len(matriz) :
            num = int(matriz2[ypokebolaint][xpokebolaint])
            if xpokebolaint != xtreinador or ypokebolaint > 0:
                matriz[ypokebolaint][xpokebolaint] = ("%s"%'o')
                if matriz2[ypokebolaint][xpokebolaint] != 0:
                    n = True
    pokemon = pokemons[num][0]
    print("Representacao grafica do lancamento:")
    imprimeMatriz(matriz)
    if n:
        print("Um %s foi capturado!" % pokemon)
    else:
        print("O lancamento nao capturou pokemon algum")
    return n,num,xpokebolaint

def espelhamentoVertical(matriz):
    '''
    Esta função espelha verticalmente uma matriz dada
    '''
    C= []
    m = len(matriz)
    for i in range(1,m+1):
        C.append(matriz[-i])
    return C

def leArquivo(nomeArquivo):
    '''
    Esta função lê um arquivo ('entrada.txt' por default) e
    retorna uma lista de listas.
    '''
    arquivo = open(nomeArquivo,'r')
    Raw_pokemons = arquivo.readlines()
    Raw_pokemons
    L = []
    Lista_pokemons = []
    for i in range(len(Raw_pokemons)):
        j = []
        j.append(Raw_pokemons[i])
        L.append(j)
        Lista_pokemons.append(L[i][0].split())

    #print(lista_pokemons)

    return Lista_pokemons


def criaMatriz(m, n):

    M = []
    for j in range(m):
        l = []
        for j in range(n):
            l.append(0)
        M.append(l)
    return M


def populaMatriz(matriz, pokemons):
    '''
    Esta função recebe uma matriz e uma lista contendo listas que
    representam os pokémons na forma [nome, raio, x, y] e preenche-a
    os pokémons conforme a representação retangular considerando os
    raios da representação.
    '''
    C = []
    for i in range(1,len(pokemons)):
        id = i
        raio = int(pokemons[i][1])
        x = int(pokemons[i][3])
        y = int(pokemons[i][2])
        C = preenchePokemon(matriz,id,x,y,raio)
    return C


def preenchePokemon(matriz, id, x, y, raio):
    '''
    Esta função é auxiliar da função populaMatriz. Ela insere
    um Pokémon na matriz de acordo com sua representação retangular
    baseada no raio ao redor do ponto central (x,y)

    '''
    x1 = x-raio
    x2 = x+1+raio
    y1 = y-raio
    y2 = y+1+raio
    for i in range(x1,x2):
        for j in range(y1 , y2):
            if 0 <= i < len(matriz) and 0 <= j < len(matriz[0]):
                matriz[i][j] = id

    return matriz



def removePokemon(matriz, id , pokemons):
    '''
    Esta função recebe uma matriz, o numeral que representa o pokémon
    a ser removido da matriz (id) e a lista contendo as listas que
    representam pokémons, substituindo os numerais id por zero
    '''
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == id:
                matriz[i][j] = 0

    return matriz


def imprimeMatriz(matriz):
    '''
    Esta função imprime a matriz dada.

    '''
    matriz = espelhamentoVertical(matriz)
    m = len(matriz)
    n = len(matriz[0])
    for i in range(m):
        for j in range(n):
            if matriz[i][j] == 0:
                print('.',end = "" )
            elif matriz[i][j] == '-1':
                print('T',end = "")
            elif type(matriz[i][j]) == int :
                print("%0d"%(matriz[i][j]),end = '')
            else:
                print("%0s"%(matriz[i][j]),end = '')
        print()

    return None


def atualizaPosicao(x, y, vx, vy, dt=DELTA_T):
    '''
    Esta função calcula as atualizações das posições de x e y usando
    as velocidades escalares respectivamente dadas por vx e vy.

    '''
    g = GRAVIDADE
    x = x + vx * dt
    y = y + vy * dt + -0.5*(g * (dt ** 2))
    return x,y


def atualizaVelocidade(vx, vy, dt=DELTA_T):
    '''
    Esta função calcula e atualiza as velocidades vx e vy para o
    próximo intervalo de tempo.
    '''
    g = GRAVIDADE
    vynew = vy - g*dt
    return vx,vynew


def grau2Radiano(theta):
    '''
    Esta função converte o ângulo theta em graus para radianos.
    '''
    theta_rad = theta *math.pi/180
    return theta_rad

def arremesso(npokebolas,matriz):
    Treinador = int(input("Digite a coordenada x do treinador: \n"))
    print("pokebolas disponiveis = %d" % npokebolas)
    M = preenchePokemon(matriz, '%d'% -1, 0, Treinador, 0)
    return M,Treinador
def main():
    nome = input("Digite o nome do arquivo: \n")
    N = int(input("Digite o numero N de pokebolas: \n"))
    pokemons = leArquivo(nome)
    contador = int(len(pokemons))-1
    contador_sucesso = 0
    Campo_ini = criaMatriz(int(pokemons[0][0]),int(pokemons[0][1]))
    Campo_2 = populaMatriz(Campo_ini,pokemons)
    Campo_3,xtreinador = arremesso(N,Campo_2)
    print("Estado atual do jogo: \n")
    imprimeMatriz(Campo_3)
    Campo_4 = clona_matriz(Campo_3)
    while N > 0:
        Campo_4 = clona_matriz(Campo_3)
        capturou,qual,xtreinadornew = simula_lancamento(Campo_4,pokemons,xtreinador)
        if capturou:
            contador_sucesso +=1
        N -= 1
        if N > 0 and contador_sucesso < contador:
            if capturou:
                M = removePokemon(Campo_3,'-1',pokemons)
                M = removePokemon(M,'o',pokemons)
                xtreinador = xtreinadornew
                M = preenchePokemon(Campo_3, '%d'% -1, 0, xtreinadornew, 0)
            else:
                M = removePokemon(Campo_3,'-1',pokemons)
                M = removePokemon(M,'o',pokemons)
                xtreinador = int(input("Digite a coordenada x do treinador: \n"))
                M = preenchePokemon(Campo_3, '%d'% -1, 0, xtreinador, 0)
            Campo_new = removePokemon(Campo_3, qual , pokemons)
            print("pokebolas disponiveis =", N)
            print("Estado atual do jogo:")
            imprimeMatriz(Campo_new)
        elif contador_sucesso >= contador:
            N = 0
            print("Parabens! Todos pokemons foram capturados")

        else:
            print("Jogo encerrado")


main()
