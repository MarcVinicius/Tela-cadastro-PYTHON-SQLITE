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
        conn = sqlite3.connect('Banco/prod.db')
        cursor = conn.cursor()
        cursor.execute(comando)
        conn.commit()
        conn.close()
        #return conn

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
                    conexao(f"""INSERT INTO FUNC (nome, loginbd, senhabd, dtcadastro, ativo, dtinativacao, dtnasc, codsetor) values ('{self.nome}', '{self.login}', '{self.senha}', DATE('now'), 'S', null, '{self.dtnasc}', '{int(self.codsetor)}')""")
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
    cadastrar()
    sys.exit(app.exec_())