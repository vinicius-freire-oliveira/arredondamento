num = float(input('Numero original: '))

# Verifica se o número é inteiro ou decimal
if num == round(num):  # Se o número é igual ao seu arredondamento, então é inteiro
    print("Inteiro")
else:  # Caso contrário, é decimal
    print("Decimal")
    
    # Imprime o número arredondado para baixo
    print("Arredondado para baixo: ", round(num - 0.5))
    
    # Imprime o número arredondado para cima
    print("Arredondado para cima: ", round(num + 0.5))





