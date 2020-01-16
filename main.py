from ag import AlgoritmoGenetico

dados = [
    {'item': 'Lapis', 'peso': 1, 'valor': 2},
    {'item': 'Borracha', 'peso': 1, 'valor': 1},
    {'item': 'Caderno', 'peso': 3, 'valor': 4},
    {'item': 'Livro', 'peso': 4, 'valor': 5},
    {'item': 'Caneta', 'peso': 1, 'valor': 2},
    {'item': 'Cálculadora', 'peso': 3, 'valor': 3},
]

def funFitness(genes, dados):
    peso = 0
    valor = 0
    
    for i in range(len(genes)):
        #Adiciona os itens na bolsa
        if (genes[i]==1):
            peso += dados[i]['peso']
            valor += dados[i]['valor']
    
    if (peso > 10):
        return 0
    return valor

ag = AlgoritmoGenetico(dados,funcaoFitness=funFitness)
ag.executa()
print(ag.populacao)

