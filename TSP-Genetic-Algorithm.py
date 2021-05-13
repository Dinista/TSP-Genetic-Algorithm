import math, random
import heapq
import pandas  as pd
import numpy as np
import matplotlib.pyplot as plt

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
        return self.getDistance() < other.getDistance()




arquivo = open("berlin.txt", 'r')

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
        population.append(createRoute(grafo))
    return population


#PopulationOrdered = []

#for individuals in population:
    #heapq.heappush(PopulationOrdered, (individuals.getFitness(), individuals))

#heapq._heapify_max(PopulationOrdered)


def selection (population):
    population_fitness = sum([chromosome.getFitness() for chromosome in population]) 
    chromosome_probabilities = [chromosome.getFitness()/population_fitness for chromosome in population]
    return np.random.choice(population, p=chromosome_probabilities)


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
    ordered = getBestIndividual(population)
    
    for i in range(0, 55):
        nextGeneration.append(ordered[i][1])
    
    for i in range(0, popSize):
        father = selection(population)
        mother = selection(population)
        while(father == mother):
            mother = selection(population)
        child = crossover(father, mother)
        nextGeneration.append(mutation(child, mutationRate))
    return nextGeneration

def getBestIndividual (population):
    orderedPopulation = []
    for individual in population:
        orderedPopulation.append((individual.getFitness(), individual))
    orderedPopulation.sort(key=lambda x:x[0], reverse=True)
    return orderedPopulation

def GA ():
    menorValor = 9999999999
    progress = []
    population = generate_population(grafo, 200)
    print("Distancia inicial:", int(getBestIndividual(population)[0][1].getDistance()))
    for i in range(0, 800):
        population = nextGeneration(population, 0.001)
        Melhor = int(getBestIndividual(population)[0][1].getDistance())
        progress.append(Melhor)
        if ( Melhor < menorValor):
            menorValor = Melhor
    
    plt.plot(progress)
    plt.ylabel('Distância')
    plt.xlabel('Geração')
    plt.show()

    print("Distância final:", menorValor)

arquivo.close()

GA()




