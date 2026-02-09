# programa para ler três valores inteiro diferente "a,b,c" (se a < b e b = c ou a + b = c) (Condição_vedadeira)  se não (Condição falsa)

a = int(input('Digite o 1° número inteiro '))
b = int(input('Digite o 2° número inteiro '))
c = int(input('Digite o 3° número inteiro '))

if a < b and b > c or a + b == c:
    print('Condição verdadeira')
else:
    print('Condição falsa')