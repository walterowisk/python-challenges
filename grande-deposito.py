# Você foi contratado por um banco para desenvolver um programa que auxilie seus 
# clientes a realizar depósitos em suas contas. O programa deve solicitar ao cliente 
# o valor do depósito e verificar se o valor é válido. Se o valor for maior do que zero, 
# o programa deve adicionar o valor ao saldo da conta. Caso contrário, o programa deve exibir 
# uma mensagem de erro e solicitar um novo valor. O programa deve continuar solicitando valores 
# de depósito até que seja digitado um valor válido.
# Entrada:
# O programa deve utilizar o Scanner para receber os valores de depósito digitados pelo cliente. 
# Os valores podem ser decimais, representando valores em reais.
# Saída:
# O programa deve exibir uma mensagem de sucesso quando um valor de depósito válido for informado 
# e o saldo da conta for atualizado. Caso um valor inválido seja digitado, o programa deve exibir 
# uma mensagem de erro e solicitar um novo valor.

# ===============================================================

saldo_conta = 0.0 # Inicializa o saldo da conta como zero

valor = float(input("Digite o valor do depósito: "))

if valor > 0:
    saldo_conta += valor
    print(f"Depósito realizado com sucesso! \nSaldo atual: R$ {saldo_conta:.2f}")
elif valor == 0:
   print("Encerrando o programa...")
else:
  print("Valor inválido! Digite um valor maior que zero.")