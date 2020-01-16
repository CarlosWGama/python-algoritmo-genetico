from ag import AlgoritmoGenetico
import random
adversario = ['PEDRA', 'PAPEL', 'TESOURA', 'PAPEL', 'PAPEL', 'TESOURA']


def funFitness(cromossomo, adversario):
    pontos = 0
    for i in range(len(cromossomo)):
        if (cromossomo[i] == 'PEDRA'):
            pontos +=  1 if adversario[i] == 'TESOURA' else -1 if adversario[i] == 'PAPEL' else 0
        if (cromossomo[i] == 'TESOURA'):
            pontos +=  1 if adversario[i] == 'PAPEL' else -1 if adversario[i] == 'PEDRA' else 0
        if (cromossomo[i] == 'PAPEL'):
            pontos +=  1 if adversario[i] == 'PEDRA' else -1 if adversario[i] == 'TESOURA' else 0
    return pontos

def criaIndividuo(adversario):
    #           0         1          2
    opcoes = ['PEDRA', 'PAPEL', 'TESOURA']
    genes = []
    for _ in range(len(adversario)):
        indiceSorteado = random.randint(0, 2)
        genes.append(opcoes[indiceSorteado])
    return genes

def mutacao(genes):
    opcoes = ['PEDRA', 'PAPEL', 'TESOURA']
    
    #Seleciona os indices aleatorios
    indiceAleatorio = random.randint(0, len(genes)-1)
    indiceOpcoes = random.randint(0, 2)
    
    #Realiza mutação
    genes[indiceAleatorio] = opcoes[indiceOpcoes]
    return genes

ag = AlgoritmoGenetico(adversario, funcaoFitness=funFitness)
ag.funCriaIndividuo  = criaIndividuo
ag.funMutacao = mutacao
ag.executa()
print(ag.melhorResultado())