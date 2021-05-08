import math, random
import heapq

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

a = [()]

for i in aux:
    heapq.heappush(a, (i.getFitness(), i))


heapq._heapify_max(a)

def selection (a):
    elite = []
    selected = []
    for i in range(0, 9):
        elite.append(heapq.heappop(a))
    
    for 
    a[random.randint(0, 99)]
    

selection(a)

arquivo.close()
    




