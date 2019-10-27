import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QGridLayout, QVBoxLayout, QGroupBox, QTabWidget, QComboBox
from PyQt5.QtCore import Qt
from MISODataViewer.Controller import Controller


class App(QMainWindow):
    def __init__(self):
        super().__init__()

        # Controller to handle events, analyze data, handle requests.
        # tests for connection to API and DB
        self.comm = Controller.Controller()
        self.connection_status = ''
        self.set_connection_status(self.comm.is_connection_good())

        # current report info
        self.selected_report = ''

        # title of window
        self.title = 'MISO Data Viewer'

        # data filters/choosers
        # left option column
        self.cb_report_chooser = QComboBox()
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

        # setup event handlers on controls
        self.event_handler_setup()

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
        self.cb_report_chooser.addItem('Choose data set...')
        reports_list = self.comm.get_avail_reports_names()
        for report in reports_list:
            self.cb_report_chooser.addItem(report)

        vb_layout.addWidget(self.cb_report_chooser)
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

    def event_handler_setup(self):
        self.cb_report_chooser.currentIndexChanged.connect(self.chosen_report_changed)

    def chosen_report_changed(self):
        print('testingggg')

    def set_connection_status(self, status):
        if status:
            self.connection_status = 'Success'
        else:
            self.connection_status = 'Fail'