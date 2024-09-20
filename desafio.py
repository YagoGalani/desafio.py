menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

'''

saldo = 0
limite = 500
extrato = ''
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == 'd':
        print('Depósito')
        valor_deposito = float(input('Digite o valor que voçê deseja depositar: '))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f'Deposito: R$ {valor_deposito:.2f}\n'
        else:
            print('Valor inválido!')

    elif opcao == 's':
        print('Saque')

        if saldo > 0 and LIMITE_SAQUES > 0:
            print(f'Você possui Limite de saque de {LIMITE_SAQUES} diárias!')
            valor_saque = float(input('Digite o valor que voçê deseja sacar: '))

            if (valor_saque > saldo) or (valor_saque > limite):
                print('Impossível realizar o valor de saque informado.')
            else:
                saldo -= valor_saque
                LIMITE_SAQUES -= 1
                extrato += f'Saque: R$ {valor_saque:.2f}\n'

        elif saldo <= 0:
            print('Saldo insuficiente!')

        elif LIMITE_SAQUES == 0:
            print('Limite de saques diários já realizados.')

    elif opcao == 'e':
        print('Extrato: \n')
        if extrato == '':
            print(f'O valor que voçê possuí na sua conta bancária no momento é de R${saldo :.2f}!')
        else:
            print(extrato)
            print(f'O valor que voçê possuí na sua conta bancária no momento é de R${saldo :.2f}!')

    
    elif opcao == 'q':
        print('Obrigado por usar nosso sistema!')
        break

    else:
        print('Opção inválida, digite novamente!')
