menu = """

======= Selecione a opção desejada =======

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

==========================================

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Digite um valor para depósito: "))
        
        if valor > 0:
            print("Depósito realizado com sucesso!")
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        elif valor > limite:
            print("Sua conta atual só pode receber depósitos de até R$ 500,00!")
        else:
            print("Falha na operação! Digite um valor válido!")
            
    elif opcao == "s":
        saque = float(input("Informe o valor para saque: "))
        
        excedeu_saldo = saque > saldo
        excedeu_limite = saque > limite
        execedeu_saques = numero_saques >= LIMITE_SAQUE
        
        if excedeu_saldo:
            print("Falha na operação! Você não tem saldo sufuciente!")
            
        elif excedeu_limite:
            print("Falha na operação! O valor do saque excede o limite.")
            
        elif saque > 0 and execedeu_saques:
            print("Falha na operação! Você atingiu o limite de 3 saques!")
        
        elif saque > 0 and not execedeu_saques:
            print("Saque realizado com sucesso!")
            saldo -= saque
            extrato += f"Saque: R$ {saque:.2f}\n"
            numero_saques += 1
        else:
            print("Falha na operação! Digite um valor válido!")
            
    elif opcao == "e":
        
        print("\n=============== Extrato ===============")
        print("Nenhuma movimentação realizada!" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=======================================")
        
    elif opcao == "q":
        break
    
    else:
        print("Falha na operação! Selecione uma opção válida!")
