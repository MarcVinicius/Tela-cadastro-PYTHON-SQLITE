import sqlite3
from unittest import FunctionTestCase

from PyQt5 import QtCore, QtGui, QtWidgets

from tela_cadastrar import Ui_Form
from tela_main import Ui_main_wIndow
from tela_editar import Ui_tela_editar


#classe tela principal
class main(QtWidgets.QApplication, Ui_main_wIndow):
    def __init__(self):
        super().__init__()
        self.setup(self)

#classe tela cadastrar e editar
class cadastrar(QtWidgets.QApplication, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setup(self)

#classe tela editar
class editar(QtWidgets.QApplication, Ui_tela_editar):
    def __init__(self):
        super().__init__()
        self.setup(self)

#Classe conexao banco
class conexao:
    def __init__(self, comando):
        self.conn = sqlite3.connect('Banco/prod.db')
        self.comando = comando
        #self.cursor = self.conn.cursor()
        #self.cursor.execute(comando)
        #self.conn.commit()
        #self.conn.close()
        #return conn

    def insert_update(self):
        cursor = self.conn.cursor()
        cursor.execute(self.comando)
        self.conn.commit()
        self.conn.close()
        #return conn
    
    def fetchall(self):
        cursor = self.conn.cursor()
        consulta = cursor.execute(self.comando)
        consulta_fe = consulta.fetchall()
        return consulta_fe
    
#chamando telas func
class chamarTelaFunc:
    def __init__(self):
        pass

    def cad(self, form, ui):
        form.show()
        Form.setWindowTitle("Cadastrar")
        Form.setFixedSize(505, 475)
        #ui.nome_lnedit.setText("teste")

    def edit(self, Form, ui):
        Form.show()
        Form.setWindowTitle("Manutenção Registro")

#editando dados funcionario
class inserirEditarFunc:
    def __init__(self, nome, login, senha, senha2, dtnasc, codsetor):
        self.nome = nome
        self.login = login
        self.senha = senha
        self.senha2 = senha2
        self.dtnasc = dtnasc
        self.codsetor = codsetor       
    
    def inserir(self):
        if '' not in (self.nome, self.login, self.senha, self.senha2, self.dtnasc, self.codsetor):
            if self.senha == self.senha2:
                try:
                    conexao(f"""INSERT INTO FUNC (nome, loginbd, senhabd, dtcadastro, ativo, dtinativacao, dtnasc, codsetor) values ('{self.nome}', '{self.login}', '{self.senha}', DATE('now'), 'S', null, '{self.dtnasc}', '{int(self.codsetor)}')""").insert_update()
                except:
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle("ERRO")
                    msg.setText("Erro ao gravar dados")
                    msg.exec_()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("ERRO")
                msg.setText("As senhas devem ser iguais")
                msg.exec_()

        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("ERRO")
            msg.setText("Preencha todos os campos")
            msg.exec_()



#chamar tela cadastro/edicao
def chamar_tela_cadastro():
    def chamar_tela_cad():
        chamarTelaFunc().cad(Form, ui2)

    ui.criar_btt.clicked.connect(chamar_tela_cad)

def chamar_tela_editar():
    def chamar_tela_edit():
        chamarTelaFunc().edit(tela_editar, ui3)

    ui.manutencao_btt.clicked.connect(chamar_tela_edit)

def cadastrar():
    def cadastrar_func():
        nome = ui2.nome_lnedit.text()
        login = ui2.login_lnedit.text()
        senha = ui2.senha_lnedit.text()
        senha2 = ui2.senha2_lnedit.text()
        dtnasc = ui2.datanasc_lnedit.text()
        codsetor = ui2.codsetor_lnedit.text()

        inserirEditarFunc(nome, login, senha, senha2, dtnasc, codsetor).inserir()
    
    ui2.salvar_btt.clicked.connect(cadastrar_func)

def tela_pesquisa():
    def pesquisar():
        campo = ui3.textopesquisa_lnedit.text()

        if campo == '':
            consulta_fe = conexao("SELECT ID, NOME, DTCADASTRO, CASE WHEN ATIVO = 'S' THEN 'ATIVO' ELSE 'INATIVO' END AS SITUACAO, DTINATIVACAO, DTNASC, CODSETOR, CODSETOR FROM FUNC").fetchall()
            ui3.tabela.setRowCount(len(consulta_fe))

            print(str(consulta_fe))

            for i in range(0, len(consulta_fe)):
                for j in range(0, 8):
                    ui3.tabela.setItem(i, j, QtWidgets.QTableWidgetItem(str(consulta_fe[i][j])))

            ui3.tabela.verticalHeader().setVisible(False)
        
        else:
            if ui3.pesquisa_cbbox.currentText() == 'CODIGO':
                if campo.isnumeric():
                    consulta_fe = conexao(f"SELECT ID, NOME, DTCADASTRO, CASE WHEN ATIVO = 'S' THEN 'ATIVO' ELSE 'INATIVO' END AS SITUACAO, DTINATIVACAO, DTNASC, CODSETOR, CODSETOR FROM FUNC WHERE ID = {int(campo)}").fetchall()
                    ui3.tabela.setRowCount(len(consulta_fe))

                    for i in range(0, len(consulta_fe)):
                        for j in range(0, 8):
                            ui3.tabela.setItem(i, j, QtWidgets.QTableWidgetItem(str(consulta_fe[i][j])))

                    ui3.tabela.verticalHeader().setVisible(False)

            else:
                consulta_fe = conexao(f"SELECT ID, NOME, DTCADASTRO, CASE WHEN ATIVO = 'S' THEN 'ATIVO' ELSE 'INATIVO' END AS SITUACAO, DTINATIVACAO, DTNASC, CODSETOR, CODSETOR FROM FUNC WHERE NOME LIKE '%{campo}%'").fetchall()
                ui3.tabela.setRowCount(len(consulta_fe))

                for i in range(0, len(consulta_fe)):
                    for j in range(0, 8):
                        ui3.tabela.setItem(i, j, QtWidgets.QTableWidgetItem(str(consulta_fe[i][j])))

                ui3.tabela.verticalHeader().setVisible(False)

    def fechar():
        tela_editar.close()

    ui3.pesquisar_btt.clicked.connect(pesquisar)
    ui3.fechar_btt.clicked.connect(fechar)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_wIndow = QtWidgets.QWidget()
    Form = QtWidgets.QWidget()
    tela_editar = QtWidgets.QWidget()
    #tela principal
    ui = Ui_main_wIndow()
    ui.setupUi(main_wIndow)
    #tela cadastro/edição
    ui2 = Ui_Form()
    ui2.setupUi(Form)
    #tela edição
    ui3 = Ui_tela_editar()
    ui3.setupUi(tela_editar)
    #mostrar tela principal
    main_wIndow.show()
    #funcoes
    chamar_tela_cadastro()
    chamar_tela_editar()
    tela_pesquisa()
    cadastrar()
    sys.exit(app.exec_())