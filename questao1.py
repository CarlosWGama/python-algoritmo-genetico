from ag import AlgoritmoGenetico

personagens = [
    {'personagem': 'p1', 'ataque': 10, 'defesa': 3},
    {'personagem': 'p2', 'ataque': 2, 'defesa': 4},
    {'personagem': 'p3', 'ataque': 4, 'defesa': 8},
    {'personagem': 'p4', 'ataque': 6, 'defesa': 5},
    {'personagem': 'p5', 'ataque': 2, 'defesa': 6},
    {'personagem': 'p6', 'ataque': 7, 'defesa': 4},
    {'personagem': 'p7', 'ataque': 5, 'defesa': 5},
    {'personagem': 'p8', 'ataque': 3, 'defesa': 8},
    {'personagem': 'p9', 'ataque': 5, 'defesa': 7},
    {'personagem': 'p10', 'ataque': 12, 'defesa': 1},
    {'personagem': 'p11', 'ataque': 8, 'defesa': 5},
    {'personagem': 'p12', 'ataque': 6, 'defesa': 4},
    {'personagem': 'p13', 'ataque': 3, 'defesa': 11},
    {'personagem': 'p14', 'ataque': 4, 'defesa': 6},
    {'personagem': 'p15', 'ataque': 5, 'defesa': 8},
]

#Melhores ataque
def funFitnessA(genes, personagens):
    selecionados = 0
    totalAtaque = 0
    for i in range(len(genes)):
        if (genes[i] == 1): #Selecionado
            selecionados += 1
            totalAtaque += personagens[i]['ataque']

    if (selecionados != 3):
        return 0
    return totalAtaque

#Melhores ataque e defesas
advesario = 10
def funFitnessB(genes, personagens):
    selecionados = 0
    atkGrp = 0
    defGrp = 0
    atkAdv = 13
    defAdv = 21
    for i in range(len(genes)):
        if (genes[i] == 1): #Selecionado
            selecionados += 1
            atkGrp += personagens[i]['ataque']
            defGrp += personagens[i]['defesa']

    if (selecionados != 3):
        return 0

    danoGrp = atkGrp - defAdv if atkGrp > defAdv else 0 
    danoAdv = atkAdv - defGrp if atkAdv > defGrp else 0 

    return danoGrp - danoAdv

ag = AlgoritmoGenetico(personagens, 10, 900, probMutacao=100, funcaoFitness=funFitnessB)
ag.executa()
print(ag.melhorResultado())