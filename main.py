import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD
from keras.initializers import HeNormal

# leer los datos
datos = pd.read_csv('altura_peso.csv', sep=",")
print(datos)

# preparar los datos
x = datos['Altura'].values
y = datos['Peso'].values

# normalizar los datos (media = 0, desviación estándar = 1)
x = (x - np.mean(x)) / np.std(x)
y = (y - np.mean(y)) / np.std(y)

# definir el modelo
modelo = Sequential()
input_dim = 1
output_dim = 1
modelo.add(Dense(output_dim, input_dim=input_dim, activation='linear',kernel_initializer=HeNormal()))

# definir el optimizador
sgd = SGD(learning_rate=0.0004)

# compilar el modelo
modelo.compile(loss='mse', optimizer=sgd)

# entrenar el modelo
num_epochs = 10000
batch_size = x.shape[0]
historia = modelo.fit(x, y, epochs=num_epochs, batch_size=batch_size, verbose=1)

# obtener los parámetros del modelo después del entrenamiento
capas = modelo.layers[0]
w, b = capas.get_weights()
print(f'Parámetros después del entrenamiento: w = {w[0][0]:.1f}, b = {b[0]:.1f}')

# graficar el error cuadrático medio (ECM) vs. número de épocas
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(historia.history['loss'])
plt.xlabel('Epoch')
plt.ylabel('MSE')
plt.title('ECM vs. Epochs')

# superponer la recta de regresión resultante sobre los datos originales
plt.subplot(1, 2, 2)
plt.scatter(x, y, label='Datos originales')
y_regr = modelo.predict(x)
plt.plot(x, y_regr, 'r', label='Regresión lineal')
plt.xlabel('Altura')
plt.ylabel('Peso')
plt.title('Datos originales y regresión lineal')
plt.legend()

plt.tight_layout()
plt.show()

# realizar una predicción para una altura específica
altura_pred = np.array([170])
peso_pred = modelo.predict(altura_pred)
print(f'Predicción del peso para una persona de {altura_pred[0]} cm: {peso_pred[0][0]:.1f} kg')
