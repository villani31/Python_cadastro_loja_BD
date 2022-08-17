import classes_DB_loja
import os

# Menu principal do sistema
def MenuPrincipal():
    opcao = 0
    try:
        while (opcao != 5):
            # limpa tela
            os.system("cls" if os.name == "nt" else "clear")
            print(" "*25,"+ ".ljust(45,"-"),"+")
            print(" "*25,"|      SEJA BEM BINDO AO SISTEMA DA LOJA      |")
            print(" "*25,"+ ".ljust(45,"-"),"+")
            print(" ")
            print("Menu Principal:")
            print("="*54)
            print("| 1 - Cadastrar Produto  |  2 - Alterar Produto      |")
            print("| 3 - Excluir Produto    |  4 - Visualizar Produtos  |")
            print("|                  5 - Encerrar                      |")
            print("="*54)
            opcao = int(input("Digite a opção desejada: "))
            # limpa tela
            os.system("cls" if os.name == "nt" else "clear")
            if (opcao == 1):
                produto = input("Qual produto deseja cadastrar: ")
                try:    
                    classes_DB_loja.db.MenuCadastrar(produto)
                    input("Pressione enter para continuar...")
                except:
                    print('Erro ao cadastrar, produto já existe..')
                    input("Pressione enter para continuar...")
            elif (opcao == 2):
                id = input("Digite o ID do prodotu que vai ser alterado: ")
                produto = input("Digite o nome do produto que vai ser alterado: ")
                classes_DB_loja.db.MenuAlterar(produto,id)
                input("Pressione enter para continuar...")
            elif (opcao == 3):
                id = input("Digite o ID do produto que será exluido: ")
                classes_DB_loja.db.MenuExluir(id)
                input("Pressione enter para continuar...")
            elif (opcao == 4):
                classes_DB_loja.db.MenuVisualizar()
                input("Pressione enter para continuar...")
            elif (opcao == 5):
                print("Sistema encerrado pelo usuário...")
            else:
                print("Opção inválida...")
                input("Pressione enter para continuar...")
    except:
        print("Opção invãlida...")
        input("Pressione enter para continuar...")
        MenuPrincipal()
        