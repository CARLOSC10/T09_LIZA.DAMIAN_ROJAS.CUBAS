import libreria
import os

#ARGUMENTOS
MAS=int(os.sys.argv[1])
velo=int(os.sys.argv[2])


energia_cinetica=libreria.energia_cinetica(MAS,velo)
print("LA ENERGIA CINETICA ES:",energia_cinetica)
