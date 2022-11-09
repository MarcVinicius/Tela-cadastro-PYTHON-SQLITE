from unittest import FunctionTestCase
from PyQt5 import QtCore, QtGui, QtWidgets
from tela_main import Ui_main_wIndow
from tela_cadastrar import Ui_Form

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

#chamar tela cadastro/edicao
def chamar_tela_cadastro():
    def chamar_tela_cad():
        Form.show()

    ui.criar_btt.clicked.connect(chamar_tela_cad)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_wIndow = QtWidgets.QWidget()
    Form = QtWidgets.QWidget()
    #tela principal
    ui = Ui_main_wIndow()
    ui.setupUi(main_wIndow)
    #tela cadastro/edição
    ui2 = Ui_Form()
    ui2.setupUi(Form)
    main_wIndow.show()
    #funcoes
    chamar_tela_cadastro()
    sys.exit(app.exec_())