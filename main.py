#Ejercicio 1
from re import S


def digitos(numero_de_tarjeta: str) -> int:
    return len(numero_de_tarjeta)

#Ejercicio 2
def obtener_prefijo(numero_de_tarjeta: str,tamaño_prefijo: int) -> int:
    return int(numero_de_tarjeta[:tamaño_prefijo])

#Ejercicio 3
def tipo_tarjeta(numero_de_tarjeta: str) -> str:
    condicion_amex   = bool ((obtener_prefijo(numero_de_tarjeta, 2) == 34 or obtener_prefijo(numero_de_tarjeta, 2) == 37) and digitos(numero_de_tarjeta) == 15)
    condicion_master = bool (obtener_prefijo(numero_de_tarjeta,2) >= 51 and obtener_prefijo(numero_de_tarjeta, 2)<= 55 and digitos(numero_de_tarjeta) == 16)
    condicion_visa   = bool(obtener_prefijo(numero_de_tarjeta,1) == 4 and (digitos(numero_de_tarjeta) == 13 or digitos(numero_de_tarjeta) == 16))
    if condicion_master:
        return 'Mastercard'
    elif condicion_visa:
        return 'Visa'
    elif condicion_amex:
        return 'American Express'
    else:
        return 'Invalid'

#Ejercicio 4
def digitos_impares(numero_de_tarjeta : str) -> list[int]:
    pos_impares = []
    for i in range (len(numero_de_tarjeta)):
        if (((i+1) % 2) != 0): 
            pos_impares.append(int(numero_de_tarjeta[len(numero_de_tarjeta)-1-i]))
    return  pos_impares

#Ejercicio 5
def digitos_pares(numero_de_tarjeta: str) -> list[int]:
    pos_pares = []
    for i in range (len(numero_de_tarjeta)):
        if (((i+1) % 2) == 0): 
            pos_pares.append(int(numero_de_tarjeta[len(numero_de_tarjeta)-1-i]))
    return  pos_pares   

#Ejercicio 6
def sumar_digitos(lista_digitos : list[int]) -> int:
    suma = 0
    for numero in lista_digitos:
        numero_str = str(numero) 
        for digito in numero_str:
            suma += int(digito) 

            
    return suma


#Ejercicio 7
def luhn(numero_de_tarjeta :  str) -> bool:

    def pordos(mult):
        return mult *2
    lista_de_pares = digitos_pares(numero_de_tarjeta)
    multi = map (pordos,lista_de_pares)

    sumauno = sumar_digitos (multi) #3
    numcuatro = digitos_impares (numero_de_tarjeta) #4
    s =  sumar_digitos (numcuatro)


    cinco = s + sumauno 
    
    

    if ((cinco) %10) == 0:

        bool = True

    else: 

        bool = False
    return bool
    



   





    
    return

#Ejercicio 8
def validar_tarjeta(numero_de_tarjeta : str) -> bool:
    return 