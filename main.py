#Ejercicio 1
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
    return

#Ejercicio 7
def luhn(numero_de_tarjeta :  str) -> bool:
    return

#Ejercicio 8
def validar_tarjeta(numero_de_tarjeta : str) -> bool:
    return 