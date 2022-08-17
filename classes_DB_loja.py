# importando pacotes
import mysql.connector
import funcoes_loja
import pandas as pd

class ConexaoDb:
    def __init__(self,host,port,database,user,password):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password

        global conn
        conn = mysql.connector.connect(
            host = self.host,
            port = self.port,
            database = self.database,
            user = self.user,
            password = self.password
        )

        # Teste conexao com o banco de dados
        # if (conn.is_connected):
        #     print("Conectado com sucesso")
    
    # Valida se usuario e senha está cadastrado no banco de dados
    def VerificaUsuario(self,usuario,senha):
        print("\t","="*48)
        print("\t | BEM VINDO AO SISTEMA DE CADASTRO DE PRODUTOS |")
        print("\t","="*48)
        print("")
        contador = 3
        verifica = False
        while (contador > 0):
            cursor = conn.cursor()
            cursor.execute("SELECT usuario_acesso, senha_acesso FROM acesso WHERE usuario_acesso = '" + usuario + "' AND senha_acesso = '" + senha + "';")
            result = cursor.fetchall()
            for x in result:
                if ((x[0] == usuario) and (x[1] == senha)):
                    print("Login feito com sucesso")
                    verifica = True
                    contador = 0
                    break
            
            if (not result):
                print(f"Usuario/senha invalido, {contador} tentativa de acesso.")
                contador -= 1
                usuario = input("Login do sistema: ")
                senha = input("Senha do sistema: ")
        
        if (verifica):
            funcoes_loja.MenuPrincipal()
    
    # Opcao 1 do menu cadastrar produto
    def MenuCadastrar(self,produto):
        cursor = conn.cursor()
        cursor.execute("INSERT INTO produtos (nome_produto) VALUES ('"+ produto +"');")
        conn.commit()
        print(f"Produto {produto} cadastrado com sucesso...")

    # Opcao 2 do menu alterar produto
    def MenuAlterar(self,produto,id):
        cursor = conn.cursor()
        cursor.execute("UPDATE produtos SET nome_produto = '" + produto + "' WHERE id_produto = "+ str(id) + ";")
        conn.commit()
        print(f"Produto alterado para {produto} com sucesso...")

    # Opcao 3 do menu excluir produtos
    def MenuExluir(self,id):
        cursor = conn.cursor()
        cursor.execute("DELETE FROM produtos WHERE id_produto = "+ str(id) + ";")
        conn.commit()
        print("Produto excuido com sucesso...")

    # Opcao 4 do menu visualizar produtos
    def MenuVisualizar(self):
        cursor = conn.cursor()
        cursor.execute("SELECT id_produto, nome_produto FROM produtos;")
        resultado = cursor.fetchall()
        print("=================================")
        print(">>> Visualização dos Produtos <<<")
        print("=================================")
        print("")
        print("ID Produtos")
        print("------------")
        for id, result in resultado:
            print(id,result)


##########################################
# Dados conexao com o banco mysql server #
##########################################
db = ConexaoDb(
    "localhost",
    "3307",
    "loja_informatica",
    "root",
    "thiago"
)

#db.MenuVisualizar()