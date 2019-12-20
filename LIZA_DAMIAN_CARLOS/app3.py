import libreria
import os

#ARGUMENTOS
anio_act=int(os.sys.argv[1])
anio_nacimi=int(os.sys.argv[2])

edad=libreria.edad(anio_act,anio_nacimi)
print("LA EDAD DE KELLY ES:",edad)
