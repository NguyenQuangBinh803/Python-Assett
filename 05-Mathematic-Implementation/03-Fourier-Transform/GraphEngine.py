import matplotlib.pyplot as plt


class GraphicEngine:
    def __init__(self):
        pass

    def plot_signal(self, list_of_input_signal):
        fig, axs = plt.subplots(len(list_of_input_signal))
        for i in range(len(list_of_input_signal)):
            axs[i].plot(list_of_input_signal[i])

        plt.show()
