from flowShop import *

def main():

    flowshop = Flowshop(nb_machines=4)
    flowshop.randFlowshop()
    jobOrder = flowshop.reductionPb()
    flowshop.BandB(2)
    # printJobOrder(jobOrder)
    return 0

main()
