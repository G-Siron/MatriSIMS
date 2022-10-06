# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Figure_Statistics.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1200, 630)
        self.Frame_FigStats = QtWidgets.QWidget(Form)
        self.Frame_FigStats.setGeometry(QtCore.QRect(9, 9, 1181, 581))
        self.Frame_FigStats.setObjectName("Frame_FigStats")
        self.pushButton_saveFigure = QtWidgets.QPushButton(Form)
        self.pushButton_saveFigure.setGeometry(QtCore.QRect(1050, 594, 140, 32))
        self.pushButton_saveFigure.setObjectName("pushButton_saveFigure")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_saveFigure.setText(_translate("Form", "Save Figure"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

