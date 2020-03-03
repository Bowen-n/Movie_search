# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './dytt.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(900, 700)
        Form.setMinimumSize(QtCore.QSize(0, 369))
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 0, 3, 1, 1)
        self.search_button = QtWidgets.QPushButton(Form)
        self.search_button.setObjectName("search_button")
        self.gridLayout.addWidget(self.search_button, 0, 4, 1, 1)
        self.copy_link = QtWidgets.QPushButton(Form)
        self.copy_link.setObjectName("copy_link")
        self.gridLayout.addWidget(self.copy_link, 0, 5, 1, 1)
        self.search_result = QtWidgets.QTreeWidget(Form)
        self.search_result.setObjectName("search_result")
        self.search_result.headerItem().setText(0, "查找结果")
        self.gridLayout.addWidget(self.search_result, 1, 0, 1, 6)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "电影天堂搜索"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">电影名称</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">片源</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("Form", "电影天堂"))
        self.search_button.setText(_translate("Form", "查找"))
        self.copy_link.setText(_translate("Form", "复制链接"))
        self.search_result.headerItem().setText(1, _translate("Form", "清晰度"))
        self.search_result.headerItem().setText(2, _translate("Form", "下载链接"))

