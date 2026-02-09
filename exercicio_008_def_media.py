#Calcular media com def

def lernotas():
    n1 = float(input('Digite a primeira nota do aluno '))
def lernotas():
    n2 = float(input('Informe a segunda nota '))


def resultado(n1,n2):
    media = (n1 + n2) /2
    print('Nota 1: ', n1)
    print('Nota 2: ', n2)
    print('Média: ', media, ' Resultado ', end='')

    if media >= 7.0:
        print('Aprovado')
    else:
        print('Reprovado')


a = lernotas()
b = lernotas()
resultado(a,b)