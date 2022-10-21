# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QDialog, QWidget, QVBoxLayout, QLabel, QTableWidgetItem, QTableView, QAbstractItemView
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QDoubleValidator
from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib  
matplotlib.use('Qt5Agg')   
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib.gridspec import GridSpec
from matplotlib.patches import Circle
from scipy import stats
import sys
import os
import re
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.regression.linear_model import WLS as WLS
from statsmodels.regression.linear_model import OLS as OLS
from statsmodels.sandbox.regression.predstd import wls_prediction_std
import datetime as dt
import time as tm
from itertools import islice
import mpl_toolkits.mplot3d


import Matrix_SIMS_Layout
import Figure_std_Layout
import Figure_Statistics
import Table_Input_Matrix
import About_Layout
import Stats_Window


# Matrix_SIMS version 1.0.0
# Created and maintained by Guillaume Siron 

class About_Layout(QWidget, About_Layout.Ui_Form):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

class Stats_Window_show(QWidget, Stats_Window.Ui_Form):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        self.pushButton_saveStats.clicked.connect(self.save_Stats_file)

        global set_text_Stats
        if nb_variables_value == 1:
            if polynomial_order == 1:
                str_a0 = "%.2f" %(a0)
                str_a1 = "%.2f" %(a1)
                set_text_Stats = 'Statistics:\n\n2SD = ' + str_sd_std_SIMS + ' permil\n2SE = ' + str_se_std_SIMS + ' permil\n\nMSWD = ' + str_MSWD + '\n\nEquation:\ny = ' + str_a1 + ' x + ' + str_a0 + '\n\n' + str_Summary
                self.textEdit_Stats.setText(set_text_Stats)
            elif polynomial_order == 2:
                str_a0 = "%.2f" %(a0)
                str_a1 = "%.2f" %(a1)
                str_a2 = "%.3f" %(a2)
                set_text_Stats = 'Statistics:\n\n2SD = ' + str_sd_std_SIMS + ' permil\n2SE = ' + str_se_std_SIMS + ' permil\n\nMSWD = ' + str_MSWD + '\n\nEquation:\ny = ' + str_a2 + ' x^2 + ' + str_a1 + ' x + ' + str_a0 + '\n\n' + str_Summary
                self.textEdit_Stats.setText(set_text_Stats)
            elif polynomial_order == 3:
                str_a0 = "%.2f" %(a0)
                str_a1 = "%.2f" %(a1)
                str_a2 = "%.3f" %(a2)
                str_a3 = "%.4f" %(a3)
                set_text_Stats = 'Statistics:\n\n2SD = ' + str_sd_std_SIMS + ' permil\n2SE = ' + str_se_std_SIMS + ' permil\n\nMSWD = ' + str_MSWD + '\n\nEquation:\ny = ' + str_a3 + ' x^3 + ' + str_a2 + ' x^2 + ' + str_a1 + ' x + ' + str_a0 + '\n\n' + str_Summary
                self.textEdit_Stats.setText(set_text_Stats)
            elif polynomial_order == 4:
                str_a0 = "%.2f" %(a0)
                str_a1 = "%.2f" %(a1)
                str_a2 = "%.3f" %(a2)
                str_a3 = "%.4f" %(a3)
                str_a4 = "%.4f" %(a4)
                set_text_Stats = 'Statistics:\n\n2SD = ' + str_sd_std_SIMS + ' permil\n2SE = ' + str_se_std_SIMS + ' permil\n\nMSWD = ' + str_MSWD + '\n\nEquation:\ny = ' + str_a4 + ' x^4 + ' + str_a3 + ' x^3 + ' + str_a2 + 'x^2\n + ' + str_a1 + ' x + ' + str_a0 + '\n\n' + str_Summary
                self.textEdit_Stats.setText(set_text_Stats)
            elif polynomial_order == 5:
                str_a0 = "%.2f" %(a0)
                str_a1 = "%.2f" %(a1)
                str_a2 = "%.3f" %(a2)
                str_a3 = "%.4f" %(a3)
                str_a4 = "%.4f" %(a4)
                str_a5 = "%.5f" %(a5)
                set_text_Stats = 'Statistics:\n\n2SD = ' + str_sd_std_SIMS + ' permil\n2SE = ' + str_se_std_SIMS + ' permil\n\nMSWD = ' + str_MSWD + '\n\nEquation:\ny = ' + str_a5 + ' x^5 + ' + str_a4 + ' x^4 + ' + str_a3 + ' x^3\n + ' + str_a2 + 'x^2 + ' + str_a1 + ' x + ' + str_a0 + '\n\n' + str_Summary
                self.textEdit_Stats.setText(set_text_Stats)
            elif polynomial_order == 6:
                str_a0 = "%.2f" %(a0)
                str_a1 = "%.2f" %(a1)
                str_a2 = "%.3f" %(a2)
                str_a3 = "%.4f" %(a3)
                str_a4 = "%.4f" %(a4)
                str_a5 = "%.5f" %(a5)
                str_a6 = "%.5f" %(a6)
                sset_text_Stats = 'Statistics:\n\n2SD = ' + str_sd_std_SIMS + ' permil\n2SE = ' + str_se_std_SIMS + ' permil\n\nMSWD = ' + str_MSWD + '\n\nEquation:\ny = ' + str_a6 + ' x^6 + ' + str_a5 + ' x^5 + ' + str_a4 + ' x^4\n + ' + str_a3 + ' x^3 + ' + str_a2 + 'x^2 + ' + str_a1 + ' x + ' + str_a0 + '\n\n' + str_Summary
                self.textEdit_Stats.setText(set_text_Stats)
            elif polynomial_order == 7:
                str_a0 = "%.2f" %(a0)
                str_a1 = "%.2f" %(a1)
                str_a2 = "%.3f" %(a2)
                str_a3 = "%.4f" %(a3)
                str_a4 = "%.4f" %(a4)
                str_a5 = "%.5f" %(a5)
                str_a6 = "%.5f" %(a6)
                str_a7 = "%.5f" %(a7)
                set_text_Stats = 'Statistics:\n\n2SD = ' + str_sd_std_SIMS + ' permil\n2SE = ' + str_se_std_SIMS + ' permil\n\nMSWD = ' + str_MSWD + '\n\nEquation:\ny = ' + str_a7 + ' x^7 + ' + str_a6 + ' x^6 + ' + str_a5 + ' x^5\n + ' + str_a4 + ' x^4 + ' + str_a3 + ' x^3 + ' + str_a2 + 'x^2 + ' + str_a1 + ' x + ' + str_a0 + '\n\n' + str_Summary
                self.textEdit_Stats.setText(set_text_Stats)
        elif nb_variables_value == 2:
            if polynomial_order == 1:
                str_a0 = "%.2f" %(a0)
                str_a1 = "%.2f" %(a1)
                str_a2 = "%.2f" %(a2)
                set_text_Stats = 'Statistics:\n\nStd1:\n2SD = ' + str_sd_std1_SIMS + ' permil\n2SE = ' + str_se_std1_SIMS + '\n\nStd2:\n2SD = ' + str_sd_std2_SIMS + ' permil\n2SE = ' + str_se_std2_SIMS+ ' permil\n\nMSWD = ' + str_MSWD_tot + '\n\nEquation:\ny (std1) = ' + str_a2 + ' x + ' + str_a0 + '\n\ny (std2) = ' + str_a2 + ' x + ' + str_a1 + '\n\n'+ str_Summary
                self.textEdit_Stats.setText(set_text_Stats)
            elif polynomial_order == 2:
                str_a0 = "%.2f" %(a0)
                str_a1 = "%.2f" %(a1)
                str_a2 = "%.3f" %(a2)
                str_a3 = "%.3f" %(a3)
                set_text_Stats = 'Statistics:\n\nStd1:\n2SD = ' + str_sd_std1_SIMS + ' permil\n2SE = ' + str_se_std1_SIMS + '\n\nStd2:\n2SD = ' + str_sd_std2_SIMS + ' permil\n2SE = ' + str_se_std2_SIMS+ ' permil\n\nMSWD = ' + str_MSWD_tot + '\n\nEquation:\ny = ' + str_a2 + ' x^2 + ' + str_a1 + ' x + ' + str_a0 + '\n\n' + str_Summary
                self.textEdit_Stats.setText(set_text_Stats)
            elif polynomial_order == 3:
                str_a0 = "%.2f" %(a0)
                str_a1 = "%.2f" %(a1)
                str_a2 = "%.3f" %(a2)
                str_a3 = "%.4f" %(a3)
                set_text_Stats = 'Statistics:\n\nStd1:\n2SD = ' + str_sd_std1_SIMS + ' permil\n2SE = ' + str_se_std1_SIMS + '\n\nStd2:\n2SD = ' + str_sd_std2_SIMS + ' permil\n2SE = ' + str_se_std2_SIMS+ ' permil\n\nMSWD = ' + str_MSWD_tot + '\n\nEquation:\ny = ' + str_a3 + ' x^3 + ' + str_a2 + ' x^2 + ' + str_a1 + ' x + ' + str_a0 + '\n\n' + str_Summary
                self.textEdit_Stats.setText(set_text_Stats)
            elif polynomial_order == 4:
                str_a0 = "%.2f" %(a0)
                str_a1 = "%.2f" %(a1)
                str_a2 = "%.3f" %(a2)
                str_a3 = "%.4f" %(a3)
                str_a4 = "%.4f" %(a4)
                set_text_Stats = 'Statistics:\n\nStd1:\n2SD = ' + str_sd_std1_SIMS + ' permil\n2SE = ' + str_se_std1_SIMS + '\n\nStd2:\n2SD = ' + str_sd_std2_SIMS + ' permil\n2SE = ' + str_se_std2_SIMS+ ' permil\n\nMSWD = ' + str_MSWD_tot + '\n\nEquation:\ny = ' + str_a4 + ' x^4 + ' + str_a3 + ' x^3 + ' + str_a2 + 'x^2\n + ' + str_a1 + ' x + ' + str_a0 + '\n\n' + str_Summary
                self.textEdit_Stats.setText(set_text_Stats)
        elif nb_variables_value == 3:
            if polynomial_order == 1:
                str_a0 = "%.2f" %(a0)
                str_a1 = "%.2f" %(a1)
                str_a2 = "%.2f" %(a2)
                str_a3 = "%.2f" %(a3)
                set_text_Stats = 'Statistics:\n\nStd1:\n2SD = ' + str_sd_std1_SIMS + ' permil\n2SE = ' + str_se_std1_SIMS + '\n\nStd2:\n2SD = ' + str_sd_std2_SIMS + ' permil\n2SE = ' + str_se_std2_SIMS+ ' permil\n\nMSWD = ' + str_MSWD_tot + '\n\nEquation:\ny (std1) = ' + str_a2 + ' x + ' + str_a0 + '\n\ny (std2) = ' + str_a2 + ' x + ' + str_a1 + '\n\n'+ str_Summary
                self.textEdit_Stats.setText(set_text_Stats)
            elif polynomial_order == 2:
                str_a0 = "%.2f" %(a0)
                str_a1 = "%.2f" %(a1)
                str_a2 = "%.3f" %(a2)
                str_a3 = "%.3f" %(a3)
                set_text_Stats = 'Statistics:\n\nStd1:\n2SD = ' + str_sd_std1_SIMS + ' permil\n2SE = ' + str_se_std1_SIMS + '\n\nStd2:\n2SD = ' + str_sd_std2_SIMS + ' permil\n2SE = ' + str_se_std2_SIMS+ ' permil\n\nMSWD = ' + str_MSWD_tot + '\n\nEquation:\ny = ' + str_a2 + ' x^2 + ' + str_a1 + ' x + ' + str_a0 + '\n\n' + str_Summary
                self.textEdit_Stats.setText(set_text_Stats)
            elif polynomial_order == 3:
                str_a0 = "%.2f" %(a0)
                str_a1 = "%.2f" %(a1)
                str_a2 = "%.3f" %(a2)
                str_a3 = "%.4f" %(a3)
                set_text_Stats = 'Statistics:\n\nStd1:\n2SD = ' + str_sd_std1_SIMS + ' permil\n2SE = ' + str_se_std1_SIMS + '\n\nStd2:\n2SD = ' + str_sd_std2_SIMS + ' permil\n2SE = ' + str_se_std2_SIMS+ ' permil\n\nMSWD = ' + str_MSWD_tot + '\n\nEquation:\ny = ' + str_a3 + ' x^3 + ' + str_a2 + ' x^2 + ' + str_a1 + ' x + ' + str_a0 + '\n\n' + str_Summary
                self.textEdit_Stats.setText(set_text_Stats)
            elif polynomial_order == 4:
                str_a0 = "%.2f" %(a0)
                str_a1 = "%.2f" %(a1)
                str_a2 = "%.3f" %(a2)
                str_a3 = "%.4f" %(a3)
                str_a4 = "%.4f" %(a4)
                set_text_Stats = 'Statistics:\n\nStd1:\n2SD = ' + str_sd_std1_SIMS + ' permil\n2SE = ' + str_se_std1_SIMS + '\n\nStd2:\n2SD = ' + str_sd_std2_SIMS + ' permil\n2SE = ' + str_se_std2_SIMS+ ' permil\n\nMSWD = ' + str_MSWD_tot + '\n\nEquation:\ny = ' + str_a4 + ' x^4 + ' + str_a3 + ' x^3 + ' + str_a2 + 'x^2\n + ' + str_a1 + ' x + ' + str_a0 + '\n\n' + str_Summary
                self.textEdit_Stats.setText(set_text_Stats)


    def save_Stats_file(self):
        name_Stats_file = QFileDialog.getSaveFileName(self, 'Save Figure')
        name_save_Stats_file = name_Stats_file[0] + '.txt'
        stats = open(name_save_Stats_file,'w')
        stats.write(set_text_Stats)

class Data_selection_Window(QWidget, Table_Input_Matrix.Ui_Form):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        self.tableWidget_InputMat.setSelectionBehavior(QTableView.SelectRows)
        self.tableWidget_InputMat.setSelectionMode(QAbstractItemView.MultiSelection)
        if B_Mat_mod == 0:
            self.tableWidget_InputMat.setRowCount(len(B[var1_name]))
            self.tableWidget_InputMat.setColumnCount(len(B.columns))
            header = list(B.columns)
            self.tableWidget_InputMat.setHorizontalHeaderLabels(header)
            for i in range(len(B[var1_name])):
                for j in range(len(B.columns)):
                    self.tableWidget_InputMat.setItem(i,j,QTableWidgetItem(str(B.iloc[i, j])))

        if B_Mat_mod == 1:
            self.tableWidget_InputMat.setRowCount(len(B_mod[var1_name]))
            self.tableWidget_InputMat.setColumnCount(len(B_mod.columns))
            header = list(B_mod.columns)
            self.tableWidget_InputMat.setHorizontalHeaderLabels(header)
            for i in range(len(B_mod[var1_name])):
                for j in range(len(B_mod.columns)):
                    self.tableWidget_InputMat.setItem(i,j,QTableWidgetItem(str(B_mod.iloc[i, j])))

        self.pushButton_Delete.clicked.connect(self.Delete_Analysis)
        self.pushButton_Section.clicked.connect(self.Std_selection)
        
    def Delete_Analysis(self):
        global B_Mat_mod
        global B_mod
        global new_Cycles_tot
        indexes = self.tableWidget_InputMat.selectionModel().selectedRows()
        for index in sorted(indexes):
            Filename_to_delete = str(self.tableWidget_InputMat.item(index.row(),1).text())
            Filename_to_delete = float(Filename_to_delete)
            if B_Mat_mod == 0:
                B_mod = B[B[var1_name] != Filename_to_delete]
            elif B_Mat_mod == 1:
                B_mod = B_mod[B_mod[var1_name] != Filename_to_delete]
        B_Mat_mod = 1


    def Std_selection(self):
        global B_Mat_mod
        global B_section
        global Section_value
        global Unknown_data
        global Cycles_section
        global Unknown_section
        Unknown_section = []
        Cycles_section = []
        Cycles_sections = []
        global Analyses_section
        Analyses_section = []
        global Selection_section
        Selection_section = []
        B_section = []
        B_sections = []
        global x_unk
        x_unk = []
        indexes = self.tableWidget_InputMat.selectionModel().selectedRows()
        for index in sorted(indexes):
            Analysis_section = str(self.tableWidget_InputMat.item(index.row(),0).text())
            Analyses_section.append(Analysis_section)
            Selection_section_i = str(self.tableWidget_InputMat.item(index.row(),0).text())
            Selection_section.append(Selection_section_i)
        if B_Mat_mod == 0:
            for i in range(len(Selection_section)):
                Str_to_match = Selection_section[i]
                B_sections.append(B[B[var1_name].astype(str).str.contains(Str_to_match, regex=False)])
                if i == 0:
                    Unknown_section = B[B[var1_name] != Selection_section[i]]
                elif i >= 1:
                    Unknown_section = Unknown_section[Unknown_section[var1_name] != Selection_section[i]]
        elif B_Mat_mod == 1:
            for i in range(len(Selection_section)):
                Str_to_match = Selection_section[i]
                B_sections.append(B_mod[B_mod[var1_name].astype(str).str.contains(Str_to_match, regex=False)])
                if i == 0:
                    Unknown_section = B_mod[B_mod[var1_name] != Selection_section[i]]
                elif i >= 1:
                    Unknown_section = Unknown_section[Unknown_section[var1_name] != Selection_section[i]]
        Section_value = 1
        Unknown_data = 1
        x_unk = Unknown_section[var1_name]
        B_section = pd.concat(B_sections)


# class PopUp_Ref_iso_Layout(QDialog, PopUp_Ref_iso_Layout.Ui_Dialog_Ref_iso):
#     def __init__(self):
#         super(self.__class__, self).__init__()
#         self.setupUi(self)

#         self.lineEdit_Ref_iso.editingFinished.connect(self.Press_ref_iso)
#         self.lineEdit_sigma_iso.editingFinished.connect(self.Press_sigma_iso)
        
#     def Press_ref_iso(self):
#         global Ref_std_iso_value
#         try:
#             Ref_std_iso_value_str = self.lineEdit_Ref_iso.text()
#             Ref_std_iso_value = float(Ref_std_iso_value_str)
#         except Exception as e:
#             msg = QMessageBox()
#             msg.setIcon(QMessageBox.Warning)
#             msg.setText("Some information is missing")
#             msg.setWindowTitle("B reference data error")
#         else:
#             Ref_std_iso_value_str = self.lineEdit_Ref_iso.text()
#             Ref_std_iso_value = float(Ref_std_iso_value_str)
#     def Press_sigma_iso(self):
#         global Ref_sigma_iso_value
#         try:
#             Ref_sigma_iso_value_str =self.lineEdit_sigma_iso.text()
#             Ref_sigma_iso_value = float(Ref_sigma_iso_value_str)
#         except Exception as e:
#             msg = QMessageBox()
#             msg.setIcon(QMessageBox.Warning)
#             msg.setText("Some information is missing")
#             msg.setWindowTitle("B reference data error")
#         else:
#             Ref_std_iso_value_str = self.lineEdit_Ref_iso.text()
#             Ref_std_iso_value = float(Ref_std_iso_value_str)


class Figure_residuals_Window(QWidget, Figure_std_Layout.Ui_Form):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.pushButton_saveFigure.clicked.connect(self.save_residuals_Fig)

        self.dpi = 100
        self.figResiduals = plt.Figure((10.7, 6.8), dpi=self.dpi)
        self.FigCanvas = FigureCanvas(self.figResiduals)
        self.FigCanvas.setParent(self.Frame_FigData)
        axes = self.figResiduals.add_subplot(111)
        if nb_variables_value == 1 and polynomial_order >= 1:
            axes.errorbar(x_std,r_std, yerr=error_IMF_std, fmt='ko', ecolor='k', capthick=2)
            axes.plot(x, np.zeros((len(x), 1)), 'k--', linewidth=2)
            axes.plot(x, sigma_fit_u, 'k:', linewidth=0.3)
            axes.plot(x, sigma_fit_l, 'k:', linewidth=0.3)
            axes.set_xlabel(var1_name, fontsize=15)
            axes.set_ylabel(u"$Residuals$ (‰)")
            self.FigCanvas.subplots_adjust(0.06, 0.1, 0.97, 0.95)
        elif nb_variables_value == 2 and polynomial_order >= 1:
            axes.errorbar(x1_std,r_std1, yerr=error_IMF_std1, fmt='ko', ecolor='k', capthick=2)
            axes.errorbar(x2_std,r_std2, yerr=error_IMF_std2, fmt='kd', ecolor='k', capthick=2)
            axes.plot(x, np.zeros((len(x), 1)), 'k--', linewidth=2)
            axes.set_xlabel('Time (h)')
            axes.set_ylabel(u"$Residuals$ (‰)")
            self.FigCanvas.subplots_adjust(0.06, 0.1, 0.97, 0.95)
        elif nb_variables_value == 3 and polynomial_order >= 1:
            axes.errorbar(x1_std,r_std1, yerr=error_IMF_std1, fmt='ko', ecolor='k', capthick=2)
            axes.errorbar(x2_std,r_std2, yerr=error_IMF_std2, fmt='kd', ecolor='k', capthick=2)
            axes.errorbar(x3_std,r_std3, yerr=error_IMF_std3, fmt='ks', ecolor='k', capthick=2)
            axes.plot(x, np.zeros((len(x), 1)), 'k--', linewidth=2)
            axes.set_xlabel('Time (h)')
            axes.set_ylabel(u"$Residuals$ (‰)")
            self.FigCanvas.subplots_adjust(0.06, 0.1, 0.97, 0.95)
        self.FigCanvas.show()

    def save_residuals_Fig(self):
        name_Fig_Residuals = QFileDialog.getSaveFileName(self, 'Save File')
        name_save_Fig_residuals = name_Fig_Residuals[0] + '.eps'
        self.figResiduals.savefig(name_save_Fig_residuals, dpi=300, format=None)


class Figure_std_Window(QWidget, Figure_std_Layout.Ui_Form):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.pushButton_saveFigure.clicked.connect(self.save_data_Fig)

        self.dpi = 100
        self.figData = plt.Figure((10.7, 6.8), dpi=self.dpi)
        self.FigCanvas = FigureCanvas(self.figData)
        self.FigCanvas.setParent(self.Frame_FigData)
        axes = self.figData.add_subplot(111)
        if self.nb_variables_value == 1 and self.polynomial_order >= 1:
            axes.errorbar(x_std,IMF_std, yerr=error_IMF_std, fmt='ko', ecolor='k', capthick=2)
            axes.plot(x, fit_std, 'k--', linewidth=1)
            axes.plot(x, fit_predicted_u, 'k-.', linewidth=1)
            axes.plot(x, fit_predicted_l, 'k-.', linewidth=1)
            axes.set_ylabel(target_name, fontsize=15)
            axes.set_xlabel(var1_name, fontsize=15)
            self.figData.subplots_adjust(0.06, 0.1, 0.97, 0.95)
        elif self.nb_variables_value == 2 and self.polynomial_order >= 1:
            axes.errorbar(x1_std,IMF_std1, yerr=error_IMF_std1, fmt='ko', ecolor='k', capthick=2)
            axes.errorbar(x2_std,IMF_std2, yerr=error_IMF_std2, fmt='kd', ecolor='k', capthick=2)
            axes.plot(x, fit_std1, 'k--', linewidth=1)
            axes.plot(x, fit_std2, 'k--', linewidth=1)
            axes.plot(x1_std, interval_u_std1, 'k-.', linewidth=1)
            axes.plot(x1_std, interval_l_std1, 'k-.', linewidth=1)
            axes.plot(x2_std, interval_u_std2, 'k-.', linewidth=1)
            axes.plot(x2_std, interval_l_std2, 'k-.', linewidth=1)
            axes.set_ylabel(target_name, fontsize=15)
            axes.set_xlabel(var1_name, fontsize=15)
            self.figData.subplots_adjust(0.06, 0.1, 0.97, 0.95)
        elif self.nb_variables_value == 3 and self.polynomial_order >= 1:
            axes.errorbar(x1_std,IMF_std1, yerr=error_IMF_std1, fmt='ko', ecolor='k', capthick=2)
            axes.errorbar(x2_std,IMF_std2, yerr=error_IMF_std2, fmt='kd', ecolor='k', capthick=2)
            axes.errorbar(x3_std,IMF_std3, yerr=error_IMF_std3, fmt='ks', ecolor='k', capthick=2)
            axes.plot(x, fit_std1, 'k--', linewidth=1)
            axes.plot(x, fit_std2, 'k--', linewidth=1)
            axes.plot(x, fit_std3, 'k--', linewidth=1)
            axes.plot(x1_std, interval_u_std1, 'k-.', linewidth=1)
            axes.plot(x1_std, interval_l_std1, 'k-.', linewidth=1)
            axes.plot(x2_std, interval_u_std2, 'k-.', linewidth=1)
            axes.plot(x2_std, interval_l_std2, 'k-.', linewidth=1)
            axes.plot(x3_std, interval_u_std3, 'k-.', linewidth=1)
            axes.plot(x3_std, interval_l_std3, 'k-.', linewidth=1)
            axes.set_ylabel(target_name, fontsize=15)
            axes.set_xlabel(var1_name, fontsize=15)
            self.figData.subplots_adjust(0.06, 0.1, 0.97, 0.95)
        self.FigCanvas.show()

    def save_data_Fig(self):
        name_Fig_Data = QFileDialog.getSaveFileName(self, 'Save File')
        name_save_Fig_Data = name_Fig_Data[0] + '.eps'
        self.figData.savefig(name_save_Fig_Data, dpi=300, format=None)


class Figure_Stats_Window(QWidget, Figure_Statistics.Ui_Form):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.pushButton_saveFigure.clicked.connect(self.save_stats_Fig)

        self.dpi = 100
        self.figStats = plt.Figure((11.8, 5.8), dpi=self.dpi)
        self.FigCanvas = FigureCanvas(self.figStats)
        self.FigCanvas.setParent(self.Frame_FigStats)
        axe1 = self.figStats.add_subplot(121)
        axe1.set_xlabel('Degrees fo freedom')
        axe1.set_ylabel('MSWD')
        axe1.set_xlim([0, 100])
        axe1.set_ylim([0, 3.5])
        x_df = np.linspace(0,100,400)
        sd_MSWDp = 1 + 2 * np.sqrt(2/x_df)
        sd_MSWDm = 1 - 2 * np.sqrt(2/x_df)
        s_MSWDm = 1 - np.sqrt(2/x_df)
        s_MSWDp = 1 + np.sqrt(2/x_df)
        axe1.plot(df_std, MSWD, 'ko', markersize=6)
        axe1.plot(x_df, np.ones((len(x_df), 1)), 'k--', linewidth=2)
        axe1.plot(x_df, sd_MSWDp, 'k:', linewidth=1)
        axe1.plot(x_df, sd_MSWDm, 'k:', linewidth=1)
        axe1.plot(x_df, s_MSWDp, 'k-.', linewidth=1)
        axe1.plot(x_df, s_MSWDm, 'k-.', linewidth=1)        
        axe2 = self.figStats.add_subplot(122)
        res = stats.probplot(r_std, fit=False, plot=axe2)
        axe2.get_lines()[0].set_marker('o')
        axe2.get_lines()[0].set_markerfacecolor('k')
        axe2.get_lines()[0].set_markeredgecolor('k')
        axe2.get_lines()[0].set_markersize(3)
        axe2.get_lines()[1].set_linewidth(1)
        axe2.get_lines()[1].set_linestyle('--')
        axe2.get_lines()[1].set_color("black")
        axe2.set_title('Normal Probability Plot')
        axe2.set_xlabel('Normal Theoretical Quantiles')
        axe2.set_ylabel('Standard(s) Quantiles')
        self.figStats.subplots_adjust(0.06, 0.1, 0.98, 0.94)

    def save_stats_Fig(self):
        name_Fig_Stats = QFileDialog.getSaveFileName(self, 'Save File')
        name_save_Fig_Stats = name_Fig_Stats[0] + '.eps'
        self.figStats.savefig(name_save_Fig_Stats, dpi=300, format=None)


class Matrix_SIMS_App(QMainWindow, Matrix_SIMS_Layout.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        self.home()

## Define all default variables

    global B_Mat_mod
    B_Mat_mod = 0
    global Error_x_value
    Error_x_value = 0
    global Section_value
    Section_value = 0
    global Unknown_data
    Unknown_data = 0
    global nb_variables_value
    nb_variables_value = 1
    global drift_iso_value
    drift_iso_value = 1
    global polynomial_order
    polynomial_order = 1
    global Auto_bias_iso_value
    Auto_bias_iso_value = 0


## Define all connections for the GUI

    def home(self):
        self.actionQuit.triggered.connect(self.close_application)
        self.actionAbout_MatriSIMS.triggered.connect(self.display_About_window)
        self.actionData.triggered.connect(self.Input_data)
        self.actionAdvanced_statistics.triggered.connect(self.figure_Statistics)
        self.actionStatistics.triggered.connect(self.Window_Statistics_fit)
        self.actionStandards.triggered.connect(self.figure_standards_show)
        self.actionResiduals_2.triggered.connect(self.figure_residuals_show)
        self.actionStandard_data.triggered.connect(self.output_standard_data)
        self.actionSample_data.triggered.connect(self.output_sample_data)
        self.actionInput_data.triggered.connect(self.input)
        self.pushButton_file.clicked.connect(self.file_browse)
        self.pushButton_fit.clicked.connect(self.plot_data)
        self.comboBox_nb_variables.activated.connect(self.nb_variables)
        self.comboBox_fit_order.activated.connect(self.fit_order)
        self.checkBox_error_X.stateChanged.connect(self.enable_error_X)
        self.checkBox_bias_iso.stateChanged.connect(self.enable_ref_value_iso)
        self.comboBox_target.activated.connect(self.target_variable)
        self.comboBox_target_error.activated.connect(self.target_error_variable)
        self.comboBox_var1_name.activated.connect(self.var1_name_iso)
        self.comboBox_var2_name.activated.connect(self.var2_name_iso)
        self.comboBox_var3_name.activated.connect(self.var3_name_iso)
        self.comboBox_var1_error_name.activated.connect(self.error1_name_iso)
        self.comboBox_var2_error_name.activated.connect(self.error2_name_iso)
        self.comboBox_var3_error_name.activated.connect(self.error3_name_iso)
    

## Define all actions for each interaction with the GUI

    def close_application(self):
        choice = QMessageBox.question(self, 'Quit!?',
                                      "Do you really want to quit the application? Any unsaved changes will be lost.",
                                      QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            sys.exit()
        else:
            pass

    def display_About_window(self):
        self.About_Window = About_Window()
        self.About_Window.show()


    def file_browse(self):
        global name
        name, _ = QFileDialog.getOpenFileNames(self, "Select the .asc files to import", "Desktop", filter='*.xlsx')
        global Input
        Input = pd.read_excel(name[0])
        self.populate_dropdown_menus()


    def populate_dropdown_menus(self):
        global list_item
        list_item = list(Input.columns.values)
        _translate = QtCore.QCoreApplication.translate
        for i in range(len(list_item)):
            self.comboBox_target.addItem("")
            self.comboBox_target_error.addItem("")
            self.comboBox_var1_name.addItem("")
            self.comboBox_var2_name.addItem("")
            self.comboBox_var3_name.addItem("")
            self.comboBox_var1_error_name.addItem("")
            self.comboBox_var2_error_name.addItem("")
            self.comboBox_var3_error_name.addItem("")
            self.comboBox_target.setItemText(i, _translate("MainWindow", list_item[i]))
            self.comboBox_target_error.setItemText(i, _translate("MainWindow", list_item[i]))
            self.comboBox_var1_name.setItemText(i, _translate("MainWindow", list_item[i]))
            self.comboBox_var2_name.setItemText(i, _translate("MainWindow", list_item[i]))
            self.comboBox_var3_name.setItemText(i, _translate("MainWindow", list_item[i]))
            self.comboBox_var1_error_name.setItemText(i, _translate("MainWindow", list_item[i]))
            self.comboBox_var2_error_name.setItemText(i, _translate("MainWindow", list_item[i]))
            self.comboBox_var3_error_name.setItemText(i, _translate("MainWindow", list_item[i]))

    # def import_data(self):
    #     global Input
    #     Input = pd.read_excel(name[0])
    #     self.variables_def()


    def target_variable(self, target_name_arg):
        print(self.comboBox_target.itemText(target_name_arg))
        global target_name
        target_name = None
        target_name_str = self.comboBox_target.itemText(target_name_arg)
        target_name = str(target_name_str)

    def target_error_variable(self, target_name_error_arg):
        global target_error_name
        target_error_name = None
        target_error_name_str = self.comboBox_target.itemText(target_name_error_arg)
        target_error_name = str(target_error_name_str)        

    def var1_name_iso(self, target_var1_name_arg):
        global var1_name
        var1_name = None
        var1_name_str = self.comboBox_target.itemText(target_var1_name_arg)
        var1_name = str(var1_name_str)

    def var2_name_iso(self, target_var2_name_arg):
        global var2_name
        var2_name = None
        var2_name_str = self.comboBox_target.itemText(target_var2_name_arg)
        var2_name = str(var2_name_str)

    def var3_name_iso(self, target_var3_name_arg):
        global var3_name
        var3_name = None
        var3_name_str = self.comboBox_target.itemText(target_var3_name_arg)
        var3_name = str(var3_name_str)

    def error1_name_iso(self, target_var1_error_name_arg):
        global error1_name
        error1_name = None
        error1_name_str = self.comboBox_target.itemText(target_var1_error_name_arg)
        error1_name = str(error1_name_str)

    def error2_name_iso(self, target_var2_error_name_arg):
        global error2_name
        error2_name = None
        error2_name_str = self.comboBox_target.itemText(target_var2_error_name_arg)
        error2_name = str(error2_name_str)

    def error3_name_iso(self, target_var3_error_name_arg):
        global error3_name
        error3_name = None
        error3_name_str = self.comboBox_target.itemText(target_var3_error_name_arg)
        error3_name = str(error3_name_str)

    def variables_def(self):
        global B
        B = Input.sort_values(by=[var1_name])
        global IMF_std
        global error_IMF_std
        if B_Mat_mod == 0:
            if Section_value == 0:
                IMF_std = B[target_name]
                error_IMF_std = B[target_error_name]
                if nb_variables_value == 1:
                    global x_std
                    x_std = B[var1_name]
                    if Error_x_value == 1:
                        global x_error_std
                        x_error_std = B[error1_name]
                elif nb_variables_value == 2:
                    global x1_std
                    global x2_std
                    x1_std = B[var1_name]
                    x2_std = B[var2_name]
                    if Error_x_value == 1:
                        global x1_error_std
                        global x2_error_std
                        x1_error_std = B[error1_name]
                        x2_error_std = B[error2_name]
                elif nb_variables_value == 3:
                    global x3_std
                    x1_std = B[var1_name]
                    x2_std = B[var2_name]
                    x3_std = B[var3_name]
                    if Error_x_value == 1:
                        global x3_error_std
                        x1_error_std = B[error1_name]
                        x2_error_std = B[error2_name]
                        x3_error_std = B[error3_name]
            else:
                IMF_std = B_section[target_name]
                error_IMF_std = B_section[target_error_name]
                if nb_variables_value == 1:
                    x_std = B_section[var1_name]
                    if Error_x_value == 1:
                        x_error_std = B_section[error1_name]
                elif nb_variables_value == 2:
                    x1_std = B_section[var1_name]
                    x2_std = B_section[var2_name]
                    if Error_x_value == 1:
                        x1_error_std = B_section[error1_name]
                        x2_error_std = B_section[error2_name]
                elif nb_variables_value == 3:
                    x1_std = B_section[var1_name]
                    x2_std = B_section[var2_name]
                    x3_std = B_section[var3_name]
                    if Error_x_value == 1:
                        x1_error_std = B_section[error1_name]
                        x2_error_std = B_section[error2_name]
                        x3_error_std = B_section[error3_name]
        else:
            if Section_value == 0:
                IMF_std = B_mod[target_name]
                error_IMF_std = B_mod[target_error_name]
            else:
                IMF_std = B_section[target_name]
                error_IMF_std = B_section[target_error_name]
                if nb_variables_value == 1:
                    x_std = B_section[var1_name]
                    if Error_x_value == 1:
                        x_error_std = B_section[error1_name]
                elif nb_variables_value == 2:
                    x1_std = B_section[var1_name]
                    x2_std = B_section[var2_name]
                    if Error_x_value == 1:
                        x1_error_std = B_section[error1_name]
                        x2_error_std = B_section[error2_name]
                elif nb_variables_value == 3:
                    x1_std = B_section[var1_name]
                    x2_std = B_section[var2_name]
                    x3_std = B_section[var3_name]
                    if Error_x_value == 1:
                        x1_error_std = B_section[error1_name]
                        x2_error_std = B_section[error2_name]
                        x3_error_std = B_section[error3_name]
        self.fit_data()

        

    def fit_data(self):
        global x1
        global x2
        global x3
        global x_std_2
        global x_std_3
        global x_std_4
        global fit_std
        global r_std
        global wls_mod
        global a0
        global a1
        global a2
        global a3
        global a4
        global a5
        global a6
        global a7
        global iv_u
        global iv_l
        global results
        global w_std
        global X
        global Y
        global x
        global p_values_a0
        global p_values_a1
        global p_values_a2
        global alpha
        global IMF_m
        msg_pvalues = QMessageBox()
        msg_pvalues.setIcon(QMessageBox.Warning)
        msg_pvalues.setText("One or more coefficient has a low p-value.\nOne or more coefficient is not statistically significant.\nCheck the stats.txt file.")
        msg_pvalues.setWindowTitle("Warning: fit not meaningfull")
        alpha = 0.05
        polynomial_order == 5
        if Auto_bias_iso_value == 1 and Unknown_data == 1:
            if nb_variables_value == 1:
                x1_unk = Unknown_section[var1_name]
            elif nb_variables_value == 1:
                x1_unk = Unknown_section[var1_name]
                x2_unk = Unknown_section[var2_name]
            else:
                x1_unk = Unknown_section[var1_name]
                x2_unk = Unknown_section[var2_name]
                x3_unk = Unknown_section[var3_name]
        if nb_variables_value == 1 and polynomial_order == 1:
            X = np.column_stack((np.ones((len(x_std), 1)), x_std))
            w_std = 1 / (np.asarray(error_IMF_std) ** 2)
            wls_model = WLS(IMF_std, X, weights=w_std)
            results = wls_model.fit()
            a0 = results.params[0]
            a1 = results.params[1]
            x = np.linspace(min(np.asarray(x_std)), max(np.asarray(x_std)), 200)
            fit_std = a1 * x + a0
            wls_mod = results.predict()
            r_std = np.asarray(IMF_std) - np.asarray(wls_mod)
            if Auto_bias_iso_value == 1 and Unknown_data == 1:
                IMF_m = a1 * x1_unk + a0
            p_values_a0 = results.pvalues[0]
            p_values_a1 = results.pvalues[1]
            if p_values_a0 >= 0.05 or p_values_a1 >= 0.05:
                msg_pvalues.exec_()
            else:
                pass
        elif nb_variables_value == 1 and polynomial_order == 2:
            x_std_2 = np.asarray(x_std) ** 2
            X = np.column_stack((np.ones((len(x_std), 1)), x_std, x_std_2))
            w_std = 1 / (np.asarray(error_IMF_std) ** 2)
            wls_model = WLS(IMF_std, X, weights=w_std)
            results = wls_model.fit()
            a0 = results.params[0]
            a1 = results.params[1]
            a2 = results.params[2]
            x = np.linspace(min(np.asarray(x_std)), max(np.asarray(x_std)), 200)
            fit_std = a2 * (x ** 2) + a1 * x + a0
            wls_mod = results.predict()
            r_std = np.asarray(IMF_std) - np.asarray(wls_mod)
            if Auto_bias_iso_value == 1 and Unknown_data == 1:
                IMF_m = a2 * (x1_unk ** 2) + a1 * x1_unk + a0
            p_values_a0 = results.pvalues[0]
            p_values_a1 = results.pvalues[1]
            p_values_a2 = results.pvalues[2]
            if p_values_a0 >= 0.05 or p_values_a1 >= 0.05 or p_values_a2 >= 0.05:
                msg_pvalues.exec_()
            else:
                pass
        elif nb_variables_value == 1 and polynomial_order == 3:
            x_std_2 = np.asarray(x_std) ** 2
            x_std_3 = np.asarray(x_std) ** 3
            X = np.column_stack((np.ones((len(x_std), 1)), x_std, x_std_2, x_std_3))
            w_std = 1 / (np.asarray(error_IMF_std) ** 2)
            wls_model = WLS(IMF_std, X, weights=w_std)
            results = wls_model.fit()
            a0 = results.params[0]
            a1 = results.params[1]
            a2 = results.params[2]
            a3 = results.params[3]
            x = np.linspace(min(np.asarray(x_std)), max(np.asarray(x_std)), 200)
            fit_std = a3 * (x ** 3) + a2 * (x ** 2) + a1 * x + a0
            wls_mod = results.predict()
            r_std = np.asarray(IMF_std) - np.asarray(wls_mod)
            if Auto_bias_iso_value == 1 and Unknown_data == 1:
                IMF_m = a3 * (x1_unk ** 3) + a2 * (x1_unk ** 2) + a1 * x1_unk + a0
            p_values_a0 = results.pvalues[0]
            p_values_a1 = results.pvalues[1]
            p_values_a2 = results.pvalues[2]
            p_values_a3 = results.pvalues[3] 
            if p_values_a0 >= 0.05 or p_values_a1 >= 0.05 or p_values_a2 >= 0.05 or p_values_a3 >= 0.05:
                msg_pvalues.exec_()
            else:
                pass
        elif nb_variables_value == 1 and polynomial_order == 4:
            x_std_2 = np.asarray(x_std) ** 2
            x_std_3 = np.asarray(x_std) ** 3
            x_std_4 = np.asarray(x_std) ** 4
            X = np.column_stack((np.ones((len(x_std), 1)), x_std, x_std_2, x_std_3, x_std_4))
            w_std = 1 / (np.asarray(error_IMF_std) ** 2)
            wls_model = WLS(IMF_std, X, weights=w_std)
            results = wls_model.fit()
            a0 = results.params[0]
            a1 = results.params[1]
            a2 = results.params[2]
            a3 = results.params[3]
            a4 = results.params[4]
            x = np.linspace(min(np.asarray(x_std)), max(np.asarray(x_std)), 200)
            fit_std = a4 * (x ** 4) + a3 * (x ** 3) + a2 * (x ** 2) + a1 * x + a0
            wls_mod = results.predict()
            r_std = np.asarray(IMF_std) - np.asarray(wls_mod)
            if Auto_bias_iso_value == 1 and Unknown_data_value == 1:
                IMF_m = a4 * (x1_unk ** 4) + a3 * (x1_unk ** 3) + a2 * (x1_unk ** 2) + a1 * x1_unk + a0
            p_values_a0 = results.pvalues[0]
            p_values_a1 = results.pvalues[1]
            p_values_a2 = results.pvalues[2]
            p_values_a3 = results.pvalues[3] 
            p_values_a4 = results.pvalues[4]
            if p_values_a0 >= 0.05 or p_values_a1 >= 0.05 or p_values_a2 >= 0.05 or p_values_a3 >= 0.05 or p_values_a4 >= 0.05:
                msg_pvalues.exec_()
            else:
                pass
        # elif nb_variables_value == 1 and polynomial_order == 5:
        #     def func(x,b0,b1,b2,b3):
        #         """ Hill equation, takes:
        #         x, independant variable,
        #         4 coefficients (b0, b1, b2, b3)
        #         return y """

        #         y = b0 + (b1 * np.asarray(x)**b2) / (b3**b2 + np.asarray(x)**b2)
        #         return y

        #     popt, pcov = optimize.curve_fit(func_hill, xdata=x-std, ydata=IMF_std)

        #     return popt, pcov, fit_std, r_std

        elif nb_variables_value == 2 and polynomial_order == 1:
            print(Input)
            print(x1_std)
            print(x2_std)
            X = np.column_stack((np.ones((len(x1_std), 1)), x1_std, x2_std))
            w_std = 1 / (np.asarray(error_IMF_std) ** 2)
            wls_model = WLS(IMF_std, X, weights=w_std)
            results = wls_model.fit()
            global Summary
            Summary = results.summary()
            print(Summary)
            a0 = results.params[0]
            a1 = results.params[1]
            a2 = results.params[2]
            x1 = np.linspace(min(np.asarray(x1_std)), max(np.asarray(x1_std)), 200)
            x2 = np.linspace(min(np.asarray(x2_std)), max(np.asarray(x2_std)), 200)
            fit_std = a1 * x1 + a2 * x2 + a0
            wls_mod = results.predict()
            r_std = np.asarray(IMF_std) - np.asarray(wls_mod)
            if Auto_bias_iso_value == 1 and Unknown_data == 1:
                IMF_m = a1 * x1_unk + a2 * x2_unk + a0
            p_values_a0 = results.pvalues[0]
            p_values_a1 = results.pvalues[1]
            p_values_a2 = results.pvalues[2]
            if p_values_a0 >= 0.05 or p_values_a1 >= 0.05 or p_values_a2 >= 0.05:
                msg_pvalues.exec_()
            else:
                pass 
        elif nb_variables_value == 2 and polynomial_order == 2:
            x1_std_2 = np.asarray(x1_std) ** 2
            x2_std_2 = np.asarray(x2_std) ** 2
            X = np.column_stack((np.ones((len(x1_std), 1)), x1_std, x1_std_2, x2_std, x2_std_2))
            w_std = 1 / (np.asarray(error_IMF_std) ** 2)
            wls_model = WLS(IMF_std, X, weights=w_std)
            results = wls_model.fit()
            a0 = results.params[0]
            a1 = results.params[1]
            a2 = results.params[2]
            a3 = results.params[3]
            a4 = results.params[4]
            x1 = np.linspace(min(np.asarray(x1_std)), max(np.asarray(x1_std)), 200)
            x2 = np.linspace(min(np.asarray(x2_std)), max(np.asarray(x2_std)), 200)
            fit_std = a1 * x1 + a2 * x1 ** 2 + a3 * x2 + a4 * x2 ** 2 + a0
            wls_mod = results.predict()
            r_std = np.asarray(IMF_std) - np.asarray(wls_mod)
            if Auto_bias_iso_value == 1 and Unknown_data == 1:
                IMF_m = a1 * x1_unk + a2 * x1_unk ** 2 + a3 * x2_unk + a4 * x2_unk ** 2 + a0
            p_values_a0 = results.pvalues[0]
            p_values_a1 = results.pvalues[1]
            p_values_a2 = results.pvalues[2]
            p_values_a3 = results.pvalues[3]
            p_values_a4 = results.pvalues[4]
            if p_values_a0 >= 0.05 or p_values_a1 >= 0.05 or p_values_a2 >= 0.05 or p_values_a3 >= 0.05 or p_values_a4 >= 0.05:
                msg_pvalues.exec_()
            else:
                pass  
        elif nb_variables_value == 2 and polynomial_order == 3:
            x1_std_2 = np.asarray(x1_std) ** 2
            x1_std_3 = np.asarray(x1_std) ** 3
            x2_std_2 = np.asarray(x2_std) ** 2
            x2_std_3 = np.asarray(x2_std) ** 3
            X = np.column_stack((np.ones((len(x1_std), 1)), x1_std, x1_std_2, x1_std_3, x2_std, x2_std_2, x2_std_3))
            w_std = 1 / (np.asarray(error_IMF_std) ** 2)
            wls_model = WLS(IMF_std, X, weights=w_std)
            results = wls_model.fit()
            a0 = results.params[0]
            a1 = results.params[1]
            a2 = results.params[2]
            a3 = results.params[3]
            a4 = results.params[4]
            a5 = results.params[5]
            a6 = results.params[6]
            x1 = np.linspace(min(np.asarray(x1_std)), max(np.asarray(x1_std)), 200)
            x2 = np.linspace(min(np.asarray(x2_std)), max(np.asarray(x2_std)), 200)
            fit_std = a1 * x1 + a2 * x1 ** 2 + a3 * x1 ** 3 + a4 * x2 + a5 * x2 ** 2 + a6 * x2 ** 3 + a0
            wls_mod = results.predict()
            r_std = np.asarray(IMF_std) - np.asarray(wls_mod)
            if Auto_bias_iso_value == 1 and Unknown_data == 1:
                IMF_m = a1 * x1_unk + a2 * x1_unk ** 2 + a3 * x1_unk ** 3 + a4 * x2_unk + a5 * x2_unk ** 2 + a6 * x2_unk ** 3 + a0
            p_values_a0 = results.pvalues[0]
            p_values_a1 = results.pvalues[1]
            p_values_a2 = results.pvalues[2]
            p_values_a3 = results.pvalues[3] 
            p_values_a4 = results.pvalues[4] 
            p_values_a5 = results.pvalues[5] 
            p_values_a6 = results.pvalues[6] 
            if p_values_a0 >= 0.05 or p_values_a1 >= 0.05 or p_values_a2 >= 0.05 or p_values_a3 >= 0.05 or p_values_a4 >= 0.05 or p_values_a5 >= 0.05 or p_values_a6 >= 0.05:
                msg_pvalues.exec_()
            else:
                pass 
        elif nb_variables_value == 2 and polynomial_order == 4:
            x1_std_2 = np.asarray(x1_std) ** 2
            x1_std_3 = np.asarray(x1_std) ** 3
            x1_std_4 = np.asarray(x1_std) ** 4
            x2_std_2 = np.asarray(x2_std) ** 2
            x2_std_3 = np.asarray(x2_std) ** 3
            x2_std_4 = np.asarray(x2_std) ** 4
            X = np.column_stack((np.ones((len(x1_std), 1)), x1_std, x1_std_2, x1_std_3, x1_std_4, x2_std, x2_std_2, x2_std_3, x2_std_4))
            w_std = 1 / (np.asarray(error_IMF_std) ** 2)
            wls_model = WLS(IMF_std, X, weights=w_std)
            results = wls_model.fit()
            a0 = results.params[0]
            a1 = results.params[1]
            a2 = results.params[2]
            a3 = results.params[3]
            a4 = results.params[4]
            a5 = results.params[5]
            a6 = results.params[6]
            a7 = results.params[7]
            a8 = results.params[8]
            x1 = np.linspace(min(np.asarray(x1_std)), max(np.asarray(x1_std)), 200)
            x2 = np.linspace(min(np.asarray(x2_std)), max(np.asarray(x2_std)), 200)
            fit_std = a1 * x1 + a2 * x1 ** 2 + a3 * x1 ** 3 + a4 * x1 ** 4 + a5 * x2 + a6 * x2 ** 2 + a7 * x2 ** 3 + a8 * x2 ** 4 + a0
            wls_mod = results.predict()
            r_std = np.asarray(IMF_std) - np.asarray(wls_mod)
            if Auto_bias_iso_value == 1 and Unknown_data == 1:
                IMF_m = a1 * x1_unk + a2 * x1_unk ** 2 + a3 * x1_unk ** 3 + a4 * x1_unk ** 4 + a5 * x2_unk + a6 * x2_unk ** 2 + a7 * x2_unk ** 3 + a8 * x2_unk ** 4 + a0
            p_values_a0 = results.pvalues[0]
            p_values_a1 = results.pvalues[1]
            p_values_a2 = results.pvalues[2]
            p_values_a3 = results.pvalues[3] 
            p_values_a4 = results.pvalues[4] 
            p_values_a5 = results.pvalues[5]
            p_values_a6 = results.pvalues[6]
            p_values_a7 = results.pvalues[7] 
            p_values_a8 = results.pvalues[8] 
            if p_values_a0 >= 0.05 or p_values_a1 >= 0.05 or p_values_a2 >= 0.05 or p_values_a3 >= 0.05 or p_values_a4 >= 0.05 or p_values_a5 >= 0.05 or p_values_a6 >= 0.05 or p_values_a7 >= 0.05 or p_values_a8 >= 0.05:
                msg_pvalues.exec_()
            else:
                pass 
        elif nb_variables_value == 3 and polynomial_order == 1:
            X = np.column_stack((np.ones((len(x1_std), 1)), x1_std, x2_std, x3_std))
            w_std = 1 / (np.asarray(error_IMF_std) ** 2)
            wls_model = WLS(IMF_std, X, weights=w_std)
            results = wls_model.fit()
            a0 = results.params[0]
            a1 = results.params[1]
            a2 = results.params[2]
            a3 = results.params[3]
            x1 = np.linspace(min(np.asarray(x1_std)), max(np.asarray(x1_std)), 200)
            x2 = np.linspace(min(np.asarray(x2_std)), max(np.asarray(x2_std)), 200)
            x3 = np.linspace(min(np.asarray(x3_std)), max(np.asarray(x3_std)), 200)
            fit_std = a1 * x1 + a2 * x2 + a3 * x3 + a0
            wls_mod = results.predict()
            r_std = np.asarray(IMF_std) - np.asarray(wls_mod)
            if Auto_bias_iso_value == 1 and Unknown_data == 1:
                IMF_m = a1 * x1_unk + a2 * x2_unk + a3 * x3_unk + a0
            p_values_a0 = results.pvalues[0]
            p_values_a1 = results.pvalues[1]
            p_values_a2 = results.pvalues[2]
            p_values_a3 = results.pvalues[3] 
            if p_values_a0 >= 0.05 or p_values_a1 >= 0.05 or p_values_a2 >= 0.05 or p_values_a3 >= 0.05:
                msg_pvalues.exec_()
            else:
                pass
        elif nb_variables_value == 3 and polynomial_order == 2:
            x1_std_2 = np.asarray(x1_std) ** 2
            x2_std_2 = np.asarray(x2_std) ** 2
            x3_std_2 = np.asarray(x3_std) ** 2
            X = np.column_stack((np.ones((len(x1_std), 1)), x1_std, x1_std_2, x2_std, x2_std_2, x3_std, x3_std_2))
            w_std = 1 / (np.asarray(error_IMF_std) ** 2)
            wls_model = WLS(IMF_std, X, weights=w_std)
            results = wls_model.fit()
            a0 = results.params[0]
            a1 = results.params[1]
            a2 = results.params[2]
            a3 = results.params[3]
            a4 = results.params[4]
            a5 = results.params[5]
            a6 = results.params[6]
            x1 = np.linspace(min(np.asarray(x1_std)), max(np.asarray(x1_std)), 200)
            x2 = np.linspace(min(np.asarray(x2_std)), max(np.asarray(x2_std)), 200)
            x3 = np.linspace(min(np.asarray(x3_std)), max(np.asarray(x3_std)), 200)
            fit_std = a1 * x1 + a2 * x1 ** 2 + a3 * x2 + a4 * x2 ** 2 + a5 * x3 + a6 * x3 ** 2 + a0
            wls_mod = results.predict()
            r_std = np.asarray(IMF_std) - np.asarray(wls_mod)
            if Auto_bias_iso_value == 1 and Unknown_data == 1:
                IMF_m = a1 * x1_unk + a2 * x1_unk ** 2 + a3 * x2_unk + a4 * x2_unk ** 2 + a5 * x3_unk + a6 * x3_unk ** 2 + a0
            p_values_a0 = results.pvalues[0]
            p_values_a1 = results.pvalues[1]
            p_values_a2 = results.pvalues[2]
            p_values_a3 = results.pvalues[3] 
            p_values_a4 = results.pvalues[4] 
            p_values_a5 = results.pvalues[5]
            p_values_a6 = results.pvalues[6]
            if p_values_a0 >= 0.05 or p_values_a1 >= 0.05 or p_values_a2 >= 0.05 or p_values_a3 >= 0.05 or p_values_a4 >= 0.05 or p_values_a5 >= 0.05 or p_values_a6 >= 0.05:
                msg_pvalues.exec_()
            else:
                pass
        elif nb_variables_value == 3 and polynomial_order == 3:
            x1_std_2 = np.asarray(x1_std) ** 2
            x1_std_3 = np.asarray(x1_std) ** 3
            x2_std_2 = np.asarray(x2_std) ** 2
            x2_std_3 = np.asarray(x2_std) ** 3
            x3_std_2 = np.asarray(x3_std) ** 2
            x3_std_3 = np.asarray(x3_std) ** 3
            X = np.column_stack((np.ones((len(x1_std), 1)), x1_std, x1_std_2, x1_std_3, x2_std, x2_std_2, x2_std_3, x3_std, x3_std_2, x3_std_3))
            w_std = 1 / (np.asarray(error_IMF_std) ** 2)
            wls_model = WLS(IMF_std, X, weights=w_std)
            results = wls_model.fit()
            a0 = results.params[0]
            a1 = results.params[1]
            a2 = results.params[2]
            a3 = results.params[3]
            a4 = results.params[4]
            a5 = results.params[5]
            a6 = results.params[6]
            a7 = results.params[7]
            a8 = results.params[8]
            a9 = results.params[9]
            x1 = np.linspace(min(np.asarray(x1_std)), max(np.asarray(x1_std)), 200)
            x2 = np.linspace(min(np.asarray(x2_std)), max(np.asarray(x2_std)), 200)
            x3 = np.linspace(min(np.asarray(x3_std)), max(np.asarray(x3_std)), 200)
            fit_std = a1 * x1 + a2 * x1 ** 2 + a3 * x1 ** 3  + a4 * x2 + a5 * x2 ** 2 + a6 * x2 ** 3 + a7 * x3 + a8 * x3 ** 2 + a9 * x3 ** 3 + a0
            wls_mod = results.predict()
            r_std = np.asarray(IMF_std) - np.asarray(wls_mod)
            if Auto_bias_iso_value == 1 and Unknown_data == 1:
                IMF_m = a1 * x1_unk + a2 * x1_unk ** 2 + a3 * x1_unk ** 3  + a4 * x2_unk + a5 * x2_unk ** 2 + a6 * x2_unk ** 3 + a7 * x3_unk + a8 * x3_unk ** 2 + a9 * x3_unk ** 3 + a0
            p_values_a0 = results.pvalues[0]
            p_values_a1 = results.pvalues[1]
            p_values_a2 = results.pvalues[2]
            p_values_a3 = results.pvalues[3] 
            p_values_a4 = results.pvalues[4] 
            p_values_a5 = results.pvalues[5]
            p_values_a6 = results.pvalues[6]
            p_values_a7 = results.pvalues[7] 
            p_values_a8 = results.pvalues[8] 
            p_values_a9 = results.pvalues[9]
            if p_values_a0 >= 0.05 or p_values_a1 >= 0.05 or p_values_a2 >= 0.05 or p_values_a3 >= 0.05 or p_values_a4 >= 0.05 or p_values_a5 >= 0.05 or p_values_a6 >= 0.05 or p_values_a7 >= 0.05 or p_values_a8 >= 0.05 or p_values_a9 >= 0.05:
                msg_pvalues.exec_()
            else:
                pass
        elif nb_variables_value == 3 and polynomial_order == 4:
            x1_std_2 = np.asarray(x1_std) ** 2
            x1_std_3 = np.asarray(x1_std) ** 3
            x1_std_4 = np.asarray(x1_std) ** 4
            x2_std_2 = np.asarray(x2_std) ** 2
            x2_std_3 = np.asarray(x2_std) ** 3
            x2_std_4 = np.asarray(x2_std) ** 4
            x3_std_2 = np.asarray(x3_std) ** 2
            x3_std_3 = np.asarray(x3_std) ** 3
            x3_std_4 = np.asarray(x3_std) ** 4
            X = np.column_stack((np.ones((len(x1_std), 1)), x1_std, x1_std_2, x1_std_3, x1_std_4, x2_std, x2_std_2, x2_std_3, x2_std_4, x3_std, x3_std_2, x3_std_3, x3_std_4))
            w_std = 1 / (np.asarray(error_IMF_std) ** 2)
            wls_model = WLS(IMF_std, X, weights=w_std)
            results = wls_model.fit()
            a0 = results.params[0]
            a1 = results.params[1]
            a2 = results.params[2]
            a3 = results.params[3]
            a4 = results.params[4]
            a5 = results.params[5]
            a6 = results.params[6]
            a7 = results.params[7]
            a8 = results.params[8]
            a9 = results.params[9]
            a10 = results.params[10]
            a11 = results.params[11]
            a12 = results.params[12]
            x1 = np.linspace(min(np.asarray(x1_std)), max(np.asarray(x1_std)), 200)
            x2 = np.linspace(min(np.asarray(x2_std)), max(np.asarray(x2_std)), 200)
            x3 = np.linspace(min(np.asarray(x3_std)), max(np.asarray(x3_std)), 200)
            fit_std = a1 * x1 + a2 * x1 ** 2 + a3 * x1 ** 3 + a4 * x1 ** 4 + a5 * x2 + a6 * x2 ** 2 + a7 * x2 ** 3 + a8 * x2 ** 4 + a9 * x3 + a10 * x3 ** 2 + a11 * x3 ** 3 + a12 * x3 ** 4 + a0
            wls_mod = results.predict()
            r_std = np.asarray(IMF_std) - np.asarray(wls_mod)
            if Auto_bias_iso_value == 1 and Unknown_data == 1:
                IMF_m = a1 * x1_unk + a2 * x1_unk ** 2 + a3 * x1_unk ** 3 + a4 * x1_unk ** 4 + a5 * x2_unk + a6 * x2_unk ** 2 + a7 * x2_unk ** 3 + a8 * x2_unk ** 4 + a9 * x3_unk + a10 * x3_unk ** 2 + a11 * x3_unk ** 3 + a12 * x3_unk ** 4 + a0
            p_values_a0 = results.pvalues[0]
            p_values_a1 = results.pvalues[1]
            p_values_a2 = results.pvalues[2]
            p_values_a3 = results.pvalues[3] 
            p_values_a4 = results.pvalues[4] 
            p_values_a5 = results.pvalues[5]
            p_values_a6 = results.pvalues[6]
            p_values_a7 = results.pvalues[7] 
            p_values_a8 = results.pvalues[8] 
            p_values_a9 = results.pvalues[9]
            p_values_a10 = results.pvalues[10]
            p_values_a11 = results.pvalues[11] 
            p_values_a12 = results.pvalues[12] 
            if p_values_a0 >= 0.05 or p_values_a1 >= 0.05 or p_values_a2 >= 0.05 or p_values_a3 >= 0.05 or p_values_a4 >= 0.05 or p_values_a5 >= 0.05 or p_values_a6 >= 0.05 or p_values_a7 >= 0.05 or p_values_a8 >= 0.05 or p_values_a9 >= 0.05 or p_values_a10 >= 0.05 or p_values_a11 >= 0.05 or p_values_a12 >= 0.05:
                msg_pvalues.exec_()
            else:
                pass
        if nb_variables_value == 1:
            self.confint()
        elif nb_variables_value >= 2:
            self.stats_data()
        

    def confint(self):
        global interval_u
        global interval_l
        global interval_u_fit
        global interval_l_fit
        global interval_u_r
        global interval_l_r
        global interval_u_fit_r
        global interval_l_fit_r
        global Summary
        global predicted
        global covB
        global predicted_fit_u
        global predicted_fit_l
        global sigma_fit_unk
        global fit_predicted
        global fit_predicted_u
        global fit_predicted_l
        global sigma_fit_u
        global sigma_fit_l
        Summary = results.summary()
        predicted = results.predict()
        covB = results.cov_params()
        predvar = results.mse_resid/ np.mean(np.asarray(w_std)) + (X * np.dot(covB, X.T).T).sum(1)
        predstd = np.sqrt(predvar)
        predvar_fit = (X * np.dot(covB, X.T).T).sum(1)
        predstd_fit = np.sqrt(predvar_fit)
        tppf = stats.t.isf(alpha/2., results.df_resid)
        interval_u = predicted + tppf * predstd
        interval_l = predicted - tppf * predstd
        interval_u_fit = tppf * predstd_fit
        interval_l_fit = - tppf * predstd_fit
        if polynomial_order == 1:
            x_std_2 = np.asarray(x_std)**2
            X_2 = np.column_stack((np.ones((len(x_std), 1)), x_std, x_std_2))
            fit_interval_u_fit = WLS(interval_u_fit, X_2)
            fit_interval_l_fit = WLS(interval_l_fit, X_2)
            results_fit_u = fit_interval_u_fit.fit()
            results_fit_l = fit_interval_l_fit.fit()
            predicted_fit_u = results_fit_u.predict()
            predicted_fit_l = results_fit_l.predict()
            a00 = results_fit_u.params[0]
            a11 = results_fit_u.params[1]
            a22 = results_fit_u.params[2]
            fit_predicted = a00 + a11 * x + a22 * x ** 2
            if Unknown_data == 1:
                sigma_fit_unk = a00 + a11 * np.asarray(x_unk) + a22 * np.asarray(x_unk) ** 2
            Summary_fit_u = results_fit_u.summary()
            Summary_fit_l = results_fit_l.summary()
            residuals_fit = interval_u_fit - results_fit_u.predict()
        elif polynomial_order == 2:
            x_std_2 = np.asarray(x_std)**2
            x_std_3 = np.asarray(x_std)**3
            x_std_4 = np.asarray(x_std)**4
            X_2 = np.column_stack((np.ones((len(x_std), 1)), x_std, x_std_2, x_std_3, x_std_4))
            fit_interval_u_fit = WLS(interval_u_fit, X_2)
            fit_interval_l_fit = WLS(interval_l_fit, X_2)
            results_fit_u = fit_interval_u_fit.fit()
            results_fit_l = fit_interval_l_fit.fit()
            predicted_fit_u = results_fit_u.predict()
            predicted_fit_l = results_fit_l.predict()
            a00 = results_fit_u.params[0]
            a11 = results_fit_u.params[1]
            a22 = results_fit_u.params[2]
            a33 = results_fit_u.params[3]
            a44 = results_fit_u.params[4]
            fit_predicted = a00 + a11 * x + a22 * x ** 2 + a33 * x ** 3 + a44 * x ** 4
            if Unknown_data == 1:
                sigma_fit_unk = a00 + a11 * np.asarray(x_unk) + a22 * np.asarray(x_unk) ** 2 + a33 * np.asarray(x_unk) ** 3 + a44 * np.asarray(x_unk) ** 4
            Summary_fit_u = results_fit_u.summary()
            Summary_fit_l = results_fit_l.summary()
            residuals_fit = interval_u_fit - results_fit_u.predict()
        elif polynomial_order == 3:
            x_std_2 = np.asarray(x_std)**2
            x_std_3 = np.asarray(x_std)**3
            x_std_4 = np.asarray(x_std)**4
            x_std_5 = np.asarray(x_std)**5
            x_std_6 = np.asarray(x_std)**6
            X_2 = np.column_stack((np.ones((len(x_std), 1)), x_std, x_std_2, x_std_3, x_std_4, x_std_5, x_std_6))
            fit_interval_u_fit = WLS(interval_u_fit, X_2)
            fit_interval_l_fit = WLS(interval_l_fit, X_2)
            results_fit_u = fit_interval_u_fit.fit()
            results_fit_l = fit_interval_l_fit.fit()
            predicted_fit_u = results_fit_u.predict()
            predicted_fit_l = results_fit_l.predict()
            a00 = results_fit_u.params[0]
            a11 = results_fit_u.params[1]
            a22 = results_fit_u.params[2]
            a33 = results_fit_u.params[3]
            a44 = results_fit_u.params[4]
            a55 = results_fit_u.params[5]
            a66 = results_fit_u.params[6]
            fit_predicted = a00 + a11 * x + a22 * x ** 2 + a33 * x ** 3 + a44 * x ** 4 + a55 * x ** 5 + a66 * x ** 6
            if Unknown_data == 1:
                sigma_fit_unk = a00 + a11 * np.asarray(x_unk) + a22 * np.asarray(x_unk) ** 2 + a33 * np.asarray(x_unk) ** 3 + a44 * np.asarray(x_unk) ** 4 + a55 * np.asarray(x_unk) ** 5 + a66 * np.asarray(x_unk) ** 6
            Summary_fit_u = results_fit_u.summary()
            Summary_fit_l = results_fit_l.summary()
            residuals_fit = interval_u_fit - results_fit_u.predict()
        elif polynomial_order == 4:
            x_std_2 = np.asarray(x_std)**2
            x_std_3 = np.asarray(x_std)**3
            x_std_4 = np.asarray(x_std)**4
            x_std_5 = np.asarray(x_std)**5
            x_std_6 = np.asarray(x_std)**6
            x_std_7 = np.asarray(x_std)**7
            x_std_8 = np.asarray(x_std)**8
            X_2 = np.column_stack((np.ones((len(x_std), 1)), x_std, x_std_2, x_std_3, x_std_4, x_std_5, x_std_6, x_std_7, x_std_8))
            fit_interval_u_fit = WLS(interval_u_fit, X_2)
            fit_interval_l_fit = WLS(interval_l_fit, X_2)
            results_fit_u = fit_interval_u_fit.fit()
            results_fit_l = fit_interval_l_fit.fit()
            predicted_fit_u = results_fit_u.predict()
            predicted_fit_l = results_fit_l.predict()
            a00 = results_fit_u.params[0]
            a11 = results_fit_u.params[1]
            a22 = results_fit_u.params[2]
            a33 = results_fit_u.params[3]
            a44 = results_fit_u.params[4]
            a55 = results_fit_u.params[5]
            a66 = results_fit_u.params[6]
            a77 = results_fit_u.params[7]
            a88 = results_fit_u.params[8]
            fit_predicted = a00 + a11 * x + a22 * x ** 2 + a33 * x ** 3 + a44 * x ** 4 + a55 * x ** 5 + a66 * x ** 6 + a77 * x ** 7 + a88 * x ** 8
            if Unknown_data == 1:
                sigma_fit_unk = a00 + a11 * np.asarray(x_unk) + a22 * np.asarray(x_unk) ** 2 + a33 * np.asarray(x_unk) ** 3 + a44 * np.asarray(x_unk) ** 4 + a55 * np.asarray(x_unk) ** 5 + a66 * np.asarray(x_unk) ** 6 + a77 * np.asarray(x_unk) ** 7 + a88 * np.asarray(x_unk) ** 8
            Summary_fit_u = results_fit_u.summary()
            Summary_fit_l = results_fit_l.summary()
            residuals_fit = interval_u_fit - results_fit_u.predict()
        fit_predicted_u = fit_std + fit_predicted
        fit_predicted_l = fit_std - fit_predicted
        sigma_fit_u = fit_predicted 
        sigma_fit_l = - fit_predicted
        if Unknown_data == 1:
            global Unknown_section
            Unknown_section = Unknown_section.assign(error_fit=sigma_fit_unk)
            Unknown_section.rename(columns={'error_fit' : '95% c.i. fit (‰)'})
        self.stats_data()


    def stats_data(self):
        global MSWD
        global df_std
        global sd_std_SIMS
        global se_std_SIMS
        global str_sd_std_SIMS
        global str_se_std_SIMS
        global str_Summary
        global str_MSWD
        df_std = len(IMF_std) - (1 + polynomial_order * nb_variables_value)
        sd_std_SIMS = 2 * np.std(np.asarray(r_std), ddof=1)
        str_sd_std_SIMS = "%.2f" %(sd_std_SIMS)
        se_std_SIMS = np.asarray(sd_std_SIMS)/(np.sqrt(len(IMF_std)))
        str_se_std_SIMS = "%.2f" %(se_std_SIMS)
        chi2_std = (np.asarray(r_std) / np.asarray(error_IMF_std)) ** 2
        MSWD = sum(chi2_std) / df_std
        str_MSWD = "%.2f" %(MSWD)
        str_Summary = str(Summary)
        self.label_stats.setText('Statistics:\n\n2s = ' + str_sd_std_SIMS + ' permil\n2se = ' + str_se_std_SIMS + ' permil\n\nMSWD = ' + str_MSWD)
        if Auto_bias_iso_value == 1 and Unknown_data == 1:
            global Unknown_section
            delta_ref = (((np.asarray(Unknown_section[target_name])/1000) + 1)/(np.exp(np.asarray((IMF_m/1000)))) - 1) * 1000
            error_ref = 1000 * np.sqrt((np.asarray(Unknown_section[target_error_name])/1000) ** 2 + (np.asarray(sigma_fit_unk)/1000) ** 2)
            Unknown_section = Unknown_section.assign(delta_ref=delta_ref)
            Unknown_section = Unknown_section.assign(error_ref=error_ref)
            Unknown_section = Unknown_section.assign(error_fit=sigma_fit_unk)
            Unknown_section.rename(columns={'delta_ref' : 'delat ref (‰)', 'error_ref' : '2se ref (‰)'})


    def plot_data(self):
        if name:
            self.variables_def()
            if nb_variables_value == 1 and polynomial_order >= 1:
                self.dpi = 100
                self.fig = plt.Figure((12.0, 9.0), dpi=self.dpi)
                self.canvas = FigureCanvas(self.fig)
                self.canvas.setParent(self.main_frame)
                gs = GridSpec(3, 3)
                ax1 = self.fig.add_subplot(gs[:-1, :])
                ax1.errorbar(x_std,IMF_std, yerr=error_IMF_std, fmt='ko', ecolor='k', capthick=2)
                ax1.plot(x, fit_std, 'k--', linewidth=1)
                ax1.plot(x, fit_predicted_u, 'k-.', linewidth=1)
                ax1.plot(x, fit_predicted_l, 'k-.', linewidth=1)
                ax1.set_ylabel(target_name, fontsize=15)
                ax2 = self.fig.add_subplot(gs[-1, :], sharex=ax1)
                ax2.errorbar(x_std,r_std, yerr=error_IMF_std, fmt='ko', ecolor='k', capthick=2)
                ax2.plot(x, np.zeros((len(x), 1)), 'k--', linewidth=2)
                ax2.plot(x, sigma_fit_u, 'k:', linewidth=0.3)
                ax2.plot(x, sigma_fit_l, 'k:', linewidth=0.3)
                ax2.set_xlabel(var1_name, fontsize=15)
                ax2.set_ylabel(u"$Residuals$ (‰)")
                self.fig.subplots_adjust(0.06, 0.1, 0.97, 0.95)
            elif nb_variables_value == 2 and polynomial_order >= 1:
                self.dpi = 100
                self.fig = plt.Figure((12.0, 9.0), dpi=self.dpi)
                self.canvas = FigureCanvas(self.fig)
                self.canvas.setParent(self.main_frame)
                gs = GridSpec(3, 3)
                ax1 = self.fig.add_subplot(111, projection='3d')
                ax1.scatter(x1_std,x2_std, IMF_std)
                # ax1.errorbar([x1_std,x2_std], IMF_std, yerr=error_IMF_std, fmt='ko', ecolor='k', capthick=2)
                ax1.plot_trisurf(x1_std, x2_std, wls_mod)
                # ax1.plot(x, fit_std2, 'k--', linewidth=1)
                # ax1.plot(x1_std, interval_u_std1, 'k-.', linewidth=1)
                # ax1.plot(x1_std, interval_l_std1, 'k-.', linewidth=1)
                # ax1.plot(x2_std, interval_u_std2, 'k-.', linewidth=1)
                # ax1.plot(x2_std, interval_l_std2, 'k-.', linewidth=1)
                ax1.set_xlabel(var1_name, fontsize=15)
                ax1.set_ylabel(var2_name, fontsize=15)
                ax1.set_zlabel(target_name, fontsize=15)
                # ax2 = self.fig.add_subplot(gs[-1, :], sharex=ax1)
                # ax2.errorbar(x1_std,r_std, yerr=error_IMF_std, fmt='ko', ecolor='k', capthick=2)
                # # ax2.plot(x, np.zeros((len(x), 1)), 'k--', linewidth=2)
                # ax2.set_xlabel(var1_name, fontsize=15)
                # ax2.set_ylabel(u"$Residuals$ (‰)")
                self.fig.subplots_adjust(0.06, 0.1, 0.97, 0.95)
            elif nb_variables_value == 3 and polynomial_order >= 1:
                self.dpi = 100
                self.fig = plt.Figure((12.0, 9.0), dpi=self.dpi)
                self.canvas = FigureCanvas(self.fig)
                self.canvas.setParent(self.main_frame)
                gs = GridSpec(3, 3)
                ax1 = self.fig.add_subplot(gs[:-1, :])
                ax1.errorbar(x1_std,IMF_std1, yerr=error_IMF_std1, fmt='ko', ecolor='k', capthick=2)
                ax1.errorbar(x2_std,IMF_std2, yerr=error_IMF_std2, fmt='kd', ecolor='k', capthick=2)
                ax1.errorbar(x3_std,IMF_std3, yerr=error_IMF_std3, fmt='ks', ecolor='k', capthick=2)
                ax1.plot(x, fit_std1, 'k--', linewidth=1)
                ax1.plot(x, fit_std2, 'k--', linewidth=1)
                ax1.plot(x, fit_std3, 'k--', linewidth=1)
                ax1.plot(x1_std, interval_u_std1, 'k-.', linewidth=1)
                ax1.plot(x1_std, interval_l_std1, 'k-.', linewidth=1)
                ax1.plot(x2_std, interval_u_std2, 'k-.', linewidth=1)
                ax1.plot(x2_std, interval_l_std2, 'k-.', linewidth=1)
                ax1.plot(x3_std, interval_u_std3, 'k-.', linewidth=1)
                ax1.plot(x3_std, interval_l_std3, 'k-.', linewidth=1)
                ax1.set_ylabel(target_name, fontsize=15)
                ax2 = self.fig.add_subplot(gs[-1, :], sharex=ax1)
                ax2.errorbar(x1_std,r_std1, yerr=error_IMF_std1, fmt='ko', ecolor='k', capthick=2)
                ax2.errorbar(x2_std,r_std2, yerr=error_IMF_std2, fmt='kd', ecolor='k', capthick=2)
                ax2.errorbar(x3_std,r_std3, yerr=error_IMF_std3, fmt='ks', ecolor='k', capthick=2)
                Time_tot_std = np.vstack((np.asarray(x1_std).reshape(len(x1_std),1), np.asarray(x2_std).reshape(len(x2_std),1), np.asarray(x3_std).reshape(len(x3_std),1)))
                ax2.plot(x, np.zeros((len(x), 1)), 'k--', linewidth=2)
                ax2.set_xlabel('Time (h)')
                ax2.set_ylabel(u"$Residuals$ (‰)")
                self.fig.subplots_adjust(0.06, 0.1, 0.97, 0.95)
            self.canvas.show()
 



    def enable_error_X(self, state):
        global Error_x_value
        Error_x_value = None
        if state == Qt.Checked:
            Error_x_value = 1
            if nb_variables_value == 1:
                self.lineEdit_error_variable_1.setEnabled(True)
                self.label_error_variable_1.setEnabled(True)
            elif nb_variables_value == 2:
                self.lineEdit_error_variable_1.setEnabled(True)
                self.label_error_variable_1.setEnabled(True)
                self.lineEdit_error_variable_2.setEnabled(True)
                self.label_error_variable_2.setEnabled(True)
            elif nb_variables_value == 3:
                self.lineEdit_error_variable_1.setEnabled(True)
                self.label_error_variable_1.setEnabled(True)
                self.lineEdit_error_variable_2.setEnabled(True)
                self.label_error_variable_2.setEnabled(True)
                self.lineEdit_error_variable_3.setEnabled(True)
                self.label_error_variable_3.setEnabled(True)
        else:
            Error_x_value = 0
            if nb_variables_value == 1:
                self.lineEdit_error_variable_1.setEnabled(False)
                self.label_error_variable_1.setEnabled(False)
            elif nb_variables_value == 2:
                self.lineEdit_error_variable_1.setEnabled(False)
                self.label_error_variable_1.setEnabled(False)
                self.lineEdit_error_variable_2.setEnabled(False)
                self.label_error_variable_2.setEnabled(False)
            elif nb_variables_value == 3:
                self.lineEdit_error_variable_1.setEnabled(False)
                self.label_error_variable_1.setEnabled(False)
                self.lineEdit_error_variable_2.setEnabled(False)
                self.label_error_variable_2.setEnabled(False)
                self.lineEdit_error_variable_3.setEnabled(False)
                self.label_error_variable_3.setEnabled(False)

    def nb_variables(self, index_nb_variables):
        global nb_variables_value
        nb_variables_value = None
        if self.comboBox_nb_variables.itemText(index_nb_variables) == '1 variable':
            nb_variables_value = 1
            self.lineEdit_inde_variable_2.setEnabled(False)
            self.lineEdit_error_variable_2.setEnabled(False)
            self.lineEdit_inde_variable_3.setEnabled(False)
            self.lineEdit_error_variable_3.setEnabled(False)
            self.label_inde_variable_2.setEnabled(False)
            self.label_error_variable_2.setEnabled(False)
            self.label_inde_variable_3.setEnabled(False)
            self.label_error_variable_3.setEnabled(False)
        elif self.comboBox_nb_variables.itemText(index_nb_variables) == '2 variables':
            nb_variables_value = 2
            self.lineEdit_inde_variable_2.setEnabled(True)
            if Error_x_value == 1:
                self.lineEdit_error_variable_2.setEnabled(True)
            else:
                self.lineEdit_error_variable_2.setEnabled(False)
            self.lineEdit_inde_variable_3.setEnabled(False)
            self.lineEdit_error_variable_3.setEnabled(False)
            self.label_inde_variable_2.setEnabled(True)
            if Error_x_value == 1:
                self.label_error_variable_2.setEnabled(True)
            else:
                self.label_error_variable_2.setEnabled(False)
            self.label_inde_variable_3.setEnabled(False)
            self.label_error_variable_3.setEnabled(False)
        elif self.comboBox_nb_variables.itemText(index_nb_variables) == '3 variables':
            nb_variables_value = 3
            self.lineEdit_inde_variable_2.setEnabled(True)
            if Error_x_value == 1:
                self.lineEdit_error_variable_2.setEnabled(True)
            else:
                self.lineEdit_error_variable_2.setEnabled(False)
            self.lineEdit_inde_variable_3.setEnabled(True)
            if Error_x_value == 1:
                self.lineEdit_error_variable_3.setEnabled(True)
            else:
                self.lineEdit_error_variable_3.setEnabled(False)
            self.label_inde_variable_2.setEnabled(True)
            if Error_x_value == 1:
                self.label_error_variable_2.setEnabled(True)
            else:
                self.label_error_variable_2.setEnabled(False)
            self.label_inde_variable_3.setEnabled(True)
            if Error_x_value == 1:
                self.label_error_variable_3.setEnabled(True)
            else:
                self.label_error_variable_3.setEnabled(False)

    def fit_order(self, fit_index_iso):
        global polynomial_order
        polynomial_order = None
        if self.comboBox_fit_order.itemText(fit_index_iso) == 'Linear':
            polynomial_order = 1
        elif self.comboBox_fit_order.itemText(fit_index_iso) == '2nd order polynomial':
            polynomial_order = 2
        elif self.comboBox_fit_order.itemText(fit_index_iso) == '3rd order polynomial':
            polynomial_order = 3
        elif self.comboBox_fit_order.itemText(fit_index_iso) == '4th order polynomial':
            polynomial_order = 4
        elif self.comboBox_fit_order.itemText(fit_index_iso) == '5th order polynomial':
            polynomial_order = 5
        elif self.comboBox_fit_order.itemText(fit_index_iso) == '6th order polynomial':
            polynomial_order = 6
        elif self.comboBox_fit_order.itemText(fit_index_iso) == '7th order polynomial':
            polynomial_order = 7

    def enable_ref_value_iso(self, state):
        global Auto_bias_iso_value
        Auto_bias_iso_value = None
        if state == Qt.Checked:
            Auto_bias_iso_value = 1
        else:
            Auto_bias_iso_value = 0

    def figure_standards_show(self):
        self.Fig_Standards_iso = Figure_std_Window()
        self.Fig_Standards_iso.show()


    def figure_residuals_show(self):
        self.Fig_Residuals = Figure_residuals_Window()
        self.Fig_Residuals.show()


    def Input_data(self):
        self.Data_selection = Data_selection_Window()
        self.Data_selection.show()


    def figure_Statistics(self):
        self.Fig_Stats = Figure_Stats_Window()
        self.Fig_Stats.show()


    def Window_Statistics_fit(self):
        self.Stats_show = Stats_Window_show()
        self.Stats_show.show()

    def output_standard_data(self):
        name_output_standards = QFileDialog.getSaveFileName(self, 'Save File')
        name_save_output_standards = name_output_standards[0] + '.csv'

        if B_Mat_mod == 0:
            if Section_value == 0:
                global B
                B = B.assign(residuals=r_std)
                B = B.assign(error_fit=interval_u_fit)
                B.rename(columns={'error_fit' : '95% c.i. (‰)', 'residuals' : 'Residuals (‰)'})
                B.to_csv(name_save_output_standards, index=False)
            else:
                global B_section
                B_section = B_section.assign(residuals=r_std)
                B_section = B_section.assign(error_fit=interval_u_fit)
                B_section.rename(columns={'error_fit' : '95% c.i. (‰)', 'residuals' : 'Residuals (‰)'})
                B_section.to_csv(name_save_output_standards, index=False)
        else:
            if Section_value == 0:
                global B_mod
                B_mod = B_mod.assign(residuals=r_std)
                B_mod = B_mod.assign(error_fit=interval_u_fit)
                B_mod.rename(columns={'error_fit' : '95% c.i. (‰)', 'residuals' : 'Residuals (‰)'})
                B_mod.to_csv(name_save_output_standards, index=False)
            else:
                B_section = B_section.assign(residuals=r_std)
                B_section = B_section.assign(error_fit=interval_u_fit)
                B_section.rename(columns={'error_fit' : '95% c.i. (‰)', 'residuals' : 'Residuals (‰)'})
                B_section.to_csv(name_save_output_standards, index=False)


    def output_sample_data(self):
        name_output_sample = QFileDialog.getSaveFileName(self, 'Save File')
        name_save_output_sample = name_output_sample[0] + '.csv'
        Unknown_section.to_csv(name_save_output_sample, index=False)


    def input(self):
        name_input_matrix = QFileDialog.getSaveFileName(self, 'Save File')
        name_save_input_matrix = name_input_matrix[0] + '.csv'
        B.to_csv(name_save_input_matrix,index=False)



def main():
    app = QApplication(sys.argv)
    form = Matrix_SIMS_App()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
    