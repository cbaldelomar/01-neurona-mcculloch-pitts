import sys

sys.path.append("./libs")
from neuronas import NeuronaMcCullochPittsTodoEnUno


def main():
    print("prueba de estar dentro de main")
    neurona = NeuronaMcCullochPittsTodoEnUno()
    print(neurona.threshold)


if __name__ == "__main__":
    main()
