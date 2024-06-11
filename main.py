saldo = 0.0
LIMITE_SAQUES = 3
LIMITE_VALOR_SAQUE = 500.0
saques_restantes = LIMITE_SAQUES
extrato = ""

def sacar():
    global saldo, saques_restantes, extrato

    if(saldo > 0):
        if(saques_restantes > 0):
            valor_saque = float(input("Insira o valor a ser sacado:"))
            
            if(valor_saque <= saldo):
                saques_restantes -= 1
                saldo -= valor_saque
                mensagem_saque = f"\nValor sacado: {valor_saque}. Saldo final: {saldo}"
                print(mensagem_saque)
                extrato += mensagem_saque
            else:
                print(f"Saldo insuficiente, você deve sacar um valor menor ou igual a R${saldo:.2f} e R${LIMITE_VALOR_SAQUE}")
        else:
            print("Você atingiu o máximo de saques diários, tente novamente amanhã")
    else:
        print("Você não tem saldo para realizar saques")


def depositar():
    global saldo, extrato
    valor_dep = float(input("Insira o valor a ser depositado: "))

    saldo += valor_dep
    mensagem_dep = f"\nDepósito realizado no valor de R${valor_dep:.2f}"
    print(mensagem_dep)
    extrato += mensagem_dep


def visualizar_extrato():
    global extrato
    print("EXTRATO".center(20, "#"))
    if(extrato != ""):
        print(extrato)
    else:
        print("Ainda não foram feitas movimentações na conta")


while True:
    print("Seja bem-vindo(a) ao seu banco!".center(50, "="))
    print("Qual operação deseja realizar?".center(50, "="))
    print(
        '''1- Saque
2- Depositar
3- Verificar extrato
4- Sair'''
    )
    operacao = input()

    if(operacao == "1"):
        sacar()
        print(f"Saldo atual: R${saldo:.2f}")

    elif(operacao == "2"):
        depositar()
        print(f"Saldo atual: R${saldo:.2f}")

    elif(operacao == "3"):
        visualizar_extrato()
        print(f"Saldo atual: R${saldo:.2f}")
    elif(operacao == "4"):
        break
    else:
        print("Opção inválida, tente novamente")
    print("=========================")