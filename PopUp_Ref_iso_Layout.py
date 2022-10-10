# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PopUp_Ref_iso_Layout.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_Ref_iso(object):
    def setupUi(self, Dialog_Ref_iso):
        Dialog_Ref_iso.setObjectName("Dialog_Ref_iso")
        Dialog_Ref_iso.resize(239, 168)
        self.buttonBox_Ref_iso_Layout = QtWidgets.QDialogButtonBox(Dialog_Ref_iso)
        self.buttonBox_Ref_iso_Layout.setGeometry(QtCore.QRect(10, 130, 191, 32))
        self.buttonBox_Ref_iso_Layout.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox_Ref_iso_Layout.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox_Ref_iso_Layout.setObjectName("buttonBox_Ref_iso_Layout")
        self.label_ref_std = QtWidgets.QLabel(Dialog_Ref_iso)
        self.label_ref_std.setGeometry(QtCore.QRect(30, 47, 134, 16))
        self.label_ref_std.setObjectName("label_ref_std")
        self.label_std = QtWidgets.QLabel(Dialog_Ref_iso)
        self.label_std.setGeometry(QtCore.QRect(20, 17, 201, 16))
        self.label_std.setObjectName("label_std")
        self.label_sigma_std = QtWidgets.QLabel(Dialog_Ref_iso)
        self.label_sigma_std.setGeometry(QtCore.QRect(30, 90, 134, 16))
        self.label_sigma_std.setObjectName("label_sigma_std")
        self.lineEdit_Ref_iso = QtWidgets.QLineEdit(Dialog_Ref_iso)
        self.lineEdit_Ref_iso.setGeometry(QtCore.QRect(180, 40, 40, 30))
        self.lineEdit_Ref_iso.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.lineEdit_Ref_iso.setObjectName("lineEdit_Ref_iso")
        self.lineEdit_sigma_iso = QtWidgets.QLineEdit(Dialog_Ref_iso)
        self.lineEdit_sigma_iso.setGeometry(QtCore.QRect(180, 83, 40, 30))
        self.lineEdit_sigma_iso.setObjectName("lineEdit_sigma_iso")

        self.retranslateUi(Dialog_Ref_iso)
        self.buttonBox_Ref_iso_Layout.accepted.connect(Dialog_Ref_iso.accept)
        self.buttonBox_Ref_iso_Layout.rejected.connect(Dialog_Ref_iso.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Ref_iso)

    def retranslateUi(self, Dialog_Ref_iso):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Ref_iso.setWindowTitle(_translate("Dialog_Ref_iso", "Dialog"))
        self.label_ref_std.setText(_translate("Dialog_Ref_iso", "Reference value (‰)"))
        self.label_std.setText(_translate("Dialog_Ref_iso", "Standard :"))
        self.label_sigma_std.setText(_translate("Dialog_Ref_iso", "Uncertainty (2SD, ‰)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_Ref_iso = QtWidgets.QDialog()
    ui = Ui_Dialog_Ref_iso()
    ui.setupUi(Dialog_Ref_iso)
    Dialog_Ref_iso.show()
    sys.exit(app.exec_())

