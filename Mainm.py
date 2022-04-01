from flowShop import *

def main():

    flowshop = Flowshop(nb_machines=4, nb_jobs=4)
    flowshop.randFlowshop()
    flowshop.printJobs()
    jobOrder = flowshop.reductionPb()
    flowshop.BandB()
    return 0

main()
