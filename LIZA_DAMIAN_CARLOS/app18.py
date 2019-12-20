import libreria
import os

#ARGUMENTOS
ma=int(os.sys.argv[1])
gra=int(os.sys.argv[2])
alt=int(os.sys.argv[3])

energia_potencial=libreria.energia_potencial(ma,gra,alt)
print("LA ENERGIA POTENCIAL ES:",energia_potencial)
