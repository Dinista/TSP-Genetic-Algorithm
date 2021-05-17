import math, random, time
import heapq
import matplotlib.pyplot as plt #biblioteca para gerar gráficos
import glob, os #leitura de arquivo
#import cProfile, pstats
#import bisect



class Node:
    def __init__(self, name=None, x=None, y=None):
        self.name = name
        self.x = int(x)
        self.y = int(y)
    
    def getX(self):
        return self.x

    def getY(self):
        return self.y
    
    def distanceTo(self, node):
        #xDistance = abs(self.getX() - city.getX())
        #yDistance = abs(self.getY() - city.getY())
        #distance = math.sqrt((xDistance ** 2) + (yDistance ** 2))
        nodeA = (self.getX(), self.getY())
        nodeB = (node.getX(), node.getY())
        distance = math.dist(nodeA, nodeB)
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
            self.fitness = 1 / float(self.getDistance())
        return self.fitness

    def getDistance(self):
        if self.distance == 0:
            routeDistance = 0
            for nodeIndex in range(0, len(self.route)):
                fromNode = self.route[nodeIndex]
                destinationNode = None
                if nodeIndex + 1 < len(self.route):
                    destinationNode = self.route[nodeIndex + 1]
                else:
                    destinationNode = self.route[0]
                
                routeDistance += fromNode.distanceTo(destinationNode)
            
            self.distance = routeDistance
        
        return self.distance

    def __lt__(self, other):
        return int(self.getDistance()) < int(other.getDistance())


def createRoute (grafo):
    route = random.sample(grafo, len(grafo))
    return Route(route)

def generate_population (grafo, population_size):
    population = []
    for i in range(0, population_size):
        heapq.heappush(population, createRoute(grafo))
    return population


#PopulationOrdered = []

#for individuals in population:
    #heapq.heappush(PopulationOrdered, (individuals.getFitness(), individuals))

#heapq._heapify_max(PopulationOrdered)

def selection(population):
    f_max = population[0].getFitness()
    terminou = True
    while(terminou):
        index = random.randint(0, len(population) - 1)
        i = population[index]
        if (random.uniform(0, 1) < i.getFitness() / f_max):
            return i

#def selection (population):
    #father = rw_selection(population)
    #mother = rw_selection(population)
    #while (father == mother):
        #mother = rw_selection(population)
    
    #return father, mother


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

def nextGeneration(population, mutationRate, popSize1, localSearch):
    popSize = popSize1 - int(popSize1 * 0.25)
    nextGeneration = []
    #ordered = getBestIndividual(population)
    elitSize = int(popSize1 * 0.25)
    nextGeneration = heapq.nsmallest(elitSize, population)
    #for i in range(0, 55):
        #nextGeneration.append(ordered[i][1])
        #heapq.nsmallest
    for i in range(0, popSize):
        father = selection(population)
        mother = selection(population)
        
        while(father == mother):
            mother = selection(population)
        
        child = crossover(father, mother)
        heapq.heappush(nextGeneration , mutation(child, mutationRate))
    
    if (localSearch == True):
        result = two_opt(nextGeneration[0])
        if nextGeneration[0].getDistance() != result.getDistance():
            nextGeneration[0] = result

    return nextGeneration

#def getBestIndividual (population):
    #orderedPopulation = []
    #for individual in population:
        #orderedPopulation.append((individual.getFitness(), individual))
    #orderedPopulation.sort(key=lambda x:x[0], reverse=True)
    #return orderedPopulation


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
                    if new_route.getDistance() < best.getDistance():
                         best = new_route
                         break
                         improved = True
          route = best
     return best

def GA (graph, fileName, popSize, mutationRate, numberOfGenerations, localSearch):
    menorValor = 9999999999
    progress = []
    population = generate_population(graph, popSize)
    print("Distância inicial:", int(population[0].getDistance()))
    #pr = cProfile.Profile()
    #pr.enable()
    inicio = time.time()
    for i in range(0, numberOfGenerations):
        population = nextGeneration(population, mutationRate, popSize, localSearch)
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
    fim = time.time()
    print("Distância final:", menorValor)
    print("Tempo de execução:",round(((fim - inicio)*1000)/1000,3),"s\n")
    plt.plot(progress)
    plt.title(fileName)
    plt.ylabel('Distância')
    plt.xlabel('Geração')
    plt.show()

def readFile ():
    os.chdir("./Tests")
    files = []
    for file in enumerate(glob.glob("*.txt")):
        files.append(file[1])
        print("[", file[0], "]", file[1])
    print("Insira o número correspondente ao arquivo que deseja ler:")
    
    while(True):
        op = int(input())
        if (op >= len(files) or op < 0):
            print("Opção inválida! Digite novamente.")
        else:
            break
    
    os.system('cls')
    print("Arquivo:", str(files[op]))
    
    graph = []
    arquivo = open(str(files[op]), 'r')
    linhas = arquivo.readlines()
    
    while(not linhas[0].split()[0].isdigit()):
        linhas.pop(0)

    for index in range(0, len(linhas) - 1):
        if (linhas[index] == "EOF"):
            break;
        linha = linhas[index].split()
        graph.append(Node(linha[0], linha[1], linha[2]))

    arquivo.close()
    
    return graph, str(files[op])

def main ():
    entrada, fileName = readFile()
    populationSize = 200 
    mutationRate = 0.001
    numberOfGenerations = 700
    localSearch = False
    GA(entrada, fileName, populationSize, mutationRate, numberOfGenerations, localSearch)

if __name__ == "__main__":
    main()


