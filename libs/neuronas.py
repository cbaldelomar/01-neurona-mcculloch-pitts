"""Nuronas"""


class NeuronaMcCullochPittsTodoEnUno:
    """Neurona McCulloch-Pitts con 3 entradas y un umbral"""

    def __init__(self, threshold, input1, input2, input3):
        self.threshold = threshold
        self.input1 = input1
        self.input2 = input2
        self.input3 = input3

    def activacion(self):
        """Calcula la activación de la neurona McCulloch-Pitts"""
        if self.input1 + self.input2 + self.input3 >= self.threshold:
            return 1

        return 0


class NeuronaMcCullochPittsSencilla:
    """Neurona McCulloch-Pitts con 3 pesos y un umbral"""

    def __init__(self, synapsis1, synapsis2, synapsis3, threshold):
        self.threshold = threshold
        self.w1 = synapsis1
        self.w2 = synapsis2
        self.w3 = synapsis3

    def activacion(self, x1, x2, x3):
        """Calcula la activación de la neurona McCulloch-Pitts con tres entradas"""
        if (x1 * self.w1) + (x2 * self.w2) + (x3 * self.w3) >= self.threshold:
            return 1

        return 0
