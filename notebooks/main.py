import sys

sys.path.append("../libs")
from neuronas import NeuronaMcCullochPittsSencilla


def main():
    # D.1.5.b

    neurona = NeuronaMcCullochPittsSencilla(0.5, 1, 2, 1.1)

    # tiempo libre (1), motivacion (0), suscripcion (0)
    imprimir(neurona.activacion(1, 0, 0))

    # tiempo libre (1), motivacion (1), suscripcion (0)
    imprimir(neurona.activacion(1, 1, 0))

    # tiempo libre (0), motivacion (1), suscripcion (0)
    imprimir(neurona.activacion(0, 1, 0))

    # tiempo libre (0), motivacion (0), suscripcion (1)
    imprimir(neurona.activacion(0, 0, 1))


def imprimir(decision):
    if decision == 1:
        print("Sí, ir al gym")
    if decision == 0:
        print("No, no ir al gym")


if __name__ == "__main__":
    main()
