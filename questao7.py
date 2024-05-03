conta = int(input('Digite o numero da sua conta: '))
saldo = float(input('Qual é seu saldo:  '))
debito = float(input('Quanto de debito: '))
credito = float(input('Quanto de crédito: '))
total = saldo - (debito + credito)
if total >= 0:
    print('Seu saldo atual é R${}, ele é positivo'.format(total))
else:
    print('Seu saldo atual é R${},ele é negativo'.format(total))
    