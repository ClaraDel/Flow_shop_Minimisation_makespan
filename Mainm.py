from flowShop import *

import time as t

def main():

    #initialisation du problème d'ordonnancement
    nb_machines = 10
    nb_jobs = 50

    flowshop = Flowshop(nb_machines, nb_jobs)
    flowshop.printJobs()

    # appel de l'heuristique voulue
    startTime = t.time()
    [currentSequece, makespanFinal] = flowshop.NEH()
    print("L'ordre final des tâches est", end=' ')
    for i in range(len(currentSequece)):
        print(currentSequece[i][0], end=' ')
    print("avec un Makespan de ", makespanFinal)
    print("Temps d'exécution depuis le début de la méthode :", t.time() - startTime)

    startTime = t.time()
    flowshop.JohnsonOuCDS()
    print("Temps d'exécution depuis le début de la méthode :", t.time() - startTime)

    startTime = t.time()
    ordre = flowshop.hPalmer()
    makespan = flowshop.makespan(ordre, nb_jobs - 1, nb_machines)
    print("Temps d'exécution depuis le début de la méthode :", t.time() - startTime)
    print("Pour l'heuristique de Palmer, l'ordre optimale est :", end=' ')
    for i in range(len(ordre)):
        print(ordre[0][i], end=' ')
    print("avec un makespan de :", makespan)

    # startTime = t.time()
    # flowshop.methExa()
    # print("Temps d'exécution depuis le début de la méthode :", t.time() - startTime)

    return 0

main()
