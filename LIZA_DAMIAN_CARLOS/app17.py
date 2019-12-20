import libreria
import os

#ARGUMENTOS
calor=int(os.sys.argv[1])
trabaj=int(os.sys.argv[2])

termodinamica=libreria.termodinamica(calor,trabaj)
print("LA TERMODINAMICA ES:",termodinamica)
