# Implementar uma solução que organize em ordem alfabética uma lista de ativos que será 
# informada pelos usuários. Os ativos são representados por strings que representam seus tipos, 
# como por exemplo: Reservas de liquidez, Ativos intangiveis e dentre outros.

# Entrada:
# A primeira entrada consiste em um número inteiro que representa a  quantidade de ativos 
# que o usuário possui. Em seguida, o usuário deverá  informar, em linhas separadas, 
# os tipos (strings) dos respectivos ativos.

# Saída:
# Seu programa deve exibir a lista de Ativos organizada em ordem alfabética. 
# Cada ativo deve ser apresentado em uma linha separada.

# =====================================================================

# Solicita a quantidade de ativos ao usuário
quantidade_ativos = int(input("Digite a quantidade de ativos: "))

# Inicializa uma lista vazia para armazenar os ativos
ativos = []

# Solicita ao usuário os tipos de ativos e os armazena na lista
for i in range(quantidade_ativos):
    ativo = input(f"Digite o tipo do ativo {i + 1}: ")
    ativos.append(ativo)

# Ordena a lista de ativos em ordem alfabética
ativos.sort()

# Exibe os ativos organizados em ordem alfabética
print("Ativos organizados em ordem alfabética:")
for ativo in ativos:
    print(ativo)
