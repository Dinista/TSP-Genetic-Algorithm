import math, random
import heapq
import pandas  as pd
import numpy as np

class Node:
    def __init__(self, name=None, x=None, y=None):
        self.name = name
        self.x = int(x)
        self.y = int(y)
    
    def getX(self):
        return self.x

    def getY(self):
        return self.y
    
    def distanceTo(self, city):
        xDistance = abs(self.getX() - city.getX())
        yDistance = abs(self.getY() - city.getY())
        distance = math.sqrt((xDistance ** 2) + (yDistance ** 2))
        return distance

class Tour:
    def __init__(self, route):
        self.distance = 0
        self.fitness = 0
        self.route = route

    def getFitness(self):
        if self.fitness == 0:
            self.fitness = 1/float(self.getDistance())
        return self.fitness

    def getDistance(self):
        if self.distance == 0:
            tourDistance = 0
            for cityIndex in range(0, len(self.route)):
                fromCity = self.route[cityIndex]
                destinationCity = None
                if cityIndex+1 < len(self.route):
                    destinationCity = self.route[cityIndex+1]
                else:
                    destinationCity = self.route[0]
                
                tourDistance += fromCity.distanceTo(destinationCity)
            
            self.distance = tourDistance
        
        return self.distance




arquivo = open("kroA100.tsp.txt", 'r')

linhas = arquivo.readlines()

linhas = linhas[6:]

grafo = []

for index in range(0, len(linhas) - 1):
    if (linhas[index] == "EOF"):
        break;
    linha = linhas[index].split()
    grafo.append(Node(linha[0], linha[1], linha[2]))


def generate (grafo):
    route = random.sample(grafo, len(grafo))
    return Tour(route)

def generate_population (grafo, population_size):
    population = []
    for i in range(0, population_size):
        population.append(generate(grafo))
    return population

aux = generate_population(grafo, 100)

a = []

for i in aux:
    heapq.heappush(a, (i.getFitness(), i))

heapq._heapify_max(a)

def selection (popRanked):
    eliteSize = 10
    selectionResults = []
    for i in range(0, eliteSize):
        retirado = heapq.heappop(popRanked)
        #selectionResults.append(heapq.heappop(popRanked))
        if(len(retirado) > 0):
             selectionResults.append(retirado)
        
        heapq._heapify_max(popRanked)
    
    # touneio
    
    for selected in range(0, 55): 
        a = [popRanked[random.randint(0, 89)],
            popRanked[random.randint(0, 89)],
            popRanked[random.randint(0, 89)],
            popRanked[random.randint(0, 89)],
            popRanked[random.randint(0, 89)]]
        a.sort(reverse=True)
        selectionResults.append(a)
    
    return selectionResults

#t = selection(a)

selecionados = selection(a)

""" def breed(parentA, parentB):
    #parent1 = parentA.route
    #parent2 = parentB.route
    child = []
    childP1 = []
    childP2 = []
    
    geneA = int(random.random() * len(parent1))
    geneB = int(random.random() * len(parent1))
    
    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)

    for i in range(startGene, endGene):
        childP1.append(parent1[i])
        
    childP2 = [item for item in parent2 if item not in childP1]

    child = childP1 + childP2
    return child """

""" def breedPopulation(matingpool):
    children = []
    #ength = len(matingpool) - 10
    pool = random.sample(matingpool, len(matingpool))
    # Aqui novamente usamos o elitismo para manter as melhores rotas/indivíduos 
    for i in range(0, 10):
        children.append(matingpool[i])
    # Aqui utilizamos a função de breed mencionada acima para preencher o resto
    # dos indivíduos
    for i in range(10, len(matingpool)):
        child = (breed(pool[i][1][1].route, pool[len(matingpool)-i-1][1].route),breed(pool[i][1].route, pool[len(matingpool)-i-1][1][1].route))
        children.append(child)
    return children """


""" breedPopulation(selecionados) """

arquivo.close()
    




