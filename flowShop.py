import random

class Flowshop:

    def __init__(self, jobs=None, nb_machines=2, nb_jobs=6):
        self.nb_machines = nb_machines
        self.nb_jobs = nb_jobs
        self.jobs = self.randFlowshop()
        print(self.nb_jobs, self.nb_machines)

    def randFlowshop(self):
        jobs = [[random.randrange(1, 20) for _ in range(self.nb_jobs)] for _ in range(self.nb_machines)]
        return jobs

    def printJobs(self):
        print(self.jobs)

 #   def separation(jobs):

    def minTime(jobs):
        min = 666
        for j in range(0, jobs.length - 1):
            if jobs(j)[0] < min:
                min = jobs(j)
            if jobs(j)(1) < min:
                min = jobs(j)(1)

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