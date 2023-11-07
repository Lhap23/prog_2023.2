# Construção de listas
alunos = ["abc", "def", "ghi"]
lista = [1, 4.5, False, [1, 2, 3]]# não é uma boa prática

# Acesso a elementos
print(alunos[1])
# print(alunos[3]) -> erro de indice
print(alunos[-1]) # último elemento da lista

# Matrizes
coordenadas = [
    [ 2, 6],
    [ 1, 10],
    [-1, -5]
]
print(coordenadas[0][1])

# fatiamento
print("-" * 40)
alunos = ["abc", "def", "ghi", "jkl", "mno", "pqr"]
print(alunos[1:5])
print(alunos[1:6:2])
print(alunos[:4:2])# começa no icício da lista
print(alunos[1::2])# termina no final da lista
print(alunos[1:])
print(alunos[::-1])# inverte a lista

# Operações com listas - Pertencimento
print("-" * 40)
print("def" in alunos)
print("stu" in alunos)
print("stu" not in alunos)

# Operações com lista - Soma
print([1, 2] + [3, 4])

# Operações com listas - Multiplicação
print([0] * 10)

# Operações com lstas - Iteração
print("-" * 40)
for aluno in alunos:
    print(aluno)

for indice, aluno in enumerate(alunos):
    print(indice, aluno, sep=" - ")

notas = [7.5, 6.5, 8.2, 4.8, 6.4, 2.3]
for nota, aluno in zip(notas, alunos):
    print(aluno, nota, sep=": ")

# não é uma boa prática -> não é pythonico
for indice in range(len(alunos)):
    print(alunos[indice])

# Funções e Métodos com listas
print("-" * 40)
print(len(alunos))
alunos.append("stu") # sempre no final da lista
print(alunos)
alunos.insert(3, "vwx")
print(alunos)
alunos.extend(["yza", "bcd"])
print(alunos)

print("-" * 40)
print(alunos.pop())
print(alunos)
print(alunos.pop(3))
print(alunos)
print(alunos.remove("jkl")) # remove a primeira ocorrência de elemento
print(alunos)

if "jkl" in alunos: # caso o contrário, pode subir um erro de valor
    alunos.remove("jkl")

print(alunos.index("mno"))

alunos = ["abc", "def", "abc", "abc"]
print(alunos.count("abc"))

print(max(notas))
print(min(notas))
print(sum(notas))

print(notas)
notas_ord = sorted(notas)
print(notas_ord)
print(notas)

notas.sort()
print(notas)

# Compreensão de listas
print("-" * 40)
numeros = [1, 2, 3, 4, 5, 6, 7]
quadrados = []

for numero in numeros:
    quadrados.append(numeros ** 2 for numeros in numeros)
    print(quadrados)

quadrados2 = [numero ** 2 for numero in numeros]
print(quadrados2)

quadrado_impar = [numero ** 2 for numero in numeros if numero % 2 ==1]
print(quadrado_impar)

# Linearização de matrizes
coodenadas = [x for y in coordenadas for x in y]
print(coordenadas)

# Dados Mutáveis vs. Imutáveis
print("-" * 40)
x = 2
y = x
x = 3
print(x, y)

a = [1]
b = a
a.append(2)
a[0] = 999
print(a, b)

def limpa_dados(lista, valor_a_limpar):
    for dado in lista:
        if dado == valor_a_limpar:
            lista.remove(dado)

print("-" * 40)
nomes = ["a", "b", "c", "a", "a", "d", "a"]
novos_nomes = nomes.copy() # gera uma nova lista, em outro endereço de memória
limpa_dados(novos_nomes, "a")
print(nomes)
print(novos_nomes)

print("-" * 40)
def adiciona_elemento(elem, lista=[]):
    if lista is None:
        lista = []
    lista.append(elem)
    return lista

a = [1, 2, 3]
adiciona_elemento(4, a)
adiciona_elemento(5, a)
adiciona_elemento(6, a)
print(a)

b = adiciona_elemento(8) # [8]
print(b)
b = adiciona_elemento(7) # [7]
print(b)

# Tuplas
