#estrutura simples

# Entrada dos dados
A = input('Informe um valor para a variável A: ')
B =input('Informe outro valor para a  variável B: ')

# valida
if (A>B):
    aux=A;
    A=B;
    B=aux;

# Resultado
print('O valor variável A agora é : ', A);
print('O valor variável B agora é : ', B);    