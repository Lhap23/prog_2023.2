"""
Uma empresa resolveu dar um aumento de salário aos seus colaboradores
e lhe contrataram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste
segundo a tabela a seguir, baseado no salário atual.
Após o aumento ser realizado, informe na tela:
. O salário antes do reajuste;
. O percentual de aumento aplicado;
. O valor do aumento;
. O novo salário, após o aumento.

- Salários até R$ 280,00 (incluindo)      Aumento de 20%
- Salários entre R$ 280,00 e R$ 700,00    Aumento de 15%
- Salários entre R$ 700,00 e R$ 1500,00   Aumento de 10%
- Salários de R$ 1500,00 em diante        Aumento de 5%
"""

salario_atual = float(input("Digite o salário atual: R$"))

def calc_reajuste(salario_atual):
    if salario_atual <= 280.00:
        aumento_salario = 20
    elif salario_atual <= 700.00:
        aumento_salario = 15
    elif salario_atual <= 1500.00:
        aumento_salario = 10
    else:
        aumento_salario = 5

    aumento = (aumento_salario / 100) * salario_atual
    salario_novo = aumento + salario_atual

    return salario_atual, aumento, salario_novo, aumento_salario

salario_antigo, valor_aumento ,salario_novo , percentual_aumento = calc_reajuste(salario_atual)

print("O salário antes do reajuste é ", salario_antigo)
print("O percentual de aumento aplicado foi de: ", percentual_aumento, "%")
print("O valor do aumento foi de: ", valor_aumento)
print("O novo salário é de: ", salario_novo)

"""
Implementa uma função que receba um número e exiba
o dia correspondente da semana (1-Domingo, 2- Segunda, etc.), se digitar
outro valor deve aparecer valor inválido.
"""

dia = int(input("Digite um número que corresponda ao dia da semana que você quer: "))

def dias_semanais(dia):
    if dia == 1:
        print("Domingo")
    elif dia == 2:
        print("Segunda")
    elif dia == 3:
        print("Terça")
    elif dia == 4:
        print("Quarta")
    elif dia == 5:
        print("Quinta")
    elif dia == 6:
        print("Sexta")
    elif dia == 7:
        print("Sábado")
    else:
        print("Valor inválido")
 
dias_semanais(dia)

"""
Faça um programa que calcule as raízes de uma
equação do segundo grau, na forma ax^2 + bx + c.
O programa deverá receber os valores de a, b e c
e fazer as consistências, informando ao usuário nas seguintes situações:

.Se o usuário informar o valor de a igual a zero, a equação
não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;

.Se o delta calculado for negativo, 
a equação não possui raízes reais. Informe ao usuário e encerre o programa;

.Se o delta calculado for igual a zero 
a equação possui apenas uma raiz real, informe-a ao usuário;

.Se o delta for positivo, a equação 
possui duas raízes reais, informe-as ao usuário.
"""

a = float(input("Entre com o valor de a: "))
b = float(input("Entre com o valor de b: "))
c = float(input("Entre com o valor de c: "))

delta = (b ** 2 - 4 * a * c)

def func_segGrau(a, delta):
    if a == 0:
        print("A equação não é de segundo grau, o programa está sendo encerrado.")
    elif delta == 0:
        print("A equação possuí apenas uma raiz.")
    elif delta > 0:
        print("A equação possuí duas raizes.")
    else:
        print("A equação não possuí raízes, o programa está sendo encerrado.")

func_segGrau(a, delta)




    