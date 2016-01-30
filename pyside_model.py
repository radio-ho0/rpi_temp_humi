#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Administrator <Administrator@INA>
#
# Distributed under terms of the MIT license.

"""

"""

import sys
from PySide import QtGui

class TempWidget(QtGui.QWidget):
    def __init__(self):

        super(TempWidget, self).__init__()
        self.initUi()

    def initUi(self):
        '''
            init the ui!!!
        '''
        label_hw = QtGui.QLabel('hello world!', self)
        label_hw.move( 10, 10)

        self.show()

def main():
    app = QtGui.QApplication( sys.argv )
    m_widget = TempWidget()
    m_widget.resize( 480, 360 )
    m_widget.setWindowTitle('hello world!')

    sys.exit( app.exec_())

if '__main__' == __name__ :
    main()

