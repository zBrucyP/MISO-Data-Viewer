import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QGridLayout, QVBoxLayout, QGroupBox, QTabWidget, QComboBox
from PyQt5.QtCore import Qt
from MISODataViewer.Logic_Handler import Data_Communicator


class App(QMainWindow):
    def __init__(self):
        super().__init__()

        # used to communicate with API and bring data to GUI
        self.data_comm = Data_Communicator.DataCommunicator()
        self.connection_status = ''
        self.set_connection_status(self.data_comm.test_conn())

        # title of window
        self.title = 'MISO Data Viewer'

        # left option column
        self.left_groupbox = self.config_left_options_bar()

        # right data visualization & display
        self.right_groupbox = self.config_right_data_area()

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
        """attaches every element at the top level, inserts variables, shows GUI"""
        self.setWindowTitle(self.title)
        self.statusBar().showMessage('UI Ready... Connection: ' + str(self.connection_status))
        self.setGeometry(self.left, self.top, self.width, self.height)
        # layout cannot be assigned to a QMainWindow, so assign to widget and set as central widget
        # https://stackoverflow.com/questions/37304684/qwidgetsetlayout-attempting-to-set-qlayout-on-mainwindow-which-already
        wid = QtWidgets.QWidget(self)
        self.setCentralWidget(wid)
        wid.setLayout(self.window_layout)
        self.show()

    def config_left_options_bar(self):
        """returns a groupbox (a column) with various options"""
        gb = QGroupBox('Options')
        vb_layout = QVBoxLayout()
        vb_layout.setAlignment(Qt.AlignTop)

        # combo boxes
        cb = QComboBox()
        cb.addItem('Choose data set...')

        vb_layout.addWidget(cb)
        gb.setLayout(vb_layout)

        return gb

    def config_right_data_area(self):
        """returns a groupbox with tabs"""
        gb = QGroupBox('Data')
        data_tabs_wdgt = QTabWidget()
        tab_graph = QWidget()
        tab_data = QWidget()
        data_tabs_wdgt.addTab(tab_graph, 'Visual')
        data_tabs_wdgt.addTab(tab_data, 'View Data')
        data_vbox_layout = QVBoxLayout()
        data_vbox_layout.addWidget(data_tabs_wdgt)
        gb.setLayout(data_vbox_layout)

        return gb

    def set_connection_status(self, status):
        if status:
            self.connection_status = 'Success'
        else:
            self.connection_status = 'Failed'