# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './exampleLoaderTemplate.ui'
#
# Created: Mon Feb 25 09:02:09 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(623, 380)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0,0,0,0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.exampleTree = QtWidgets.QTreeWidget(self.widget)
        self.exampleTree.setObjectName(_fromUtf8("exampleTree"))
        self.exampleTree.headerItem().setText(0, _fromUtf8("1"))
        self.exampleTree.header().setVisible(False)
        self.verticalLayout.addWidget(self.exampleTree)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pyqtCheck = QtWidgets.QCheckBox(self.widget)
        self.pyqtCheck.setObjectName(_fromUtf8("pyqtCheck"))
        self.horizontalLayout.addWidget(self.pyqtCheck)
        self.pysideCheck = QtWidgets.QCheckBox(self.widget)
        self.pysideCheck.setObjectName(_fromUtf8("pysideCheck"))
        self.horizontalLayout.addWidget(self.pysideCheck)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.forceGraphicsCheck = QtWidgets.QCheckBox(self.widget)
        self.forceGraphicsCheck.setObjectName(_fromUtf8("forceGraphicsCheck"))
        self.horizontalLayout_2.addWidget(self.forceGraphicsCheck)
        self.forceGraphicsCombo = QtWidgets.QComboBox(self.widget)
        self.forceGraphicsCombo.setObjectName(_fromUtf8("forceGraphicsCombo"))
        self.forceGraphicsCombo.addItem(_fromUtf8(""))
        self.forceGraphicsCombo.addItem(_fromUtf8(""))
        self.forceGraphicsCombo.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.forceGraphicsCombo)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.loadBtn = QtWidgets.QPushButton(self.widget)
        self.loadBtn.setObjectName(_fromUtf8("loadBtn"))
        self.verticalLayout.addWidget(self.loadBtn)
        self.widget1 = QtWidgets.QWidget(self.splitter)
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.loadedFileLabel = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.loadedFileLabel.setFont(font)
        self.loadedFileLabel.setText(_fromUtf8(""))
        self.loadedFileLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.loadedFileLabel.setObjectName(_fromUtf8("loadedFileLabel"))
        self.verticalLayout_2.addWidget(self.loadedFileLabel)
        self.codeView = QtWidgets.QPlainTextEdit(self.widget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("FreeMono"))
        self.codeView.setFont(font)
        self.codeView.setObjectName(_fromUtf8("codeView"))
        self.verticalLayout_2.addWidget(self.codeView)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, QtWidgets.QApplication.UnicodeUTF8))
        self.pyqtCheck.setText(QtWidgets.QApplication.translate("Form", "Force PyQt", None, QtWidgets.QApplication.UnicodeUTF8))
        self.pysideCheck.setText(QtWidgets.QApplication.translate("Form", "Force PySide", None, QtWidgets.QApplication.UnicodeUTF8))
        self.forceGraphicsCheck.setText(QtWidgets.QApplication.translate("Form", "Force Graphics System:", None, QtWidgets.QApplication.UnicodeUTF8))
        self.forceGraphicsCombo.setItemText(0, QtWidgets.QApplication.translate("Form", "native", None, QtWidgets.QApplication.UnicodeUTF8))
        self.forceGraphicsCombo.setItemText(1, QtWidgets.QApplication.translate("Form", "raster", None, QtWidgets.QApplication.UnicodeUTF8))
        self.forceGraphicsCombo.setItemText(2, QtWidgets.QApplication.translate("Form", "opengl", None, QtWidgets.QApplication.UnicodeUTF8))
        self.loadBtn.setText(QtWidgets.QApplication.translate("Form", "Run Example", None, QtWidgets.QApplication.UnicodeUTF8))

