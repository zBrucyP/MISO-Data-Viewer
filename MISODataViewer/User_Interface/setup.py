import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QGridLayout, QVBoxLayout, QGroupBox


class App(QMainWindow):
    def __init__(self):
        super().__init__()

        # title of window
        self.title = 'MISO Data Viewer'

        # left option column
        #left_groupbox =

        # layout
        self.horizontalGroupBox = QGroupBox('')
        self.window_layout = QVBoxLayout()
        self.window_layout.addWidget(self.horizontalGroupBox)
        layout = QGridLayout()
        layout.setColumnStretch(1,4)
        layout.setColumnStretch(2,4)

        # parent menu bar
        main_menu = self.menuBar()
        file_menu = main_menu.addMenu('File')

        # toolbar
        self.toolbar = self.addToolBar('Exit')

        # sizing
        self.left = 150
        self.top = 150
        self.width = 1200
        self.height = 800

        # call for the GUI to display with above specified values
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.statusBar().showMessage('Ready')
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setLayout(self.window_layout)
        self.show()