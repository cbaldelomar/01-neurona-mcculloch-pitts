class NeuronaMcCullochPittsTodoEnUno:
    def __init__(self, input1, input2, input3):
        self.threshold = 1
        self.input1 = input1
        self.input2 = input2
        self.input3 = input3

    def activacion(self):
        if self.input1 + self.input2 + self.input3 >= self.threshold:
            return 1
        else:
            return 0
