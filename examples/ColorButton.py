# -*- coding: utf-8 -*-
"""
Simple example demonstrating a button which displays a colored rectangle
and allows the user to select a new color by clicking on the button.
"""

import initExample ## Add path to library (just for examples; you do not need this)


import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui, QtWidgets
import numpy as np

app = QtWidgets.QApplication([])
win = QtWidgets.QMainWindow()
btn = pg.ColorButton()
win.setCentralWidget(btn)
win.show()
win.setWindowTitle('pyqtgraph example: ColorButton')

def change(btn):
    print("change", btn.color())
def done(btn):
    print("done", btn.color())

btn.sigColorChanging.connect(change)
btn.sigColorChanged.connect(done)

## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtWidgets.QApplication.instance().exec_()
