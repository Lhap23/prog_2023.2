"""
Elabore um código em Python que resolva
 uma equação do segundo grau
ax² + bx + c = 0. O programa deve
pedir os parâmetros
a, b e c da equação e deve
Calcular as raízes pela
 fórmula de Bhaskara.
Considere que as raízes são reais.
 Exemplo: a = 1, b = -6, c = 8
   dá como raízes 4 e 2.
"""

a = float(input("Entre com o valor de a: "))
b = float(input("Entre com o valor de b: "))
c = float(input("Entre com o valor de c: "))

d = (b**2 - 4*a*c)
x1 = (-b + d**(1/2)) / (2*a)
x2 = (-b - d**(1/2)) / (2*a)

print("O valor do primeiro x é:", x1, "e o valor do segundo x é:", x2)

"""
Elabore um programa que leia uma variável inteira ano.
Em seguida, exiba na tela o resultado da expressão lógica que indica se um ano é ou não bissexto.
Um ano é bissexto se ele é múltiplo de quatro.
No entanto anos múltiplos de 100 que não são múltiplos de 400 não são bissextos.
Então 1995 não é bissexto, 2012 é bissexto, 1900 não é bissexto e 2000 é bissexto.
"""

ano = int(input("Digite um ano de sua escolha: "))
bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
print(bissexto and f"{ano} é um ano bissexto." or f"{ano} não é um ano bissexto.")