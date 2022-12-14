# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_cadastrar.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(505, 475)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(120, 10, 251, 211))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formulario = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formulario.setContentsMargins(0, 0, 0, 0)
        self.formulario.setObjectName("formulario")
        self.nome_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.nome_label.setObjectName("nome_label")
        self.formulario.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nome_label)
        self.login_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.login_label.setObjectName("login_label")
        self.formulario.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.login_label)
        self.senha_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.senha_label.setObjectName("senha_label")
        self.formulario.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.senha_label)
        self.datanasc_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.datanasc_label.setObjectName("datanasc_label")
        self.formulario.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.datanasc_label)
        self.codsetor_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.codsetor_label.setObjectName("codsetor_label")
        self.formulario.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.codsetor_label)
        self.nome_lnedit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.nome_lnedit.setObjectName("nome_lnedit")
        self.formulario.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nome_lnedit)
        self.login_lnedit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.login_lnedit.setObjectName("login_lnedit")
        self.formulario.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.login_lnedit)
        self.senha_lnedit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.senha_lnedit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.senha_lnedit.setClearButtonEnabled(False)
        self.senha_lnedit.setObjectName("senha_lnedit")
        self.formulario.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.senha_lnedit)
        self.datanasc_lnedit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.datanasc_lnedit.setObjectName("datanasc_lnedit")
        self.formulario.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.datanasc_lnedit)
        self.codsetor_lnedit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.codsetor_lnedit.setObjectName("codsetor_lnedit")
        self.formulario.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.codsetor_lnedit)
        self.senha2_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.senha2_label.setObjectName("senha2_label")
        self.formulario.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.senha2_label)
        self.senha2_lnedit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.senha2_lnedit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.senha2_lnedit.setObjectName("senha2_lnedit")
        self.formulario.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.senha2_lnedit)
        self.versenha_ckbox = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.versenha_ckbox.setObjectName("versenha_ckbox")
        self.formulario.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.versenha_ckbox)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(340, 390, 160, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.form_botoes = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.form_botoes.setContentsMargins(0, 0, 0, 0)
        self.form_botoes.setObjectName("form_botoes")
        self.salvar_btt = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.salvar_btt.setObjectName("salvar_btt")
        self.form_botoes.addWidget(self.salvar_btt)
        self.cancelar_btt = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.cancelar_btt.setObjectName("cancelar_btt")
        self.form_botoes.addWidget(self.cancelar_btt)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.nome_lnedit, self.login_lnedit)
        Form.setTabOrder(self.login_lnedit, self.senha_lnedit)
        Form.setTabOrder(self.senha_lnedit, self.senha2_lnedit)
        Form.setTabOrder(self.senha2_lnedit, self.datanasc_lnedit)
        Form.setTabOrder(self.datanasc_lnedit, self.codsetor_lnedit)
        Form.setTabOrder(self.codsetor_lnedit, self.versenha_ckbox)
        Form.setTabOrder(self.versenha_ckbox, self.salvar_btt)
        Form.setTabOrder(self.salvar_btt, self.cancelar_btt)

        def visibilidade_senha():
            if self.versenha_ckbox.isChecked() == True:
                self.senha2_lnedit.setEchoMode(QtWidgets.QLineEdit.Normal)
                self.senha_lnedit.setEchoMode(QtWidgets.QLineEdit.Normal)

            else:
                self.senha2_lnedit.setEchoMode(QtWidgets.QLineEdit.Password)
                self.senha_lnedit.setEchoMode(QtWidgets.QLineEdit.Password)
        
        self.versenha_ckbox.clicked.connect(visibilidade_senha)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.nome_label.setText(_translate("Form", "NOME"))
        self.login_label.setText(_translate("Form", "LOGIN"))
        self.senha_label.setText(_translate("Form", "SENHA"))
        self.datanasc_label.setText(_translate("Form", "DATA NASC."))
        self.codsetor_label.setText(_translate("Form", "CODSETOR"))
        self.senha2_label.setText(_translate("Form", "REPETIR SENHA"))
        self.versenha_ckbox.setText(_translate("Form", "Ver senha"))
        self.salvar_btt.setText(_translate("Form", "SALVAR"))
        self.cancelar_btt.setText(_translate("Form", "CANCELAR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
