# Desenvolver uma solução que permita ao cliente equilibrar seu saldo bancário. 
# O programa deve solicitar uma entrada que representa o saldo atual 
# do funcionário, e após, seja informado o valor de duas transações, 
# sendo elas: um depósito e um saque. O programa deve atualizar o saldo com base 
# nas transações e exibir o saldo final.
# Informação: As transações de depósito e retirada devem ser tratadas como 
# valores positivos e negativos, respectivamente, para garantir que o cálculo do saldo final 
# seja realizado corretamente.

# Entrada
# saldoAtual: um número decimal representando o saldo atual da conta bancária.
# valorDeposito: um número decimal representando o valor a ser depositado na conta.
# valorRetirada: um número decimal representando o valor a ser retirado da conta.

# Regra de Formatação: Considere apenas uma casa decimal para esse desafio.

# Saída
# Um número decimal que representa o saldo atualizado na conta bancária após o processamento 
# das transações.

# Solicita as entradas do usuário
saldoAtual = float(input("Digite o saldo atual da conta bancária: "))
valorDeposito = float(input("Digite o valor do depósito: "))
valorRetirada = float(input("Digite o valor da retirada: "))

# Calcula o saldo atualizado
saldoAtualizado = saldoAtual + valorDeposito - valorRetirada

# Exibe o saldo atualizado com uma casa decimal
print(f"O saldo atualizado da conta bancária é: {saldoAtualizado:.1f}")
