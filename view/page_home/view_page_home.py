from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, QHBoxLayout, QGroupBox, QVBoxLayout, QLabel

from model.configs import DICT_TYPE_RUNES_NAME, DICT_PROC_TYPE_NAME, DICT_CARAC_NAME
from view.page_home.window_home import PageHome


class ViewPageHome:

    def __init__(self):
        self.page_home = PageHome()

    def get_page(self):
        return self.page_home

    def event_button_path_file(self):
        reponse = QFileDialog.getOpenFileName(caption='Select the JSON File')
        self.page_home.line_edit_path_file.setText(reponse[0])

    def event_runes(self, runes):
        """
        The worst code of my life, one day I will surely have the courage to redo it better!
        """
        i_layout = 0
        temp_layout = QHBoxLayout()

        for i_rune in range(len(runes)):
            if i_layout == 3:
                self.page_home.layout_cards_runes.addLayout(temp_layout)
                temp_layout = QHBoxLayout()
                i_layout = 0
            rune = runes[i_rune]
            group_box_rune = QGroupBox(DICT_TYPE_RUNES_NAME[rune.set_id] + " : " + DICT_PROC_TYPE_NAME[rune.extra])
            # layout information rune
            layout_information = QVBoxLayout()
            id_value = "ID : " + str(rune.id)
            sell_value = "Sell value : " + str(rune.sell_value)
            effi_value = "Natural efficency  : " + str(int(rune.effi_stats * 10000)/100) + " %"
            effi_overal = "Overall efficency  : " + str(int(rune.effi_real * 10000)/100) + " %"
            grindable = "Grind  : " + str(int(rune.grindable * 10000)/100) + " %"
            label_informations_text = id_value + "\n" + \
                                      sell_value + "\n" + \
                                      effi_overal + '\n' + \
                                      effi_value + "\n" + \
                                      grindable
            label_informations = QLabel(label_informations_text)
            layout_information.addWidget(label_informations)
            # Load the image and resize it
            pixmap = QPixmap(rune.path)
            width, height = 50, 50
            resized_pixmap = pixmap.scaled(width, height)
            # Create a label and set the pixmap
            label = QLabel()
            label.setPixmap(resized_pixmap)
            # Create a QImage
            layout_global_rune = QHBoxLayout()
            layout_global_rune.addWidget(label)
            layout_global_rune.addLayout(layout_information)
            layout_global_rune.addStretch()
            # labels stats runes
            primary_value = "Primary : " + str(rune.primary[1]) + str(DICT_CARAC_NAME[rune.primary[0]])
            inate_value = "Inate : " + (
                "N/A" if rune.inate[0] == 0 else str(rune.inate[1]) + str(DICT_CARAC_NAME[rune.inate[0]]))
            subs_value = ""
            for sub in rune.subs:
                res = str(sub[1])
                if sub[3] > 0:
                    res += "(+" + str(sub[3]) + ")"
                res += str(DICT_CARAC_NAME[sub[0]])
                if sub[2]:
                    res += " (G)"
                subs_value += res + '\n'
            label_stats_text = primary_value + "\n" + \
                               inate_value + "\n" + \
                               subs_value
            label_stats = QLabel(label_stats_text)
            # layout labels stats runes
            layout_stats = QVBoxLayout()
            layout_stats.addWidget(label_stats)
            # Layout Box
            layout_group_box_rune = QVBoxLayout()
            layout_group_box_rune.addLayout(layout_global_rune)
            layout_group_box_rune.addLayout(layout_stats)
            # addStretch HERE <-------------------
            layout_group_box_rune.addStretch()
            group_box_rune.setLayout(layout_group_box_rune)
            temp_layout.addWidget(group_box_rune)
            i_layout += 1
        if i_layout > 0:
            self.page_home.layout_cards_runes.addLayout(temp_layout)

    def event_rune_type(self, runes):
        # TODO : Clearly not an effective method but given the amount of data it will work
        self.delete_layout(self.page_home.layout_cards_runes)
        self.event_runes(runes)

    def event_effeicency(self, runes):
        # TODO :Clearly not an effective method but given the amount of data it will work
        self.delete_layout(self.page_home.layout_cards_runes)
        self.event_runes(runes)

    def event_button_load_file(self):
        return self.page_home.line_edit_path_file.text()

    def get_button_file_path(self):
        return self.page_home.button_path_file.clicked

    def get_button_load_file(self):
        return self.page_home.button_load_file.clicked

    def get_button_power_bi(self):
        return self.page_home.button_power_bi.clicked

    def get_combobox_rune_type(self):
        return self.page_home.combo_box_rune_type.currentIndexChanged

    def get_combobox_efficency(self):
        return self.page_home.combo_box_efficiency.currentIndexChanged

    def get_combobox_efficency_selection(self):
        return self.page_home.combo_box_efficiency_selection.currentIndexChanged

    def get_combobox_efficency_selection_index(self):
        return self.page_home.combo_box_efficiency_selection.currentIndex()

    def run_window(self):
        self.page_home.show()

    def stop_window(self):
        self.page_home.close()

    def get_rune_type(self):
        return self.page_home.combo_box_rune_type.currentText()

    def get_efficency(self):
        return self.page_home.combo_box_efficiency.currentText()

    def delete_layout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
            elif child.layout() is not None:
                self.delete_layout(child.layout())
