menu = """

[1] Depositar 
[2] Sacar   
[3] Extrato
[4] Sair 

=>  """

saldo = 0 
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao =input(menu)

    if opcao == '1':
        valor = float(input('Informe o valor do deposito: '))

        if valor > 0:
            saldo += valor
            extrato += f'O valor do desposito é de: R${valor:.2f}\n'

        else:
            print('A operação falhou! por favor informe um numero valido. ')
    
    elif opcao == "2":
        valor = float(input('Informe o valor do saque: '))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print('A operação falhou! Você não tem saldo suficiente. ')
        elif excedeu_limite:
            print('A operação falhou! O valor do saque excede o limite. ')
        elif excedeu_saque:
            print('A operação falhou! Numero maximo de saques diarios execedido. ')

        elif valor > 0:
            saldo -= valor
            extrato += f'O valor do saque é de: R${valor:.2f}\n'
            numero_saques += 1

        else:
            print('A operção falhou! O valor informado é ivalido. ')

    elif opcao == '3':
        print('\n==================== EXTRATO ===========================')
        print('Não foram realizadas movimentações nesse periodo. ' if not extrato else extrato)
        print(f'\n Olá, seu saldo atual é de: R${saldo:.2f}')
        print('==========================================================')

    elif opcao == '4':
        break

    else:
        print('Operação invalida, por favor selecione movamente a operação desejada. ')

