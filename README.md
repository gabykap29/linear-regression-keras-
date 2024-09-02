# Proyecto de Regresión Lineal con Keras

Este proyecto utiliza Keras para construir y entrenar un modelo de regresión lineal para predecir el peso basado en la altura. El código incluye la visualización del error cuadrático medio (ECM) durante el entrenamiento, así como la predicción del peso para una altura específica.

## Requisitos

- **Anaconda**: Se recomienda usar Anaconda para manejar el entorno de Python.
- **Python**: 3.7 o superior.
- **Bibliotecas**: Pandas, NumPy, Matplotlib, Keras.

## Instalación

### 1. Clonar el Repositorio

Primero, clona este repositorio en tu máquina local (si es que aún no lo has hecho):

```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio
```

2. Crear un Entorno con Conda
Crea un nuevo entorno con Conda. Asegúrate de ajustar la versión de Python si es necesario:

```bash
conda create --name mi_entorno python=3.7
```
3. Activar el Entorno
Activa el entorno que acabas de crear:
```bash
conda activate mi_entorno
```
4. Instalar las Dependencias
Instala las bibliotecas necesarias en el entorno:

```bash
conda install pandas numpy matplotlib
pip install keras
```
5. Preparar el Archivo de Datos
Asegúrate de que el archivo altura_peso.csv esté en el directorio raíz del proyecto. Este archivo debe contener las columnas Altura y Peso.

### Uso
Para ejecutar el script, asegúrate de que el entorno mi_entorno esté activo y luego ejecuta el siguiente comando:

```bash
python main.py
```

Este comando ejecutará el script `main.py`, que:

1. Leerá los datos del archivo `altura_peso.csv`.
2. Construirá y entrenará un modelo de regresión lineal usando Keras.
3. Graficará el error cuadrático medio (ECM) durante el entrenamiento.
4. Superpondrá la recta de regresión sobre los datos originales.
5. Realizará una predicción del peso para una altura específica (por ejemplo, 170 cm) y la imprimirá en pantalla.

## Ejemplo de Salida

```less
Parámetros después del entrenamiento: w = 0.5, b = 10.0
Predicción del peso para una persona de 170 cm: 70.0 kg
```
