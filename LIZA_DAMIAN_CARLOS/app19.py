import libreria
import os

valor3=int(os.sys.argv[1])
valor4=int(os.sys.argv[2])

divi=libreria.division(valor3,valor4)
msg="LA DIVISION DE LOS DOS VALORES {} y {} ES: {}"
print(msg.format(valor3,valor4,divi))
