# Recebe o numero do usúario

num = int(input(Digite um numero inteiro ))

# definir impar epar
imparPar = num%2

# verificar se par ou não, e resultado
if imparPar == 0:
    print(str(num) + ' é Par')
else:
    print(str(num) + ' é Impar')    