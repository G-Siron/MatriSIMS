# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Matrix_SIMS_Layout_v2.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1567, 928)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.main_frame = QtWidgets.QWidget(self.centralwidget)
        self.main_frame.setObjectName("main_frame")
        self.horizontalLayout.addWidget(self.main_frame)
        self.tabAnalyses_type = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabAnalyses_type.sizePolicy().hasHeightForWidth())
        self.tabAnalyses_type.setSizePolicy(sizePolicy)
        self.tabAnalyses_type.setMinimumSize(QtCore.QSize(330, 0))
        self.tabAnalyses_type.setObjectName("tabAnalyses_type")
        self.pushButton_file = QtWidgets.QPushButton(self.tabAnalyses_type)
        self.pushButton_file.setGeometry(QtCore.QRect(170, 10, 114, 32))
        self.pushButton_file.setObjectName("pushButton_file")
        self.comboBox_nb_variables = QtWidgets.QComboBox(self.tabAnalyses_type)
        self.comboBox_nb_variables.setGeometry(QtCore.QRect(10, 162, 151, 32))
        self.comboBox_nb_variables.setObjectName("comboBox_nb_variables")
        self.comboBox_nb_variables.addItem("")
        self.comboBox_nb_variables.addItem("")
        self.comboBox_nb_variables.addItem("")
        self.label_files_iso = QtWidgets.QLabel(self.tabAnalyses_type)
        self.label_files_iso.setGeometry(QtCore.QRect(20, 15, 181, 21))
        self.label_files_iso.setObjectName("label_files_iso")
        self.comboBox_fit_order = QtWidgets.QComboBox(self.tabAnalyses_type)
        self.comboBox_fit_order.setEnabled(True)
        self.comboBox_fit_order.setGeometry(QtCore.QRect(20, 417, 165, 41))
        self.comboBox_fit_order.setObjectName("comboBox_fit_order")
        self.comboBox_fit_order.addItem("")
        self.comboBox_fit_order.addItem("")
        self.comboBox_fit_order.addItem("")
        self.comboBox_fit_order.addItem("")
        self.comboBox_fit_order.addItem("")
        self.comboBox_fit_order.addItem("")
        self.comboBox_fit_order.addItem("")
        self.checkBox_bias_iso = QtWidgets.QCheckBox(self.tabAnalyses_type)
        self.checkBox_bias_iso.setGeometry(QtCore.QRect(20, 472, 201, 20))
        self.checkBox_bias_iso.setObjectName("checkBox_bias_iso")
        self.pushButton_fit = QtWidgets.QPushButton(self.tabAnalyses_type)
        self.pushButton_fit.setGeometry(QtCore.QRect(40, 532, 241, 32))
        self.pushButton_fit.setObjectName("pushButton_fit")
        self.label_nb_variables = QtWidgets.QLabel(self.tabAnalyses_type)
        self.label_nb_variables.setGeometry(QtCore.QRect(20, 132, 291, 21))
        self.label_nb_variables.setObjectName("label_nb_variables")
        self.label_inde_variable_3 = QtWidgets.QLabel(self.tabAnalyses_type)
        self.label_inde_variable_3.setEnabled(False)
        self.label_inde_variable_3.setGeometry(QtCore.QRect(20, 329, 121, 16))
        self.label_inde_variable_3.setObjectName("label_inde_variable_3")
        self.label_inde_variable_2 = QtWidgets.QLabel(self.tabAnalyses_type)
        self.label_inde_variable_2.setEnabled(False)
        self.label_inde_variable_2.setGeometry(QtCore.QRect(20, 267, 121, 16))
        self.label_inde_variable_2.setObjectName("label_inde_variable_2")
        self.label_inde_variable_1 = QtWidgets.QLabel(self.tabAnalyses_type)
        self.label_inde_variable_1.setGeometry(QtCore.QRect(20, 205, 121, 16))
        self.label_inde_variable_1.setObjectName("label_inde_variable_1")
        self.label_stats = QtWidgets.QLabel(self.tabAnalyses_type)
        self.label_stats.setGeometry(QtCore.QRect(30, 592, 271, 241))
        self.label_stats.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_stats.setObjectName("label_stats")
        self.label_target_variable = QtWidgets.QLabel(self.tabAnalyses_type)
        self.label_target_variable.setGeometry(QtCore.QRect(20, 62, 141, 16))
        self.label_target_variable.setObjectName("label_target_variable")
        self.label_error_variable_1 = QtWidgets.QLabel(self.tabAnalyses_type)
        self.label_error_variable_1.setEnabled(False)
        self.label_error_variable_1.setGeometry(QtCore.QRect(20, 236, 121, 16))
        self.label_error_variable_1.setObjectName("label_error_variable_1")
        self.label_error_variable_2 = QtWidgets.QLabel(self.tabAnalyses_type)
        self.label_error_variable_2.setEnabled(False)
        self.label_error_variable_2.setGeometry(QtCore.QRect(20, 298, 121, 16))
        self.label_error_variable_2.setObjectName("label_error_variable_2")
        self.label_error_variable_3 = QtWidgets.QLabel(self.tabAnalyses_type)
        self.label_error_variable_3.setEnabled(False)
        self.label_error_variable_3.setGeometry(QtCore.QRect(20, 360, 121, 16))
        self.label_error_variable_3.setObjectName("label_error_variable_3")
        self.label_polynomial_order = QtWidgets.QLabel(self.tabAnalyses_type)
        self.label_polynomial_order.setGeometry(QtCore.QRect(20, 392, 291, 21))
        self.label_polynomial_order.setObjectName("label_polynomial_order")
        self.label_target_error_variable = QtWidgets.QLabel(self.tabAnalyses_type)
        self.label_target_error_variable.setGeometry(QtCore.QRect(20, 95, 141, 16))
        self.label_target_error_variable.setObjectName("label_target_error_variable")
        self.checkBox_error_X = QtWidgets.QCheckBox(self.tabAnalyses_type)
        self.checkBox_error_X.setGeometry(QtCore.QRect(180, 166, 101, 20))
        self.checkBox_error_X.setObjectName("checkBox_error_X")
        self.comboBox_target = QtWidgets.QComboBox(self.tabAnalyses_type)
        self.comboBox_target.setGeometry(QtCore.QRect(180, 55, 130, 32))
        self.comboBox_target.setObjectName("comboBox_target")
        self.comboBox_target.addItem("")
        self.comboBox_target_error = QtWidgets.QComboBox(self.tabAnalyses_type)
        self.comboBox_target_error.setGeometry(QtCore.QRect(180, 90, 130, 32))
        self.comboBox_target_error.setObjectName("comboBox_target_error")
        self.comboBox_target_error.addItem("")
        self.comboBox_var1_name = QtWidgets.QComboBox(self.tabAnalyses_type)
        self.comboBox_var1_name.setGeometry(QtCore.QRect(165, 200, 130, 32))
        self.comboBox_var1_name.setObjectName("comboBox_var1_name")
        self.comboBox_var1_name.addItem("")
        self.comboBox_var1_error_name = QtWidgets.QComboBox(self.tabAnalyses_type)
        self.comboBox_var1_error_name.setEnabled(False)
        self.comboBox_var1_error_name.setGeometry(QtCore.QRect(165, 231, 130, 32))
        self.comboBox_var1_error_name.setObjectName("comboBox_var1_error_name")
        self.comboBox_var1_error_name.addItem("")
        self.comboBox_var2_error_name = QtWidgets.QComboBox(self.tabAnalyses_type)
        self.comboBox_var2_error_name.setEnabled(False)
        self.comboBox_var2_error_name.setGeometry(QtCore.QRect(165, 293, 130, 32))
        self.comboBox_var2_error_name.setObjectName("comboBox_var2_error_name")
        self.comboBox_var2_error_name.addItem("")
        self.comboBox_var2_name = QtWidgets.QComboBox(self.tabAnalyses_type)
        self.comboBox_var2_name.setEnabled(False)
        self.comboBox_var2_name.setGeometry(QtCore.QRect(165, 262, 130, 32))
        self.comboBox_var2_name.setObjectName("comboBox_var2_name")
        self.comboBox_var2_name.addItem("")
        self.comboBox_var3_error_name = QtWidgets.QComboBox(self.tabAnalyses_type)
        self.comboBox_var3_error_name.setEnabled(False)
        self.comboBox_var3_error_name.setGeometry(QtCore.QRect(165, 355, 130, 32))
        self.comboBox_var3_error_name.setObjectName("comboBox_var3_error_name")
        self.comboBox_var3_error_name.addItem("")
        self.comboBox_var3_name = QtWidgets.QComboBox(self.tabAnalyses_type)
        self.comboBox_var3_name.setEnabled(False)
        self.comboBox_var3_name.setGeometry(QtCore.QRect(165, 324, 130, 32))
        self.comboBox_var3_name.setObjectName("comboBox_var3_name")
        self.comboBox_var3_name.addItem("")
        self.horizontalLayout.addWidget(self.tabAnalyses_type)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1567, 24))
        self.menubar.setObjectName("menubar")
        self.menuProceSIMS = QtWidgets.QMenu(self.menubar)
        self.menuProceSIMS.setObjectName("menuProceSIMS")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuFitting = QtWidgets.QMenu(self.menubar)
        self.menuFitting.setObjectName("menuFitting")
        self.menuFigures = QtWidgets.QMenu(self.menubar)
        self.menuFigures.setObjectName("menuFigures")
        self.menuOutput = QtWidgets.QMenu(self.menubar)
        self.menuOutput.setObjectName("menuOutput")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuInput_data = QtWidgets.QMenu(self.menubar)
        self.menuInput_data.setObjectName("menuInput_data")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout_MatriSIMS = QtWidgets.QAction(MainWindow)
        self.actionAbout_MatriSIMS.setObjectName("actionAbout_MatriSIMS")
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionNew_project = QtWidgets.QAction(MainWindow)
        self.actionNew_project.setObjectName("actionNew_project")
        self.actionOpen_project = QtWidgets.QAction(MainWindow)
        self.actionOpen_project.setObjectName("actionOpen_project")
        self.actionSave_project = QtWidgets.QAction(MainWindow)
        self.actionSave_project.setObjectName("actionSave_project")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionResiduals = QtWidgets.QAction(MainWindow)
        self.actionResiduals.setObjectName("actionResiduals")
        self.actionAdvanced_statistics = QtWidgets.QAction(MainWindow)
        self.actionAdvanced_statistics.setObjectName("actionAdvanced_statistics")
        self.actionStandards = QtWidgets.QAction(MainWindow)
        self.actionStandards.setObjectName("actionStandards")
        self.actionResiduals_2 = QtWidgets.QAction(MainWindow)
        self.actionResiduals_2.setEnabled(True)
        self.actionResiduals_2.setObjectName("actionResiduals_2")
        self.actionAll_data = QtWidgets.QAction(MainWindow)
        self.actionAll_data.setObjectName("actionAll_data")
        self.actionStandard_data = QtWidgets.QAction(MainWindow)
        self.actionStandard_data.setObjectName("actionStandard_data")
        self.actionSample_data = QtWidgets.QAction(MainWindow)
        self.actionSample_data.setObjectName("actionSample_data")
        self.actionWhole_session = QtWidgets.QAction(MainWindow)
        self.actionWhole_session.setObjectName("actionWhole_session")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionOptics_and_primary = QtWidgets.QAction(MainWindow)
        self.actionOptics_and_primary.setObjectName("actionOptics_and_primary")
        self.actionInput_data = QtWidgets.QAction(MainWindow)
        self.actionInput_data.setObjectName("actionInput_data")
        self.actionData = QtWidgets.QAction(MainWindow)
        self.actionData.setObjectName("actionData")
        self.actionStatistics = QtWidgets.QAction(MainWindow)
        self.actionStatistics.setObjectName("actionStatistics")
        self.actionDeadtime = QtWidgets.QAction(MainWindow)
        self.actionDeadtime.setEnabled(False)
        self.actionDeadtime.setObjectName("actionDeadtime")
        self.actionBackground = QtWidgets.QAction(MainWindow)
        self.actionBackground.setEnabled(False)
        self.actionBackground.setObjectName("actionBackground")
        self.actionChange_of_cycles = QtWidgets.QAction(MainWindow)
        self.actionChange_of_cycles.setEnabled(False)
        self.actionChange_of_cycles.setObjectName("actionChange_of_cycles")
        self.actionReset = QtWidgets.QAction(MainWindow)
        self.actionReset.setObjectName("actionReset")
        self.menuProceSIMS.addAction(self.actionAbout_MatriSIMS)
        self.menuProceSIMS.addAction(self.actionPreferences)
        self.menuProceSIMS.addAction(self.actionQuit)
        self.menuFile.addAction(self.actionNew_project)
        self.menuFile.addAction(self.actionOpen_project)
        self.menuFile.addAction(self.actionSave_project)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFitting.addAction(self.actionAdvanced_statistics)
        self.menuFitting.addAction(self.actionStatistics)
        self.menuFigures.addAction(self.actionStandards)
        self.menuFigures.addAction(self.actionResiduals_2)
        self.menuOutput.addAction(self.actionStandard_data)
        self.menuOutput.addAction(self.actionSample_data)
        self.menuOutput.addAction(self.actionInput_data)
        self.menuHelp.addAction(self.actionOptics_and_primary)
        self.menuInput_data.addAction(self.actionData)
        self.menubar.addAction(self.menuProceSIMS.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuInput_data.menuAction())
        self.menubar.addAction(self.menuFitting.menuAction())
        self.menubar.addAction(self.menuFigures.menuAction())
        self.menubar.addAction(self.menuOutput.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_file.setText(_translate("MainWindow", "Select"))
        self.comboBox_nb_variables.setItemText(0, _translate("MainWindow", "1 variable"))
        self.comboBox_nb_variables.setItemText(1, _translate("MainWindow", "2 variables"))
        self.comboBox_nb_variables.setItemText(2, _translate("MainWindow", "3 variables"))
        self.label_files_iso.setText(_translate("MainWindow", "Select the input file:"))
        self.comboBox_fit_order.setItemText(0, _translate("MainWindow", "Linear"))
        self.comboBox_fit_order.setItemText(1, _translate("MainWindow", "2nd order polynomial"))
        self.comboBox_fit_order.setItemText(2, _translate("MainWindow", "3rd order polynomial"))
        self.comboBox_fit_order.setItemText(3, _translate("MainWindow", "4th order polynomial"))
        self.comboBox_fit_order.setItemText(4, _translate("MainWindow", "5th order polynomial"))
        self.comboBox_fit_order.setItemText(5, _translate("MainWindow", "6th order polynomial"))
        self.comboBox_fit_order.setItemText(6, _translate("MainWindow", "7th order polynomial"))
        self.checkBox_bias_iso.setText(_translate("MainWindow", "Automatic bias correction"))
        self.pushButton_fit.setText(_translate("MainWindow", "Fit data!"))
        self.label_nb_variables.setText(_translate("MainWindow", "Select the number of independent variables:"))
        self.label_inde_variable_3.setText(_translate("MainWindow", "Variable 3 name :"))
        self.label_inde_variable_2.setText(_translate("MainWindow", "Variable 2 name:"))
        self.label_inde_variable_1.setText(_translate("MainWindow", "Variable 1 name:"))
        self.label_stats.setText(_translate("MainWindow", "Statistics:"))
        self.label_target_variable.setText(_translate("MainWindow", "Target variable name:"))
        self.label_error_variable_1.setText(_translate("MainWindow", "Error 1 name:"))
        self.label_error_variable_2.setText(_translate("MainWindow", "Error 2 name:"))
        self.label_error_variable_3.setText(_translate("MainWindow", "Error 3 name :"))
        self.label_polynomial_order.setText(_translate("MainWindow", "Select the polynomial order:"))
        self.label_target_error_variable.setText(_translate("MainWindow", "Target error name:"))
        self.checkBox_error_X.setText(_translate("MainWindow", " Error on X"))
        self.comboBox_target.setItemText(0, _translate("MainWindow", "Select name"))
        self.comboBox_target_error.setItemText(0, _translate("MainWindow", "Select name"))
        self.comboBox_var1_name.setItemText(0, _translate("MainWindow", "Select name"))
        self.comboBox_var1_error_name.setItemText(0, _translate("MainWindow", "Select name"))
        self.comboBox_var2_error_name.setItemText(0, _translate("MainWindow", "Select name"))
        self.comboBox_var2_name.setItemText(0, _translate("MainWindow", "Select name"))
        self.comboBox_var3_error_name.setItemText(0, _translate("MainWindow", "Select name"))
        self.comboBox_var3_name.setItemText(0, _translate("MainWindow", "Select name"))
        self.menuProceSIMS.setTitle(_translate("MainWindow", "MatriSIMS"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuFitting.setTitle(_translate("MainWindow", "Fitting"))
        self.menuFigures.setTitle(_translate("MainWindow", "Figures"))
        self.menuOutput.setTitle(_translate("MainWindow", "Output"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuInput_data.setTitle(_translate("MainWindow", "Input data"))
        self.actionAbout_MatriSIMS.setText(_translate("MainWindow", "About MatriSIMS"))
        self.actionPreferences.setText(_translate("MainWindow", "Preferences"))
        self.actionNew_project.setText(_translate("MainWindow", "New project"))
        self.actionOpen_project.setText(_translate("MainWindow", "Open project"))
        self.actionSave_project.setText(_translate("MainWindow", "Save"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionResiduals.setText(_translate("MainWindow", "Residuals"))
        self.actionAdvanced_statistics.setText(_translate("MainWindow", "Advanced statistics"))
        self.actionStandards.setText(_translate("MainWindow", "Standards"))
        self.actionResiduals_2.setText(_translate("MainWindow", "Residuals"))
        self.actionAll_data.setText(_translate("MainWindow", "All data"))
        self.actionStandard_data.setText(_translate("MainWindow", "Standard data"))
        self.actionSample_data.setText(_translate("MainWindow", "Sample data"))
        self.actionWhole_session.setText(_translate("MainWindow", "Whole session"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionOptics_and_primary.setText(_translate("MainWindow", "Tutorial"))
        self.actionInput_data.setText(_translate("MainWindow", "Input data"))
        self.actionData.setText(_translate("MainWindow", "Data"))
        self.actionStatistics.setText(_translate("MainWindow", "Statistics"))
        self.actionDeadtime.setText(_translate("MainWindow", "Deadtime"))
        self.actionBackground.setText(_translate("MainWindow", "Background"))
        self.actionChange_of_cycles.setText(_translate("MainWindow", "Change # of cycles"))
        self.actionReset.setText(_translate("MainWindow", "Reset"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
