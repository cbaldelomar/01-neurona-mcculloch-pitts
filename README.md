# Neurona McCulloch-Pitts

Este proyecto implementa modelos de neuronas tipo McCulloch-Pitts en Python, con ejemplos de uso tanto en scripts como en notebooks.

## Estructura del proyecto

- [`libs/neuronas.py`](libs/neuronas.py): Implementación de las clases de neuronas.
- [`notebooks/main.py`](notebooks/main.py): Script de ejemplo para probar la neurona sencilla.
- [`notebooks/01-cbaldelomar-import-neurons.ipynb`](notebooks/01-cbaldelomar-import-neurons.ipynb): Ejemplo de uso en Jupyter Notebook.

## Uso

### Ejecutar el script principal

```sh
python notebooks/main.py
```

### Usar en un notebook

Asegúrate de agregar la ruta de `libs` al `sys.path` antes de importar:

```python
import sys
sys.path.append("../libs")
from neuronas import NeuronaMcCullochPittsTodoEnUno, NeuronaMcCullochPittsSencilla
```

## Requisitos

- Python 3.13 o compatible
- Jupyter Notebook (opcional, para ejecutar los notebooks)