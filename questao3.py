from ag import AlgoritmoGenetico
import random

letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']

def funFitness(cromossomo, letras):
    dados = 0
   
    for i in range(len(cromossomo)):
        #Mesma letra nas posições
        if (cromossomo[i] == letras[i]): 
            dados += 1
    return dados

def criaIndividuo(letras):
    #Cria uma copia igual, para não embaralha a original
    copia = letras[:] 
    #Embaralha os valores
    random.shuffle(copia)
    return copia

def mutacao(genes):
    pos1 = random.randint(0, len(genes)-1)
    pos2 = random.randint(0, len(genes)-1)

    #Inverte a posição
    x = genes[pos1]
    y = genes[pos2]
    genes[pos1] = y
    genes[pos2] = x
    return genes

def crossover(pai1, pai2):
    indiceAleatorio = random.randint(0, len(pai1)-1)

    #Pega os primeiros do pai 1
    genes1_1 = pai1[:indiceAleatorio]
    #Recupera na ordem os próximos do pai 2
    genes1_2 = []
    for letra in pai2:
        if (letra not in genes1_1):
            genes1_2.append(letra)

    #Pega os primeiros do pai 2
    genes2_1 = pai2[:indiceAleatorio]
    #Recupera na ordem os próximos do pai 1
    genes2_2 = []    
    for letra in pai1:
        if (letra not in genes2_1):
            genes2_2.append(letra)

    genes1 = genes1_1 + genes1_2
    genes2 = genes2_1 + genes2_2

    return genes1, genes2

ag = AlgoritmoGenetico(letras, 10, 500, funcaoFitness=funFitness)
ag.funCriaIndividuo = criaIndividuo
ag.funCrossover = crossover
ag.funMutacao = mutacao
ag.executa()
print(ag.melhorResultado())