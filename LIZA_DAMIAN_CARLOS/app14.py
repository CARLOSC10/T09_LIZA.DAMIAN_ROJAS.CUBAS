import libreria
import os

#ARGUMENTOS
cost_regidez=float(os.sys.argv[1])
deforma=float(os.sys.argv[2])

fuerza_elatica=libreria.fuerza_elastica(cost_regidez,deforma)
print("LA FUERZA ELASTICA ES:",fuerza_elatica)
