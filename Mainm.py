from flowShop import *

def main():

    #initialisation du problème d'ordonnancement
    nb_machines = 6
    nb_jobs = 5
    flowshop = Flowshop(nb_machines, nb_jobs)
    #flowshop.randFlowshop()
    flowshop.printJobs()

    # appel de l'heuristique voulue
    flowshop.NEH()
    #flowshop.JohnsonOuCDS()

    #lowshop.NEH()
    #flowshop.methExa()
    return 0

main()
