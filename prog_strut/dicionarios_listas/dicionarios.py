"""
Estrutura de Dados
-Conjuntos
    - Mutáveis
    - Não ordenados
    - Únicos
    - Não suporta indexação
- Dicionários
    - Mutáveis
    - Não ordenados
    - Únicos
    - Suportam indexação por chaves imutáveis
"""

numeros = [1, 8, 5, 1, 2, 6, 1, 2, 8, 4, 3]
numeros_unicos = set(numeros)
numeros_unicos.add(9)
numeros_unicos.add(8)
numeros_unicos.add(0)
print(numeros_unicos)

outros_numeros = set()
outros_numeros.add(3)
outros_numeros.add(8)
outros_numeros.add(7)
outros_numeros.add(3)
print(outros_numeros)

outros_numeros.remove(7)
print(outros_numeros)

numeros = list(set(numeros))
print(numeros)

outros_numeros = {1, 2, 3, 8, 4, 1, 2, 4, 2, 3}
print(outros_numeros)

print("-" * 40)

# aluno = { chave: valor}

aluno = {
    "nome": "Victor",
    "matrícula": "12345",
    1.45: 45,
    False: 10,
    (1, 2): "sem sentido"
}
print(aluno["nome"])
print(aluno["matrícula"])
print(aluno[False])
# print(aluno["matrícula"]) -> gera KeyError

print(aluno.get("matricula", "Erro! Chave não existe."))

aluno = {
    "nome": "Victor",
    "matrícula": "123456",
    "curso": "engenharinha de computação",
    "disciplina": {
        {
            "nome": "Programação",
            "cód": "IBM1737",
            "notas": {
                "ap1": 7.5,
                "ap2": 8.2,
                "ac": 4.5
            }
        },
        {
            "nome": "Cálculo",
            "cód": "IBM1730",
            "notas": {
                "ap1": 8.2,
                "ap2": 6.4,
                "ac": 9.4
            }
        }
    }   
}
print (aluno["disciplinas"][0]["cód"])

print("-" * 40)
for chave in aluno: # itera sobre as chabes de um dict
    print(chave)

print("-" * 40)
for chave in aluno.keys():
    print(chave)

print("-" * 40)
for valor in aluno.value(): # itera sobre os valores de dict
    print(valor)

print("-" * 40)
for chave, valor in aluno.items(): # Itera sobre as chaves e os valores de um dict
    print(chave, "-", valor)
    