"""
Monte uma função que recebe um salário por hora
e o número de horas trabalhadas no mês, e retorne
o salário a ser recebido.
"""

def salarioHora(s, h):
    salario = s * h
    return(salario)

soldo = salarioHora(13, 220)

#print(soldo)

"""
Elabore uma função que receba três números e exiba na tela: (1) o produto do dobro
do primeiro com metade do segundo;
(2) a soma do triplo do primeiro com o terceiro;
e (3) o terceiro elevado ao cubo.
"""

def exibirN(n1, n2, n3):
    calc1 = n1 * n1 * (n2 / 2)
    calc2 = n1 * n1 + n3
    calc3 = n3**3
    print("Produto do dobro do primeiro com metade do segundo:", calc1)
    print("Soma do triplo do primeiro com o terceiro:", calc2)
    print("Terceiro elevado ao cubo:", calc3)

exibirN(3, 4, 6)

"""
Elabore uma função com as mesmas regras
do exercício anterior, porém
retornando os três resultados, ao
invés de exibi-los na tela.
"""
def exibirN(n1, n2, n3):
    calc1 = n1 * n1 * (n2 / 2)
    calc2 = n1 * n1 + n3
    calc3 = n3**3
    return calc1, calc2, calc3

resultado = exibirN(3, 4, 6)

# print(resultado) # a questão não pediu para exibir porém está aqui em via das dúvidas

"""
Elabore uma função que receba uma variável inteira ano.
Em seguida, retorne o resultado da expressão lógica que indica se um ano é ou não bissexto.
Um ano é bissexto se ele é múltiplo de quatro.
No entanto anos múltiplos de 100 que não são múltiplos de 400 não são bissextos.
Então 1995 não é bissexto, 2012 é bissexto, 1900 não é bissexto e 2000 é bissexto.
"""

def intAno(ano):
    bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
    return (bissexto)

ano = int(input("Digite um ano: "))
resultadoAno = intAno(ano)
print(resultadoAno)



