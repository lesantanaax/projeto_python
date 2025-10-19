import os

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")

def exibir_opcoes():
    print('1. Cadastrar em corridas')
    print('2. Listar melhores corridas')
    print('3. Atividades em São Paulo')
    print('4. Sair\n')

def finalizar_app():
    os.system('cls')
    # os.system('clear')
    print('Finalizando o app')

def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção: '))
    # opcao_escolhida = int(opcao_escolhida)
    
    if opcao_escolhida == 1:
        cadastrar_corrida()     
    elif opcao_escolhida == 2:
        listar_corridas()
    elif opcao_escolhida == 3:
        reativar_cadastro()
    else:
        finalizar_app()

def cadastrar_corrida():
    print('Cadastrar em Corridas')
    nome = input('Digite seu nome: ')
    email = input('Digite seu email: ')
    idade = int(input('Digite sua idade: '))
    print(f'Nome: {nome}\nEmail: {email}\nIdade: {idade}')
    print('Cadastro realizado com sucesso!')   

def listar_corridas():
    print('Lista das corridas que você pode participar:')
    print('1. São Silvestre - 15km')
    print('2. Meia Maratona de São Paulo - 21km')
    print('3. Maratona de São Paulo - 42km')
    print('4. Volta da Pampulha - 18km')

def reativar_cadastro():  
    print('Reativar cadastro')  


def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()