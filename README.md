# Sherock II: Electric Boogaloo

## Introducción
¡La búsqueda continúa! Sherlock obtuvo el programa correcto, pero no le sirvió para validar su tarjeta de crédito. Además de los prefijos, se debe aplicar el algoritmo de luhn, que se asegura que no haya errores de tipeo en la tarjeta. Entonces, les encargó a ustedes, desarrolladores, que armen el programa para verificar tarjetas, pero esta vez en python.

## Explicación
Esta sección está para que entiendan el objetivo, pero el trabajo es más guiado. Pueden ir directo a consigna y volver a esta sección a medida que necesiten.

La validación de tarjetas de crédito se hace en dos pasos:

1. Validar que la tarjeta sea de algún emisor válido, sea Visa, Mastercard, etc.

2. Verificar validez mediante el algoritmo de Luhn.

A continuación detallo este proceso. Para más información, pueden ir a https://www.ibm.com/docs/en/order-management-sw/9.3.0?topic=cpms-handling-credit-cards.

### Validación del tipo de tarjeta

La tarjeta es de un tipo válido si el prefijo y longitud cumplen con alguna de las compañías que las emiten. A continuación está la tabla de empresas y sus prefijos y longitudes asociadas.

| Tipo de Tarjeta | Prefijo | Digitos |
|---|---|---|
| American Express | 34 ó 37 | 15 |
| Mastercard | 51 a 55 inclusive | 16 |
| Visa | 4 | 13 ó 16 |
| Diners Club y Carte Blanche | 36 ó 38, o 300 a 305 inclusive | 14 |
| Discover | 6011 | 16 |
| JCB | 2123 ó 1800 | 15 |
| JCB | 3 | 16 |


### Algoritmo de Luhn

Luhn es un algoritmo sencillo para chequear si el número de tarjeta es válido. No es tanto una medida de seguridad para evitar fraude, sino más bien es para detectar errores de tipeo o de errores en el envío de datos.
Funciona de la siguiente manera:

1. Se toman todos los dígitos pares de un número de tarjeta.
2. Se multiplican estos dígitos por 2.
3. Se suman todos los dígitos del resultado del ítem 2.
4. Se toman todos los dígitos impares del número de tarjeta.
5. Se suman estos dígitos al resultado del ítem 3.
6. Se toma el resto de dividir a esta suma por 10 (suma % 10). Si este resto final es 0, la tarjeta es válida, si no, no lo es.

**EJEMPLO**
Supongamos que tengo el número de tarjeta: 4624 7482 3324 9080.

1. Tomo los dígitos pares: **4**6**2**4 **7**4**8**2 **3**3**2**4 **9**0**8**0.
2. Los multiplico por 2:
```
4 × 2 = 8
2 × 2 = 4
7 × 2 = 14
8 × 2 = 16
3 × 2 = 6
2 × 2 = 4
9 × 2 = 18
8 × 2 = 16
```
3. Sumo los dígitos obtenidos: 8 + 4 + 1 + 4 + 1 + 6 + 6 + 4 + 1 + 8 + 1 + 6 = 50.
4. Tomo los dígitos impares: 4**6**2**4** 7**4**8**2** 3**3**2**4** 9**0**8**0**
5. Sumo los dígitos: 6 + 4 + 4 + 2 + 3 + 4 + 0 + 0 = 23. Luego, lo sumo al resultado del ítem 3: 50 + 23 = 73.
6. Tomo resto de dividir por 10: 73 %10 = 3

Como el resto NO es 0, entonces este número de tarjeta es inválido.

## Consigna
Para hacer el ejercicio deben bajar los archivos del campus. Ustedes solo van a completar el archivo main.py, los otros archivos son para que corran los tests. Los tests se corren escribiendo ``python -m pytest test_tarjeta.py`` en la consola. Recuerden que la consola debe estar abierta en el lugar donde se encuentran los archivos, si no tienen que especificar la ruta al escribir el nombre del archivo. También se pueden correr para cada ejercicio parcialmente, y cómo se hace esto está aclarado en cada ejercicio.

1. Completar la función ``digitos``, que dado un string que contiene solo dígitos me indique cuántos dígitos hay.
**¡TESTEEN!** Corran los tests con ``python -m pytest test_tarjeta.py::TestDigitos``.

2. Completar ``obtener_prefijo``, que dado un string que contiene solo dígitos y un número n, de los primeros n dígitos de dicho string en forma de entero. Pueden asumir que n no es mayor a la longitud del string pasado por parámetro.
**¡TESTEEN!** Corran los tests con ``python -m pytest test_tarjeta.py::TestPrefijos``.

3. Completar la función ``tipo_tarjeta``, que dado un numero de tarjeta (un string que contiene solo dígitos) valida si es una tarjeta Mastercard, Visa, American Express o es inválida. Para esto, debe devolver el string Mastercard, American Express, Visa o Invalid. Deben usar las funciones de los ítems anteriores. Pueden usar el esqueleto propuesto o borrarlo y empezar de cero si les resulta confuso. Traten de que haya un único if por compañía bancaria, pero no es obligatorio. A continuación la parte relevante de la tabla:

| Tipo de Tarjeta | Prefijo | Dígitos |
|---|---|---|
| American Express | 34 ó 37 | 15 |
| Mastercard | 51 a 55 inclusive | 16 |
| Visa | 4 | 13 ó 16|

**¡TESTEEN!** Corran los tests con ``python -m pytest test_tarjeta.py::TestTarjetas``. También pueden correrlos para cada empresa individualmente (son los mismos pero separados) con:

```python -m pytest test_tarjeta.py::TestTarjetas::TestAmex```

```python -m pytest test_tarjeta.py::TestTarjetas::TestVisa```

```python -m pytest test_tarjeta.py::TestTarjetas::TestMastercard```

```python -m pytest test_tarjeta.py::TestTarjetas::TestInvalidas```

4. Completar ``digitos_impares``, que dado un número de tarjeta (un string que contiene solo dígitos), devuelva la lista de los dígitos en posiciones impares. Las posiciones se cuentan de atrás para adelante, es decir, en el número 459, el 9 sería la primera posición, el 5 la segunda y el 4 la tercera. Ejemplo: Si el número de tarjeta es 45623, la función debe devolver ``[4,6,3]``. Si el número de tarjeta es 456231, la función debe devolver ``[5,2,1]`` (pueden variar el orden, lo importante es que est ́en los correctos). **TIP**: Tal vez recorrer de atrás para adelante tenga más sentido...
**¡TESTEEN!** Corran los tests con ``python -m pytest test_tarjeta.py::TestDigitosImpares``.

5. Completar ``digitos_pares``, que dado un número de tarjeta (un string que contiene solo dígitos), devuelva la lista de dígitos en posiciones pares contadas de atrás hacia adelante, de forma análoga al item anterior (pueden variar el orden, lo importante es que estén los correctos).
**¡TESTEEN!** Corran los tests con ``python -m pytest test_tarjeta.py::TestDigitosPares``.

6. Completar ``sumar_digitos``, que dada una lista de números, devuelva la suma de los dígitos de todos los números. Ejemplo: Si los números son ``[16,3,456]``, la función debe devolver 25 ya que 1+6+3+4+5+6 = 25. **TIP**: Puede que les sirva reconvertir los números a string para “extraer” los dígitos.
**¡TESTEEN!** Corran los tests con ``python -m pytest test_tarjeta.py::TestSumaDigitos``.

7. Completar la función ``luhn`` que aplica el Algoritmo de Luhn a un número de tarjeta (un string que contiene solo d ígitos) y devuelva True o False (los valores booleanos, no texto) si la tarjeta es válida on no para Luhn. El algoritmo es el que está en la explicación de la sección anterior. Es esperado que usen las funciones de los ítems 4, 5 y 6.
**¡TESTEEN!** Corran los tests con ``python -m pytest test_tarjeta.py::TestLuhn``.

8. Finalmente, completar la función validar tarjeta dado un número de tarjeta (un string que contiene solo dígitos), devuelva True o False (los valores booleanos, no texto) si la tarjeta es válida o no. Es esperado que usen las funciones de los items 3 y 7.
**¡TESTEEN!** Corran los tests con ``python -m pytest test_tarjeta.py::TestValidar``.
