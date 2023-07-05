from main import digitos,obtener_prefijo,tipo_tarjeta,digitos_impares,digitos_pares,sumar_digitos,luhn,validar_tarjeta

class TestDigitos:
    def test_digitos_uno(self):
        numero = '570'
        digitos_reales = 3
        digitos_calculados = digitos(numero)
        assert digitos_reales == digitos_calculados,f'El número {numero} tiene {digitos_reales} dígitos, pero su función dio que tiene {digitos_calculados} dígitos.'

    def test_digitos_dos(self):
        numero = '4624748233249080'
        digitos_reales = 16
        digitos_calculados = digitos(numero)
        assert digitos_reales == digitos_calculados,f'El número {numero} tiene {digitos_reales} dígitos, pero su función dio que tiene {digitos_calculados} dígitos.'

class TestPrefijos:
    def test_prefijo_de_1_digito(self):
        number = '4624748233249080'
        prefix_size = 1
        expected_prefix = 4
        obtained_prefix = obtener_prefijo(number,prefix_size)
        assert type(obtained_prefix) == int, f'Obtener prefijo debe ser de tipo entero, no {type(obtained_prefix)}'
        assert expected_prefix == obtained_prefix, f'El prefijo de tamaño {prefix_size} de {number} es {expected_prefix}, pero la función dio {obtained_prefix}'

    def test_prefijo_de_2_digitos(self):
        number = '4624748233249080'
        prefix_size = 2
        expected_prefix = 46
        obtained_prefix = obtener_prefijo(number,prefix_size)
        assert type(obtained_prefix) == int, f'Obtener prefijo debe ser de tipo entero, no {type(obtained_prefix)}'
        assert expected_prefix == obtained_prefix, f'El prefijo de tamaño {prefix_size} de {number} es {expected_prefix}, pero la función dio {obtained_prefix}'

    def test_prefijo_de_3_digitos(self):
        number = '4624748233249080'
        prefix_size = 3
        expected_prefix = 462
        obtained_prefix = obtener_prefijo(number,prefix_size)
        assert type(obtained_prefix) == int, f'Obtener prefijo debe ser de tipo entero, no {type(obtained_prefix)}'
        assert expected_prefix == obtained_prefix, f'El prefijo de tamaño {prefix_size} de {number} es {expected_prefix}, pero la función dio {obtained_prefix}'

class TestTarjetas:
  
  class TestAmex:
    
    def test_American_Express_Prefijo_34(self):
        card = '342474823324908'
        expected_card_type = 'American Express'
        obtained_card_type = tipo_tarjeta(card)
        assert expected_card_type == obtained_card_type,f'La tarjeta {card} es {expected_card_type}, pero la función dio {obtained_card_type}'

    def test_American_Express_Prefijo_37(self):
        card = '372474823324908'
        expected_card_type = 'American Express'
        obtained_card_type = tipo_tarjeta(card)
        assert expected_card_type == obtained_card_type,f'La tarjeta {card} es {expected_card_type}, pero la función dio {obtained_card_type}'

    def test_American_Express_Digitos_14_prefijo_correcto(self):
        card = '34247482332490'
        expected_card_type = 'American Express'
        obtained_card_type = tipo_tarjeta(card)
        assert obtained_card_type != None, 'Cuando una tarjeta es inválida debe devolver el string Invalid, no None'
        assert expected_card_type != obtained_card_type,f'La tarjeta {card} no es {expected_card_type} ya que tiene 14 dígitos'

    def test_American_Express_Digitos_12_prefijo_correcto(self):
        card = '342474823324'
        expected_card_type = 'American Express'
        obtained_card_type = tipo_tarjeta(card)
        assert obtained_card_type != None, 'Cuando una tarjeta es inválida debe devolver el string Invalid, no None'
        assert expected_card_type != obtained_card_type,f'La tarjeta {card} no es {expected_card_type} ya que tiene 12 dígitos'

    def test_American_Express_Digitos_17_prefijo_correcto(self):
        card = '34247482332490123'
        expected_card_type = 'American Express'
        obtained_card_type = tipo_tarjeta(card)
        assert obtained_card_type != None, 'Cuando una tarjeta es inválida debe devolver el string Invalid, no None'
        assert expected_card_type != obtained_card_type,f'La tarjeta {card} no es {expected_card_type} ya que tiene 17 dígitos'

    def test_American_Express_Digitos_prefijo_incorrecto(self):
        card = '362474823324908'
        expected_card_type = 'American Express'
        obtained_card_type = tipo_tarjeta(card)
        assert obtained_card_type != None, 'Cuando una tarjeta es inválida debe devolver el string Invalid, no None'
        assert expected_card_type != obtained_card_type,f'La tarjeta {card} no es {expected_card_type} ya que tiene 15 dígitos pero el prefijo es incorrecto'
  
  class TestVisa:

    def test_Visa_Prefijo(self):
        card = '4424748233249080'
        expected_card_type = 'Visa'
        obtained_card_type = tipo_tarjeta(card)
        assert expected_card_type == obtained_card_type,f'La tarjeta {card} es {expected_card_type}, pero la función dio {obtained_card_type}'

    def test_Visa_16_Digitos(self):
        card = '4424748233249080'
        expected_card_type = 'Visa'
        obtained_card_type = tipo_tarjeta(card)
        assert expected_card_type == obtained_card_type,f'La tarjeta {card} es {expected_card_type}, pero la función dio {obtained_card_type}'

    def test_Visa_13_Digitos(self):
        card = '4424748233249'
        expected_card_type = 'Visa'
        obtained_card_type = tipo_tarjeta(card)
        assert expected_card_type == obtained_card_type,f'La tarjeta {card} es {expected_card_type}, pero la función dio {obtained_card_type}'

    def test_Visa_Digitos_Incorrectos_14(self):
        card = '44247482332490'
        expected_card_type = 'Visa'
        obtained_card_type = tipo_tarjeta(card)
        assert obtained_card_type != None, 'Cuando una tarjeta es inválida debe devolver el string Invalid, no None'
        assert expected_card_type != obtained_card_type,f'La tarjeta {card} no es {expected_card_type} ya que tiene 14 dígitos'

    def test_Visa_Digitos_Incorrectos_17(self):
        card = '44247482332490111'
        expected_card_type = 'Visa'
        obtained_card_type = tipo_tarjeta(card)
        assert obtained_card_type != None, 'Cuando una tarjeta es inválida debe devolver el string Invalid, no None'
        assert expected_card_type != obtained_card_type,f'La tarjeta {card} no es {expected_card_type} ya que tiene 17 dígitos'

    def test_Visa_Digitos_Incorrectos_12(self):
        card = '442474823324'
        expected_card_type = 'Visa'
        obtained_card_type = tipo_tarjeta(card)
        assert obtained_card_type != None, 'Cuando una tarjeta es inválida debe devolver el string Invalid, no None'
        assert expected_card_type != obtained_card_type,f'La tarjeta {card} no es {expected_card_type} ya que tiene 12 dígitos'
  
  class TestMastercard:
    
    def test_Mastercard_Prefijo(self):
        card = '5124748233249080'
        expected_card_type = 'Mastercard'
        obtained_card_type = ''
        for digit in range(1,6):
            card = card[0] + str(digit) + card[2:]
            obtained_card_type = tipo_tarjeta(card)
            assert expected_card_type == obtained_card_type,f'La tarjeta {card} es {expected_card_type}, pero la función dio {obtained_card_type}'

    def test_Mastercard_Prefijo_Invalido(self):
        card = '5124748233249080'
        expected_card_type = 'Mastercard'
        obtained_card_type = ''
        for digit in [0,6]:
            card = card[0] + str(digit) + card[2:]
            obtained_card_type = tipo_tarjeta(card)
            assert obtained_card_type != None, 'Cuando una tarjeta es inválida debe devolver el string Invalid, no None'
            assert expected_card_type != obtained_card_type,f'La tarjeta {card} NO es {expected_card_type}, pero la función dio {obtained_card_type}. ¡Guarda el prefijo!'

    def test_Mastercard_Longitud_Invalida_Menor(self):
        card = '512474823324908'
        expected_card_type = 'Mastercard'
        obtained_card_type = tipo_tarjeta(card)
        assert obtained_card_type != None, 'Cuando una tarjeta es inválida debe devolver el string Invalid, no None'
        assert expected_card_type != obtained_card_type,f'La tarjeta {card} NO es {expected_card_type}, y la función dio {obtained_card_type}. ¡Guarda los digitos!'

    def test_Mastercard_Longitud_Invalida_Mayor(self):
        card = '51247482332490800'
        expected_card_type = 'Mastercard'
        obtained_card_type = tipo_tarjeta(card)
        assert obtained_card_type != None, 'Cuando una tarjeta es inválida debe devolver el string Invalid, no None'
        assert expected_card_type != obtained_card_type,f'La tarjeta {card} NO es {expected_card_type}, y la función dio {obtained_card_type}. ¡Guarda los digitos!'
  
  class TestInvalidas:
    
    def test_tarjetas_invalidas(self):
        card = '4424'
        expected_card_type = 'Invalid'
        obtained_card_type = tipo_tarjeta(card)
        assert expected_card_type == obtained_card_type,f'La tarjeta {card} es {expected_card_type}, pero la función dio {obtained_card_type}'

class TestDigitosImpares:
    
    def test_digitos_impares_1_digito(self):
        number = '1'
        expected_digits = [1]
        obtained_digits = digitos_impares(number)
        assert type(obtained_digits) == list,f'La función debe devolver una lista, no {type(obtained_digits)}'
        for element in obtained_digits:
            assert type(element) == int,'La lista devuelta debe contener solo números enteros'
        assert expected_digits == sorted(obtained_digits),f'Los digitos impares de {number} son {expected_digits}, pero la función devolvió {obtained_digits}'

    def test_digitos_impares_5_digitos(self):
        number = '12846'
        expected_digits = [1,6,8]
        obtained_digits = digitos_impares(number)
        assert type(obtained_digits) == list,f'La función debe devolver una lista, no {type(obtained_digits)}'
        for element in obtained_digits:
            assert type(element) == int,'La lista devuelta debe contener solo números enteros'
        assert expected_digits == sorted(obtained_digits),f'Los digitos impares de {number} son {expected_digits}, pero la función devolvió {obtained_digits}'

    def test_digitos_impares_6_digitos(self):
        number = '128469'
        expected_digits = [2,4,9]
        obtained_digits = digitos_impares(number)
        assert type(obtained_digits) == list,f'La función debe devolver una lista, no {type(obtained_digits)}'
        for element in obtained_digits:
            assert type(element) == int,'La lista devuelta debe contener solo números enteros'
        assert expected_digits == sorted(obtained_digits),f'Los digitos impares de {number} son {expected_digits}, pero la función devolvió {obtained_digits}'

class TestDigitosPares:
    
    def test_digitos_pares_1_digito(self):
        number = '1'
        expected_digits = []
        obtained_digits = digitos_pares(number)
        assert type(obtained_digits) == list,f'La función debe devolver una lista, no {type(obtained_digits)}'
        for element in obtained_digits:
            assert type(element) == int,'La lista devuelta debe contener solo números enteros'
        assert expected_digits == sorted(obtained_digits),f'Los digitos pares de {number} son {expected_digits}, pero la función devolvió {obtained_digits}'

    def test_digitos_pares_5_digitos(self):
        number = '12846'
        expected_digits = [2,4]
        obtained_digits = digitos_pares(number)
        assert type(obtained_digits) == list,f'La función debe devolver una lista, no {type(obtained_digits)}'
        for element in obtained_digits:
            assert type(element) == int,'La lista devuelta debe contener solo números enteros'
        assert expected_digits == sorted(obtained_digits),f'Los digitos impares de {number} son {expected_digits}, pero la función devolvió {obtained_digits}'

    def test_digitos_pares_6_digitos(self):
        number = '128469'
        expected_digits = [1,6,8]
        obtained_digits = digitos_pares(number)
        assert type(obtained_digits) == list,f'La función debe devolver una lista, no {type(obtained_digits)}'
        for element in obtained_digits:
            assert type(element) == int,'La lista devuelta debe contener solo números enteros'
        assert expected_digits == sorted(obtained_digits),f'Los digitos impares de {number} son {expected_digits}, pero la función devolvió {obtained_digits}'

class TestSumaDigitos:

    def test_suma_digitos_1_digito(self):
        digit_list = [1,6,8,0,5]
        expected_sum = sum(digit_list)
        obtained_sum = sumar_digitos(digit_list)
        assert type(obtained_sum) == int, 'La función debe dar un número entero como resultado'
        assert expected_sum == obtained_sum,f'La suma de dígitos de {digit_list} es {expected_sum}, pero la función dio {obtained_sum}'

    def test_suma_digitos_multiples_digitos(self):
        digit_list = [14,6,805,6023,51]
        expected_sum = 41
        obtained_sum = sumar_digitos(digit_list)
        assert type(obtained_sum) == int, 'La función debe dar un número entero como resultado'
        assert expected_sum == obtained_sum,f'La suma de dígitos de {digit_list} es {expected_sum}, pero la función dio {obtained_sum}'

class TestLuhn:
    def test_luhn_sin_multiplicar_valida(self):
        number = str(809050701)
        expected_result = True
        obtained_result = luhn(number)
        assert type(obtained_result) == bool,f'El Algoritmo de Luhn debe devolver True o False, no {obtained_result}'
        assert expected_result == obtained_result,f'La tarjeta {number} es {"válida" if expected_result else "inválida"}, pero luhn dio que es {"válida" if obtained_result else "inválida"}.'
    
    def test_luhn_sin_multiplicar_invalida(self):
        number = str(809060701)
        expected_result = False
        obtained_result = luhn(number)
        assert type(obtained_result) == bool,f'El Algoritmo de Luhn debe devolver True o False, no {obtained_result}'
        assert expected_result == obtained_result,f'La tarjeta {number} es {"válida" if expected_result else "inválida"}, pero luhn dio que es {"válida" if obtained_result else "inválida"}.'

    def test_luhn_multiplicando_1digito_valida(self):
        number = str(809450711)
        expected_result = True
        obtained_result = luhn(number)
        assert type(obtained_result) == bool,f'El Algoritmo de Luhn debe devolver True o False, no {obtained_result}'
        assert expected_result == obtained_result,f'La tarjeta {number} es {"válida" if expected_result else "inválida"}, pero luhn dio que es {"válida" if obtained_result else "inválida"}.'

    def test_luhn_multiplicando_1digito_invalida(self):
        number = str(809470721)
        expected_result = False
        obtained_result = luhn(number)
        assert type(obtained_result) == bool,f'El Algoritmo de Luhn debe devolver True o False, no {obtained_result}'
        assert expected_result == obtained_result,f'La tarjeta {number} es {"válida" if expected_result else "inválida"}, pero luhn dio que es {"válida" if obtained_result else "inválida"}.'
    
    def test_luhn_multiplicando_2digitos_valida(self):
        number = str(889456711)
        expected_result = True
        obtained_result = luhn(number)
        assert type(obtained_result) == bool,f'El Algoritmo de Luhn debe devolver True o False, no {obtained_result}'
        assert expected_result == obtained_result,f'La tarjeta {number} es {"válida" if expected_result else "inválida"}, pero luhn dio que es {"válida" if obtained_result else "inválida"}.'

    def test_luhn_multiplicando_2digitos_invalida(self):
        number = str(889456721)
        expected_result = False
        obtained_result = luhn(number)
        assert type(obtained_result) == bool,f'El Algoritmo de Luhn debe devolver True o False, no {obtained_result}'
        assert expected_result == obtained_result,f'La tarjeta {number} es {"válida" if expected_result else "inválida"}, pero luhn dio que es {"válida" if obtained_result else "inválida"}.'

class TestValidar:
    def test_invalida_compania_invalida_luhn(self):
        number = str(56)
        expected_result = False
        obtained_result = validar_tarjeta(number)
        assert type(obtained_result) == bool,f'La validación de tarjetas debe devolver True o False, no {obtained_result}'
        assert expected_result == obtained_result,f'La tarjeta {number} es {"válida" if expected_result else "inválida"}, pero la función dio que es {"válida" if obtained_result else "inválida"}.'

    def test_valida_compania_invalida_luhn(self):
        number = str(4624748233249080)
        expected_result = False
        obtained_result = validar_tarjeta(number)
        assert type(obtained_result) == bool,f'La validación de tarjetas debe devolver True o False, no {obtained_result}'
        assert expected_result == obtained_result,f'La tarjeta {number} es {"válida" if expected_result else "inválida"}, pero la función dio que es {"válida" if obtained_result else "inválida"}.'

    def test_invalida_compania_valida_luhn(self):
        number = str(889456711)
        expected_result = False
        obtained_result = validar_tarjeta(number)
        assert type(obtained_result) == bool,f'La validación de tarjetas debe devolver True o False, no {obtained_result}'
        assert expected_result == obtained_result,f'La tarjeta {number} es {"válida" if expected_result else "inválida"}, pero la función dio que es {"válida" if obtained_result else "inválida"}.'

    def test_valida_compania_valida_luhn(self):
        number = str(4624748233249582)
        expected_result = True
        obtained_result = validar_tarjeta(number)
        assert type(obtained_result) == bool,f'La validación de tarjetas debe devolver True o False, no {obtained_result}'
        assert expected_result == obtained_result,f'La tarjeta {number} es {"válida" if expected_result else "inválida"}, pero la función dio que es {"válida" if obtained_result else "inválida"}.'