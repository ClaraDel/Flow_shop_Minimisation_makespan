# Python program to find single source shortest paths
# for Directed Acyclic Graphs Complexity :OV(V+E)
from collections import defaultdict


# Graph is represented using adjacency list. Every
# node of adjacency list contains vertex number of
# the vertex to which edge connects. It also contains
# weight of the edge
class Graph:
    def __init__(self, vertices):

        self.V = vertices  # No. of vertices

        # dictionary containing adjacency List
        self.graph = defaultdict(list)

        # on initiaise la distance à devoir comparer à infini sauf la source qui vaut 0
        self.dist = [float("Inf")] * (self.V)

        # pile des vertices à parcourir dans l'ordre topologique
        self.stack = []

    # construction du graph : on n'ajoute que les noeuds ayant au moins un voisin
    def addEdge(self, u, v, w):
        #u : numéro de vertice
        #v = : vertice voisin relié à u
        #w : longueur de l'arrête entre u et v
        self.graph[u].append((v, w))

    def triTopologique(self, nb_machines, nb_jobs):
        # on créée une pile de tous les vertex triée dans l'ordre topologique)
        for i in range(nb_machines-1, -1, -1):
            for j in range(nb_jobs-1, -1, -1):
                self.stack.append(j*nb_machines+i)
        print("stack =", self.stack)


    ''' The function to find shortest paths from given vertex.
        It uses recursive topologicalSortUtil() to get topological
        sorting of given graph.'''

    def shortestPath(self, s):

        # Mark all the vertices as not visited
        visited = [False] * self.V
        self.dist[s] = 0

        # on parcours l'ordre topologique des noeuds
        while self.stack:

            # Get the next vertex from topological order
            i = self.stack.pop()

            # on met à jour les distances si elles sont mieux que les valeurs précédentes
            for node, weight in self.graph[i]:
                if self.dist[node] > self.dist[i] + weight:
                    self.dist[node] = self.dist[i] + weight


    def setMakespan(self, lastWeight):
        makespan = 0
        makespan = self.dist[self.V-1]-lastWeight
        return -makespan
