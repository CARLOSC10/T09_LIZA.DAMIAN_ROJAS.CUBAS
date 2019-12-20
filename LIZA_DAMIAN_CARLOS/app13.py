import libreria
import os

#ARGUMENTOS
vueltas=float(os.sys.argv[1])
tiem_empleado=float(os.sys.argv[2])

frecuencia=libreria.frecuencia(vueltas,tiem_empleado)
print("LA FRECUENCIA ES:",frecuencia)
