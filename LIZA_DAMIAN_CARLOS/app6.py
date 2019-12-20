import libreria
import os

#ARGUMENTOS
veloc=float(os.sys.argv[1])
tiempo=float(os.sys.argv[2])

movimiento=libreria.mr(veloc,tiempo)
print("EL MOVIMIENTO RECTILINEO UNIFORME(MRU) ES:",movimiento)
