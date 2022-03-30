from flowShop import *

def main():

    flowshop = Flowshop()
    flowshop.randFlowshop()
    flowshop.printJobs()
    jobOrder = flowshop.triSep()
    print(jobOrder)
    return 0

main()
