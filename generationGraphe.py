import matplotlib.pyplot as plt

def graphique(titre, data):
    plt.title(titre)
    for d in range(1, len(data)):
        plt.plot(d, data[d][1], 'b.')
        plt.plot(d, data[d][2], 'g.')
        plt.plot(d, data[d][0], 'r.')
    plt.legend(['CDS', 'Palmer', 'NEH'])
    plt.show()