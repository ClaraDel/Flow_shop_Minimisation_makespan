from flowShop import *

def main():

    flowshop = Flowshop(nb_machines=5, nb_jobs=5)
    flowshop.randFlowshop()
    flowshop.printJobs()
    jobOrder = flowshop.reductionPb()
    flowshop.BandB()
    flowshop.methExa()
    return 0

main()
