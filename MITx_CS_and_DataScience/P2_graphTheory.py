# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 16:35:35 2019

@author: Lia Bozneanu

Graph Theory
- adjacency matrix - rows = source nodes // columns = destination nodes
- adjacency list - associate with each node a list of destination nodes

DFS - Depth-first Search
BFS - Breadth-first Search
"""

  
###############################################################################
# Recursion limit
###############################################################################               

import sys
# check the recursion limit
sys.getrecursionlimit()
# change the recursion limit
sys.setrecursionlimit(3000) 


###############################################################################
# Graph Theory
###############################################################################               

# the node
class Node(object):
    def __init__(self, name):
        """Assumes name is a string"""
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self, src, dest):
        """Assumes src and dest are nodes"""
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()
               
class Digraph(object):
    """edges is a dict mapping each node to a list of its children"""
    def __init__(self):
        self.edges = {}
    def addNode(self, node):
        if node in self.edges:
            raise ValueError('Duplicate node')
        else:
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.edges
    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        raise NameError(name)
    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName() + '->'\
                         + dest.getName() + '\n'
        return result[:-1] #omit final newline

class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)

''' graphType may be a graph or a diagraph'''    
def buildCityGraph(graphType):
    g = graphType()
    for name in ('Boston', 'Providence', 'New York', 'Chicago',
                 'Denver', 'Phoenix', 'Los Angeles'): #Create 7 nodes
        g.addNode(Node(name))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('Providence')))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('Boston')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('New York'), g.getNode('Chicago')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Denver')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Los Angeles'), g.getNode('Boston')))
    return g
    
print(buildCityGraph(Graph))
print(buildCityGraph(Digraph))

# Optimisation problems - shortest path

# ex. 2
###############################################################################
        
# Consider our representation of permutations of students in a line from 
# Exercise 1. (The teacher only swaps the positions of two students that are
# next to each other in line.) Let's consider a line of three students, Alice,
# Bob, and Carol (denoted A, B, and C). Using the Graph class created in the
# lecture, we can create a graph with the design chosen in Exercise 1:
# vertices represent permutations of the students in line; edges connect two
# permutations if one can be made into the other by swapping
# two adjacent students.

# We construct our graph by first adding the following nodes:

nodes = []
nodes.append(Node("ABC")) # nodes[0]
nodes.append(Node("ACB")) # nodes[1]
nodes.append(Node("BAC")) # nodes[2]
nodes.append(Node("BCA")) # nodes[3]
nodes.append(Node("CAB")) # nodes[4]
nodes.append(Node("CBA")) # nodes[5]

g = Graph()
for n in nodes:
    g.addNode(n)
    
##########################
for node in nodes:
    n = node.getName()
    for other_node in nodes:
        if other_node.getName() == n[1]+n[0]+n[2] or other_node.getName() == n[0]+n[2]+n[1]:
            #Digraph.addEdge(g, Edge(node, other_node)) '''replaced by the next 2 lines'''
            # filter out the existing edges
            if not other_node in g.childrenOf(node):
                g.addEdge(Edge(node, other_node))    
    
##########################
# counter - used to get rid of duplicates
counter = 0

for i in nodes:
    a = i.getName()
    counter += 1
    for j in nodes[counter:]:
        b = j.getName()
        if a[0] == b[0] or a[2] == b[2]:
            g.addEdge(Edge(i,j))

###############################################################################
# Depth-first Search (DFS)
###############################################################################

def printPath(path):
    """Assumes path is a list of nodes"""
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result 

def DFS(graph, start, end, path, shortest, toPrint = False):
    """Assumes graph is a Digraph; start and end are nodes;
          path and shortest are lists of nodes
       Returns a shortest path from start to end in graph"""
    path = path + [start]
    if toPrint:
        print('Current DFS path:', printPath(path))
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
            if shortest == None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest,
                              toPrint)
                if newPath != None:
                    shortest = newPath
        elif toPrint:
            print('Already visited', node)
    return shortest
    
def shortestPath(graph, start, end, toPrint = False):
    """Assumes graph is a Digraph; start and end are nodes
       Returns a shortest path from start to end in graph"""
    return DFS(graph, start, end, [], None, toPrint)

# SP = shortest Path
def testSP(source, destination):
    g = buildCityGraph(Digraph)
    sp = shortestPath(g, g.getNode(source), g.getNode(destination),
                      toPrint = True)
    if sp != None:
        print('Shortest path from', source, 'to',
              destination, 'is', printPath(sp))
    else:
        print('There is no path from', source, 'to', destination)

#testSP('Chicago', 'Boston')
testSP('Boston', 'Phoenix')

###############################################################################
# Breadtf-first Search (BFS)
###############################################################################

def BFS(graph, start, end, toPrint = False):
    """Assumes graph is a Digraph; start and end are nodes
       Returns a shortest path from start to end in graph"""
    initPath = [start]
    pathQueue = [initPath]
    while len(pathQueue) != 0:
        #Get and remove oldest element in pathQueue
        tmpPath = pathQueue.pop(0)
        if toPrint:
            print('Current BFS path:', printPath(tmpPath))
        lastNode = tmpPath[-1]
        if lastNode == end:
            return tmpPath
        for nextNode in graph.childrenOf(lastNode):
            if nextNode not in tmpPath:
                newPath = tmpPath + [nextNode]
                pathQueue.append(newPath)
    return None

def shortestPath(graph, start, end, toPrint = False):
    """Assumes graph is a Digraph; start and end are nodes
       Returns a shortest path from start to end in graph"""
    return BFS(graph, start, end, toPrint)
    
testSP('Boston', 'Phoenix')
    
    
###############################################################################
# Weighted Shortest Path - DFS only
###############################################################################

def cost(path):
    result = 0
    for i in range(len(path)):
        result += str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result 


def DFS(graph, start, end, path, shortest, toPrint = False):
    """Assumes graph is a Digraph; start and end are nodes;
          path and shortest are tuples containing a list of
          nodes and a cost
       Returns a shortest path from start to end in graph"""
    path = (path + [start], 0)
    if toPrint:
        print('Current DFS path:', printPath(path[0]))
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
            if shortest == None or cost(path) < cost(shortest):
                newPath = DFS(graph, node, end, path, shortest,
                              toPrint)
                if newPath != None:
                    shortest = newPath
                    
def testSP():
    nodes = []
    for name in ('Boston', 'Providence', 'New York', 'Chicago',
                 'Denver', 'Phoenix', 'Los Angeles'): #Create 6 nodes
        nodes.append(Node(str(name)))
    g = Digraph()
    for n in nodes:
        g.addNode(n)
    g.addEdge(WeightedEdge(nodes[0],nodes[1]))
    g.addEdge(WeightedEdge(nodes[1],nodes[2]))
    g.addEdge(WeightedEdge(nodes[2],nodes[3]))
    g.addEdge(WeightedEdge(nodes[2],nodes[4]))
    g.addEdge(WeightedEdge(nodes[3],nodes[4]))
    g.addEdge(WeightedEdge(nodes[3],nodes[5]))
    g.addEdge(WeightedEdge(nodes[0],nodes[2],10))
    g.addEdge(WeightedEdge(nodes[1],nodes[0]))
    g.addEdge(WeightedEdge(nodes[3],nodes[1]))
    g.addEdge(WeightedEdge(nodes[4],nodes[0]))
    sp = shortestPath(g, nodes[0], nodes[5], toPrint = True)
    print('Shortest path is', printPath(sp))
    sp = BFS(g, nodes[0], nodes[5])
    print('Shortest path found by BFS:', printPath(sp))
    
testSP()

def printPath(path)"
    ''' assumes path is a list of nodes'''
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) -1:
            result = result + '->'
    return result

def DFS(graph, start, end, path, shortest, toPrint = False):
    ''' assumes graph is a Diagraph: start and end are nodes
        path and shortest are lists of nodes
        Returns a shortest path from start to end in graph 
    '''
    path = path + [start]
    if toPrint:
        print('Current DFS path: ', printPath(path))
    if start == end:
        return path
    for node in graph.children0f(start):
        if node not in path:    # avoid cycles
            if shortest == None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest, toPrint)
                if newPath != None:
                    shortest = newPath
        elif toPrint:
            print('Already visited)', node)
    return shortest

def shortestPath(graph, start, end):
    return DFS(graph, start, end, [], None, toPrint)

def testSP(source, destination):
    g = buildCityGraph(Diagraph)
    sp = shortestPath(g, g.getNode(source), g.getNode(destination), toPrint = True)
    if sp != None:
        print('Shortest path from ', source, ' to ', destination)

testSP('Chicago', 'Boston')
assert False


# ex. 5

# In the following examples, assume all graphs are undirected. That is,
# an edge from A to B is the same as an edge from B to A and counts as 
# exactly one edge.

# A clique is an unweighted graph where each node connects to all other nodes.
# We denote the clique with n nodes as KN. Answer the following questions
# in terms of n.

'''
1. How many edges are in KN?
    n * (n - 1)/2

2. Consider the new version of DFS. This traverses paths until all non-circular
   paths from the source to the destination have been found, and returns the 
   shortest one.
   Let A be the source node, and B be the destination in KN. How many paths
   of length 2 exist from A to B?
   n - 2   (We have a source A and a destination B. Paths of length 2 contain
            exactly three three nodes. We must select one more node to place
            in the middle of our path. As we cannot select the A or B, we are
            left with N - 2 choices to construct a path.)

3. How many paths of length 3 exist from A to B?
   (n - 2) * (n - 3)

4. Continuing the logic used above, calculate the number of paths of length m
   from A to B, where 1≤m≤(n−1), and write this number as a ratio of factorials.
   fact(n - 2)/fact(n - m - 1)
   
'''


# ex. 7
# Write a WeightedEdge class that extends Edge. Its constructor requires a
# weight parameter, as well as the parameters from Edge. You should
# additionally include a getWeight method. The string value of a WeightedEdge
# from node A to B with a weight of 3 should be "A->B (3)".

class WeightedEdge(Edge):
    def __init__(self, src, dest, weight):
        Edge.__init__(self, src, dest)
        self.weight = weight
    def getWeight(self):
        return self.weight
    def __str__(self):
        return Edge.__str__(self) + " (" + str(self.weight) + ")"
    


        




































