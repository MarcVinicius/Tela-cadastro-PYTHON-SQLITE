import sqlite3
from unittest import FunctionTestCase

from PyQt5 import QtCore, QtGui, QtWidgets

from tela_cadastrar import Ui_Form
from tela_main import Ui_main_wIndow
from tela_editar import Ui_tela_editar

#propiedades globais
estado = 0 #se = 1 inserir, se = 2 editar
codfuncedit = 0 #codigo do funcionario que esta sendo editado


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

    def insert_update(self):
        cursor = self.conn.cursor()
        cursor.execute(self.comando)
        self.conn.commit()
        self.conn.close()
    
    def fetchall(self):
        cursor = self.conn.cursor()
        consulta = cursor.execute(self.comando)
        consulta_fe = consulta.fetchall()
        return consulta_fe

    def fetchone(self):
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

    def lista(self, Form, ui):
        Form.show()
        Form.setWindowTitle("Manutenção Registro")

    def edit(self, Form, ui, nome, login, dtnasc, codsetor):
        Form.show()
        Form.setFixedSize(505, 475)
        Form.setWindowTitle("Manutenção Registro")
        ui.nome_lnedit.setText(nome)
        ui.login_lnedit.setText(login)
        ui.datanasc_lnedit.setText(dtnasc)
        ui.codsetor_lnedit.setText(codsetor)

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
        estado = 1

    ui.criar_btt.clicked.connect(chamar_tela_cad)

def chamar_tela_lista():
    def chamar_tela_list():
        chamarTelaFunc().lista(tela_editar, ui3)

    ui.manutencao_btt.clicked.connect(chamar_tela_list)
    
def chamar_tela_editar():
    def chamar_tela_edit():
        linhaatual = ui3.tabela.currentRow()
        try:
            consulta_fe = conexao(f"SELECT * FROM FUNC WHERE ID = {str(ui3.tabela.item(linhaatual, 0).text())}").fetchone()
            print(consulta_fe[0][0])
            #codigo = ui3.tabela.item(linhaatual, )
            usuario = consulta_fe[0][1]
            login = consulta_fe[0][2]
            dtnasc= consulta_fe[0][7]
            codsetor = str(consulta_fe[0][8])
            codfuncedit = int(consulta_fe[0][0])
            estado = 2
            chamarTelaFunc().edit(Form, ui2, usuario, login, dtnasc, codsetor)
        
        except:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("ERRO")
            msg.setText("Selecione um registro")
            msg.exec_()

    ui3.editar_btt.clicked.connect(chamar_tela_edit)

#ui3.editar_btt.clicked.connect(chamar_tela_editar)

def cadastrar():
    def cadastrar_func():
        nome = ui2.nome_lnedit.text()
        login = ui2.login_lnedit.text()
        senha = ui2.senha_lnedit.text()
        senha2 = ui2.senha2_lnedit.text()
        dtnasc = ui2.datanasc_lnedit.text()
        codsetor = ui2.codsetor_lnedit.text()
        
        if estado == 1:
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
        tela_editar.destroy()

    #inativando usuario
    def inativar_ativar():
        linhaatual = ui3.tabela.currentRow()
        if linhaatual != -1:
            consulta_fe = conexao(f"SELECT * FROM FUNC WHERE ID = {str(ui3.tabela.item(linhaatual, 0).text())}").fetchone()
            codfunc = consulta_fe[0][0]
            situacao = consulta_fe[0][5]

            if situacao == 'S':
                conexao(f"UPDATE FUNC SET ATIVO = 'N', DTINATIVACAO = DATE('now') WHERE ID = {codfunc}").insert_update()
                ui3.tabela.setItem(int(linhaatual), 3, QtWidgets.QTableWidgetItem('INATIVO'))
                ui3.tabela.setItem(int(linhaatual), 4, QtWidgets.QTableWidgetItem('HOJE'))
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("ERRO")
                msg.setText("Usuario inativado com sucesso")
                msg.exec_()
            
            else:
                conexao(f"UPDATE FUNC SET ATIVO = 'S' WHERE ID = {codfunc}").insert_update()
                ui3.tabela.setItem(int(linhaatual), 3, QtWidgets.QTableWidgetItem('ATIVO'))
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("ERRO")
                msg.setText("Usuario ativado com sucesso")
                msg.exec_()
                
    ui3.pesquisar_btt.clicked.connect(pesquisar)
    ui3.fechar_btt.clicked.connect(fechar)
    ui3.inativar_btt.clicked.connect(inativar_ativar)

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
    chamar_tela_lista()
    chamar_tela_editar()
    tela_pesquisa()
    cadastrar()
    sys.exit(app.exec_())