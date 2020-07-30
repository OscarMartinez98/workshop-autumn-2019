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
RADIANS = (PI)/180

# Funcion para calcular la distancia entre dos puntos en R²
L = lambda x, x0, y, y0 : np.sqrt(((x-x0)**2)+((y-y0)**2))

if __name__ == '__main__':
	pi_aproximation = 0

	radius = float(input("Radio de la circunferencia: "))

	polygon_sides = int(input("Ingrese los lados del poligono: "))
	polygon_grades = (2 * PI) / polygon_sides
	polygon = {'x': [], 'y': []}

	for k in range(polygon_sides + 1):
		polygon['x'].append(radius * np.cos(polygon_grades * k))
		polygon['y'].append(radius * np.sin(polygon_grades * k))
		if k > 0:
			pi_aproximation += L(
				polygon['x'][k], 
				polygon['x'][k-1], 
				polygon['y'][k], 
				polygon['y'][k-1]
				)

	if radius != 0.5:
		pi_aproximation = pi_aproximation / (2 * radius)
	
	print('Error: {}'.format(np.pi - pi_aproximation))

	#Agregar la aproximacion de pi
	plt.title('Aproximacion actual: {}'.format(pi_aproximation))

	#Agregar el poligono a la ventana
	plt.plot(polygon['x'], polygon['y'])

	#Agregar un circulo de radio r a la ventana
	circle1=plt.Circle((0,0), radius, fill=False)
	plt.gcf().gca().add_artist(circle1) 
	# gfc -> Get current figure
	# gca -> Get current axis
	
	# Definir que el tamaño del eje x & y sean proporcionales
	plt.axis('equal')

	# Mostrar la ventana generada
	plt.show()