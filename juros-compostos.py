# Imagine que você está desenvolvendo um aplicativo para um banco que deseja 
# calcular os juros compostos de um investimento. Seu objetivo é criar uma função 
# que receba três parâmetros: o valor inicial do investimento, a taxa de juros anual 
# e o período de tempo em anos. A função deve calcular e retornar o valor final do investimento 
# após o período determinado, levando em consideração os juros compostos.
# Entrada:
# A função deve receber os seguintes parâmetros:
# valor_inicial: um número inteiro ou decimal representando o valor inicial do investimento.
# taxa_juros: um número decimal representando a taxa de juros anual. Por exemplo, se a taxa for de 5%, o valor passado será 0.05.
# periodo: um número inteiro representando a quantidade de anos do investimento.
# Saída:
# A função deve retornar o valor final do investimento após o período determinado, considerando os juros compostos. 
# O valor final deve ser arredondado para duas casas decimais.

# ====================================================================

valor_inicial = float(input("Digite o valor inicial do investimento: "))
taxa_juros = float(input("Digite a taxa de juros anual (por exemplo, 5% como 0.05): "))
periodo = int(input("Digite o período de investimento em anos: "))

valor_final = valor_inicial

# Itera com base no período em anos para calcular o valorFinal com os juros.
for _ in range(periodo):
    valor_final += valor_final * taxa_juros

print("Valor final do investimento: R$", round(valor_final, 2))
