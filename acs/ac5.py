"""
Faça um programa para imprimir o texto abaixo, para
um n informado pelo usuário.
Use uma função que receba um valor n inteiro imprima até a n-ésima linha.

 1
 1   2
 1   2   3
 .....
 1   2   3   ...  n
"""

def imprimir_padrao(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

n = int(input("Digite um número inteiro: "))
imprimir_padrao(n)

"""
Faça uma função que informe a quantidade de dígitos
de um determinado número inteiro informado.
"""
def contar_digitos(numero):
    numero_str = str(numero)
    return len(numero_str)

numero = int(input("Digite um número inteiro: "))
quantidade_digitos = contar_digitos(numero)
print(f"O número {numero} tem {quantidade_digitos} dígitos.")

"""
Faça um programa que solicite ao usuário 2 números inteiros.
A seguir, calcule e mostre a divisão do primeiro pelo segundo. 
Para resolver este problema, utilize a instrução try-except, particularmente
analizando as exceções do tipo ValueError e ZeroDivisionError. 
Inclua uma instrução finally para exibir o resultado da operação.
"""
def dividir_numeros():
    try:
        num1 = int(input("Digite o primeiro número inteiro: "))
        num2 = int(input("Digite o segundo número inteiro: "))
        resultado = num1 / num2
    except ValueError:
        print("Erro: Valor inserido não é um número inteiro.")
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
    finally:
        print("Resultado da operação (se aplicável):", resultado)

dividir_numeros()