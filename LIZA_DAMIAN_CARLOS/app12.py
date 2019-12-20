import libreria
import os

#ARGUMENTOS
veloc_inicial=float(os.sys.argv[1])
acele=float(os.sys.argv[2])
tiem=float(os.sys.argv[3])

movimiento_rectilinio=libreria.mrv(veloc_inicial,acele,tiem)
print("EL MOVIMIENTO RECTILINEO UNIFORMEMENTE VARIADO(MRUV) ES:",movimiento_rectilinio)
