# Form implementation generated from reading ui file 'app\forms\ui\create_user.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_CreateUserWindow(object):
    def setupUi(self, CreateUserWindow):
        CreateUserWindow.setObjectName("CreateUserWindow")
        CreateUserWindow.resize(352, 210)
        self.centralwidget = QtWidgets.QWidget(parent=CreateUserWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.name_line = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.name_line.setObjectName("name_line")
        self.horizontalLayout.addWidget(self.name_line)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.phone_line = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.phone_line.setObjectName("phone_line")
        self.horizontalLayout_2.addWidget(self.phone_line)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.email_line = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.email_line.setObjectName("email_line")
        self.horizontalLayout_3.addWidget(self.email_line)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.login_line = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.login_line.setObjectName("login_line")
        self.horizontalLayout_4.addWidget(self.login_line)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.password_line = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.password_line.setObjectName("password_line")
        self.horizontalLayout_6.addWidget(self.password_line)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.create_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.create_btn.setText("")
        self.create_btn.setObjectName("create_btn")
        self.horizontalLayout_5.addWidget(self.create_btn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.cancel_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout_5.addWidget(self.cancel_btn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        CreateUserWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(CreateUserWindow)
        QtCore.QMetaObject.connectSlotsByName(CreateUserWindow)

    def retranslateUi(self, CreateUserWindow):
        _translate = QtCore.QCoreApplication.translate
        CreateUserWindow.setWindowTitle(_translate("CreateUserWindow", "MainWindow"))
        self.label.setText(_translate("CreateUserWindow", "Имя:"))
        self.label_2.setText(_translate("CreateUserWindow", "Телефон:"))
        self.label_3.setText(_translate("CreateUserWindow", "Почта:"))
        self.label_4.setText(_translate("CreateUserWindow", "Логин:"))
        self.label_5.setText(_translate("CreateUserWindow", "Пароль:"))
        self.cancel_btn.setText(_translate("CreateUserWindow", "Отмена"))
