import random
#from numpy import copy
import itertools as it
import time as t
import Instances as inst

class Flowshop:

    def __init__(self, nb_machines, nb_jobs):
        self.nb_machines = nb_machines
        self.nb_jobs = nb_jobs
        #self.jobs = self.randFlowshop()
        self.jobs = inst.A
        self.makespans = []
        print("--- Initialisation d'un problème d'ordonnancement avec ", self.nb_jobs, "tâches et ", self.nb_machines, "machines ---")

    def __int__(self, stringFile):
        file = open(stringFile,"r")
        print(file.read())

    def randFlowshop(self):
        jobs = [[random.randrange(1, 50) for _ in range(self.nb_machines + 1)] for _ in range(self.nb_jobs)]
        for i in range(self.nb_jobs):
            jobs[i][0] = i
        return jobs

    def printJobs(self):
        print("Liste des tâches initialisées :")
        for i in range(self.nb_jobs):
            print("Job n°", self.jobs[i][0], self.jobs[i][1:])

    # heuristique de Campbell, Dudek et Smith
    def CDS(self):
        if self.nb_machines > 2:
            minMakespan = 0
            for k in range(1, self.nb_machines):
                # print("pour k = ", k)
                jobsSum = []
                for i in range(self.nb_jobs):
                    fList = self.jobs[i][1:k + 1].copy()
                    lList = self.jobs[i][k + 1:].copy()
                    jobsSum.append([self.jobs[i][0], sum(fList), sum(lList)])
                # on récupère la liste des tâches triée dans l'odre de l'algorithme de Johnson
                jobsOrdered = self.Johnson(jobs=jobsSum)
                # on l'affiche dans la console
                # self.printJobOrder(jobsOrdered)
                # on calculz le makespan pour cet ordre précis
                #makespans = self.makespan(jobsOrdered, self.nb_machines - 1, self.nb_jobs)
                makespan = self.makespan(jobsOrdered, self.nb_jobs-1, self.nb_machines)
                # on l'ajoute à une liste
                if makespan < minMakespan or minMakespan == 0:
                    makespanMin = makespan
                    orderMin = jobsOrdered
                    indiceMin = k
                # self.makespans.append(makespans)
                # print("Makespan de la solution avec k =", k, ":", self.makespans[-1])
            # on récupère le makespan le plus petit
            # [makespanMin, indiceMin] = self.getMinMakespan(self.makespans)
            # on print la solution finale
            self.printSolution(indiceMin, makespanMin, orderMin)

    def getMinMakespan(self, makespans):
        temp = makespans[0]
        indiceMin = 0
        for i in range(1, len(self.makespans)):
            if(temp > self.makespans[i]):
                indiceMin = i
                temp = self.makespans[i]
        return temp, indiceMin

    def printSolution(self, indiceMin, makespanMin, orderMin):
        print("La meilleur solution retenue est l'ordre ", end=' ')
        for i in range(self.nb_jobs):
            print(orderMin[i][0], end=' ')
        print("avec k =", indiceMin + 1, "avec un makespan =", makespanMin)

    def Johnson(self, jobs):
        U = []
        V = []
        # Sépare la matrice tâches/machine en deux ensemble
        # U = ensemble de tâches dont pi1 < pi2
        # V = ensemble de tâches dont pi1 >= pi2
        for i in range(len(jobs)):
            if jobs[i][1] < jobs[i][2]:
                U.append(jobs[i])
            else:
                V.append(jobs[i])
        # trie dans un ordre croissant
        U = self.tri_insertion(U)
        # trie dans un ordre décroissant
        V = self.tri_insertionDec(V)
        return U + V

    def tri_insertion(self, tab):
        for i in range(len(tab)):
            temp = tab[i]
            j = i
            while j > 0 and tab[j - 1][1] > temp[1]:
                tab[j] = tab[j - 1]
                j = j - 1
            tab[j] = temp
        return tab

    def tri_insertionDec(self, tab):
        for i in range(len(tab)):
            temp = tab[i]
            j = i
            while j > 0 and tab[j - 1][1] < temp[1]:
                tab[j] = tab[j - 1]
                j = j - 1
            tab[j] = temp
        return tab

    def JohnsonOuCDS(self):
        if self.nb_machines >= 3:
            print("\nDébut de la méthode Dudek Smith")
            self.CDS()
        else:
            print("\nDébut de la méthode Johnson")
            self.Johnson()

    def makespan(self, order, i, m):
        # self.jobs[tab[i][0]][1:]
        if i == 0 and m == 1:
            t = self.jobs[order[i][0]][1]
        elif i == 0:
            t = self.jobs[order[i][0]][m] + self.makespan(order, 0, m - 1)
        elif m == 1:
            t = self.jobs[order[i][0]][m] + self.makespan(order, i - 1, 1)
        else:
            t = self.jobs[order[i][0]][m] + max(self.makespan(order, i - 1, m), self.makespan(order, i, m - 1))
        return t

    def printJobOrder(self, tab):
        print("Ordre des tâches :")
        for i in range(len(tab)):
            print("Tâche n°", tab[i][0], self.jobs[tab[i][0]][1:])

    def methExa(self):
        print("\nDébut de la méthode exacte")
        minMakespan = 0
        for order in it.permutations(self.jobs, self.nb_jobs):
            temp = self.makespan(order, self.nb_jobs - 1, self.nb_machines)
            if temp < minMakespan or minMakespan == 0:
                minMakespan = temp
                meilleurOrdre = order
        print("La méthode exacte donne un makespan minimum de :", minMakespan, "et l'ordre est :", end=' ')
        for i in range(self.nb_jobs):
            print(meilleurOrdre[i][0], end=' ')
        print()

    def iterTriDynamique(self):
        order = []
        compList = [[0]]
        for j in range(self.nb_jobs - 1):
            abc = self.makespan((self.jobs(j),self.jobs(j + 1)), self.nb_machines - 1, 2)
            cba = self.makespan((self.jobs(j + 1),self.jobs(j)), self.nb_machines - 1, 2)
            if abc > cba:
                compList[0].append(j + 1)
                # call self.calcVirtualTemp
            else:
                temp = [j + 1].append(compList[0])
                compList[0] = temp
                # call self.calcVirtualTemp


    def calcVirtualTemp(self, tab, virt, k, i):
        b = tab[k][i - 1]
        for m in range(k - 1):
            a = a + tab[m][i]
            b = b + tab[m][i - 1]
        if tab[k][i] + a > b:
            virt[i] = tab[k + 1][i] + a + tab[k][i] - b
        else:
            virt[i] = tab[k][i]
        return virt

    # Heuristique de Nawaz, Enscore et Ham
    def NEH(self):
        print("\nDébut de la méthode Nawaz, Enscore et Ham")
        #1 : somme de tous les temps d'opérations sur chaque machine
        jobsSum = []
        for i in range(self.nb_jobs):
            jobsSum.append([self.jobs[i][0], sum(self.jobs[i][1:])])
        # print("jobsSum", jobsSum)

        #2 : trier le tableau
        jobsSumTrie = self.tri_insertionDec(jobsSum)
        # print("jobsSumTrie", jobsSumTrie)

        #3 prendre la tâche la plus grande non encore triée
        currentSequece = [jobsSumTrie[0]]

        for i in range(1, self.nb_jobs):
            # nouvelle tâche qu'il va falloir bien placer dans la séquence déjà triée
            jobEnCours = jobsSumTrie[i]
            makespanMin = float("inf")
            #on parcours les placements possibles de jobEnCours
            for j in range(0, i+1):
                # On insère jobEnCours dans la séquence
                seqJobsenCours = self.insertion(currentSequece, j, jobEnCours)

                makespan = self.makespan(seqJobsenCours, len(seqJobsenCours) - 1, self.nb_machines)
                # print("Le makespan avec l'ordre", seqJobsenCours, "vaut", makespan)

                if makespanMin > makespan:
                    bestSeqJobs = seqJobsenCours
                    makespanMin = makespan
            currentSequece = bestSeqJobs
            # print("la meilleur séquence retenue est", currentSequece)
        makespanFinal = self.makespan(currentSequece, len(currentSequece) - 1, self.nb_machines)
        return currentSequece, makespanFinal

    def BranchAndBound(self):
        end = True
        jobs = []
        jobsRestants = self.jobs.copy()
        while end:
            nodeWeight = min(self.calculLowerBounds(jobsRestants))
            for j in range(len(jobsRestants)):
                temp = min(self.calculLowerBounds(jobsRestants))
                if  temp < nodeWeight:
                    nodeWeight = temp
            end = False

    def calculLowerBounds(self, jobs):
        lowerBounds = []
        for m in range(1, self.nb_machines + 1):
            minPts = []
            lb = jobs[1][m] + jobs[len(jobs) - 1][m]
            minPts.append(sum(jobs[1][1:m - 1] + jobs[1][m + 1:]))
            for j in range(2, len(jobs) - 1):
                lb = lb + jobs[j][m]
                minPts.append(sum(jobs[j][1:m - 1] + jobs[j][m + 1:]))
            minPts.append(sum(jobs[len(jobs) - 1][1:m - 1] + jobs[len(jobs) - 1][m + 1:]))
            lb = lb + min(minPts)
            lowerBounds.append(lb)
        return lowerBounds

    # insert a new job
    def insertion(self, seq, index_position, value):
        newListJobs = seq[:]
        newListJobs.insert(index_position, value)
        return newListJobs

    def hPalmer(self):
        print("Début de l'heuristique de Palmer :")
        ordre = []
        for j in range(self.nb_jobs):
            f = 0
            for m in range(1, self.nb_machines + 1):
                f = f + (self.nb_machines - 2 * m + 1) * self.jobs[j][m]
            ordre.append(f)
            ordre = self.tri_insertion(ordre)
        return ordre
