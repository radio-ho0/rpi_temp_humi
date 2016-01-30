#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
"""

"""

import sys
import time
import datetime
import dht11
import RPi.GPIO as GPIO
from PySide import QtGui, QtCore



# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
#instance = dht11.DHT11(pin = 14)
instance = dht11.DHT11(pin = 18)






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

        self.lb_18b20_temp = QtGui.QLabel('Ds18b20')
        self.le_18b20_temp = QtGui.QLineEdit()

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget( lb_dht11_hum, 1, 0, 1, 1)
        grid.addWidget( le_dht11_hum, 1, 1, 1, 1)

        grid.addWidget( lb_dht11_temp, 2, 0, 1, 1)
        grid.addWidget( le_dht11_temp, 2, 1, 1, 1)

        grid.addWidget( self.lb_18b20_temp, 3, 0, 1, 1)
        grid.addWidget( self.le_18b20_temp, 3, 1, 1, 1)

        self.setLayout(grid)

        self.le_18b20_temp.setText('18')

        update_timer = QtCore.QTimer(self)
        update_timer.timeout.connect(self.get_all_temp)
        update_timer.start(2000)

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
	
    def get_all_temp(self):
#        get_dht11()
        self.get_db18b20()

    def get_db18b20(self):
        tempfile = open("/sys/bus/w1/devices/28-031571bf56ff/w1_slave")
        
        thetext = tempfile.read()
        tempfile.close
        tempdata = thetext.split("\n")[1].split(" ")[9]
        temperature = float(tempdata[2:])
        temperature = temperature / 1000
        self.le_18b20_temp.setText( str(temperature) )
        print("db18b20: " , temperature)

    def get_dht11(self):
        result = instance.read()
        if result.is_valid():
                print("Last valid input: " + str(datetime.datetime.now()))
                print("Temperature: %d C" % result.temperature)
                print("Humidity: %d %%" % result.humidity)
                le_dht11_hum.setText(result.humidity)
                le_dht11_temp.setText(result.temperature)
		

def main():
    app = QtGui.QApplication(sys.argv)
    m_widget = TempWidget()
    m_widget.resize( 480, 360 )
    m_widget.setWindowTitle('Temperature viewer!')
    sys.exit( app.exec_())

if __name__ == '__main__' :
    main()
