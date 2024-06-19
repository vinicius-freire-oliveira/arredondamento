def arredondamento_customizado(numero):
    # Separa a parte inteira e decimal do número
    parte_inteira, parte_decimal = str(numero).split('.')
    
    # Determina o número de casas decimais a serem utilizadas
    casas_decimais = 1
    
    # Se o algarismo posterior ao último de interesse for menor do que 5, o último algarismo de interesse não é alterado
    if len(parte_decimal) > casas_decimais and int(parte_decimal[casas_decimais]) < 5:
        return float(parte_inteira + '.' + parte_decimal[:casas_decimais]), casas_decimais
    # Se o algarismo posterior ao último de interesse for maior do que 5, acrescenta-se uma unidade ao último algarismo de interesse
    elif len(parte_decimal) > casas_decimais and int(parte_decimal[casas_decimais]) > 5:
        return float(parte_inteira + '.' + str(int(parte_decimal[:casas_decimais]) + 1)), casas_decimais
    # Se o algarismo posterior ao último de interesse for igual a 5, verifica os algarismos subsequentes
    elif len(parte_decimal) > casas_decimais and int(parte_decimal[casas_decimais]) == 5:
        if '5' == parte_decimal[casas_decimais:]:
            # Se 5 for o último algarismo ou se houver apenas zeros após o 5, o último algarismo de interesse é mantido se for par e aumentado em uma unidade se for ímpar
            if int(parte_decimal[casas_decimais - 1]) % 2 == 0 or any(digito != '0' for digito in parte_decimal[casas_decimais + 1:]):
                return float(parte_inteira + '.' + parte_decimal[:casas_decimais]), casas_decimais
            else:
                return float(parte_inteira + '.' + str(int(parte_decimal[:casas_decimais]) + 1)), casas_decimais
        # Se houver algum algarismo não nulo em qualquer casa decimal após o 5, acrescenta-se uma unidade ao último algarismo de interesse
        elif any(digito != '0' for digito in parte_decimal[casas_decimais + 1:]):
            return float(parte_inteira + '.' + str(int(parte_decimal[:casas_decimais]) + 1)), casas_decimais
        else:
            # Se houver apenas zeros após o 5, o último algarismo de interesse é mantido se for par e aumentado em uma unidade se for ímpar
            if int(parte_decimal[casas_decimais - 1]) % 2 == 0:
                return float(parte_inteira + '.' + parte_decimal[:casas_decimais]), casas_decimais
            else:
                return float(parte_inteira + '.' + str(int(parte_decimal[:casas_decimais]) + 1)), casas_decimais
    else:
        return float(parte_inteira + '.' + parte_decimal[:casas_decimais]), casas_decimais

# Exemplos de uso para uma casa decimal
numeros = [2.134, 35.182, 6.25003]
for numero in numeros:
    resultado, casas_decimais = arredondamento_customizado(numero)
    print(f'O arredondamento com uma casa decimal de {numero} é {resultado:.1f}')
