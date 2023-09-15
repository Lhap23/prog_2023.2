"""
Elabore uma função e_primo(num) que retorna
se um número num é primo ou não.
Caso num não seja primo, liste todos os números pelos quais num é divisível
"""

def e_primo(num):
    for divi in range(2, num):
        if num % divi == 0:
            print(f"O{num} não é primo e é divisível por, {divi}")


    else: 
        print(f"{num}, é primo")

e_primo(17)

"""
Faça um programa que receba o valor de
uma dívida e mostre as opções de parcelamento.
O resultado final deve conter as opções de 1, 3, 6, 9 ou 12 parcelas, e
o percentual de juros para cada parcela deve ser determinado conform
a primeira tabela, abaixo. O relatório com as opções de pagamento
deve conter os seguintes dados: valor dos juros, valor total da
dívida (incluindo juros), quantidade de parcelas e valor da parcela.
A segunda tabela, abaixo, mostra um exemplo de como o resultado deve ser exibido.
No momento, não é necessário formatar os valores.
"""

def calcular_taxa_juros(valor_emprestimo, parcelas):
    if parcelas == 1:
        return 0.0
    elif parcelas == 3:
        return valor_emprestimo * 0.10
    elif parcelas == 6:
        return valor_emprestimo * 0.15
    elif parcelas == 9:
        return valor_emprestimo * 0.20
    elif parcelas == 12:
        return valor_emprestimo * 0.25
    else:
        return None

def mostrar_opcoes_financiamento(valor_emprestimo):
    print("Opções de Financiamento:")
    print(f"Parcelas: 1 | Taxa de Juros: 0% | Total: R${valor_emprestimo} | Valor da Parcela: R${valor_emprestimo}")

    for parcela in range(3, 13, 3):
        taxa_juros = calcular_taxa_juros(valor_emprestimo, parcela)
        if taxa_juros is not None:
            total_a_pagar = valor_emprestimo + taxa_juros
            valor_da_parcela = total_a_pagar / parcela
            print(f"Parcelas: {parcela} | Taxa de Juros: {taxa_juros}% | Total: R${total_a_pagar} | Valor da Parcela: R${valor_da_parcela}")

valor_emprestimo = float(input("Digite o valor do empréstimo: "))
mostrar_opcoes_financiamento(valor_emprestimo)

"""
Faça um programa que leia uma quantidade indeterminada de números
positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100].
A entrada de dados deverá terminar quando for lido um número negativo.
"""

intervalo0_25 = 0
intervalo26_50 = 0
intervalo51_75 = 0
intervalo76_100 = 0

continuar = True

while continuar:
    a = int(input("Digite um valor (Digite um número negativo para encerrar): "))
    
    if a < 0:
        continuar = False
    else:
        if 0 <= a <= 25:
            intervalo0_25 += 1
        elif 26 <= a <= 50:
            intervalo26_50 += 1
        elif 51 <= a <= 75:
            intervalo51_75 += 1
        elif 76 <= a <= 100:
            intervalo76_100 += 1

print("[0-25]:", intervalo0_25)
print("[26-50]:", intervalo26_50)
print("[51-75]:", intervalo51_75)
print("[76-100]:", intervalo76_100)

