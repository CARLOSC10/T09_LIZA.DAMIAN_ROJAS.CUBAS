import libreria
import os

#ARGUMENTOS
densi=int(os.sys.argv[1])
grave=int(os.sys.argv[2])
altu=int(os.sys.argv[3])

precion_hidrostatica=libreria.precion_hidrostatica(densi,grave,altu)
print("LA PRECION HIDROSTATICA ES:",precion_hidrostatica)
