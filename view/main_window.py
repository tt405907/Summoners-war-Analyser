from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QStackedWidget, QLabel, QPushButton, QLineEdit, QHBoxLayout, QWidget
from PyQt5 import QtCore

class MainWindow(QMainWindow):

    def __init__(self, page_home):
        super(MainWindow, self).__init__()
        self.setGeometry(200, 200, 650, 800)
        self.setWindowTitle("Summoners War Analyser")
        # Stack pages here
        self.stacked_widget = QStackedWidget(self)
        self.widget_page_home = page_home
        self.stacked_widget.addWidget(self.widget_page_home)
        self.stacked_widget.setCurrentIndex(0)
        # box layout main
        self.boxlayout_main = QHBoxLayout()
        self.boxlayout_main.addWidget(self.stacked_widget)
        self.boxlayout_main.addStretch()
        self.widget = QWidget()
        self.widget.setLayout(self.boxlayout_main)
        self.widget.layout().setContentsMargins(0, 0, 0, 0)
        self.setCentralWidget(self.widget)

    def layout_file_path(self):
        self.label_file_path = QLabel("Select JSON File path ")
        self.line_edit_path_file = QLineEdit("inputs/example.json")
        self.line_edit_path_file.setFixedSize(QtCore.QSize(300, 20))
        self.line_edit_path_file.setDisabled(True)
        self.button_path_file = QPushButton()
        self.button_path_file.setIcon(QIcon("view/assets/ICONE_DOSSIER.png"))
        self.button_path_file.setFixedWidth(40)
        # layout facture
        self.layout_path_file = QHBoxLayout()
        self.layout_path_file.addWidget(self.line_edit_path_file)
        self.layout_path_file.addWidget(self.button_path_file)
        self.layout_path_file.setAlignment(QtCore.Qt.AlignCenter)


