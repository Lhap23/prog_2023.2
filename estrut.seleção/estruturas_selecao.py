def e_par(num):
    if num % 2 == 0:
        print(num, "é par")
    else:
        print(num, "é impar")

    print("fim da função")

# e_par(4)
# e_par(5)

def conceito(nota):
    if nota > 9:
        print("Conceito A")
    elif nota > 8:
        print("Conceito B")
    elif nota > 7:
        print ("Conceito C")
    else:
        print("Conceito D")

# conceito(9.5)
# conceito(3.4)

# Válido a partir da versão 3.10 do Python
# def cli():
#    opcao = input("Digite 1 para inseir nome, 2 para nota, ou "
#                  "qualquer outro caractere para sair: ")
#    match opcao:
#        case"1":
#            print("Opção 1")
#        case "2":
#            print("Opção 2")
#        case _:
#            print"sair"

def e_par2(num):
    return num % 2 == 0

def maior(num1, num2):
    if num1 > num2:
        return num1

    return num2

# Ternário
def maior2(num1, num2):
    return num1 if num1> num2 else num2 if num1 == num2 else "são iguais"

# print(maior(4, 9))
# print(maior2(11, 9))
# print(maior2(9, 9))

def positivo(num):
    if num > 0:
        return "positivo"
    if num == 0:
        return "zero"

    return "negativo"

def vog_cons(vog):
    if vog == a or vog == e or vog == i or vog == o or vog == u:
        return "vogal"

    return "consoante"


def calcula_media(nota1, nota2, nota3):
    media = (nota1, nota2, nota3)

    if nota > 10 or nota1 < 0 or nota2 > 10 or nota2 < 0 or nota3 > 10 or nota3 < 0:
        print("Nota inválida")
    else:
        if media == 10:
            print("Aprovado com Distinção")
        elif media >= 7:
            print("Aprovado")
        else:
            print("Reprovado")