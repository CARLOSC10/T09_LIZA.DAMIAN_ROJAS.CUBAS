import libreria
import os

#ARGUMENTOS
angular=float(os.sys.argv[1])
radio=float(os.sys.argv[2])

tangencial=libreria.velocidad_tangencial(angular,radio)
print("LA VELOCIDAD ANGULAR ES:",tangencial)
