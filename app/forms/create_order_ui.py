# Form implementation generated from reading ui file 'app\forms\ui\create_order.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_CreateOrderWindow(object):
    def setupUi(self, CreateOrderWindow):
        CreateOrderWindow.setObjectName("CreateOrderWindow")
        CreateOrderWindow.resize(326, 154)
        self.centralwidget = QtWidgets.QWidget(parent=CreateOrderWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(30, 0))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.data_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.data_label.setMinimumSize(QtCore.QSize(30, 0))
        self.data_label.setText("")
        self.data_label.setObjectName("data_label")
        self.horizontalLayout.addWidget(self.data_label)
        self.horizontalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(30, 0))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.price_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.price_label.setMinimumSize(QtCore.QSize(30, 0))
        self.price_label.setText("")
        self.price_label.setObjectName("price_label")
        self.horizontalLayout_2.addWidget(self.price_label)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.quantityBox = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.quantityBox.setMinimumSize(QtCore.QSize(50, 0))
        self.quantityBox.setObjectName("quantityBox")
        self.horizontalLayout_3.addWidget(self.quantityBox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setMinimumSize(QtCore.QSize(30, 0))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.name_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.name_label.setMinimumSize(QtCore.QSize(30, 0))
        self.name_label.setText("")
        self.name_label.setObjectName("name_label")
        self.horizontalLayout_4.addWidget(self.name_label)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.itemBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.itemBox.setObjectName("itemBox")
        self.verticalLayout.addWidget(self.itemBox)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.create_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.create_btn.setObjectName("create_btn")
        self.horizontalLayout_6.addWidget(self.create_btn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.cancel_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout_6.addWidget(self.cancel_btn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        CreateOrderWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(CreateOrderWindow)
        QtCore.QMetaObject.connectSlotsByName(CreateOrderWindow)

    def retranslateUi(self, CreateOrderWindow):
        _translate = QtCore.QCoreApplication.translate
        CreateOrderWindow.setWindowTitle(_translate("CreateOrderWindow", "MainWindow"))
        self.label.setText(_translate("CreateOrderWindow", "Дата:"))
        self.label_2.setText(_translate("CreateOrderWindow", "Цена:"))
        self.label_3.setText(_translate("CreateOrderWindow", "Количество:"))
        self.label_4.setText(_translate("CreateOrderWindow", "Кто принял:"))
        self.create_btn.setText(_translate("CreateOrderWindow", "Создать"))
        self.cancel_btn.setText(_translate("CreateOrderWindow", "Отмена"))
