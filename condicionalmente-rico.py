# Construa uma solução algorítmica que permita aos clientes realizarem saques
# em caixas eletrônicos. No entanto, existem algumas regras a serem seguidas 
# para garantir que um saque possa ser realizado com sucesso.
# Regras do saque:
# - Cada cliente digitará o valor do seu saldoTotal de sua conta bancária e o valorSaque.
# - Um saque só pode ser realizado se o saldoDisponível na conta for igual ou superior ao valor solicitado.
# - Se o saldo for suficiente, o valor solicitado deve ser subtraído do saldo disponível, indicando que o saque foi realizado.
# - Se o saldo for insuficiente, o saque não deve ser realizado e uma mensagem adequada deve ser exibida.
# Entrada:
# A entrada consiste em dois valores inteiros que representam o total do saldo da conta e o valor do saque.
# Saída:
# Se o saque for realizado com sucesso, exibir a mensagem "Saque realizado com sucesso! Novo saldo: {saldo}", 
# onde {saldo} é o novo saldo disponível na conta.
# Se o saque não for possível devido a saldo insuficiente, exibir a mensagem "Saldo insuficiente. Saque nao realizado!"

# ==========================================================================

# Solicita os valores de saldoTotal e valorSaque ao usuário
saldoTotal = int(input("Digite o saldo total da conta: "))
valorSaque = int(input("Digite o valor do saque: "))

# Verifica se o saldo é suficiente para o saque
if saldoTotal >= valorSaque:
    saldoTotal -= valorSaque  # Subtrai o valor do saque do saldoTotal
    mensagem = f"Saque realizado com sucesso! Novo saldo: {saldoTotal}"
else:
    mensagem = "Saldo insuficiente. Saque não realizado!"

print(mensagem)
