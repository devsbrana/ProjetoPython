salario = float(input('Digite o salário do funcionário: '))
if (salario <= 1903.98):
    imposto_renda = 0
    print('Imposto de renda isento')
elif (salario > 1903.98 and salario <= 2826.65):
    imposto_renda = (salario * (7.5/100))
    salario_final = (salario - imposto_renda)
    print(f'O valor do imposto de renda é: {imposto_renda}, o salário final será: {salario_final}')
elif (salario > 2826.65 and salario <= 3751.05):
    imposto_renda = (salario * (15/100))
    salario_final = (salario - imposto_renda)
    print(f'O valor do imposto de renda é: {imposto_renda}, o salário final será: {salario_final}')
elif (salario > 3751.05 and salario <= 4664.68):
    imposto_renda = (salario * (22.5/100))
    salario_final = (salario - imposto_renda)
    print(f'O valor do imposto de renda é: {imposto_renda}, o salário final será: {salario_final}')
else:
    imposto_renda = (salario * (27.5/100))
    salario_final = (salario - imposto_renda)
    print(f'O valor do imposto de renda é: {imposto_renda}, o salário final será: {salario_final}')
