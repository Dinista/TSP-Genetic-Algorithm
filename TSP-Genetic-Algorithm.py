import math, random
import heapq
import pandas  as pd
import numpy as np
import matplotlib.pyplot as plt
import cProfile, pstats
import bisect


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
        #xDistance = abs(self.getX() - city.getX())
        #yDistance = abs(self.getY() - city.getY())
        #distance = math.sqrt((xDistance ** 2) + (yDistance ** 2))
        cityA = (self.getX(), self.getY())
        cityB = (city.getX(), city.getY())
        distance = math.dist(cityA, cityB)
        return distance
    
    def __repr__(self) -> str:
        return "(" + str(self.x) + "," + str(self.y) + ")"

class Route:
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
                if cityIndex + 1 < len(self.route):
                    destinationCity = self.route[cityIndex+1]
                else:
                    destinationCity = self.route[0]
                
                tourDistance += fromCity.distanceTo(destinationCity)
            
            self.distance = tourDistance
        
        return self.distance

    def __lt__(self, other):
        return int(self.getDistance()) < int(other.getDistance())




arquivo = open("a280.tsp.txt", 'r')

linhas = arquivo.readlines()

linhas = linhas[6:]

grafo = []

for index in range(0, len(linhas) - 1):
    if (linhas[index] == "EOF"):
        break;
    linha = linhas[index].split()
    grafo.append(Node(linha[0], linha[1], linha[2]))


def createRoute (grafo):
    route = random.sample(grafo, len(grafo))
    return Route(route)

def generate_population (grafo, population_size):
    population = []
    for i in range(0, population_size):
        heapq.heappush(population, createRoute(grafo))
    #heapq.heapify(population)
    return population


#PopulationOrdered = []

#for individuals in population:
    #heapq.heappush(PopulationOrdered, (individuals.getFitness(), individuals))

#heapq._heapify_max(PopulationOrdered)

def rw_selection(population):
    f_max = population[0].getFitness()
    terminou = True
    while(terminou):
        #Select randomly one of the individuals
        index = random.randint(0, len(population) - 1)
        i = population[index]
        #The selection is accepted with probability fitness(i) / f_max
        if (random.uniform(0, 1) < i.getFitness() / f_max):
            return i

def selection (population):
    #allF = [chromosome.getFitness() for chromosome in population]
    #ch = [chromosome/sum(allF) for chromosome in allF]
    #cfs = [sum(allF[:i+1]) for i in range(len(allF))]
    #father = population[bisect.bisect_left(cfs, random.uniform(0, cfs[-1]))]
    #mother = population[bisect.bisect_left(cfs, random.uniform(0, cfs[-1]))]
    father = rw_selection(population)
    mother = rw_selection(population)
    while (father == mother):
        mother = rw_selection(population)
    
    return father, mother


def crossover (father, mother):
    child = []
    childP1 = []
    childP2 = []
    
    geneA = int(random.random() * len(father.route))
    geneB = int(random.random() * len(father.route))
    
    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)
    for i in range(startGene, endGene):
        childP1.append(father.route[i])
        
    childP2 = [item for item in mother.route if item not in childP1]
    child = childP1 + childP2
    return Route(child)

#parent1 = selection(population)
#parent2 = selection(population)
#child = crossover(parent1, parent2)

def mutation(routeObj, mutationRate):
    route = routeObj.route
    for swap in range(len(route)):
        randomNumber = random.random()
        if (randomNumber < mutationRate):
            swapIndex = int(randomNumber * len(route))
            Node1 = route[swap]
            Node2 = route[swapIndex]

            route[swap] = Node2
            route[swapIndex] = Node1
    return Route(route)

def nextGeneration(population, mutationRate):
    nextGeneration = []
    popSize = 145;
    #ordered = getBestIndividual(population)
    nextGeneration = heapq.nsmallest(55, population)
    #for i in range(0, 55):
        #nextGeneration.append(ordered[i][1])
        #heapq.nsmallest
    for i in range(0, popSize):
        father, mother = selection(population)
        #while(father == mother):
            #father, mother = selection(population)
        child = crossover(father, mother)
        heapq.heappush(nextGeneration , mutation(child, mutationRate))
    #heapq.heappush(nextGeneration, buscaLocal(nextGeneration[0]))
    
    result = two_opt(nextGeneration[0])
    if nextGeneration[0].getDistance() != result.getDistance():
        nextGeneration[0] = result
    return nextGeneration

def getBestIndividual (population):
    orderedPopulation = []
    for individual in population:
        orderedPopulation.append((individual.getFitness(), individual))
    orderedPopulation.sort(key=lambda x:x[0], reverse=True)
    return orderedPopulation


def twoOptSwap(route, i, k):
    new_route = []
    for index in range(0, i):
        new_route.append(route[index])
    for index in range(k, i-1, -1):
        new_route.append(route[index])
    for index in range(k+1, len(route)):
        new_route.append(route[index])
    
    return new_route


def two_opt(route):
     best = route
     improved = True
     while improved:
          improved = False
          for i in range(1, len(route.route)-2):
               for j in range(i+1, len(route.route)):
                    if j-i == 1: continue # changes nothing, skip then
                    new_route = Route(twoOptSwap(best.route, i, j))
                    #print(new_route.getDistance() == best.getDistance())
                    if new_route.getDistance() < best.getDistance():  # what should cost be?
                         best = new_route
                         break
                         improved = True
                         #print("oi")
          route = best
     return best


def geraVizinho(pCaminho, pContador):
    caminho = pCaminho
    (caminho[pContador], caminho[pContador +1]) = (caminho[pContador +1], caminho[pContador])
    return caminho

def buscaLocal(objRoute):
    i = 0
    vizinho = Route([])
    for i in range(len(objRoute.route)-1):
        vizinho.route = geraVizinho(objRoute.route, i)
        if vizinho.getFitness() > objRoute.getFitness():
            objRoute = vizinho
            break

    return objRoute

def GA ():
    menorValor = 9999999999
    progress = []
    population = generate_population(grafo, 200)
    print("Distancia inicial:", int(population[0].getDistance())) #int(getBestIndividual(population)[0][1].getDistance()))
    
    #pr = cProfile.Profile()
    #pr.enable()
    
    for i in range(0, 700):
        population = nextGeneration(population, 0.001)
        Melhor = int(population[0].getDistance())
        progress.append(Melhor)
        if ( Melhor < menorValor):
            menorValor = Melhor
            menorRota = population[0]
    #pr.disable()
    #pr.dump_stats('data')
    #ps = pstats.Stats('data')
    #ps.sort_stats(pstats.SortKey.CUMULATIVE)
    #ps.print_stats()
    
    plt.plot(progress)
    plt.ylabel('Distância')
    plt.xlabel('Geração')
    plt.show()
    #print( "melhorou?", two_opt(menorRota).getDistance())
    print("Distância final:", menorValor)

arquivo.close()
GA()



