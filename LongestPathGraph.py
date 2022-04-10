from collections import defaultdict

#le graphe possède une liste de tous les noeuds qui ont des noeuds adjacents, et ce avec la distance avec ces derniers
class Graph:
    def __init__(self, nbV):
        #nombre de noeuds que contient le graphe
        self.V = nbV

        # liste de : id du noeuds puis ses voisins avce la distance
        self.graph = defaultdict(list)

        # on initiaise la distance à devoir comparer à infini sauf la source qui vaut 0
        self.dist = [float("Inf")] * (self.V)

        # pile des vertices à parcourir dans l'ordre topologique
        self.stack = []

    # construction du graphe : on n'ajoute que les noeuds ayant au moins un voisin
    def addEdge(self, u, v, w):
        #u : numéro de vertice
        #v = : vertice voisin relié à u
        #w : longueur de l'arrête entre u et v
        self.graph[u].append((v, w))

    def triTopologique(self, nb_machines, nb_jobs):
        # on créée une pile de tous les vertex triée dans l'ordre topologique
        for i in range(nb_machines-1, -1, -1):
            for j in range(nb_jobs-1, -1, -1):
                self.stack.append(j*nb_machines+i)
        #print("stack =", self.stack)

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
        # on récupère le makespan à savoit le chemin le plus grand du premier au dernier noeuds + le temps de la dernière opération
        makespan = self.dist[self.V-1]-lastWeight
        return -makespan
