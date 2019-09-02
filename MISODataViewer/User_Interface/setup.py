import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QGridLayout, QVBoxLayout, QGroupBox, QTabWidget



class App(QMainWindow):
    def __init__(self):
        super().__init__()

        # title of window
        self.title = 'MISO Data Viewer'

        # left option column
        self.left_groupbox = QGroupBox('Options')

        # right data visualization & display
        self.right_groupbox = QGroupBox('Data')
        self.data_tabs_wdgt = QTabWidget()
        self.tab_graph = QWidget()
        self.tab_data = QWidget()
        self.data_tabs_wdgt.addTab(self.tab_graph, 'Visual')
        self.data_tabs_wdgt.addTab(self.tab_data, 'View Data')
        self.right_groupbox.setLayout(self.data_tabs_wdgt)

        # layout
        self.horizontalGroupBox = QGroupBox('Viewer')
        self.window_layout = QVBoxLayout()
        self.window_layout.addWidget(self.horizontalGroupBox)
        grid = QGridLayout()
        grid.setColumnStretch(0, 1)
        grid.setColumnStretch(1, 4)

        grid.addWidget(self.left_groupbox, 0, 0)
        grid.addWidget(self.right_groupbox, 0, 1)
        self.horizontalGroupBox.setLayout(grid)

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
        # layout cannot be assigned to a QMainWindow, so assign to widget and set as central widget
        # https://stackoverflow.com/questions/37304684/qwidgetsetlayout-attempting-to-set-qlayout-on-mainwindow-which-already
        wid = QtWidgets.QWidget(self)
        self.setCentralWidget(wid)
        wid.setLayout(self.window_layout)
        self.show()