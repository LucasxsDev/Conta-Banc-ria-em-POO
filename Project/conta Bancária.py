#var
from utils import classes, interface
escolha = 0
pessoa = ''

#program
while True:
    interface.visual.tela()
    try:
        escolha = int(input('\033[33mEscolha sua opção\033[m: '))
                  
    except (ValueError, TypeError):
        print('\033[31mEscolha uma opção válida\033[m.')
        continue
        
    except KeyboardInterrupt:
        print('\n\033[31mPrograma interrompido\033[m.')
        break
        
    if escolha < 1 or escolha > 5:
        print('\033[31mEscolha uma opção válida\033[m.')
        continue
    
    if escolha == 5:
        break
    
    if escolha == 1:
        interface.linha()
        nome = input('\033[33mDigite seu nome\033[m: ')
        while True:
            try:
                conta = int(input('\033[33mNúmero da conta\033[m: '))
            except ValueError:
                print('\033[31mEscolha uma opção válida\033[m.')
                continue
            except KeyboardInterrupt:
                print('\n\033[31mPrograma interrompido\033[m.')
                break
            else:
                break
        while True:
            try:
                saldo = float(input('\033[33mSaldo atual\033[m: '))
            except ValueError:
                print('\033[31mEscolha uma opção válida\033[m.')
                continue
            except KeyboardInterrupt:
                print('\n\033[31mPrograma interrompido\033[m.')
                break
            else:
                break        
        pessoa = classes.Conta(nome=nome, numero=conta, saldo=saldo)
        interface.linha()
        continue
    
    if escolha == 2:
        if pessoa == '':
            print('\033[31mCadastre seus dados inicialmente\033[m.')
            continue
        interface.linha()
        print(classes.Conta.__getstate__(pessoa))
        interface.linha()
        continue
    
    if escolha == 3:
        if pessoa == '':
            print('\033[31mCadastre seus dados inicialmente\033[m.')
            continue
        interface.linha()
        while True:
            try:
                deposito = float(input('\033[33mValor do depósito\033[m: '))
            except (ValueError, TypeError):
                print('\033[31mEscolha uma opção válida\033[m.')
                continue
            else:
                break
        classes.Conta.deposito(pessoa, deposito)
        interface.linha()
        continue
    
    if escolha == 4:
        if pessoa == '':
            print('\033[31mCadastre seus dados inicialmente\033[m.')
            continue
        interface.linha()
        while True:
            try:
                saque = float(input('\033[33mValor de saque\033[m: '))
            except (ValueError, TypeError):
                print('\033[31mEscolha uma opção válida\033[m.')
                continue
            else:
                break
        classes.Conta.saque(pessoa, saque)
        interface.linha()
        continue

print('\033[33mMuito obrigado\033[m! \033[33mVolte sempre\033[m!')
interface.linha()