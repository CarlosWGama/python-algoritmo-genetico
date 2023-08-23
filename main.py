from ag import AlgoritmoGenetico

dados = [ 

]

def funFitness(genes, dados):
    return 0

ag = AlgoritmoGenetico(dados,funcaoFitness=funFitness)
ag.executa()
print(ag.populacao)

