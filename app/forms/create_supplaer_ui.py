# Form implementation generated from reading ui file 'app\forms\ui\create_supplaer.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_CreateSupplaerWindow(object):
    def setupUi(self, CreateSupplaerWindow):
        CreateSupplaerWindow.setObjectName("CreateSupplaerWindow")
        CreateSupplaerWindow.resize(424, 136)
        self.centralwidget = QtWidgets.QWidget(parent=CreateSupplaerWindow)
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
        self.addres_line = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.addres_line.setObjectName("addres_line")
        self.horizontalLayout_3.addWidget(self.addres_line)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.create_btn = QtWidgets.QPushButton(parent=self.centralwidget)
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
        CreateSupplaerWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(CreateSupplaerWindow)
        QtCore.QMetaObject.connectSlotsByName(CreateSupplaerWindow)

    def retranslateUi(self, CreateSupplaerWindow):
        _translate = QtCore.QCoreApplication.translate
        CreateSupplaerWindow.setWindowTitle(_translate("CreateSupplaerWindow", "MainWindow"))
        self.label.setText(_translate("CreateSupplaerWindow", "Название организации:"))
        self.label_2.setText(_translate("CreateSupplaerWindow", "Телефон:"))
        self.label_3.setText(_translate("CreateSupplaerWindow", "Аддрес:"))
        self.create_btn.setText(_translate("CreateSupplaerWindow", "Создать"))
        self.cancel_btn.setText(_translate("CreateSupplaerWindow", "Отмена"))
