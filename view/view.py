from view.page_home.view_page_home import ViewPageHome
from view.view_main_window import ViewMainWindow


class View:

    def __init__(self):
        # Main
        self.view_main = None

    # WINDOW MAIN
    def start_window_main(self):
        self.view_main = ViewMainWindow()
        self.view_main.start_window()

    def loading_pages_window_main(self):
        self.view_main.start_window()

    def get_page_main(self):
        return self.view_main

    def run_window_main(self):
        self.view_main.run_window()

    # Page HOME
    def get_view_page_home(self):
        return self.view_main.get_view_page_home()


