from flowShop import *
from generationGraphe import *
import time as t

def flowshopFct(nb_jobs, nb_machines, t_max_random, iter):

    makespansNEH =[]
    timesNEH = []
    makespansCDS =[]
    timesCDS = []
    makespansPalmer =[]
    timesPalmer = []
    makespansExa = []
    timesExa = []
    # erreursNEH = []
    # erreursCDS = []
    # erreursPalmer = []

    for n in range(iter):
        # initialisation du problème d'ordonnancement
        # nb_machines = 10
        # nb_jobs = 10
        # t_max_random = 50

        flowshop = Flowshop(nb_machines, nb_jobs, t_max_random)
        flowshop.printJobs()

        # appel de l'heuristique voulue
        # NEH
        startTime = t.time()
        [currentSequece, makespanNEH] = flowshop.NEH()
        print("L'ordre final des tâches est", end=' ')
        for i in range(len(currentSequece)):
            print(currentSequece[i][0], end=' ')
        print()
        print("Avec un Makespan de ", makespanNEH)
        currentTime = t.time() - startTime
        print("Temps d'exécution depuis le début de la méthode :", currentTime)
        makespansNEH.append(makespanNEH)
        timesNEH.append(currentTime)

        #CDS
        startTime = t.time()
        [currentSequece, makespanCDS] = flowshop.JohnsonOuCDS()
        currentTime = t.time() - startTime
        print("Temps d'exécution depuis le début de la méthode :", currentTime)
        print()
        makespansCDS.append(makespanCDS)
        timesCDS.append(currentTime)

        #PALMER
        startTime = t.time()
        ordre = flowshop.hPalmer()
        #makespan = flowshop.makespan(ordre, nb_jobs - 1, nb_machines)
        makespanPalmer = flowshop.makespanGraph(ordre, nb_jobs - 1)
        currentTime = t.time() - startTime
        print("Temps d'exécution depuis le début de la méthode :", currentTime)
        print("Pour l'heuristique de Palmer, l'ordre optimal est :", end=' ')
        for i in range(len(ordre)):
            print(ordre[i][0], end=' ')
        print()
        print("Avec un Makespan de ", makespanPalmer)
        makespansPalmer.append(makespanPalmer)
        timesPalmer.append(currentTime)

        # startTime = t.time()
        # makespanExa = flowshop.methExa()
        # currentTime = t.time() - startTime
        # print("Temps d'exécution depuis le début de la méthode :", currentTime)
        # makespansExa.append(makespanExa)
        # timesExa.append(currentTime)
        #
        # erreursNEH.append((makespanNEH - makespanExa)/makespanExa)
        # erreursCDS.append((makespanCDS - makespanExa)/makespanExa)
        # erreursPalmer.append((makespanPalmer - makespanExa)/makespanExa)

    makespanData =[sum(makespansNEH)/iter, sum(makespansCDS)/iter, sum(makespansPalmer)/iter, sum(makespansExa)/iter]
    dataTime = [sum(timesNEH)/iter, sum(timesCDS)/iter, sum(timesPalmer)/iter, sum(timesExa)/iter]
    # = [sum(erreursNEH)/iter, sum(erreursCDS)/iter, sum(erreursPalmer)/iter]
    return makespanData, dataTime#, erreurData

def main():
    for j in [10, 50, 100]:
        makespans = [[10, 20, 50]]
        times = [[10, 20, 50]]
        for m in [10, 20, 50]:
            print("Pour", j, "tâches et", m, "machines :")
            [makespan, time] = flowshopFct(j, m, 50, 1)
            # [makespan, time, erreur] = flowshopFct(j, m, 50, 1)
            makespans.append(makespan)
            times.append(time)
        titremakespans = 'Moyenne des différents makespans pour '+str(j)+' tâches'
        titreTemps = 'Moyenne des différents temps pour ' +str(j)+ ' tâches'

        graphique(titremakespans, makespans)
        graphique(titreTemps, times)
        # print(erreur)

main()