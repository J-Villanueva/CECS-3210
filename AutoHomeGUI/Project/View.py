# Views
"""
This file manages the UI Interface of the Application
Here is where events are made and sent
"""
from AdvProgProject2 import *

if __name__ == "__main__":
    import sys

    end = False
    while not end:
        app = QtWidgets.QApplication(sys.argv)
        lockScreen = QtWidgets.QWidget()
        homeScreen = QtWidgets.QMainWindow()
        ambient = QtWidgets.QWidget()
        security = QtWidgets.QWidget()
        settings = QtWidgets.QWidget()

        ui = SmartHouse()

        ui.setupUiLS(lockScreen)
        # ui.retranslateUiLS()
        # lockScreen.show()

        ui.setupUiHS(homeScreen, ambient, security, settings)
        ui.retranslateUiHS(homeScreen, ambient, security, settings)
        homeScreen.show()

        ui.setupUiAm(ambient, homeScreen)
        ui.retranslateUiAm(ambient, homeScreen)

        ui.setupUiSet(settings, homeScreen)
        ui.retranslateUiSet(settings, homeScreen)

        ui.setupUiSec(security, homeScreen)
        ui.retranslateUiSec(security, homeScreen)

        if sys.exit(app.exec_()):
            end = True
