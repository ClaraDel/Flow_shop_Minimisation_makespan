from flowShop import *

def main():

    flowshop = Flowshop(nb_machines=3)
    flowshop.randFlowshop()
    flowshop.reductionPb()
    flowshop.printJobs()
    jobOrder = flowshop.triSep()
    print(jobOrder)
    return 0

main()
