# TSP-Genetic-Algorithm

## Introduction
A genetic algorithm implementation combined with local search to solve the Travelling Salesman Problem.
All the code was made in python 3.8, and a portuguese article was written analyzing the performance applying specific inputs.
<p>The article can be found in the folder: <i> docs </i></p>

<b>Second project of the class Algorithmic Modeling and Optimization.</b>

## The problem
<p>The travelling salesman problem (TSP), is a well known problem in the field. It can be resume in one question:</p>
<p>"Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city exactly once and returns to the origin city?"</p>
<p>The code representation of this problem is a graph, where each node is a city and each edge is a path between cities. There're many techniques that can be applied to this problem, even though it's categorized as NP-complete.</p>

## How to use

### Inputs
<p>The entry is a <i>file.txt</i> containing a list of nodes with it coordinates.</p>
<p>An example of entry will be:</p>
    
    1 1380 939
    2 2848 96
    3 3510 1671
    4 457 334
    5 3888 666

<p>The first column is representing the node, and the next two columns representing it coordinates.</p>

<p>The files to be read <b>must be in the root of the folder <i>/Tests. </i></b>You will be able to select the file when you run the script.</p>


### Output

<p>The output will be the best solution (at least close to the best) for the given graph, also known as Final distance. An example of output will be:</p>

> File name: <i><b>att48.tsp</b></i><br>
 Initial distance: <i><b>984744</b></i><br>
 Final distance: <i><b>51312</b></i><br>
 Execution time: <i><b>33.14</b></i> s<br>

## Genetic Algorithm
<p>The genetic algorithm has roulette-wheel selection implemented, but considering the performance of it, an much faster alternative known as <i>roulette-wheel selection via stochastic acceptance</i> was implemented and it produces the same result in constant time <i>O(1).</i></p>

### Default configuration
<p>The genetic algorithm is set as</p>

```python
    populationSize = 200 
    mutationRate = 0.01
    numberOfGenerations = 300
```

<p>You can edit those values in <i>line 265</i></p>

### Elitism
<p>Elitism is applied selecting 25% of population, you can change it at lines 132 and 134</p>

## Local Search
<p> When you run the script, after you select the file, <b>you'll be able to activate local search or no.</b><p>
<p>The local search implemented was <i>First Improvement</i> generating neighbors with <b><i>2-opt</i></b>. It will be applied on each generation in the fittest individual.</i></b></p>
<p> * Remember: <b>2-opt has a <math>O(n²)</math> complexity, so will take much longer to calculate the solution</b><p>