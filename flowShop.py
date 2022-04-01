import random
from numpy import copy

class Flowshop:

    def __init__(self, jobs=None, nb_machines=2, nb_jobs=6):
        self.nb_machines = nb_machines
        self.nb_jobs = nb_jobs
        self.jobs = self.randFlowshop()
        print(self.nb_jobs, self.nb_machines)

    def randFlowshop(self):
        jobs = [[random.randrange(1, 50) for _ in range(self.nb_machines + 1)] for _ in range(self.nb_jobs)]
        for i in range(self.nb_jobs):
            jobs[i][0] = i
        return jobs

    def printJobs(self):
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
            for k in range(1, self.nb_machines - 1):
                jobsSum = []
                for i in range(self.nb_jobs):
                    fList = self.jobs[i][1:k + 1].copy()
                    lList = self.jobs[i][k + 1:].copy()
                    jobsSum.append([self.jobs[i][0], sum(fList), sum(lList)])
                    self.triSepReduction(jobs=jobsSum)
                self.printJobOrder(self.triSepReduction(jobsSum))
                print(self.makespan(self.nb_machines-1, self.nb_jobs))
            return 0

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
        # for i in range(self.nb_jobs):
        #     tself.jobs[i]
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

    def makespan(self, i, m):
        # self.jobs[tab[i][0]][1:]
        if i == 0 and m == 1:
            t = self.jobs[0][1]
        elif i == 0:
            t = self.jobs[i][m] + self.makespan(0, m - 1)
        elif m == 1:
            t = self.jobs[i][m] + self.makespan(i - 1, 1)
        else:
            t = self.jobs[i][m] + max(self.makespan(i - 1, m), self.makespan(i, m - 1))
        return t

    def printJobOrder(self, tab):
        print("Ordre des tâches :")
        for i in range(len(tab)):
            print("Tâche n°", tab[i][0], self.jobs[tab[i][0]][1:])
    #
    # def triDynamique(self):
    #
    #
    # def makespan2Jobs(self, tab, i, m):
    #     if i == 0 and m == 1:
    #         t = tab[0][1]
    #     elif i == 0:
    #         for j in range(self.nb_machines):
    #             t = t + tab[0][m - j]
    #     elif m == 1:
    #         t = tab[1][1] + tab[0][1]
    #     else:
    #         t = tab[1][m] + max(self.makespan2Jobs(tab, i - 1, m), self.makespan2Jobs(tab, i, m - 1))
    #     return t
    # def makespanIter():

            # for i in range(self.nb_jobs):
            #     print("avant : ", self.jobs[i])
            #     for j in range(2, self.nb_machines):
            #         self.jobs[i][1] = self.jobs[i][1] + self.jobs[i][j]
            #     del self.jobs[i][2:]
            #     print("après : ", self.jobs[i])

    # def minTime(jobs):
    #     min = 666
    #     for j in range(0, jobs.length - 1):
    #         if jobs(j)[0] < min:
    #             min = jobs(j)
    #         if jobs(j)(1) < min:
    #             min = jobs(j)(1)

    # def johnson_flowshop(jobs):
    #     r = []
    #     for i in range(1, jobs.length()):
    #         for j in range(jobs):
    #             t = minTime(jobs)
    #             if t == jobs(j)(1):
    #                 r.insert(0, )
    #             else:
    #
    #     return r
