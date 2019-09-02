import sys
from .User_Interface import setup
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':
    """Is called when the program starts, sets up the program"""
    args = sys.argv
    app = QApplication(sys.argv)
    gui = setup.App()
    sys.exit(app.exec())