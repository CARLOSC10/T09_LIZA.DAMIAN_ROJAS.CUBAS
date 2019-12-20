import libreria
import os

#ARGUMENTOS
valor01=int(os.sys.argv[1])
valor02=int(os.sys.argv[2])

mayor=libreria.mayor(valor01,valor02)
msg="El MAYOR ENTRE {} y {} ES: {}"
print(msg.format(valor01,valor02,mayor))
