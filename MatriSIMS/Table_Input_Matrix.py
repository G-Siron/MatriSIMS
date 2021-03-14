# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Table_Input_Matrix.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1200, 728)
        self.tableWidget_InputMat = QtWidgets.QTableWidget(Form)
        self.tableWidget_InputMat.setGeometry(QtCore.QRect(10, 10, 1181, 671))
        self.tableWidget_InputMat.setObjectName("tableWidget_InputMat")
        self.tableWidget_InputMat.setColumnCount(0)
        self.tableWidget_InputMat.setRowCount(0)
        self.tableWidget_InputMat.horizontalHeader().setVisible(True)
        self.tableWidget_InputMat.verticalHeader().setVisible(False)
        self.pushButton_Delete = QtWidgets.QPushButton(Form)
        self.pushButton_Delete.setGeometry(QtCore.QRect(30, 690, 121, 32))
        self.pushButton_Delete.setObjectName("pushButton_Delete")
        self.pushButton_Section = QtWidgets.QPushButton(Form)
        self.pushButton_Section.setGeometry(QtCore.QRect(160, 690, 121, 32))
        self.pushButton_Section.setObjectName("pushButton_Section")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_Delete.setText(_translate("Form", "Delete"))
        self.pushButton_Section.setText(_translate("Form", "Section"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
