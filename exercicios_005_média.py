#Entrada dos dados

notaA = float(input('Digite uma nota ))
notaB = float(input('Digite outra nota ))

#Calcular media
mediafinal = (notaA + notaB) /2

#Verificação e resultado
if mediafinal >= 7.0:
    print('Média %.2f - Aprovado ' %mediafinal )
else:
    print('Média %.2f - Reprovado ' %mediafinal)    