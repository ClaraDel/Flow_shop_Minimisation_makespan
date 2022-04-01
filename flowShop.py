import random
from numpy import copy

class Flowshop:

    def __init__(self, jobs=None, nb_machines=2, nb_jobs=6):
        self.nb_machines = nb_machines
        self.nb_jobs = nb_jobs
        self.jobs = self.randFlowshop()
        self.makespans = []
        print(self.nb_jobs, self.nb_machines)

    def randFlowshop(self):
        jobs = [[random.randrange(1, 50) for _ in range(self.nb_machines + 1)] for _ in range(self.nb_jobs)]
        for i in range(self.nb_jobs):
            jobs[i][0] = i
        return jobs

    def printJobs(self):
        print("Liste des tâches initialisées :")
        for i in range(self.nb_jobs):
            print("Job n°", self.jobs[i][0], self.jobs[i][1:])

    def triSep(self):
        U = []
        V = []
        for i in range(self.nb_jobs):
            if self.jobs[i][1] < self.jobs[i][2]:
                U.append(self.jobs[i])
            else:
                V.append(self.jobs[i])

        U = self.tri_insertion(U)
        V = self.tri_insertionDec(V)
        return U + V

    def BandB(self):
        if self.nb_machines > 2:
            for k in range(1, self.nb_machines):
                print("k = ", k)
                jobsSum = []
                for i in range(self.nb_jobs):
                    fList = self.jobs[i][1:k + 1].copy()
                    lList = self.jobs[i][k + 1:].copy()
                    jobsSum.append([self.jobs[i][0], sum(fList), sum(lList)])
                jobsOrdered = self.triSepReduction(jobs=jobsSum)
                self.printJobOrder(jobsOrdered)
                self.makespans.append(self.makespan(jobsOrdered, self.nb_machines - 1, self.nb_jobs))
                print("Makespan de la solution avec k =", k, ":", self.makespans[-1])
            [makespanMin, indiceMin] = self.getMinMakespan()
            self.printSolution(indiceMin, makespanMin)
            return 0

    def getMinMakespan(self):
        temp = self.makespans[0]
        indiceMin = 0
        for i in range(1, len(self.makespans)):
            if(temp > self.makespans[i]):
                indiceMin = i
                temp = self.makespans[i]
        return temp, indiceMin

    def printSolution(self, indiceMin, makespanMin):
        print("La meilleur solution retenue est l'ordre avec k =", indiceMin + 1, "avec un makesman =", makespanMin)


    def triSepReduction(self, jobs):
        U = []
        V = []
        for i in range(len(jobs)):
            if jobs[i][1] < jobs[i][2]:
                U.append(jobs[i])
            else:
                V.append(jobs[i])
        U = self.tri_insertion(U)
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

    def reductionPb(self):
        if self.nb_machines > 3:
            for i in range(self.nb_jobs, 1):
                self.triSepReduction(jobs=(self.jobs(i-1), self.jobs(i)))

        else:
            return self.triSep()

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

    # def triDynamique(self):
