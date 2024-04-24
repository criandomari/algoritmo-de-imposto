# Criando um algoritmo para calcular o mposto de renda

salario = 0
salario = float(input("Digite o salário do colaborador: "))

if salario <= 1903.98:
    print(f"O colaborador isento de imposto")
    print(f"Salario a receber = {salario}")
elif salario <= 2826.65:
    print(f"O colaborador deve pagar r$ 142,80 de imposto")
    print(f"Salario a receber = {salario - 142.80}")
elif salario <= 3751.05:
    print(f"O colaborador deve pagar r$ 354,80 de imposto")
    print(f"Salario a receber = {salario - 354.80}")
elif salario <= 4664.68:
    print(f"O colaborador deve pagar r$ 639,13 de imposto")
    print (f"Salario a receber = {salario - 639.13}")
else:
    print (f"O colaborador deve pagar r$ 869,36 de imposto")
    print(f"Salario a receber = {salario - 869.36}")
    
