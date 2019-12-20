import libreria
import os

#ARGUMENTOS
a_lateral=int(os.sys.argv[1])
a_base=int(os.sys.argv[2])

area_prisma=libreria.area_prisma(a_lateral,a_base)
print("AREA TOTAL DE UN PRISMA ES:",area_prisma)
