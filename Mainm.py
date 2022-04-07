from flowShop import *
import itertools as it

def main():

    #initialisation du problème d'ordonnancement
    nb_machines = 6
    nb_jobs = 6

    flowshop = Flowshop(nb_machines, nb_jobs)
    #flowshop.randFlowshop()
    flowshop.printJobs()

    # appel de l'heuristique voulue
    # [currentSequece, makespanFinal] = flowshop.NEH()
    # print("Tri terminé. L'ordre final des tâches est", currentSequece, "avec un Makespan de ", makespanFinal)
    flowshop.JohnsonOuCDS()

    flowshop.NEH()
    flowshop.methExa()


    return 0

main()
