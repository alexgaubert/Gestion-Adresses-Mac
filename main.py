#! /usr/bin/python
#-*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from fenetre import Form
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = Form()
    myapp.show()
    sys.exit(app.exec_())
