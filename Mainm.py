from flowShop import *

def main():

    flowshop = Flowshop(nb_machines=3, nb_jobs=3)
    flowshop.randFlowshop()
    flowshop.printJobs()
    jobOrder = flowshop.reductionPb()
    flowshop.BandB()
    # printJobOrder(jobOrder)
    return 0

main()
