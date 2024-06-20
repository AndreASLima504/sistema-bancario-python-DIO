usuarios = {
    "12345678901": {
        "nome": None,
        "endereco": None,
        "data_nascimento": None,
        "contas": [{
                "1": {
                "agência": None,
                "saldo": 0.0,
                "saques_restantes": 3,
                "extrato": ""
                }
        },]
    }
}

LIMITE_SAQUES = 3
LIMITE_VALOR_SAQUE = 500.0
num_contas = 1

def sacar(cpf, num_conta, valor_saque):
    
    global usuarios
    conta_atual = acessar_conta(cpf, num_conta)
    if conta_atual != None:    
        if(conta_atual["saldo"] > 0):
            if(conta_atual["saques_restantes"] > 0):
                
                if(valor_saque <= conta_atual["saldo"]):
                    conta_atual["saques_restantes"] -= 1
                    conta_atual["saldo"] -= valor_saque
                    mensagem_saque = f'\nValor sacado: {valor_saque}. Saldo final: {conta_atual["saldo"]}'
                    print(mensagem_saque)
                    conta_atual["extrato"] += mensagem_saque
                else:
                    print(f'Saldo insuficiente, você deve sacar um valor menor ou igual a R${conta_atual["saldo"]:.2f} e R${LIMITE_VALOR_SAQUE}')
            else:
                print("Você atingiu o máximo de saques diários, tente novamente amanhã")
        elif conta_atual == None:
            pass
        else:
            print("Você não tem saldo para realizar saques")


def depositar(cpf, num_conta, valor_dep):
    global usuarios
    conta_atual = acessar_conta(cpf, num_conta)

    if conta_atual != None:
        conta_atual['saldo'] += valor_dep
        mensagem_dep = f"\nDepósito realizado no valor de R${valor_dep:.2f}"
        print(mensagem_dep)
        conta_atual["extrato"] += mensagem_dep


def visualizar_extrato(cpf, num_conta):
    conta_atual = acessar_conta(cpf, num_conta)
    if conta_atual != None:    
        print("EXTRATO".center(20, "#"))
        if(conta_atual["extrato"] != ""):
            print(conta_atual["extrato"])
        else:
            print("Ainda não foram feitas movimentações na conta")



def acessar_conta(cpf, numero_conta):
    global usuarios

    if cpf not in usuarios:
        print("Titular de conta não encontrado")
        return None
    
    usuario = usuarios[cpf]

    if not usuario.get("contas"):
        print("Usuário não possui contas")
        return None
    
    for conta in usuario["contas"]:
        if numero_conta in conta:
            return next(iter(dict.values(conta)))
        
    print("Conta não encontrada")
    return None


def cadastrar_usuario():
    global usuarios
    print("Seja bem vindo ao cadastro de usuários!".center(50, "#"))
    while True:
        cpf = input("Insira seu CPF")
        if cpf in usuarios:
            print("CPF já cadastrado. Tente novamente.")
        else: break
    novoUsuario = {
        cpf: {
            "nome": input("Insira seu nome"),
            "endereco": input("Insira seu endereço"),
            "data_nascimento": input("Insira sua data de nascimento"),
            "contas": []
        }
    }

    usuarios.update(novoUsuario)

def listar_contas(cpf):
    global usuarios

    usuario_atual = usuarios[cpf]

    print("Lista de contas:".center(50, "*"))
    for conta in usuario_atual["contas"]:
        print(f'Número de conta: {next(iter(dict.keys(conta)))}  |  Saldo: {conta[next(iter(dict.keys(conta)))]["saldo"]}  |  Saques restantes: {conta[next(iter(dict.keys(conta)))]["saques_restantes"]}')

def validar_cpf(cpf):
    global usuarios
    if cpf in usuarios:
        return True
    else: return False



def criar_conta(cpf):
    global usuarios, num_contas, LIMITE_SAQUES
    if cpf in usuarios:
        print("Conta corrente criada com sucesso!".center(50, "#"))
        nova_conta = {
        str(num_contas + 1): 
            {
            "agência": "0001",
            "saldo": 0.0,
            "saques_restantes": LIMITE_SAQUES,
            "extrato": ""
            }
        }
        num_contas += 1

        usuarios[cpf]["contas"].append(nova_conta)
        print(usuarios[cpf])
    else:
        print("CPF inválido")



def menu_operacoes(cpf):
    while True:
        print("Qual operação deseja realizar?".center(50, "="))
        print(
'''    [1] Depositar
    [2] Sacar
    [3] Verificar extrato
    [4] Criar conta
    [5] Listar contas
    [6] Sair''')
        operacao = input()

        if(operacao == "1"):
            valor_dep = float(input("Insira o valor a ser depositado: "))
            num_conta = input("Qual o número da conta que deseja usar?")
            depositar(cpf, num_conta, valor_dep)


        elif(operacao == "2"):
            val_saque = float(input("Insira o valor a ser sacado:"))
            num_conta = input("Qual o número da conta que deseja usar?")
            sacar(cpf, num_conta, val_saque)

        elif(operacao == "3"):
            num_conta = input("Qual o número da conta que deseja usar?")
            visualizar_extrato(cpf, num_conta)

        
        elif(operacao == "4"):
            criar_conta(cpf)

        elif (operacao == "5"):
            listar_contas(cpf)

        elif(operacao == "6"):
            break
        else:
            print("Operação inválida, tente novamente")
            
    
    
while True:
    print("Seja bem-vindo(a) ao seu banco!".center(50, "="))
    print("Opções:".center(50, "="))
    print(
        '''[1] Acessar usuário
[2] Cadastrar usuário
[3] Sair'''
    )

    opcao_inicial = input()
    
    if opcao_inicial == "1":
        cpf_login = input("Insira seu CPF abaixo")
        if validar_cpf(cpf_login):
            menu_operacoes(cpf_login)
        else: print("CPF inválido, tente novamente")

    elif opcao_inicial == "2":
        cadastrar_usuario()
