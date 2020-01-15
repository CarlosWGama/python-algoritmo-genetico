import random

class AlgoritmoGenetico:

    def __init__(self, dados, tamPopulacao = 10, limGeracoes = 50, probMutacao=5, funcaoFitness = None, maiorFitness = True):
        self.dados = dados
        self.tamPopulacao = tamPopulacao
        self.limGeracoes = limGeracoes
        self.funcaoFitness = funcaoFitness
        self.maiorFitness = maiorFitness
        self.probMutacao = probMutacao
        self.populacao = []
        self.geracao = 1
        
        #Funções que podem ser alteradas
        self.funMutacao = self.mutacao
        self.funSelecao = self.selecao
        self.funCrossover = self.crossover
        self.funCriaIndividuo = self.criaIndividuo
        

    def executa(self):
        """ Executa o código """
        self.criaPopulacaoInicial()
        
        for i in range(self.limGeracoes-1):
            #Inicia uma nova população vazia
            novaPopulacao = []
            for j in range(int(self.tamPopulacao/2)):
                #seleciona os pais
                pai1 = self.funSelecao(self.populacao)
                pai2 = self.funSelecao(self.populacao)

                #Cross over dos filhos
                genes1, genes2 = self.funCrossover(pai1['genes'], pai2['genes'])

                #Filhos
                filho1 = {'fitness': 0, 'genes': genes1}
                probMut = random.randint(0, 100)
                if (probMut < self.probMutacao):
                    filho1['genes'] = self.funMutacao(filho1['genes'])
                filho1['fitness'] = self.funcaoFitness(filho1['genes'], self.dados)
                novaPopulacao.append(filho1)
                
                filho2 = {'fitness': 0, 'genes': genes2}
                probMut = random.randint(0, 100)
                if (probMut < self.probMutacao):
                    filho2['genes'] = self.funMutacao(filho2['genes'])
                filho2['fitness'] = self.funcaoFitness(filho2['genes'], self.dados)
                novaPopulacao.append(filho2)
            #Junt as duas populações
            self.populacao += novaPopulacao
            #Ordena
            self.populacao.sort(key=lambda c:c['fitness'], reverse=self.maiorFitness)
            #Mantem apenas os primeiros
            self.populacao = self.populacao[:self.tamPopulacao]
            self.geracao += 1


    def criaPopulacaoInicial(self):
        """ Cria a primeira população """
        for i in range(self.tamPopulacao):
            cromossomo = {
                'fitness': 0,
                'genes': []
            }
            cromossomo['genes'] = self.funCriaIndividuo(self.dados)
            cromossomo['fitness'] = self.funcaoFitness(cromossomo['genes'], self.dados)
            self.populacao.append(cromossomo)


    def criaIndividuo(self, dados):
        """ Cria um novo individuo """
        genes = []
        for i in range(len(dados)):
            genes.append(random.randint(0, 1))
        return genes

    def crossover(self, pai1, pai2):
        """ Cruza os genes dos pais gerando 2 filhos """
        posicaoCorte = random.randint(0, len(pai1)-1)
        #Corta pai 1
        pai1_1 = pai1[0:posicaoCorte]
        pai1_2 = pai1[posicaoCorte:]
        #Corta pai 2
        pai2_1 = pai1[0:posicaoCorte]
        pai2_2 = pai1[posicaoCorte:]

        filho1 = pai1_1 + pai2_2
        filho2 = pai1_2 + pai2_1
        return filho1, filho2

    def selecao(self, populacao):
        """ Realiza a escolha de um elemento para cruzar """
        #Seleção aleatória
        return populacao[random.randint(0, len(populacao)-1)]

    def mutacao(self, genes):
        """ Realiza a mutação de um item """
        #Escolhe aleatoriamente
        indice = random.randint(0, len(genes)-1)
        #inverte
        genes[indice] = 1 if genes[indice] == 0 else 1
        
        return genes 

    def melhorResultado(self):
        """ Retorna o melhor resultado """
        return self.populacao[0]