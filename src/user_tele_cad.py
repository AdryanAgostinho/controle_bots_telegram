# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_tele_cad.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from bd import bd
import vglobal
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem,QCheckBox, QMessageBox

class Ui_Form_user_tele_cad(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(464, 200)
        Form.setMinimumSize(QtCore.QSize(464, 200))
        Form.setMaximumSize(QtCore.QSize(464, 200))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/soui/sou.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("QWidget#Form{\n"
"    background-image: url(:/fundo/fundo.png);\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setStyleSheet("QFrame#frame{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 3px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(360, 90, 73, 17))
        self.checkBox.setObjectName("checkBox")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(10, 10, 420, 80))
        self.widget.setObjectName("widget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.line_nome = QtWidgets.QLineEdit(self.widget)
        self.line_nome.setObjectName("line_nome")
        self.gridLayout.addWidget(self.line_nome, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.line_id_tele = QtWidgets.QLineEdit(self.widget)
        self.line_id_tele.setObjectName("line_id_tele")
        self.gridLayout_2.addWidget(self.line_id_tele, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.line_cod_rca = QtWidgets.QLineEdit(self.widget)
        self.line_cod_rca.setObjectName("line_cod_rca")
        self.gridLayout_3.addWidget(self.line_cod_rca, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)
        self.line_cod_magento = QtWidgets.QLineEdit(self.widget)
        self.line_cod_magento.setObjectName("line_cod_magento")
        self.gridLayout_4.addWidget(self.line_cod_magento, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_4, 1, 1, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_5.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 2, 0, 1, 2)
        self.widget1 = QtWidgets.QWidget(self.frame)
        self.widget1.setGeometry(QtCore.QRect(9, 112, 431, 56))
        self.widget1.setObjectName("widget1")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.bt_salvar = QtWidgets.QPushButton(self.widget1)
        self.bt_salvar.setMinimumSize(QtCore.QSize(0, 10))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/buscar/salvar.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_salvar.setIcon(icon1)
        self.bt_salvar.setObjectName("bt_salvar")
        self.gridLayout_7.addWidget(self.bt_salvar, 0, 0, 1, 1)
        self.bt_voltar = QtWidgets.QPushButton(self.widget1)
        self.bt_voltar.setMinimumSize(QtCore.QSize(0, 10))
        self.bt_voltar.setStyleSheet("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/buscar/voltar.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_voltar.setIcon(icon2)
        self.bt_voltar.setObjectName("bt_voltar")
        self.gridLayout_7.addWidget(self.bt_voltar, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cadastrar Usuário"))
        self.checkBox.setText(_translate("Form", "Bloqueado"))
        self.label.setText(_translate("Form", "Nome:"))
        self.label_2.setText(_translate("Form", "Id_tele:"))
        self.label_3.setText(_translate("Form", "Cod_rca:"))
        self.label_4.setText(_translate("Form", "Cod_magento:"))
        self.label_5.setText(_translate("Form", "Cod_superv:"))
        self.bt_salvar.setText(_translate("Form", "salvar"))
        self.bt_voltar.setText(_translate("Form", "Voltar"))
        self.bt_voltar.clicked.connect(lambda: self.voltar(Form))
        self.bt_salvar.clicked.connect(self.cadastrar)

    def voltar(self,Form):
        Form.close()
    def cadastrar(self):
        bloqueio = "N"
        if self.checkBox.isChecked():
            bloqueio = "S"
        val_insert ={'vnome' : self.line_nome.text(),
        'vid_tele' : self.line_id_tele.text(),
        'vcod_rca' : self.line_cod_rca.text(),
        'vcod_magento' : self.line_cod_magento.text(),
        'vcod_superv' : self.lineEdit.text(),
        'vbloqueio' : bloqueio }
        try:
            con = bd.conexao.conectarbot()
            cursor = con.cursor()
            sql = "insert into users (nome,id_tele,cod_rca,cod_magento,cod_supervisores,bloqueado) values(:vnome,:vid_tele,:vcod_rca,:vcod_magento,:vcod_superv,:vbloqueio)"
            cursor.execute(sql,val_insert)
            self.pop_up = QMessageBox()
            self.pop_up.setWindowTitle("Sucesso")
            self.pop_up.setText("Sucesso ao cadastrar usuário")
            self.pop_up.exec()

        except Exception as E:
            self.pop_up = QMessageBox()
            self.pop_up.setWindowTitle("ERRO")
            self.pop_up.setText(f"Erro ao cadastrar usuário\n{str(E)}")
            self.pop_up.exec()
        finally:
            con.commit()
            cursor.close()
            con.close()
import icons.buscar
import IMAGENS_DEV_ENERGY.fundo
import IMAGENS_DEV_ENERGY.soui

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form_user_tele_cad()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
