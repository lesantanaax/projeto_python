import os

restaurantes = ['Pizza Hut', 'McDonalds', 'Burger King']

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
    print('1. Cadastrar restaurantes')
    print('2. Listar restaurantes')
    print('3. Reativar cadastro')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizando app!')

def voltar_ao_menu_principal():
    input('\nPressione Enter para voltar ao menu principal...')
    main() 
    
def opcao_invalida():
    print('Opção inválida! Tente novamente.\n')
    voltar_ao_menu_principal()    

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print('\n')

def cadastrar_novo_restaurante():
    ## Limpa a tela e exibe subtítulo
    exibir_subtitulo('Cadastrar novo restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    print(f'O restaurante: {nome_do_restaurante} foi cadastrada com sucesso!')
    
    ## Adicione o nome da corrida à lista de corridas
    restaurantes.append(nome_do_restaurante)
    voltar_ao_menu_principal()    

    
def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')
        
    for restaurante in restaurantes:
        print(f'.{restaurante}')
        
    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)
        
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()     
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            reativar_cadastro()
        else:
            finalizar_app()
    except ValueError:
        opcao_invalida()        
     
    

def reativar_cadastro():  
    print('Reativar cadastro')  


def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()