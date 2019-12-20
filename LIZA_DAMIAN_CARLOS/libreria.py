#LIZA DAMIAN CARLOS - LIBRERIA DE FUNCIONES

#EJERCICIO 01
#FUNCION PARA HALLAR EL AREA DEL TRAPECIO
#DECLARACION DE VARIABLES
base_mayor=0
base_menor=0
altura=0

#FUNCION QUE VALIDAD LA BASE MAYOR
def area_trapecio(base_mayor,base_menor,altura):
    base_invalida=(base_mayor<=0)
    while(base_invalida==True):
        base_mayor=int(input("BASE INCORRECTA:ingrese nuevamente la base mayor del trapecio correcta:"))
        base_invalida=(base_mayor<=0)
    #fin_while
    area=((base_mayor+base_menor)/2)*altura
    return area
#fin_def


#EJERCICIO 02
#FUNCION PARA HALLAR LA DISTANCIA DE UN CARRO
#DECLARACION DE VARIABLES
velocidad=0
tiempo=0

#FUNCION QUE VALIDAD LA VELOCIDAD
def distancia(velocidad,tiempo):
    velocidad_invalida=(velocidad <=0)
    while(velocidad_invalida == True):
        velocidad=int(input("VELOCIDAD INCORRECTA:ingrese nuevamente la velocidad correcta:"))
        velocidad_invalida=(velocidad <=0)
    #fin_while
    dis=velocidad*tiempo
    return dis
#fin_def


#EJERCICIO 03
#FUNCION PARA HALLAR LA EDDA DE UNA PERSONA

def edad(anio_actual,anio_nacimiento):
    edad=anio_actual - anio_nacimiento
    return edad
#fin_def


#EJERCICIO 04
#FUNCION PARA HALLAR LA ENERGIA CINETICA
#DECLARACION DE VARIABLES
MAsa=0.0
Velocidad=0.0

#FUNCION
def energia_cinetica(MAsa,Velocidad):
    ener_cine=1/2*MAsa*(Velocidad**2)
    return ener_cine
#fin_def


#EJERCICIO 05
#FUNCION DE UNA CADENA EN MINUSCULA LO CONVIERTE A MAYUSCULA
#FUNCION
def convertir(cadena):
    conv=cadena.upper()
    return conv
#fin_def


#EJERCICIO 06
#FUNCION PARA HALLAR EL MOVIMIENTO RECTILINEO UNIFORME(MRU)
#DECLARACION DE VARIABLES
velocidad=0.0
tiempo=0.0

#FUNCION
def mr(velocidad,tiempo):
    movimiento=velocidad*tiempo
    return movimiento
#fin_def


#EJERCICIO 07
#FUNCION PARA HALLAR EL VOLUMEN DE UNA PIRAMIDE
#DECLARACION DE VARIABLES
areA_BASE=0.0
alTura=0.0
#FUNCION
def volumen_piramide(areA_BASE,alTura):
    volu_piram=(areA_BASE*alTura)/3
    return volu_piram
#fin_def


#EJERCICIO 8
#FUNCION PARA HALLAR LA SUMA DE DOS VALORES
def suma(valor01,valor02):
    return valor01+valor02


#EJERCICIO 09
#FUNCION PARA HALLAR EL AREA TOTAL DE UN PRISMA
#DECLARACION DE VARIABLES
area_lateral=0.0
area_de_su_base=0.0

#FUNCION
def area_prisma(area_lateral,area_de_su_base):
    area_pris=(area_lateral+2*area_de_su_base)
    return area_pris
#fin_def


#EJERCICIO 10
#FUNCION DE UNA CADENA INVERTIDA
#FUNCION
def palin(cadena):
    invertida = cadena[::-1]
    return invertida
#fin_def


#EJERCICIO 11
#FUNCION PARA HALLAR LA RESISTENCIA ELECTRICA
#DECLARACION DE VARIABLES
resistencia_inicial=0.0
variacion_de_temperatura=0.0
coeficiente_de_temperatura=0.0

#FUNCION QUE VALIDAD LA VARIACION DE TEMPERATURA
def resistencia_electrica(resistencia_inicial,variacion_de_temperatura,coeficiente_de_temperatura):
    variacion_invalida=(variacion_de_temperatura<=0)
    while(variacion_invalida==True):
        variacion_de_temperatura=int(input("VARIACION DE TEMPERATURA INVALIDAD:ingrese nuevamente la variacion de temperatura correcta:"))
        variacion_invalida=(variacion_de_temperatura<=0)
    #fin_while
    res=(resistencia_inicial+resistencia_inicial*coeficiente_de_temperatura*variacion_de_temperatura)
    return res
#fin_def


#EJERCICIO 12
#FUNCION PARA HALLAR EL MOVIMIENTO RECTILINEO UNIFORMEMENTE VARIADO(MRUV)
#DECLARACION DE VARIABLES
velocidad_inicial=0.0
aceleracion=0.0
Tiempo=0.0

#FUNCION
def mrv(velocidad_inicial,aceleracion,Tiempo):
    movimiento_variado=velocidad_inicial+aceleracion*Tiempo
    return movimiento_variado
#fin_def


#EJERCICIO 13
#FUNCION PARA HALLAR LA FRECUENCIA
#DECLARACION DE VARIABLES
nro_vueltas=0.0
tiempo_empleado=0.0
#FUNCION QUE VALIDAD EL TIEMPO EMPLEADO
def frecuencia(nro_vueltas,tiempo_empleado):
    tiempo_invalido=(tiempo_empleado<=0)
    while(tiempo_invalido==True):
        tiempo_empleado=int(input(" VALOR DEL TIEMPO INVALIDAD:ingrese nuevamente el valor del tiempo correcta:"))
        tiempo_invalido=(tiempo_empleado<=0)
    #fin_while
    frecu=nro_vueltas/tiempo_empleado
    return frecu
#fin_def


#EJERCICIO 14
#FUNCION PARA HALLAR LA FUERZA ELASTICA
#DECLARACION DE VARIABLES
constante_rigidez=0.0
deformacion=0.0

#FUNCION
def fuerza_elastica(constante_rigidez,deformacion):
    fuerz_elas=constante_rigidez*deformacion
    return fuerz_elas
#fin_def


#EJERCICIO 15
#FUNCION PARA HALLAR EL TRABAJO

#DECLARACION DE VARIABLES
fuerza01=0
distancia2=0

#FUNCION
def trabajo(fuerza01,distancia2):
    traba=fuerza01*distancia2
    return traba
#fin_def


#EJERCICIO 16
#FUNCION QUE DEVUELVE EL MAYOR DE DOS NUMEROS

def mayor(x,y):
    if (x > y):
        return x
    else:
        return y
#fin_def

#EJERCICIO 17
#FUNCION PARA HALLAR LA PRIMERA LEY DE LA TERMODINAMICA
#DECLARACION DE VARIABLES
calor=0.0
trabajo_efectuado=0.0

#FUNCION
def termodinamica(calor,trabajo_efectuado):
    termodina=calor-trabajo_efectuado
    return termodina
#fin_def


#EJERCICIO 18
#FUNCION PARA HALLAR LA ENERGIA POTENCIAL GRAVITACIONAL

#DECLARACION DE VARIABLES
masa3=0
gravedad=0
altura3=0
#FUNCION
def energia_potencial(masa3,gravedad,altura):
    ener_pot=masa3*gravedad*altura
    return ener_pot
#fin_def


#EJERCICIO 19
#FUNCION PARA HALLAR LA DIVISION DE DOS VALORES
def division(valor03,valor04):
    return valor03/valor04


#EJERCICIO 20
#FUNCION PARA HALLAR LA FUERZA

#DECLARACION DE VARIABLES
masa1=0
aceleracion=0

#FUNCION
def fuerza(masa1,aceleracion):
    fuer=masa1*aceleracion
    return fuer
#fin_def


#EJERCICIO 21
#FUNCION PARA HALLAR EL POTENCIA

#DECLARACION DE VARIABLES
trabajo2=0
tiempo2=0

#FUNCION
def potencia(trabajo2,tiempo2):
    poten=trabajo2/tiempo2
    return poten
#fin_def


#EJERCICIO 22
#FUNCION PARA HALLAR LA VELOCIDAD TANGENCIAL
#DECLARACION DE VARIABLES
velocidad_angular=0.0
radio=0.0

#FUNCION QUE VALIDAD EL RADIO
def velocidad_tangencial(velocidad_angular,radio):
    radio_invalida=(radio<=0)
    while(radio_invalida==True):
        radio=int(input("VALOR DEL RADIO INVALIDAD:ingrese nuevamente el valor del radio correcta:"))
        radio_invalida=(radio<=0)
    #fin_while
    velo_tang=velocidad_angular*radio
    return velo_tang
#fin_def


#EJERCICIO 23
#FUNCION DE UNA CADENA EN MAYUSCULA LO CONVIERTE A MINUSCULA
#FUNCION
def convertir1(cadena0):
    conv2=cadena0.lower()
    return conv2
#fin_def


#EJERCICIO 24
#FUNCION PARA HALLAR LA PRECION HIDROSTATICA
#DECLARACION DE VARIABLES
densidad_del_liquido=0.0
gravedad=0.0
Altura=0.0

#FUNCION
def precion_hidrostatica(densidad_del_liquido,gravedad,Altura):
    pre_hidros=densidad_del_liquido*gravedad*Altura
    return pre_hidros
#fin_def


#EJERCICIO 25
#FUNCION PARA HALLAR LA DENSIDAD

#DECLARACION DE VARIABLES
masa=0
volumen=0

#FUNCION QUE VALIDAD EL VOLUMEN
def densidad(masa,volumen):
    volumen_invalido=(volumen <=0 or volumen >500)
    while(volumen_invalido == True):
        volumen=int(input("VOLUMEN INCORRECTA:ingrese nuevamente el volumen correcta:"))
        volumen_invalido=(volumen <=0 or volumen >500)
    #fin_while
    den=masa/volumen
    return den
#fin_def
