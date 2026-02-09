
#Entada dos dados
codigo = int(input('Informe o codigo do funcionário: '))
nome = str(input('Digite o nome do funcionário:  '))

salario = float(input('Informe o salário do funcionário: '))

# tipo de salario
tipo = type(salario)

#Resultado
print('Código: %d' %codigo)
print('Nome: %s' %nome)
print('Salário: %.2f' %salario)
print('Tipo: %r' %tipo)