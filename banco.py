import sqlite3

class Banco:
    def __init__(self):
        self.nome_tabela = 'tabela_teste'

    # Cria o banco
    def criar_abrir_db(self, nomedb):
        # Cria/conecta o banco
        self.con = sqlite3.connect(nomedb + '.db')
        self.sql = self.con.cursor()

    # Fecha o banco
    def fechardb(self):
        self.con.close()

    # Cria a lista no banco
    def cria_lista(self):
        # Cria a lista caso a mesma não esteja criada
        try:
            self.sql.execute(f'CREATE TABLE {self.nome_tabela} (nome, descricao, quant, preco)')
        except:
            pass


    # Ajustar conforme o código do TK:
    def adicionar(self, nome, descricao, quant, preco):
        # Adiciona os valores no banco
        self.sql.execute(f"INSERT INTO {self.nome_tabela} (nome, descricao, quant, preco) VALUES ('{nome}', '{descricao}', '{quant}', '{preco}')")
        self.con.commit()
    

    # Ajustar conforme o código do TK
    def mostra(self):
        # Pega todos os valores do banco
        self.sql.execute("SELECT * FROM tabela_teste") 
        self.reg = self.sql.fetchall()
    
    
    # Ajustar conforme o código do TK:
    def deletar(self, parametro, valor):
        # Seleciona e deleta o valor passado
        self.sql.execute(f"DELETE FROM {self.nome_tabela} WHERE {parametro} = '{valor}'")
        self.con.commit()


    def backupdb(self, nomearq):
        self.arq = open(nomearq+'.txt', 'b+a')
        self.sql.execute("SELECT * FROM tabela_teste") 
        self.registros = self.sql.fetchall()
        self.arquivos = {}
        self.listaarq = []
        for a in self.registros:
            self.cont = 0
            while True:
                self.arquivos['nome'] = a[0]
                self.arquivos['descricao'] = a[1]
                self.arquivos['quant'] = a[2]
                self.arquivos['valor'] = a[3]
                self.listaarq.append(self.arquivos.copy())
                break
        for d in self.listaarq:
            for k, v in d.items():
                self.arq.write(f'{k}: {v}')
