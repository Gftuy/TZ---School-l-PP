# Form implementation generated from reading ui file 'ui/login_form.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(416, 338)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.line_login = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.line_login.setObjectName("line_login")
        self.verticalLayout.addWidget(self.line_login)
        self.line_password = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.line_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.line_password.setObjectName("line_password")
        self.verticalLayout.addWidget(self.line_password)
        self.Button_enter = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Button_enter.setObjectName("Button_enter")
        self.verticalLayout.addWidget(self.Button_enter)
        self.push_cancel = QtWidgets.QPushButton(parent=self.centralwidget)
        self.push_cancel.setObjectName("push_cancel")
        self.verticalLayout.addWidget(self.push_cancel)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Форма входа"))
        self.label.setText(_translate("MainWindow", "Добро пожаловать"))
        self.line_login.setPlaceholderText(_translate("MainWindow", "логин"))
        self.line_password.setPlaceholderText(_translate("MainWindow", "пароль"))
        self.Button_enter.setText(_translate("MainWindow", "Вход"))
        self.push_cancel.setText(_translate("MainWindow", "Отмена"))