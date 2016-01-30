#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
"""

"""

import sys
from PySide import QtGui, QtCore

class TempWidget(QtGui.QWidget):
    def __init__(self):
        super(TempWidget, self).__init__()

        self.initUi()

    def initUi(self):

        lb_title = QtGui.QLabel('temperature viewer', self)
        lb_title.move(180, 15)
        self.initBtExit()

        lb_dht11_hum = QtGui.QLabel('Dht11 hum')
        le_dht11_hum =QtGui.QLineEdit()

        lb_dht11_temp = QtGui.QLabel('dht11 temp')
        le_dht11_temp = QtGui.QLineEdit()

        lb_18b20_temp = QtGui.QLabel('Ds18b20')
        le_18b20_temp = QtGui.QLineEdit()

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget( lb_dht11_hum, 1, 0, 1, 1)
        grid.addWidget( le_dht11_hum, 1, 1, 1, 1)

        grid.addWidget( lb_dht11_temp, 2, 0, 1, 1)
        grid.addWidget( le_dht11_temp, 2, 1, 1, 1)

        grid.addWidget( lb_18b20_temp, 3, 0, 1, 1)
        grid.addWidget( le_18b20_temp, 3, 1, 1, 1)

        self.setLayout(grid)

        le_18b20_temp.setText('18')
        self.show()

    def initBtExit(self):
        btn1 = QtGui.QPushButton('aHa!', self)
        btn1.setToolTip('Just for play!')
        btn1.resize( btn1.sizeHint())
        btn1.move( 10, 10)

        btnExit = QtGui.QPushButton('&Exit', self)
        btnExit.setToolTip('88')
        btnExit.clicked.connect(QtCore.QCoreApplication.instance().quit)
        btnExit.move( 380, 320 )

def main():
    app = QtGui.QApplication(sys.argv)
    m_widget = TempWidget()
    m_widget.resize( 480, 360 )
    m_widget.setWindowTitle('Temperature viewer!')
    sys.exit( app.exec_())

if __name__ == '__main__' :
    main()
