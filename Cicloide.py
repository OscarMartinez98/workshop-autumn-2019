################################################################################
# ------------------------------ ESCOM Learn Day ----------------------------- #
# ------------------ Autor: Jesus Adrian Montesinos Correa ------------------- #
# ---------------------- Autor: Oscar Martinez Vazquez ----------------------- #
# ------------------ Escuela Superior de Fisico Matematicas ------------------ #
# -------------------------------- Otoño 2019 -------------------------------- #
# -------- Aproximacion de PI por aproximacion de poligonos/cicloide --------- #
################################################################################

import numpy as np
import matplotlib.pyplot as plt

# Constantes importantes
PI = np.pi
CYCLOID_GENERATOR = 100

# Funcion para calcular la distancia entre dos puntos en R²
L = lambda x, x0, y, y0 : np.sqrt(((x-x0)**2)+((y-y0)**2))

if __name__ == '__main__':
	pi_aproximation = 0

	radius = float(input("Radio de la circunferencia: "))
	cycloid_grades = 2 * PI / CYCLOID_GENERATOR
	cycloid = {'x': [], 'y': []}
	for k in range(CYCLOID_GENERATOR):
		cycloid['x'].append(radius*(k*cycloid_grades-np.sin(k*cycloid_grades)))
		cycloid['y'].append(radius * (1 - np.cos(k * cycloid_grades)))
	
	polygon_sides = int(input("Ingrese los lados del poligono: "))
	polygon_grades = 2 * PI / polygon_sides
	polygon = {'x': [], 'y': []}
	for k in range(polygon_sides + 1):
		polygon['x'].append(radius*(k *polygon_grades-np.sin(k*polygon_grades)))
		polygon['y'].append(radius * (1 - np.cos(k * polygon_grades)))
		if k > 0:
			pi_aproximation += L(
				polygon['x'][k], 
				polygon['x'][k-1], 
				polygon['y'][k], 
				polygon['y'][k-1]
				)
	
	if radius != PI/6:
		pi_aproximation = (pi_aproximation * PI)/ (8 * radius)
	
	print('Error: {}'.format(np.pi - pi_aproximation))

	#Agregar la aproximacion de pi
	plt.title('Aproximacion actual: {}'.format(pi_aproximation))

	#Agregar la cicloide a la ventana
	plt.plot(cycloid['x'], cycloid['y'])

	#Agregar el poligono a la ventana
	plt.plot(polygon['x'], polygon['y'])
	
	# Definir que el tamaño del eje x & y sean proporcionales
	plt.axis('equal')

	# Mostrar la ventana generada
	plt.show()