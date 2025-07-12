import sys

sys.path.append("../libs")
from neuronas import NeuronaMcCullochPittsTodoEnUno


def main():
    # D.1.1.
    neurona = NeuronaMcCullochPittsTodoEnUno(2, 1, 0, 0)
    imprimir(neurona.activacion())

    neurona = NeuronaMcCullochPittsTodoEnUno(2, 0, 1, 0)
    imprimir(neurona.activacion())

    neurona = NeuronaMcCullochPittsTodoEnUno(2, 0, 0, 1)
    imprimir(neurona.activacion())


def imprimir(decision):
    if decision == 1:
        print("Sí, ir al gym")
    if decision == 0:
        print("No, no ir al gym")


if __name__ == "__main__":
    main()
