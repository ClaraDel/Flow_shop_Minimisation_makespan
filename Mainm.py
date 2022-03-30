from flowShop import *

def main():

    flowshop = Flowshop()
    flowshop.randFlowshop()
    flowshop.printJobs()
    U, V = flowshop.triSep()
    return 0

main()
