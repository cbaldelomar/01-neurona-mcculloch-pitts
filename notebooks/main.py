import sys

sys.path.append("./libs")
from neuronas import NeuronaMcCullochPittsTodoEnUno


def main():
    tiempo_libre = 0
    motivacion = 0
    suscripcion = 0
    neurona = NeuronaMcCullochPittsTodoEnUno(tiempo_libre, motivacion, suscripcion)
    decision = neurona.activacion()

    if decision == 1:
        print("Sí, ir al gym")
    if decision == 0:
        print("No, no ir al gym")


if __name__ == "__main__":
    main()
