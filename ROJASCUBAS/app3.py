import os
import libreria


numero_entero=int(os.sys.argv[1])
a=int(os.sys.argv[2])
b=int(os.sys.argv[3])

numero_entero,a,b=libreria.pedir_numero_entero(numero_entero,a,b)
print("El numero:"+str(numero_entero)+" pertenece al intervalo"+"["+str(a)+","+str(b)+"]")
