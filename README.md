# TSP-Genetic-Algorithm

## Introduction
A genetic algorithm implementation to solve the Travelling Salesman Problem.
All the code was made in python, and a portuguese article was written analyzing the performance applying specific inputs.
<p>The article can be found in the folder: <i> docs </i></p>

<b>Second project of the class Algorithmic Modeling and Optimization.</b>

## The problem
<p>The travelling salesman problem (TSP), is a well known problem in the field. It can be resume in one question:</p>
<p>"Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city exactly once and returns to the origin city?"</p>
<p>The code representation of this problem is a graph, where each node is a city and each edge is a path between cities. There're many techniques that can be applied to this problem, even though it's categorized as NP-complete.</p>

## How to use

### Inputs
<p>The entry is a file containing a list of nodes with it coordinates.</p>
<p>An example of entry will be:</p>
    
    1 1380 939
    2 2848 96
    3 3510 1671
    4 457 334
    5 3888 666

<p>The first column is representing the node, and the next two columns representing it coordinates.</p>

### Output

<p>The output will be the best solution (at least close to the best) for the given graph.</p>
