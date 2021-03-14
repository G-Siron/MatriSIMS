# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'About_Layout.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(290, 220)
        self.label_ProceSIMS = QtWidgets.QLabel(Form)
        self.label_ProceSIMS.setGeometry(QtCore.QRect(10, 30, 271, 91))
        self.label_ProceSIMS.setObjectName("label_ProceSIMS")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 150, 271, 61))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_ProceSIMS.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">ProceSIMS</span></p><p align=\"center\"><span style=\" font-size:14pt;\">version 1.1.1</span></p><p align=\"center\"><span style=\" font-size:14pt;\">September 25th 2019</span></p></body></html>"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\">Maintained by:</p><p align=\"center\">Guillaume Siron</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

