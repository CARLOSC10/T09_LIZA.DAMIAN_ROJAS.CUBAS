import libreria
import os

#ARGUMENTOS
resistencia=float(os.sys.argv[1])
variacion=float(os.sys.argv[2])
temperatura=float(os.sys.argv[3])

resistencia_electrica=libreria.resistencia_electrica(resistencia,variacion,temperatura)
print("LA RESISTENCIA ELECTRICA ES",resistencia_electrica)
