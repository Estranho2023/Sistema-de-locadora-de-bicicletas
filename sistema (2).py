from banco import Banco
import tkinter as tk
import tkinter.font as tkFont
from tkinter import PhotoImage
# from PIL import Image, ImageTk
import hashlib

class App:
    
    def __init__(self, root):
        self.nomebanco = 'Banco_das_bikes'
        self.db = Banco()
        #contador de produtos criados 
        self.contador = 0
        self.matriz_ldv = []
        #setting title
        root.title("undefined")
        #setting window size
        width=863
        height=632
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.titulo=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        self.titulo["font"] = ft
        self.titulo["fg"] = "white"
        self.titulo["justify"] = "left"
        self.titulo["text"] = "Locadora de Bicicleta"
        self.titulo["bg"] = "darkcyan"
        self.titulo.place(x=5,y=8,width=250,height=30)

        self.imagem = PhotoImage(file="login.png")

        self.botao_login = tk.Button(root)
        ft = tkFont.Font(family='Arial', size=10)
        self.botao_login["font"] = ft
        self.botao_login["fg"] = "white"
        self.botao_login["justify"] = "center"
        self.botao_login["text"] = "Login"
        self.botao_login['bd'] = 0
        self.botao_login['image'] = self.imagem
        self.botao_login.place(x=800, y=2, width=50, height=35) #botao com a imagem de login
        self.botao_login["command"] = self.botao_login_command

        self.texto1=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=16)
        self.texto1["font"] = ft
        self.texto1["fg"] = "#333333"
        self.texto1["justify"] = "center"
        self.texto1["text"] = "Entre"
        self.texto1.place(x=380,y=150,width=0,height=0)

        self.texto_login=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=10)
        self.texto_login["font"] = ft
        self.texto_login["fg"] = "#000000"
        self.texto_login["justify"] = "center"
        self.texto_login["text"] = "Login:"
        self.texto_login.place(x=245,y=195,width=0,height=0)

        self.caixa_login=tk.Entry(root)
        self.caixa_login["borderwidth"] = "1px"
        ft = tkFont.Font(family='Arial',size=10)
        self.caixa_login["font"] = ft
        self.caixa_login["fg"] = "#333333"
        self.caixa_login["justify"] = "left"
        self.caixa_login["text"] = "Nome de usuário"
        self.caixa_login.place(x=305,y=195,width=0,height=0)

        self.texto_senha=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=10)
        self.texto_senha["font"] = ft
        self.texto_senha["fg"] = "#000000"
        self.texto_senha["justify"] = "center"
        self.texto_senha["text"] = "Senha:"
        self.texto_senha.place(x=245,y=240,width=0,height=0)

        self.caixa_senha=tk.Entry(root)
        self.caixa_senha["borderwidth"] = "1px"
        ft = tkFont.Font(family='Arial',size=10)
        self.caixa_senha["font"] = ft
        self.caixa_senha["fg"] = "#333333"
        self.caixa_senha["justify"] = "left"
        self.caixa_senha["text"] = "Senha"
        self.caixa_senha.place(x=305,y=240,width=0,height=0)

        self.texto_email=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=10)
        self.texto_email["font"] = ft
        self.texto_email["fg"] = "#000000"
        self.texto_email["justify"] = "center"
        self.texto_email["text"] = "Email:"
        self.texto_email.place(x=245,y=285,width=0,height=0)

        self.caixa_email=tk.Entry(root)
        self.caixa_email["borderwidth"] = "1px"
        ft = tkFont.Font(family='Arial',size=10)
        self.caixa_email["font"] = ft
        self.caixa_email["fg"] = "#333333"
        self.caixa_email["justify"] = "left"
        self.caixa_email["text"] = "Email"
        self.caixa_email.place(x=305,y=285,width=0,height=0)

        self.texto_telefone=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=10)
        self.texto_telefone["font"] = ft
        self.texto_telefone["fg"] = "#000000"
        self.texto_telefone["justify"] = "center"
        self.texto_telefone["text"] = "Telefone:"
        self.texto_telefone.place(x=245,y=330,width=0,height=0)

        self.caixa_telefone=tk.Entry(root)
        self.caixa_telefone["borderwidth"] = "1px"
        ft = tkFont.Font(family='Arial',size=10)
        self.caixa_telefone["font"] = ft
        self.caixa_telefone["fg"] = "#333333"
        self.caixa_telefone["justify"] = "left"
        self.caixa_telefone["text"] = "Telefone"
        self.caixa_telefone.place(x=305,y=330,width=0,height=0) 

        self.mensagem=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=10)
        self.mensagem["font"] = ft
        self.mensagem["fg"] = "red"
        self.mensagem["justify"] = "center"
        self.mensagem["text"] = ""
        self.mensagem.place(x=305,y=290,width=100,height=0) #mensagem se o cadastro ou login deu certo

        self.botao_entrar=tk.Button(root)
        self.botao_entrar["bg"] = "#49cfc1"
        ft = tkFont.Font(family='Arial',size=10)
        self.botao_entrar["font"] = ft
        self.botao_entrar["fg"] = "#ffffff"
        self.botao_entrar["justify"] = "center"
        self.botao_entrar["text"] = "Entrar"
        self.botao_entrar['bd'] = 0
        self.botao_entrar.place(x=305,y=330,width=0,height=0)
        self.botao_entrar["command"] = self.entrado #botao de entrar na página de login

        self.botao_cadastro=tk.Button(root)
        self.botao_cadastro["bg"] = "gray"
        ft = tkFont.Font(family='Arial',size=10)
        self.botao_cadastro["font"] = ft
        self.botao_cadastro["fg"] = "white"
        self.botao_cadastro["justify"] = "center"
        self.botao_cadastro["text"] = "Não tenho conta"
        self.botao_cadastro['bd'] = 0
        self.botao_cadastro.place(x=305,y=360,width=0,height=0)
        self.botao_cadastro["command"] = self.cadastro #botao caso não tenha conta

        self.vender=tk.Button(root)
        self.vender["bg"] = "darkgray"
        ft = tkFont.Font(family='Arial',size=10)
        self.vender["font"] = ft
        self.vender["fg"] = "white"
        self.vender["justify"] = "center"
        self.vender["text"] = "Vender produtos"
        self.vender['bd'] = 0
        self.vender.place(x=680,y=8,width=120,height=25)
        self.vender["command"] = self.vender_produtos #vender produtos

        self.botao_backup=tk.Button(root)
        self.botao_backup["bg"] = "darkgray"
        ft = tkFont.Font(family='Arial',size=10)
        self.botao_backup["font"] = ft
        self.botao_backup["fg"] = "white"
        self.botao_backup["justify"] = "center"
        self.botao_backup["text"] = "Backup"
        self.botao_backup['bd'] = 0
        self.botao_backup.place(x=540,y=8,width=120,height=25)
        self.botao_backup["command"] = self.backup #backup 

        self.botao_fechar=tk.Button(root)
        self.botao_fechar["bg"] = "red"
        ft = tkFont.Font(family='Arial',size=10)
        self.botao_fechar["font"] = ft
        self.botao_fechar["fg"] = "#ffffff"
        self.botao_fechar["justify"] = "center"
        self.botao_fechar["text"] = "X"
        self.botao_fechar['bd'] = 0
        self.botao_fechar.place(x=655,y=100,width=0,height=0)
        self.botao_fechar["command"] = self.fechar #botao de fechar a tela de login/cadastro

        #modelo1
        self.label_nomeProduto=tk.Label(root)
        self.label_nomeProduto["bg"] = "#000000"
        ft = tkFont.Font(family='Times',size=10)
        self.label_nomeProduto["font"] = ft
        self.label_nomeProduto["fg"] = "#333333"
        self.label_nomeProduto["justify"] = "center"
        self.label_nomeProduto["text"] = "Nome do produto"
        self.label_nomeProduto.place(x=20,y=80,width=129,height=45)

        self.label_descricao=tk.Label(root)
        self.label_descricao["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=10)
        self.label_descricao["font"] = ft
        self.label_descricao["fg"] = "#333333"
        self.label_descricao["justify"] = "center"
        self.label_descricao["text"] = "Descrição"
        self.label_descricao.place(x=20,y=125,width=129,height=45)

        self.label_disponivel=tk.Label(root)
        self.label_disponivel["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=10)
        self.label_disponivel["font"] = ft
        self.label_disponivel["fg"] = "#333333"
        self.label_disponivel["justify"] = "center"
        self.label_disponivel["text"] = "Status: Dispovível"
        self.label_disponivel.place(x=20,y=170,width=129,height=45)

        self.label_preco=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.label_preco["font"] = ft
        self.label_preco["fg"] = "#333333"
        self.label_preco["justify"] = "left"
        self.label_preco["text"] = "Preço"
        self.label_preco.place(x=20,y=215,width=70,height=30)

        self.button_comprar=tk.Button(root)
        self.button_comprar["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        self.button_comprar["font"] = ft
        self.button_comprar["fg"] = "#000000"
        self.button_comprar["justify"] = "center"
        self.button_comprar["text"] = "Informações"
        self.button_comprar.place(x=20,y=240,width=129,height=30)
        self.button_comprar["command"] = self.button_comprar_command
       
        #local de vender produtos
        self.label_venderProduto=tk.Label(root)
        ft = tkFont.Font(family='Times',size=15)
        self.label_venderProduto["font"] = ft
        self.label_venderProduto["fg"] = "#333333"
        self.label_venderProduto["justify"] = "center"
        self.label_venderProduto["text"] = "Criar produto"
        self.label_venderProduto.place(x=345,y=150,width=0,height=0)

        self.nome_do_produto=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.nome_do_produto["font"] = ft
        self.nome_do_produto["fg"] = "#333333"
        self.nome_do_produto["justify"] = "left"
        self.nome_do_produto["text"] = "Nome do produto:"
        self.nome_do_produto.place(x=245,y=195,width=0,height=0)

        self.caixa_nome_produto=tk.Entry(root)
        self.caixa_nome_produto["borderwidth"] = "1px"
        ft = tkFont.Font(family='Arial',size=10)
        self.caixa_nome_produto["font"] = ft
        self.caixa_nome_produto["fg"] = "#333333"
        self.caixa_nome_produto["justify"] = "left"
        self.caixa_nome_produto["text"] = "Nome"
        self.caixa_nome_produto.place(x=305,y=195,width=0,height=0)

        self.descricao_produto=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.descricao_produto["font"] = ft
        self.descricao_produto["fg"] = "#333333"
        self.descricao_produto["justify"] = "left"
        self.descricao_produto["text"] = "Descrição:"
        self.descricao_produto.place(x=245,y=240,width=0,height=0)

        self.caixa_descricao_de_produto=tk.Entry(root)
        self.caixa_descricao_de_produto["borderwidth"] = "1px"
        ft = tkFont.Font(family='Arial',size=10)
        self.caixa_descricao_de_produto["font"] = ft
        self.caixa_descricao_de_produto["fg"] = "#333333"
        self.caixa_descricao_de_produto["justify"] = "left"
        self.caixa_descricao_de_produto["text"] = "Descricao"
        self.caixa_descricao_de_produto.place(x=305,y=240,width=0,height=0)

        self.quantidadedo_produto=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.quantidadedo_produto["font"] = ft
        self.quantidadedo_produto["fg"] = "#333333"
        self.quantidadedo_produto["justify"] = "left"
        self.quantidadedo_produto["text"] = "Quantidade:"
        self.quantidadedo_produto.place(x=245,y=285,width=0,height=0)

        self.caixa_quantida_de_produto=tk.Entry(root)
        self.caixa_quantida_de_produto["borderwidth"] = "1px"
        ft = tkFont.Font(family='Arial',size=10)
        self.caixa_quantida_de_produto["font"] = ft
        self.caixa_quantida_de_produto["fg"] = "#333333"
        self.caixa_quantida_de_produto["justify"] = "left"
        self.caixa_quantida_de_produto["text"] = "Quantidade"
        self.caixa_quantida_de_produto.place(x=305,y=285,width=0,height=0)

        self.preco_produto=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.preco_produto["font"] = ft
        self.preco_produto["fg"] = "#333333"
        self.preco_produto["justify"] = "left"
        self.preco_produto["text"] = "Preço:"
        self.preco_produto.place(x=245,y=330,width=0,height=0)

        self.caixa_preco_de_produto=tk.Entry(root)
        self.caixa_preco_de_produto["borderwidth"] = "1px"
        ft = tkFont.Font(family='Arial',size=10)
        self.caixa_preco_de_produto["font"] = ft
        self.caixa_preco_de_produto["fg"] = "#333333"
        self.caixa_preco_de_produto["justify"] = "left"
        self.caixa_preco_de_produto["text"] = "Preco"
        self.caixa_preco_de_produto.place(x=305,y=330,width=0,height=0)

        self.mensagem_produto=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.mensagem_produto["font"] = ft
        self.mensagem_produto["fg"] = "#333333"
        self.mensagem_produto["justify"] = "center"
        self.mensagem_produto["text"] = ""
        self.mensagem_produto.place(x=335,y=365,width=0,height=0)

        self.button_criar_produto=tk.Button(root)
        self.button_criar_produto["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        self.button_criar_produto["font"] = ft
        self.button_criar_produto["fg"] = "#000000"
        self.button_criar_produto["justify"] = "center"
        self.button_criar_produto["text"] = "Criar Produto"
        self.button_criar_produto.place(x=295,y=400,width=0,height=0)
        self.button_criar_produto["command"] = self.criar_produto

        self.button_excluir_produto=tk.Button(root)
        self.button_excluir_produto["bg"] = "blue"
        ft = tkFont.Font(family='Times',size=10)
        self.button_excluir_produto["font"] = ft
        self.button_excluir_produto["fg"] = "#000000"
        self.button_excluir_produto["justify"] = "center"
        self.button_excluir_produto["text"] = "Excluir Produto tela"
        self.button_excluir_produto.place(x=425,y=400,width=0,height=0)
        self.button_excluir_produto["command"] = self.excluindo_produto

        self.status = ''
        self.usuarios = {}
    
    def botao_login_command(self):
        #deixando nada escrito na mensagem
        self.mensagem['text'] = ''

        #deixando todas as coisas de login para evitar bugs
        self.texto1['text'] = 'Entrar'
        self.texto1.place(x=380,width=70)

        self.botao_entrar['text'] = 'Entrar'
        self.botao_entrar.place(y=290)
        self.botao_entrar['command'] = self.entrado

        self.botao_cadastro['command'] = self.cadastro
        self.botao_cadastro['text'] = 'Não tenho conta'
        self.botao_cadastro.place(y=330)

        #aparece na tela
        self.botao_fechar.place(x=655,y=100,width=20,height=20)
        self.texto1.place(x=380,y=150,width=70,height=25)
        self.texto_login.place(x=245,y=195,width=70,height=25)
        self.caixa_login.place(x=305,y=195,width=237,height=30)
        self.texto_senha.place(x=245,y=240,width=70,height=25)
        self.caixa_senha.place(x=305,y=240,width=237,height=30)
        self.botao_entrar.place(x=305,y=300,width=234,height=32)
        self.botao_cadastro.place(x=305,y=340,width=234,height=32)

        #some na tela
        self.label_nomeProduto.place(x=20,y=80,width=0,height=0)
        self.label_descricao.place(width=0,height=0)
        self.label_preco.place(width=0,height=0)
        self.button_comprar.place(width=0,height=0)


        self.label_disponivel.place(width=0,height=0)
        self.texto_email.place(width=0,height=0)
        self.texto_telefone.place(width=0,height=0)
        self.caixa_email.place(width=0,height=0)
        self.caixa_telefone.place(width=0,height=0)
        self.label_venderProduto.place(width=0,height=0)
        self.button_excluir_produto.place(width=0,height=0)
        
        self.nome_do_produto.place(width=0,height=0)
        self.descricao_produto.place(width=0,height=0)
        self.preco_produto.place(width=0,height=0)
        self.quantidadedo_produto.place(width=0,height=0)
        self.caixa_quantida_de_produto.place(width=0,height=0)
        self.caixa_preco_de_produto.place(width=0,height=0)
        self.button_excluir_produto.place(width=0,height=0)
        self.button_criar_produto.place(width=0,height=0)
        self.mensagem_produto.place(width=0,height=0)

    def entrar(self):
        #apagando oq esá escrito no entry
        self.caixa_login.delete(0, 'end')
        self.caixa_senha.delete(0, 'end')
        self.caixa_email.delete(0, 'end')
        self.caixa_telefone.delete(0, 'end')

        #mudando para a tela de entrar, ou seja, mudando o titulo, botões e oq aparece
        self.texto1['text'] = 'Entrar'
        self.texto1.place(x=380,width=70,height=50)

        self.botao_entrar['text'] = 'Entrar'
        self.botao_entrar.place(y=290)
        self.botao_entrar['command'] = self.entrado

        #mudando a funcao e mudando o botao para cadastro
        self.botao_cadastro['command'] = self.cadastro
        self.botao_cadastro['text'] = 'Não tenho conta'
        self.botao_cadastro.place(y=330)

        #sumindo com os entry de cadastro caso venha de cadastro para login
        self.texto_login['text'] = 'Login:'
        self.texto_telefone.place(width=0,height=0)
        self.texto_email.place(width=0,height=0)
        self.caixa_email.place(width=0,height=0)
        self.caixa_telefone.place(width=0,height=0)

        self.botao_fechar.place(x=655,y=100,width=20,height=20)
        self.texto1.place(x=380,y=150,width=70,height=25)
        self.texto_login.place(x=245,y=195,width=70,height=25)
        self.caixa_login.place(x=305,y=195,width=237,height=30)
        self.texto_senha.place(x=245,y=240,width=70,height=25)
        self.caixa_senha.place(x=305,y=240,width=237,height=30)
        self.botao_entrar.place(x=305,y=300,width=234,height=32)
        self.botao_cadastro.place(x=305,y=340,width=234,height=32)

        self.mensagem['text'] = ''

    def cadastro(self):
        #mudando para a tela de cadastro
        self.mensagem['text'] = ''
        self.texto1['text'] = 'Cadastro'
        self.texto1.place(x=365,width=100)

        #mudando o botao de entrar para a função cadastro, pois ele agr cadastra e n entra na conta
        self.botao_entrar['text'] = 'Cadastrar'
        self.botao_entrar['command'] = self.cadastrado
        self.botao_entrar.place(y=390)

        #e o antigo botão de cadastrar leva para a tela de entrar
        self.botao_cadastro['text'] = 'Já tenho uma conta'
        self.botao_cadastro['command'] = self.entrar
        self.botao_cadastro.place(y=430)

        #aparecendo com as coisas para tela de cadastro
        self.texto_login['text'] = 'Nome:'
        self.texto_email.place(x=230,width=100,height=30)
        self.texto_telefone.place(x=225,width=100,height=30)
        self.caixa_email.place(width=237,height=30)
        self.caixa_telefone.place(width=237,height=30)

    def cadastrado(self):
        #aqui é após ir para a tela de cadastro e apertar em 'cadastrar'
        self.mensagem.place(x=322,y=360,width=200,height=25)
        self.mensagem['text'] = 'Usuário cadastrado com sucesso!'
        self.mensagem['fg'] = 'green'
        self.caixa_login.delete(0, 'end')
        self.caixa_senha.delete(0, 'end')
        self.caixa_email.delete(0, 'end')
        self.caixa_telefone.delete(0, 'end')
        #focus_set faz com q vá para o primeiro entry
        self.caixa_login.focus_set()

    def entrado(self):
        #aqui é após estar na tela de 'entrar' e ter apertado no botão 'entrar'
        self.mensagem.place(x=322,y=275,width=200,height=25)
        self.status = 'Entrado'
        self.mensagem['text'] = 'Entrado na conta com sucesso!'
        self.mensagem['fg'] = 'green'
        print('Entrado na conta com sucesso!')

        #apagando os entry
        self.caixa_login.delete(0, 'end')
        self.caixa_senha.delete(0, 'end')
        self.caixa_email.delete(0, 'end')
        self.caixa_telefone.delete(0, 'end')

        #criptografar senha
        ##senha_limpa = self.caixa_senha.get()
        ##senha = hashlib.md5(senha_limpa.encode('utf-8')).hexdigest()

    def fechar(self):
        if self.contador == 1:
            self.produto1()

        elif self.contador == 2:
            self.produto1()
            self.produto2()

        elif self.contador == 3:
            self.produto1()
            self.produto2()
            self.produto3()

        #some com tudo que está na tela
        self.mensagem_produto['text'] = ''
        self.mensagem_produto['fg'] = 'green'
        self.texto1.place(width=0,height=0)
        self.botao_fechar.place(width=0,height=0)
        self.mensagem.place(width=0,height=0)
        self.texto_login.place(width=0,height=0)
        self.caixa_login.place(width=0,height=0)
        self.texto_senha.place(width=0,height=0)
        self.caixa_senha.place(width=0,height=0)
        self.texto_email.place(width=0,height=0)
        self.caixa_email.place(width=0,height=0)
        self.texto_telefone.place(width=0,height=0)
        self.caixa_telefone.place(width=0,height=0)
        self.botao_entrar.place(width=0,height=0)
        self.botao_cadastro.place(width=0,height=0)
        self.label_descricao.place(width=129,height=45)
        self.label_preco.place(width=70,height=25)
        self.button_comprar.place(width=129,height=30)

        self.label_nomeProduto.place(x=20,y=80,width=129,height=45)
        
        self.caixa_quantida_de_produto.place(width=0,height=0)
        self.caixa_nome_produto.place(width=0,height=0)
        self.caixa_descricao_de_produto.place(width=0,height=0)
        self.caixa_preco_de_produto.place(width=0,height=0)
        self.descricao_produto.place(x=155,width=0,height=0)
        self.nome_do_produto.place(x=155,width=0,height=0)
        self.quantidadedo_produto.place(x=155,width=0,height=0)
        self.preco_produto.place(x=155, width=0,height=0)
        self.button_criar_produto.place(width=0,height=0)
        self.button_excluir_produto.place(width=0,height=0)
        self.mensagem_produto.place(width=0,height=300)
        self.caixa_descricao_de_produto.place(width=0,height=0)
        self.caixa_nome_produto.place(width=0,height=0)
        self.caixa_descricao_de_produto.place(width=0,height=0)
        self.caixa_quantida_de_produto.place(width=0,height=0)
        self.nome_do_produto.place(width=0,height=0)
        self.descricao_produto.place(width=0,height=0)
        self.label_disponivel.place(width=129,height=45)
        self.label_venderProduto.place(width=0,height=0)

        #apagar os entry
        self.caixa_login.delete(0, 'end')
        self.caixa_quantida_de_produto.delete(0, 'end')
        self.caixa_descricao_de_produto.delete(0, 'end')
        self.caixa_email.delete(0, 'end')
        self.caixa_nome_produto.delete(0, 'end')
        self.caixa_telefone.delete(0, 'end')
        self.caixa_senha.delete(0, 'end')
        self.caixa_preco_de_produto.delete(0, 'end')

        self.caixa_nome_produto.focus_set()
        
    def botao_entrar_command(self):
        pass

    def botao_cadastro_command(self):
        print("command")

    def button_comprar_command(self):
        self.label_alugado=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.label_alugado["font"] = ft
        self.label_alugado["fg"] = "green"
        self.label_alugado["justify"] = "center"
        self.label_alugado["text"] = "Alugado com sucesso !"
        self.label_alugado.place(x=620,y=520,width=129,height=45) 

    def vender_produtos(self):
        #sumir tudo da tela
        self.mensagem_produto['text'] = ''
        self.mensagem_produto['fg'] = 'green'
        self.mensagem_produto.place(y=365)

        self.produtos_desaparecer()
        self.texto1.place(width=0,height=0)
        self.mensagem.place(width=0,height=0)
        self.texto_login.place(width=0,height=0)
        self.caixa_login.place(width=0,height=0)
        self.texto_senha.place(width=0,height=0)
        self.caixa_senha.place(width=0,height=0)
        self.texto_email.place(width=0,height=0)
        self.caixa_email.place(width=0,height=0)
        self.texto_telefone.place(width=0,height=0)
        self.caixa_telefone.place(width=0,height=0)
        self.botao_entrar.place(width=0,height=0)
        self.botao_cadastro.place(width=0,height=0)
        self.label_nomeProduto.place(x=20,y=80,width=0,height=0)
        self.label_descricao.place(width=0,height=0)
        self.label_preco.place(width=0,height=0)
        self.button_comprar.place(width=0,height=0)
        self.label_disponivel.place(width=0,height=0)
        
        #aparecer as coisas na tela vender
        self.label_venderProduto.place(width=150,height=30)
        self.botao_fechar.place(x=655,y=100,width=20,height=20)
        self.caixa_quantida_de_produto.place(width=237,height=30)
        self.caixa_nome_produto.place(width=237,height=30)
        self.caixa_descricao_de_produto.place(width=237,height=30)
        self.caixa_preco_de_produto.place(width=237,height=30)
        self.descricao_produto.place(x=155,width=129,height=30)
        self.nome_do_produto.place(x=155,width=129,height=30)
        self.quantidadedo_produto.place(x=155,width=129,height=30)
        self.preco_produto.place(x=155, width=129,height=30)
        self.button_criar_produto.place(y=400,width=115,height=30)
        self.button_excluir_produto.place(y=400, width=115,height=30)
        self.mensagem_produto.place(width=170,height=30)

        self.button_criar_produto["bg"] = "light green"
        self.button_criar_produto["fg"] = "#000000"
        self.button_criar_produto["text"] = "Criar Produto"
        self.button_criar_produto["command"] = self.criar_produto

        self.button_excluir_produto["bg"] = "red"
        self.button_excluir_produto["fg"] = "#000000"
        self.button_excluir_produto["text"] = "Excluir Produto"
        self.button_excluir_produto["command"] = self.tela_d_excluir

        self.mensagem_produto['text'] = ''

    def backup(self):
        self.db.backupdb()

    def tela_d_excluir(self):
        print('tela de excluir os produtos')
        
        self.button_excluir_produto['text'] = 'Voltar'
        self.button_excluir_produto['command'] = self.vender_produtos
        self.button_excluir_produto.place(y=250)
        self.button_excluir_produto['bg'] = 'yellow'

        self.button_criar_produto['text'] = 'Excluir'
        self.button_criar_produto['command'] = self.excluindo_produto
        self.button_criar_produto['bg'] = 'red'
        self.button_criar_produto.place(y=250)

        self.mensagem_produto['text'] = ''

        self.descricao_produto.place(width=0,height=0)
        self.preco_produto.place(width=0,height=0)
        self.quantidadedo_produto.place(width=0,height=0)
        self.caixa_quantida_de_produto.place(width=0,height=0)
        self.caixa_preco_de_produto.place(width=0,height=0)
        self.caixa_descricao_de_produto.place(width=0,height=0)

    def produtos_desaparecer(self):
        if self.contador >1:
            self.label_nomeProduto1.place(x=160,y=80,width=0,height=0)
            self.label_descricao1.place(x=160,y=125,width=0,height=0)
            self.label_disponivel1.place(x=160,y=170,width=0,height=0)
            self.label_preco1.place(x=160,y=215,width=0,height=0)
            self.button_comprar1.place(x=160,y=240,width=0,height=0)

            self.label_nomeProduto2.place(x=160,y=80,width=0,height=0)
            self.label_descricao2.place(x=160,y=125,width=0,height=0)
            self.label_disponivel2.place(x=160,y=170,width=0,height=0)
            self.label_preco2.place(x=160,y=215,width=0,height=0)
            self.button_comprar2.place(x=160,y=240,width=0,height=0)

            self.label_nomeProduto3.place(x=160,y=80,width=0,height=0)
            self.label_descricao3.place(x=160,y=125,width=0,height=0)
            self.label_disponivel3.place(x=160,y=170,width=0,height=0)
            self.label_preco3.place(x=160,y=215,width=0,height=0)
            self.button_comprar3.place(x=160,y=240,width=0,height=0)

    def produto1(self):
        self.label_nomeProduto1=tk.Label(root)
        self.label_nomeProduto1["bg"] = "#000000"
        ft = tkFont.Font(family='Times',size=10)
        self.label_nomeProduto1["font"] = ft
        self.label_nomeProduto1["fg"] = "#333333"
        self.label_nomeProduto1["justify"] = "center"
        self.label_nomeProduto1["text"] = self.matriz_ldv[0][0]
        self.label_nomeProduto1.place(x=160,y=80,width=129,height=45)

        self.label_descricao1=tk.Label(root)
        self.label_descricao1["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=10)
        self.label_descricao1["font"] = ft
        self.label_descricao1["fg"] = "#333333"
        self.label_descricao1["justify"] = "center"
        self.label_descricao1["text"] = self.matriz_ldv[0][1]
        self.label_descricao1.place(x=160,y=125,width=129,height=45)

        self.label_disponivel1=tk.Label(root)
        self.label_disponivel1["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=10)
        self.label_disponivel1["font"] = ft
        self.label_disponivel1["fg"] = "#333333"
        self.label_disponivel1["justify"] = "center"
        self.label_disponivel1["text"] = "Status: Dispovível"
        self.label_disponivel1.place(x=160,y=170,width=129,height=45)

        self.label_preco1=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.label_preco1["font"] = ft
        self.label_preco1["fg"] = "#333333"
        self.label_preco1["justify"] = "left"
        self.label_preco1["text"] = self.matriz_ldv[0][3]
        self.label_preco1.place(x=160,y=215,width=70,height=30)

        self.button_comprar1=tk.Button(root)
        self.button_comprar1["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        self.button_comprar1["font"] = ft
        self.button_comprar1["fg"] = "#000000"
        self.button_comprar1["justify"] = "center"
        self.button_comprar1["text"] = "alugar"
        self.button_comprar1.place(x=160,y=240,width=129,height=30)
        self.button_comprar1["command"] = self.button_comprar_command
        
    def produto2(self):
        self.label_nomeProduto2=tk.Label(root)
        self.label_nomeProduto2["bg"] = "#000000"
        ft = tkFont.Font(family='Times',size=10)
        self.label_nomeProduto2["font"] = ft
        self.label_nomeProduto2["fg"] = "#333333"
        self.label_nomeProduto2["justify"] = "center"
        self.label_nomeProduto2["text"] = self.matriz_ldv[1][0]
        self.label_nomeProduto2.place(x=300,y=80,width=129,height=45)

        self.label_descricao2=tk.Label(root)
        self.label_descricao2["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=10)
        self.label_descricao2["font"] = ft
        self.label_descricao2["fg"] = "#333333"
        self.label_descricao2["justify"] = "center"
        self.label_descricao2["text"] = self.matriz_ldv[1][1]
        self.label_descricao2.place(x=300,y=125,width=129,height=45)

        self.label_disponivel2=tk.Label(root)
        self.label_disponivel2["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=10)
        self.label_disponivel2["font"] = ft
        self.label_disponivel2["fg"] = "#333333"
        self.label_disponivel2["justify"] = "center"
        self.label_disponivel2["text"] = "Status: Dispovível"
        self.label_disponivel2.place(x=300,y=170,width=129,height=45)

        self.label_preco2=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.label_preco2["font"] = ft
        self.label_preco2["fg"] = "#333333"
        self.label_preco2["justify"] = "left"
        self.label_preco2["text"] = self.matriz_ldv[1][3]
        self.label_preco2.place(x=300,y=215,width=70,height=30)

        self.button_comprar2=tk.Button(root)
        self.button_comprar2["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        self.button_comprar2["font"] = ft
        self.button_comprar2["fg"] = "#000000"
        self.button_comprar2["justify"] = "center"
        self.button_comprar2["text"] = "alugar"
        self.button_comprar2.place(x=300,y=240,width=129,height=30)
        self.button_comprar2["command"] = self.button_comprar_command

    def produto3(self):
        self.label_nomeProduto3=tk.Label(root)
        self.label_nomeProduto3["bg"] = "#000000"
        ft = tkFont.Font(family='Times',size=10)
        self.label_nomeProduto3["font"] = ft
        self.label_nomeProduto3["fg"] = "#333333"
        self.label_nomeProduto3["justify"] = "center"
        self.label_nomeProduto3["text"] = self.matriz_ldv[2][0]
        self.label_nomeProduto3.place(x=440,y=80,width=129,height=45)

        self.label_descricao3=tk.Label(root)
        self.label_descricao3["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=10)
        self.label_descricao3["font"] = ft
        self.label_descricao3["fg"] = "#333333"
        self.label_descricao3["justify"] = "center"
        self.label_descricao3["text"] = self.matriz_ldv[2][1]
        self.label_descricao3.place(x=440,y=125,width=129,height=45)

        self.label_disponivel3=tk.Label(root)
        self.label_disponivel3["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=10)
        self.label_disponivel3["font"] = ft
        self.label_disponivel3["fg"] = "#333333"
        self.label_disponivel3["justify"] = "center"
        self.label_disponivel3["text"] = "Status: Dispovível"
        self.label_disponivel3.place(x=440,y=170,width=129,height=45)

        self.label_preco3=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.label_preco3["font"] = ft
        self.label_preco3["fg"] = "#333333"
        self.label_preco3["justify"] = "left"
        self.label_preco3["text"] = self.matriz_ldv[2][3]
        self.label_preco3.place(x=440,y=215,width=70,height=30)

        self.button_comprar3=tk.Button(root)
        self.button_comprar3["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        self.button_comprar3["font"] = ft
        self.button_comprar3["fg"] = "#000000"
        self.button_comprar3["justify"] = "center"
        self.button_comprar3["text"] = "alugar"
        self.button_comprar3.place(x=440,y=240,width=129,height=30)
        self.button_comprar3["command"] = self.button_comprar_command

    def criar_produto(self):
        try:
            
            self.contador += 1
            
            self.lista_de_valores = []
            get1 = self.caixa_nome_produto.get()
            get2 = self.caixa_descricao_de_produto.get()
            get3 = self.caixa_quantida_de_produto.get()
            get4 = self.caixa_preco_de_produto.get()
            self.lista_de_valores.append(get1)
            self.lista_de_valores.append(get2)
            self.lista_de_valores.append(get3)
            self.lista_de_valores.append(get4)
            self.matriz_ldv.append(self.lista_de_valores)
            print(self.matriz_ldv)
            
            #cria o produto
            self.mensagem_produto['text'] = 'Produto criado com sucesso!'
            self.mensagem_produto['fg'] = 'green'

            # Adiciona os produtos no banco
            self.db.criar_abrir_db()
            self.db.cria_lista()
            self.db.adicionar(self.caixa_nome_produto.get(), self.caixa_descricao_de_produto.get(), self.caixa_quantida_de_produto.get(), self.caixa_preco_de_produto.get())
        except Exception:
            self.db.fechardb()
            self.mensagem_produto['text'] = 'O produto já existe!'
            pass

    def excluindo_produto(self):
        try:
            self.contador -=1
            print(self.contador)
            self.get_excluir = self.caixa_nome_produto.get()
            print(self.get_excluir)
            
            self.j_m = len(self.matriz_ldv)
            if self.get_excluir == self.matriz_ldv[0][0]:
                self.excluir_p = self.matriz_ldv.pop(0)

            if self.get_excluir == self.matriz_ldv[1][0]:
                self.excluir_p = self.matriz_ldv.pop(1)
                
            if self.get_excluir == self.matriz_ldv[2][0]:
                self.excluir_p = self.matriz_ldv.pop(1)
            
            self.mensagem_produto.place(y=225)
            self.mensagem_produto['fg'] = 'red'
            self.mensagem_produto['text'] = 'Produto excluido com sucesso!'
            print(self.matriz_ldv)
        except:
            self.mensagem_produto['text'] = 'alguma coisa deu errado!!!'


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
