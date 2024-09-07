import random

# Solicitar o valor de n
n = int(input("Digite o valor de n para criar uma matriz n x n: "))

matriz_aleatoria = []


def generate_column():
    column = []
    for i in range(0, n):
        column.append(random.randint(0, 9))
    return column


for j in range(0, n):
    matriz_aleatoria.append(generate_column())

# Nome do arquivo de saída
nome_arquivo = "matriz_aleatoria.txt"

# Escrever a matriz no arquivo no formato solicitado
with open(nome_arquivo, 'w') as arquivo:
    arquivo.write(f"{n}\n")  # Escrever o valor de n na primeira linha
    for linha in matriz_aleatoria:
        linha_str = ' '.join(map(str, linha))  # Converter os números da linha para string com espaço
        arquivo.write(f"{linha_str}\n")  # Escrever cada linha no arquivo

print(f"Matriz {n}x{n} gerada e salva no arquivo '{nome_arquivo}'.")
