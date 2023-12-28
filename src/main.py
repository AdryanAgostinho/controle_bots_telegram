# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        MainWindow.setMinimumSize(QtCore.QSize(600, 600))
        MainWindow.setMaximumSize(QtCore.QSize(600, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/soui/sou.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fundo = QtWidgets.QFrame(self.centralwidget)
        self.fundo.setStyleSheet("QFrame#fundo{\n"
"    background-image: url(:/fundo/fundo.png);\n"
"}\n"
"")
        self.fundo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fundo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fundo.setObjectName("fundo")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.fundo)
        self.verticalLayout_2.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.form_login = QtWidgets.QFrame(self.fundo)
        self.form_login.setStyleSheet("QFrame#form_login{\n"
" background-color: white;\n"
" border-radius: 20px ;\n"
"}")
        self.form_login.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.form_login.setFrameShadow(QtWidgets.QFrame.Raised)
        self.form_login.setObjectName("form_login")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.form_login)
        self.verticalLayout_3.setContentsMargins(-1, 50, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_login_icone = QtWidgets.QFrame(self.form_login)
        self.frame_login_icone.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame_login_icone.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_login_icone.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_login_icone.setObjectName("frame_login_icone")
        self.label = QtWidgets.QLabel(self.frame_login_icone)
        self.label.setGeometry(QtCore.QRect(146, 0, 261, 191))
        self.label.setStyleSheet("QLabel#label{\n"
"border: 10px solid black;\n"
"border-radius: 30px;\n"
"padding: 10px;\n"
"margin: 2px\n"
"}")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icone_login/login_imagem.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.frame_login_icone)
        self.frame_login_icone_2 = QtWidgets.QFrame(self.form_login)
        self.frame_login_icone_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_login_icone_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_login_icone_2.setObjectName("frame_login_icone_2")
        self.progressBar = QtWidgets.QProgressBar(self.frame_login_icone_2)
        self.progressBar.setGeometry(QtCore.QRect(10, 257, 531, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.var_checklogin = QtWidgets.QLabel(self.frame_login_icone_2)
        self.var_checklogin.setGeometry(QtCore.QRect(11, 281, 271, 16))
        self.var_checklogin.setObjectName("var_checklogin")
        self.widget = QtWidgets.QWidget(self.frame_login_icone_2)
        self.widget.setGeometry(QtCore.QRect(50, 10, 441, 245))
        self.widget.setObjectName("widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setVerticalSpacing(30)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.line_senha = QtWidgets.QLineEdit(self.widget)
        self.line_senha.setMinimumSize(QtCore.QSize(0, 30))
        self.line_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_senha.setObjectName("line_senha")
        self.gridLayout_2.addWidget(self.line_senha, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 2, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.line_login = QtWidgets.QLineEdit(self.widget)
        self.line_login.setMinimumSize(QtCore.QSize(0, 30))
        self.line_login.setObjectName("line_login")
        self.gridLayout.addWidget(self.line_login, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.bt_login = QtWidgets.QPushButton(self.widget)
        self.bt_login.setMinimumSize(QtCore.QSize(0, 50))
        self.bt_login.setStyleSheet("QPushButton{\n"
"background-color: rgb(252, 173, 8);\n"
"border: 1px solid rgb(253, 127, 7);\n"
"border-radius: 3px;\n"
"font-size: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(252, 200, 8);\n"
"border: 1px solid rgb(253, 300, 7);\n"
"color: white;\n"
"}")
        self.bt_login.setObjectName("bt_login")
        self.gridLayout_4.addWidget(self.bt_login, 1, 0, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setEnabled(False)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 85))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 0, 0, 1, 1)
        self.bt_versenha = QtWidgets.QPushButton(self.widget)
        self.bt_versenha.setStyleSheet("QPushButton#bt_versenha{\n"
"background-color: none;\n"
"border: none;\n"
"background-image: url(:/versenha/eye_visibilit_on.png);\n"
"padding-bottom: 14px;\n"
"}")
        self.bt_versenha.setText("")
        self.bt_versenha.setObjectName("bt_versenha")
        self.gridLayout_5.addWidget(self.bt_versenha, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_5, 0, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_login_icone_2)
        self.verticalLayout_2.addWidget(self.form_login)
        self.verticalLayout.addWidget(self.fundo)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login Controle v1"))
        self.var_checklogin.setText(_translate("MainWindow", "Verificando conexao com o servidor : 18.230.186.171"))
        self.line_senha.setPlaceholderText(_translate("MainWindow", "  MinhaSenha"))
        self.label_3.setText(_translate("MainWindow", "Senha:"))
        self.label_2.setText(_translate("MainWindow", "Login:"))
        self.line_login.setPlaceholderText(_translate("MainWindow", "Usuario.Login"))
        self.bt_login.setText(_translate("MainWindow", "Login"))
import fundo_rc
import icone_login_rc
import soui_rc
import versenha_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())