# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_qadastre.ui'
#
# Created: Fri Jul  5 15:18:44 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Qadastre(object):
    def setupUi(self, Qadastre):
        Qadastre.setObjectName(_fromUtf8("Qadastre"))
        Qadastre.resize(756, 593)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Qadastre)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.splitter = QtGui.QSplitter(Qadastre)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.frame = QtGui.QFrame(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(self.frame)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox = QtGui.QComboBox(self.groupBox)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.comboBox_2 = QtGui.QComboBox(self.groupBox)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.gridLayout.addWidget(self.comboBox_2, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.comboBox_3 = QtGui.QComboBox(self.groupBox)
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.gridLayout.addWidget(self.comboBox_3, 2, 1, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout)
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_6.addWidget(self.label_10)
        self.verticalLayout.addWidget(self.groupBox)
        self.lwMenu = QtGui.QListWidget(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lwMenu.sizePolicy().hasHeightForWidth())
        self.lwMenu.setSizePolicy(sizePolicy)
        self.lwMenu.setMinimumSize(QtCore.QSize(58, 0))
        self.lwMenu.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lwMenu.setObjectName(_fromUtf8("lwMenu"))
        item = QtGui.QListWidgetItem()
        self.lwMenu.addItem(item)
        item = QtGui.QListWidgetItem()
        self.lwMenu.addItem(item)
        item = QtGui.QListWidgetItem()
        self.lwMenu.addItem(item)
        self.verticalLayout.addWidget(self.lwMenu)
        self.frame_2 = QtGui.QFrame(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.swOptions = QtGui.QStackedWidget(self.frame_2)
        self.swOptions.setObjectName(_fromUtf8("swOptions"))
        self.swPageImport = QtGui.QWidget()
        self.swPageImport.setObjectName(_fromUtf8("swPageImport"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.swPageImport)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.scrollArea = QtGui.QScrollArea(self.swPageImport)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 416, 502))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.groupBox_2 = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.btEdigeoSourceDir = QtGui.QPushButton(self.groupBox_2)
        self.btEdigeoSourceDir.setMaximumSize(QtCore.QSize(30, 16777215))
        self.btEdigeoSourceDir.setObjectName(_fromUtf8("btEdigeoSourceDir"))
        self.horizontalLayout_2.addWidget(self.btEdigeoSourceDir)
        self.verticalLayout_11.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_4.addWidget(self.label_6)
        self.lineEdit_4 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.horizontalLayout_4.addWidget(self.lineEdit_4)
        self.btEdigeoSourceProj = QtGui.QPushButton(self.groupBox_2)
        self.btEdigeoSourceProj.setMaximumSize(QtCore.QSize(30, 16777215))
        self.btEdigeoSourceProj.setObjectName(_fromUtf8("btEdigeoSourceProj"))
        self.horizontalLayout_4.addWidget(self.btEdigeoSourceProj)
        self.verticalLayout_11.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_7 = QtGui.QLabel(self.groupBox_2)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_5.addWidget(self.label_7)
        self.lineEdit_5 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.horizontalLayout_5.addWidget(self.lineEdit_5)
        self.btEdigeoTargetProj = QtGui.QPushButton(self.groupBox_2)
        self.btEdigeoTargetProj.setMaximumSize(QtCore.QSize(30, 16777215))
        self.btEdigeoTargetProj.setObjectName(_fromUtf8("btEdigeoTargetProj"))
        self.horizontalLayout_5.addWidget(self.btEdigeoTargetProj)
        self.verticalLayout_11.addLayout(self.horizontalLayout_5)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        self.groupBox_4 = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_5 = QtGui.QLabel(self.groupBox_4)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_3.addWidget(self.label_5)
        self.lineEdit_3 = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        self.btMajicSourceDir = QtGui.QPushButton(self.groupBox_4)
        self.btMajicSourceDir.setMaximumSize(QtCore.QSize(30, 16777215))
        self.btMajicSourceDir.setObjectName(_fromUtf8("btMajicSourceDir"))
        self.horizontalLayout_3.addWidget(self.btMajicSourceDir)
        self.verticalLayout_12.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_8 = QtGui.QLabel(self.groupBox_4)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_6.addWidget(self.label_8)
        self.comboBox_4 = QtGui.QComboBox(self.groupBox_4)
        self.comboBox_4.setMaximumSize(QtCore.QSize(80, 16777215))
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.horizontalLayout_6.addWidget(self.comboBox_4)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout_12.addLayout(self.horizontalLayout_6)
        self.verticalLayout_5.addWidget(self.groupBox_4)
        self.groupBox_3 = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.checkBox = QtGui.QCheckBox(self.groupBox_3)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.horizontalLayout.addWidget(self.checkBox)
        self.lineEdit = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout_10.addLayout(self.horizontalLayout)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_9 = QtGui.QLabel(self.groupBox_3)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_7.addWidget(self.label_9)
        self.lineEdit_6 = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.horizontalLayout_7.addWidget(self.lineEdit_6)
        self.verticalLayout_10.addLayout(self.horizontalLayout_7)
        self.verticalLayout_5.addWidget(self.groupBox_3)
        self.btImportRun = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.btImportRun.setObjectName(_fromUtf8("btImportRun"))
        self.verticalLayout_5.addWidget(self.btImportRun)
        self.txtImportLog = QtGui.QTextEdit(self.scrollAreaWidgetContents)
        self.txtImportLog.setObjectName(_fromUtf8("txtImportLog"))
        self.verticalLayout_5.addWidget(self.txtImportLog)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_4.addWidget(self.scrollArea)
        self.swOptions.addWidget(self.swPageImport)
        self.swPageConsult = QtGui.QWidget()
        self.swPageConsult.setObjectName(_fromUtf8("swPageConsult"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.swPageConsult)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.scrollArea_3 = QtGui.QScrollArea(self.swPageConsult)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName(_fromUtf8("scrollArea_3"))
        self.scrollAreaWidgetContents_3 = QtGui.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 416, 502))
        self.scrollAreaWidgetContents_3.setObjectName(_fromUtf8("scrollAreaWidgetContents_3"))
        self.verticalLayout_13 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.groupBox_5 = QtGui.QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.verticalLayout_14 = QtGui.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_14.setObjectName(_fromUtf8("verticalLayout_14"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_12 = QtGui.QLabel(self.groupBox_5)
        self.label_12.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_8.addWidget(self.label_12)
        self.comboBox_5 = QtGui.QComboBox(self.groupBox_5)
        self.comboBox_5.setObjectName(_fromUtf8("comboBox_5"))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.horizontalLayout_8.addWidget(self.comboBox_5)
        self.pushButton = QtGui.QPushButton(self.groupBox_5)
        self.pushButton.setMaximumSize(QtCore.QSize(80, 16777215))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_8.addWidget(self.pushButton)
        self.verticalLayout_14.addLayout(self.horizontalLayout_8)
        self.verticalLayout_13.addWidget(self.groupBox_5)
        self.groupBox_6 = QtGui.QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.verticalLayout_15 = QtGui.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_15.setObjectName(_fromUtf8("verticalLayout_15"))
        self.label_11 = QtGui.QLabel(self.groupBox_6)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayout_15.addWidget(self.label_11)
        self.comboBox_6 = QtGui.QComboBox(self.groupBox_6)
        self.comboBox_6.setObjectName(_fromUtf8("comboBox_6"))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.verticalLayout_15.addWidget(self.comboBox_6)
        self.verticalLayout_13.addWidget(self.groupBox_6)
        self.btLoadingDataRun = QtGui.QPushButton(self.scrollAreaWidgetContents_3)
        self.btLoadingDataRun.setObjectName(_fromUtf8("btLoadingDataRun"))
        self.verticalLayout_13.addWidget(self.btLoadingDataRun)
        self.txtLoadingDataLog = QtGui.QTextEdit(self.scrollAreaWidgetContents_3)
        self.txtLoadingDataLog.setObjectName(_fromUtf8("txtLoadingDataLog"))
        self.verticalLayout_13.addWidget(self.txtLoadingDataLog)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem2)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_7.addWidget(self.scrollArea_3)
        self.swOptions.addWidget(self.swPageConsult)
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.page)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.groupBox_7 = QtGui.QGroupBox(self.page)
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.label_13 = QtGui.QLabel(self.groupBox_7)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.verticalLayout_9.addWidget(self.label_13)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.btInterfaceQadastre = QtGui.QPushButton(self.groupBox_7)
        self.btInterfaceQadastre.setObjectName(_fromUtf8("btInterfaceQadastre"))
        self.horizontalLayout_9.addWidget(self.btInterfaceQadastre)
        self.btInterfaceQgis = QtGui.QPushButton(self.groupBox_7)
        self.btInterfaceQgis.setObjectName(_fromUtf8("btInterfaceQgis"))
        self.horizontalLayout_9.addWidget(self.btInterfaceQgis)
        self.verticalLayout_9.addLayout(self.horizontalLayout_9)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem3)
        self.verticalLayout_8.addWidget(self.groupBox_7)
        self.swOptions.addWidget(self.page)
        self.verticalLayout_3.addWidget(self.swOptions)
        self.verticalLayout_2.addWidget(self.splitter)
        self.buttonBox = QtGui.QDialogButtonBox(Qadastre)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Help)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(Qadastre)
        self.swOptions.setCurrentIndex(0)
        QtCore.QObject.connect(self.lwMenu, QtCore.SIGNAL(_fromUtf8("currentRowChanged(int)")), self.swOptions.setCurrentIndex)
        QtCore.QMetaObject.connectSlotsByName(Qadastre)

    def retranslateUi(self, Qadastre):
        Qadastre.setWindowTitle(QtGui.QApplication.translate("Qadastre", "Qadastre", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Qadastre", "Base de données de travail", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Qadastre", "Type de base", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("Qadastre", "pgsql", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("Qadastre", "sqlite", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Qadastre", "Connexions", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Qadastre", "Schéma", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Qadastre", "Connecté à", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.lwMenu.isSortingEnabled()
        self.lwMenu.setSortingEnabled(False)
        item = self.lwMenu.item(0)
        item.setText(QtGui.QApplication.translate("Qadastre", "Importer", None, QtGui.QApplication.UnicodeUTF8))
        item = self.lwMenu.item(1)
        item.setText(QtGui.QApplication.translate("Qadastre", "Charger", None, QtGui.QApplication.UnicodeUTF8))
        item = self.lwMenu.item(2)
        item.setText(QtGui.QApplication.translate("Qadastre", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.lwMenu.setSortingEnabled(__sortingEnabled)
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Qadastre", "Fichiers EDIGEO", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Qadastre", "Répertoire", None, QtGui.QApplication.UnicodeUTF8))
        self.btEdigeoSourceDir.setText(QtGui.QApplication.translate("Qadastre", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Qadastre", "Projection source", None, QtGui.QApplication.UnicodeUTF8))
        self.btEdigeoSourceProj.setText(QtGui.QApplication.translate("Qadastre", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Qadastre", "Projection cible", None, QtGui.QApplication.UnicodeUTF8))
        self.btEdigeoTargetProj.setText(QtGui.QApplication.translate("Qadastre", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("Qadastre", "Fichiers MAJIC", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Qadastre", "Répertoire", None, QtGui.QApplication.UnicodeUTF8))
        self.btMajicSourceDir.setText(QtGui.QApplication.translate("Qadastre", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Qadastre", "Format MAJIC", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_4.setItemText(0, QtGui.QApplication.translate("Qadastre", "2012", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_4.setItemText(1, QtGui.QApplication.translate("Qadastre", "2011", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("Qadastre", "Destination", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("Qadastre", "nouveau schéma", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Qadastre", "Année", None, QtGui.QApplication.UnicodeUTF8))
        self.btImportRun.setText(QtGui.QApplication.translate("Qadastre", "Lancer l\'import", None, QtGui.QApplication.UnicodeUTF8))
        self.txtImportLog.setHtml(QtGui.QApplication.translate("Qadastre", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Log</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setTitle(QtGui.QApplication.translate("Qadastre", "Styles à appliquer", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("Qadastre", "Thème", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_5.setItemText(0, QtGui.QApplication.translate("Qadastre", "Défaut", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Qadastre", "Importer", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_6.setTitle(QtGui.QApplication.translate("Qadastre", "Surcharge", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("Qadastre", "Comportement lors du chargement\n"
"si des données sont déjà ouvertes dans le projet", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_6.setItemText(0, QtGui.QApplication.translate("Qadastre", "Conserver les couches actuelles", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_6.setItemText(1, QtGui.QApplication.translate("Qadastre", "Remplacer par les données de la table", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_6.setItemText(2, QtGui.QApplication.translate("Qadastre", "Annuler tout le chargement", None, QtGui.QApplication.UnicodeUTF8))
        self.btLoadingDataRun.setText(QtGui.QApplication.translate("Qadastre", "Charger les données dans QGIS", None, QtGui.QApplication.UnicodeUTF8))
        self.txtLoadingDataLog.setHtml(QtGui.QApplication.translate("Qadastre", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Log</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_7.setTitle(QtGui.QApplication.translate("Qadastre", "Interface QGIS", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("Qadastre", "Vous pouvez choisir d\'appliquer une interface\n"
"simplifiée de QGIS pour consulter le cadastre\n"
"ou de revenir à l\'interface par défaut", None, QtGui.QApplication.UnicodeUTF8))
        self.btInterfaceQadastre.setText(QtGui.QApplication.translate("Qadastre", "Interface Qadastre", None, QtGui.QApplication.UnicodeUTF8))
        self.btInterfaceQgis.setText(QtGui.QApplication.translate("Qadastre", "Interface QGIS", None, QtGui.QApplication.UnicodeUTF8))

