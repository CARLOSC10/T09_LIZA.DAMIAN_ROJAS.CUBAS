#EJERCICIO 1
#crear una función para calcular area del triangulo equilátero
lado=0.0 #declarar variable
def area_del_triangulo(lado):
    lado_invalido=(lado<=0)
    while(lado_invalido==True):
        print("lado incorrecto")
        lado=float(input("ingrese lado:"))
        lado_invalido=(lado<=0)
    #fin_while
    area=((lado**2)*(3**(1/2)))/4
    return area
#fin_def

#EJERCICIO 2
#crear una función para pedir la edad de una persona
edad=0 #declarar  variable
def pedir_edad(edad):
    edad_invalida=(edad<0 or edad>120)
    while(edad_invalida==True):
        print("edad invalida")
        edad=int(input("ingrese edad:"))
        edad_invalida=(edad<=0 or edad>120)
    #fin_while
    return edad

#fin_for

#EJERCICIO 3
#crear una funcion que pida un numero entero si el  numero entero  pertenece al intervalo cerrado dado [a,b] si el numero no pertenece al intervalo pedir el numero
numero_entero,a,b=0,0,0
def pedir_numero_entero(numero_entero,a,b):
    interbalo_incorrecto=(a>b or a==b)                           #verificar intervalo [a,b], mientars :"a > b" o "a==b" es un intervalo incorrecto ,pedir el valor de a
    while(interbalo_incorrecto==True):
        print("el intervalo es incorrecto, \"[a,b]\", ingrese \"a < b\" y \"a!=b\" ")
        a=int(input("ingrese a:"))
        interbalo_incorrecto=(a>b or a==b)
    #fin_while
    #verificar si el numero entero pertenece al intervalo cerrado [a,b]
    numero_imperteneciente=(((numero_entero!=a or numero_entero!=b) and (numero_entero<a or numero_entero>b)))
    while(numero_imperteneciente==True):
        print("Numero Imperteneciente")
        numero_entero=int(input("ingrese numero:"))
        numero_imperteneciente=(((numero_entero!=a or numero_entero!=b) and (numero_entero<a or numero_entero>b)))
    #fin_while
    return numero_entero,a,b
#fin_for

#EJERCICIO 4
#crear una funcion que valide el numero del dni
nro_dni=""    #declarar variable
def validar_dni(nro_dni):
    if(isinstance(nro_dni,str)):     #comprueba si nro_dni es una cadena
        if(len(nro_dni)==8):         #si la longitud del valor de nro_dni es igual 8 hacer:
            for c in nro_dni:              #iterar nro_dni
                if c.isdigit()==False:     #se comprueba si c es un caracter de numero
                    return False
            return True
        else:
            return False
    else:
        return False
#fin_def
#EJERCICIO 5
#crear una funcion que valide el nombre de una persona
nombre=""
def validar_nombre(nombre):
    if(isinstance(nombre,str)):
        if(len(nombre)>=3):
            for item in nombre:
                if(item.isalpha()==False and item.isspace()==False):
                    return False
                #fin_if
            return True
            #fin_for
        else:
            return False
        #fin_if
    else:
        return False
    #fin_if
#fin_def

#EJERCICIO 6
#crear una funcion que calcule el promedio de 3 notas y saber su condicion
nota1,nota2,nota3,calculo=0.0,0.0,0.0,0.0
def promedio(nota1,nota2,nota3):
    calculo=(nota1+nota2+nota3)/3
    if(calculo>=10.5 or calculo<=20.0):
        return "APROBADO"
    if(calculo<10.5 or calculo>=0.0):
        return "DESAPROBADO"
#fin_def

#EJERCICIO 7
#crear una funcion que valide un nro telefonico de 9 digitos
nro_telefono=""
def numero_telefono_valido(nro_telefono):
    if(isinstance(nro_telefono,str)):
        if(len(nro_telefono)==9):
            for i in nro_telefono:
                if(i.isdigit()==False):
                    return False
                #fin_if
            return True
            #fin_for
        #fin_if
        else:
            return False
        #fin_if
    else:
        return False
    #fin_if
#fin_def

#EJERCICIO 8
#crear una funcion que pida un numero entero y retorne el numero entero positivo
nro_entero,numero_entero_invalido=0,False
def pedir_entero(nro_entero):
    nro_entero_invalido=nro_entero<=0
    while(nro_entero_invalido==True):
        print("error numero entero no es positivo")
        nro_entero=int(input("ingrese numero entero positivo: "))
        nro_entero_invalido=nro_entero<=0
     #fin_while
    return nro_entero
#fin_def
#EJERCICIO 9
#crear una funcion que pida el sexo de una persona ,si es incorrecto pedir nuevamente
sexo,sexo_invalido="",False
def pedir_sexo(sexo):
    sexo=sexo.upper()
    sexo_invalido=(sexo!="HOMBRE" and sexo!="MUJER")
    while(sexo_invalido==True):
        print("SEXO INVÁLIDO")
        sexo=input("ingrese sexo:")
        sexo=sexo.upper()
        sexo_invalido=(sexo!="HOMBRE" and sexo!="MUJER")
    #fin_while
    return sexo
#fin_def

#EJERCICIO 10
#crear una funcion que calcule el igv
precio,calculando=0.0,0.0
def IGV(precio):
    calculando=precio*0.18
    return calculando
#fin_def

#EJERCICIO 11
#crear una funcion(procedimiento) que imprima la boleta de una tienda
def mostrar_boleta(nombre_cliente,DNI,precio):
    print("###############################################")
    print("#               BOTICAS PERU                  #")
    print("###############################################")
    print("#CLIENTE:"+nombre_cliente)
    print("#DNI:"+str(DNI))
    print("#PRECIO:"+str(precio))
    print("##############################################3")

#EJERCICIO 12
#crear una funcion que calcule la velocidad inicial en (M.R.U.V)
velocidad_inicial,distancia,tiempo,aceleracion=0.0,0.0,0.0,0.0
def calcular_velocidad(distancia,tiempo,aceleracion):
    velocidad_inicial=(distancia-((1/2)*aceleracion*(tiempo**2)))/tiempo
    return velocidad_inicial
#fin_def

#EJEJRCICIO 13
#crear una funcion que calcule la cantidad de usb de 16GB en una cantidad de espacio dada
cantidad_usb,espacio_dado=0,0.0
def cantidad(espacio_dado):
    cantidad_usb=espacio_dado/16
    return cantidad_usb
#fin_def

#EJERCICIO 14
#crear una funcion que imprima un dia de la semana dado si el dia no es correcto pedir denuevo
dia,verificador_del_dia="",False
def pedir_dia(dia):
    dia=dia.upper()
    verificador_de_dia=(dia!="LUNES" and dia!="MARTES" and dia!="MIERCOLES" and dia!="JUEVES" and dia!="VIERNES" and dia!="SABADO" and dia!="DOMINGO")
    while(verificador_de_dia==True):
        print("DIA INVALIDO")
        dia=input("ingrse dia:")
        dia=dia.upper()
        verificador_de_dia=(dia!="LUNES" and dia!="MARTES" and dia!="MIERCOLES" and dia!="JUEVES" and dia!="VIERNES" and dia!="SABADO" and dia!="DOMINGO")
    #fin_while
    return dia
#fin_def

#EJERCICIO 15
#crear un programa que calcule el valor absoluto de un numero
numero,valor_absoluto=0.0,0.0
def ABSOLUTO(numero):
    valor_absoluto=abs(numero)
    return valor_absoluto
#Fin_def

#EJERCICIO 16
#crear una funcion para validar un codigo de 7 digitos alfanumerico
codigo=""
def validar_codigo(codigo):
    if(isinstance,str):
        if(len(codigo)==7):
            for caracter in codigo:
                if(caracter.isalnum()==False):
                    return False
            return True
            #fin_for
        else:
            return False
        #fin_if
    else:
        return False
    #fin_if
#fin_def

#EJERCICIO 17
#crear una funcion(PROCEDIMIENTO) que imprima un tiket de juegos si gasto mas de S/100.0 mostar biembenido al sorteo si no garcias por venir
cliente,gasto,msg="",0.0,""
def mostrar_tiket(cliente,gasto):
    if(gasto>=100.0):
        msg="BIEMBENIDO AL SORTEO"
    else:
        msg="GRACIAS POR VENIR"
    #fin_if
    print("#############################################")
    print("#                 TIKECT                    #")
    print("#############################################")
    print("#NOMBRE:",cliente)
    print("#GASTO:",gasto)
    print("#"+msg)
    print("#############################################")
#fin_def

#EJERCICIO 18
#crear una funcion que calcula el araea del rombo}
area,diag_menor,diag_mayor=0.0,0.0,0.0
def area_rombo(diag_menor,diag_mayor):
    area=(diag_menor*diag_mayor)/2
    return area
#fin_def

#EJERCICIO 19
#crear una funcion que calcule la densidad de una sustancia
densidad,volumen,masa=0.0,0.0,0.0
def calcular(volumen,masa):
    densidad=masa/volumen
    return densidad
#fin_def

#EJERCICIO 20
#crear una funcion que calcule la presion de un cuerpo
presion,area,fuerza=0.0,0.0,0.0
def CALCULAR_P(area,fuerza):
    presion=fuerza/area
    return presion
#fin_def

#EJERCICIO 21
#crear una funcion que realize el calculo de potencia de un motor
potencia,trabajo,tiempo=0.0,0.0,0.0
def CAL_POTENCIA(trabajo,tiempo):
    potencia=trabajo/tiempo
    return potencia
#fin_def

#EJERCICIO 22
#crear una funcion que compare dos numeros
a,b,comparar=0.0,0.0,0.0
def comparacion(a,b):
    if(a<b):
        return "a ES MENOR QUE b"
    else:
        return "a ES MAYOR QUE b"
    return msg
    #fin_if
#fin_def
#EJERCICIO 23
#crear una funcion que calcule arae de un hexagono regular
lado,area=0.0,0.0
def AREA_HEX(lado):
    area=6((lado**2)*(3**(1/2)))/4
    return area
#fin_def

#EJERCICIO 24
#crear una funcion(procedimiento) que imprima un recibo de lus
cliente,total_pagar,consumo_energia="",0.0,0.0
def MOSTRAR_RECIBO(cliente,total_pagar,consumo_energia):
    print("#############################################")
    print("#               RECIBO DE LUS               #")
    print("#############################################")
    print("#CLIENTE:",cliente)
    print("#TOTAL A PAGAR:",total_pagar)
    print("#CONSUMO DE ENERGIA:",consumo_energia,"KW/h")
    print("#############################################")

#EJERCICIO 25
#crear una funcion que valide una clave que solo contenga letras y una cantidad de 10 caracteres
clave=""
def validar_clave(clave):
    if(isinstance(clave,str)):
        if(len(clave)==10):
            for c in clave:
                if(c.isalpha()==False):
                    return False
                #fin_if
            return True
            #fin_for
        else:
            return False
        #fin_if
    else:
        return False
    #fin_if
#fin_for
