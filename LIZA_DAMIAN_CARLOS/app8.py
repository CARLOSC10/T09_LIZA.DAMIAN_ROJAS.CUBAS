import libreria
import os

valor5=int(os.sys.argv[1])
valor6=int(os.sys.argv[2])

s=libreria.suma(valor5,valor6)
msg1="LA SUMA DE LOS DOS VALORES {} y {} ES: {}"
print(msg1.format(valor5,valor6,s))
