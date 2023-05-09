from model.model import Model
from view.view import View


class ControllerPagehome:

    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view

    def connection_events(self):
        self.view.get_view_page_home().get_button_file_path().connect(self.event_button_file_path)
        self.view.get_view_page_home().get_button_load_file().connect(self.event_button_load_file)
        self.view.get_view_page_home().get_button_power_bi().connect(self.event_button_power_bi)
        self.view.get_view_page_home().get_combobox_rune_type().connect(self.event_combobox_rune_type)
        self.view.get_view_page_home().get_combobox_efficency().connect(self.event_combobox_efficency)
        self.view.get_view_page_home().get_combobox_efficency_selection().connect(self.event_combobox_efficency_selection)


    def event_button_file_path(self):
        self.view.get_view_page_home().event_button_path_file()

    def event_button_load_file(self):
        path_file = self.view.get_view_page_home().event_button_load_file()
        # Load process on model
        self.model.process_json_file(path_file)
        self.view.get_view_page_home().event_runes(self.model.runes)

    def event_button_power_bi(self):
        path_file = self.view.get_view_page_home().event_button_load_file()
        self.model.process_json_file(path_file)
        self.model.process_power_bi_file()

    def event_combobox_rune_type(self):
        runes = self.model.apply_filter(self.view.get_view_page_home().get_rune_type(),
                                        self.view.get_view_page_home().get_efficency(),
                                        self.get_efficency_selection_attr(self.view
                                                                          .get_view_page_home()
                                                                          .get_combobox_efficency_selection_index()))
        self.view.get_view_page_home().event_rune_type(runes)

    def event_combobox_efficency(self):
        runes = self.model.apply_filter(self.view.get_view_page_home().get_rune_type(),
                                        self.view.get_view_page_home().get_efficency(),
                                        self.get_efficency_selection_attr(self.view
                                                                          .get_view_page_home()
                                                                          .get_combobox_efficency_selection_index()))
        self.view.get_view_page_home().event_effeicency(runes)

    def event_combobox_efficency_selection(self):
        runes = self.model.apply_filter(self.view.get_view_page_home().get_rune_type(),
                                        self.view.get_view_page_home().get_efficency(),
                                        self.get_efficency_selection_attr(self.view
                                                                          .get_view_page_home()
                                                                          .get_combobox_efficency_selection_index()))
        self.view.get_view_page_home().event_effeicency(runes)

    def get_efficency_selection_attr(self, index):
        if 0 == index:
            return "effi_real"
        elif 1 == index:
            return "effi_stats"

