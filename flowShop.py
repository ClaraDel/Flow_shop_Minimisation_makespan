import random

class Flowshop:

    def __init__(self, jobs=None, nb_machines=2, nb_jobs=6):
        self.nb_machines = nb_machines
        self.nb_jobs = nb_jobs
        self.jobs = self.randFlowshop()
        print(self.nb_jobs, self.nb_machines)

    def randFlowshop(self):
        jobs = [[random.randrange(1, 20) for _ in range(self.nb_machines)] for _ in range(self.nb_jobs)]
        return jobs

    def printJobs(self):
        print(self.jobs)

    def triSep(self):
        U = []
        V = []
        for i in range(self.nb_jobs):
            if self.jobs[i][0] < self.jobs[i][1]:
                U.append(self.jobs[i])
            else:
                V.append(self.jobs[i])

        U = self.tri_insertion(U)
        V = self.tri_insertionDec(V)
        return U + V

    def tri_insertion(self, tab):
        for i in range(len(tab)):
            temp = tab[i]
            j = i
            while j > 0 and tab[j - 1] > temp:
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