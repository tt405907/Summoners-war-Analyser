from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QGroupBox, QScrollArea, \
    QComboBox
from PyQt5 import QtCore
from PyQt5.QtCore import Qt

from model.configs import DICT_TYPE_RUNES_NAME


class PageHome(QWidget):

    def __init__(self):
        super().__init__()
        # layout path file instance
        self.layout_file_path()
        # layout filters
        self.layout_filters()
        # layout runes
        self.layout_runes()
        # Global layout
        self.layout_page = QVBoxLayout()
        self.layout_page.addWidget(self.group_box_file_path)
        self.layout_page.addWidget(self.group_box_filters)
        self.layout_page.addWidget(self.scrollbar_runes)
        self.layout_page.setAlignment(QtCore.Qt.AlignTop)
        self.setLayout(self.layout_page)

    def layout_file_path(self):
        self.group_box_file_path = QGroupBox("Select JSON File path ")
        self.line_edit_path_file = QLineEdit("inputs/example.json")
        self.line_edit_path_file.setFixedSize(QtCore.QSize(600, 20))
        self.line_edit_path_file.setDisabled(True)
        # Button select file
        self.button_path_file = QPushButton()
        self.button_path_file.setIcon(QIcon("view/assets/ICONE_DOSSIER.png"))
        self.button_path_file.setFixedWidth(40)
        # Button load file
        self.button_load_file = QPushButton("Load")
        self.button_load_file.setFixedWidth(40)
        # Button power bi file
        self.button_power_bi = QPushButton("Power BI")
        self.button_power_bi.setFixedWidth(60)
        # layout facture
        self.layout_edit_path_file = QHBoxLayout()
        self.layout_edit_path_file.addWidget(self.line_edit_path_file)
        self.layout_edit_path_file.addWidget(self.button_path_file)
        self.layout_edit_path_file.addWidget(self.button_load_file)
        self.layout_edit_path_file.addWidget(self.button_power_bi)
        # Global layout of file path management
        self.layout_path_file = QVBoxLayout()
        self.layout_path_file.addLayout(self.layout_edit_path_file)
        self.group_box_file_path.setLayout(self.layout_path_file)

    def layout_filters(self):
        self.group_box_filters= QGroupBox("Filters")
        # filter by rune type
        self.group_box_rune_type = QGroupBox("Rune type")
        self.combo_box_rune_type = QComboBox()
        self.combo_box_rune_type.addItem("All")
        for value in DICT_TYPE_RUNES_NAME.values():
            self.combo_box_rune_type.addItem(value)
        self.layout_rune_type = QVBoxLayout()
        self.layout_rune_type.addWidget(self.combo_box_rune_type)
        self.group_box_rune_type.setLayout(self.layout_rune_type)
        # filter by efficiency of the rune
        self.group_box_efficiency = QGroupBox("Minimum efficiency of the rune")
        self.combo_box_efficiency = QComboBox()
        for i in range(0, 110, 10):
            self.combo_box_efficiency.addItem(str(i) + "%")
        self.layout_efficiency = QVBoxLayout()
        self.layout_efficiency.addWidget(self.combo_box_efficiency)
        self.group_box_efficiency.setLayout(self.layout_efficiency)
        self.layout_group_box_right = QVBoxLayout()
        self.layout_group_box_right.addWidget(self.group_box_efficiency)
        self.layout_group_box_right.setAlignment(Qt.AlignTop)
        # filter by efficiency
        self.group_box_efficiency_selection = QGroupBox("Filter by")
        self.combo_box_efficiency_selection = QComboBox()
        self.combo_box_efficiency_selection.addItem("Overall efficency")
        self.combo_box_efficiency_selection.addItem("Natural efficency")
        self.layout_efficiency_selection = QVBoxLayout()
        self.layout_efficiency_selection.addWidget(self.combo_box_efficiency_selection)
        self.group_box_efficiency_selection.setLayout(self.layout_efficiency_selection)
        # layout filter effi & effi rune type
        self.layout_rune_type_and_efficency_selction = QVBoxLayout()
        self.layout_rune_type_and_efficency_selction.addWidget(self.group_box_efficiency_selection)
        self.layout_rune_type_and_efficency_selction.addWidget(self.group_box_rune_type)
        # layout rune type + efficiency
        self.layout_rune_type_and_efficiency = QHBoxLayout()
        self.layout_rune_type_and_efficiency.addLayout(self.layout_rune_type_and_efficency_selction)

        self.layout_rune_type_and_efficiency.addLayout(self.layout_group_box_right)
        # Global layout of filters management
        self.layout_of_filters = QVBoxLayout()
        self.layout_of_filters.addLayout(self.layout_rune_type_and_efficiency)
        self.group_box_filters.setLayout(self.layout_of_filters)

    def layout_runes(self):
        self.scrollbar_runes = QScrollArea()
        self.widget_container = QWidget()
        self.layout_cards_runes = QVBoxLayout()
        self.widget_container.setLayout(self.layout_cards_runes)
        #Scroll Area Properties
        self.scrollbar_runes.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollbar_runes.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollbar_runes.setWidgetResizable(True)
        self.scrollbar_runes.setWidget(self.widget_container)
