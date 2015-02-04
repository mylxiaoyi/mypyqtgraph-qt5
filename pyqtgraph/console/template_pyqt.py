# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'template.ui'
#
# Created: Fri May 02 18:55:28 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(694, 497)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.output = QtWidgets.QPlainTextEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Monospace"))
        self.output.setFont(font)
        self.output.setReadOnly(True)
        self.output.setObjectName(_fromUtf8("output"))
        self.verticalLayout.addWidget(self.output)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.input = CmdInput(self.layoutWidget)
        self.input.setObjectName(_fromUtf8("input"))
        self.horizontalLayout.addWidget(self.input)
        self.historyBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.historyBtn.setCheckable(True)
        self.historyBtn.setObjectName(_fromUtf8("historyBtn"))
        self.horizontalLayout.addWidget(self.historyBtn)
        self.exceptionBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.exceptionBtn.setCheckable(True)
        self.exceptionBtn.setObjectName(_fromUtf8("exceptionBtn"))
        self.horizontalLayout.addWidget(self.exceptionBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.historyList = QtWidgets.QListWidget(self.splitter)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Monospace"))
        self.historyList.setFont(font)
        self.historyList.setObjectName(_fromUtf8("historyList"))
        self.exceptionGroup = QtWidgets.QGroupBox(self.splitter)
        self.exceptionGroup.setObjectName(_fromUtf8("exceptionGroup"))
        self.gridLayout_2 = QtWidgets.QGridLayout(self.exceptionGroup)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.clearExceptionBtn = QtWidgets.QPushButton(self.exceptionGroup)
        self.clearExceptionBtn.setEnabled(False)
        self.clearExceptionBtn.setObjectName(_fromUtf8("clearExceptionBtn"))
        self.gridLayout_2.addWidget(self.clearExceptionBtn, 0, 6, 1, 1)
        self.catchAllExceptionsBtn = QtWidgets.QPushButton(self.exceptionGroup)
        self.catchAllExceptionsBtn.setCheckable(True)
        self.catchAllExceptionsBtn.setObjectName(_fromUtf8("catchAllExceptionsBtn"))
        self.gridLayout_2.addWidget(self.catchAllExceptionsBtn, 0, 1, 1, 1)
        self.catchNextExceptionBtn = QtWidgets.QPushButton(self.exceptionGroup)
        self.catchNextExceptionBtn.setCheckable(True)
        self.catchNextExceptionBtn.setObjectName(_fromUtf8("catchNextExceptionBtn"))
        self.gridLayout_2.addWidget(self.catchNextExceptionBtn, 0, 0, 1, 1)
        self.onlyUncaughtCheck = QtWidgets.QCheckBox(self.exceptionGroup)
        self.onlyUncaughtCheck.setChecked(True)
        self.onlyUncaughtCheck.setObjectName(_fromUtf8("onlyUncaughtCheck"))
        self.gridLayout_2.addWidget(self.onlyUncaughtCheck, 0, 4, 1, 1)
        self.exceptionStackList = QtWidgets.QListWidget(self.exceptionGroup)
        self.exceptionStackList.setAlternatingRowColors(True)
        self.exceptionStackList.setObjectName(_fromUtf8("exceptionStackList"))
        self.gridLayout_2.addWidget(self.exceptionStackList, 2, 0, 1, 7)
        self.runSelectedFrameCheck = QtWidgets.QCheckBox(self.exceptionGroup)
        self.runSelectedFrameCheck.setChecked(True)
        self.runSelectedFrameCheck.setObjectName(_fromUtf8("runSelectedFrameCheck"))
        self.gridLayout_2.addWidget(self.runSelectedFrameCheck, 3, 0, 1, 7)
        self.exceptionInfoLabel = QtWidgets.QLabel(self.exceptionGroup)
        self.exceptionInfoLabel.setObjectName(_fromUtf8("exceptionInfoLabel"))
        self.gridLayout_2.addWidget(self.exceptionInfoLabel, 1, 0, 1, 7)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 5, 1, 1)
        self.label = QtWidgets.QLabel(self.exceptionGroup)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 2, 1, 1)
        self.filterText = QtWidgets.QLineEdit(self.exceptionGroup)
        self.filterText.setObjectName(_fromUtf8("filterText"))
        self.gridLayout_2.addWidget(self.filterText, 0, 3, 1, 1)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Console", None))
        self.historyBtn.setText(_translate("Form", "History..", None))
        self.exceptionBtn.setText(_translate("Form", "Exceptions..", None))
        self.exceptionGroup.setTitle(_translate("Form", "Exception Handling", None))
        self.clearExceptionBtn.setText(_translate("Form", "Clear Exception", None))
        self.catchAllExceptionsBtn.setText(_translate("Form", "Show All Exceptions", None))
        self.catchNextExceptionBtn.setText(_translate("Form", "Show Next Exception", None))
        self.onlyUncaughtCheck.setText(_translate("Form", "Only Uncaught Exceptions", None))
        self.runSelectedFrameCheck.setText(_translate("Form", "Run commands in selected stack frame", None))
        self.exceptionInfoLabel.setText(_translate("Form", "Exception Info", None))
        self.label.setText(_translate("Form", "Filter (regex):", None))

from .CmdInput import CmdInput
