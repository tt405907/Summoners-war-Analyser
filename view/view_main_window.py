import sys
from PyQt5.QtWidgets import QApplication

from view.main_window import MainWindow
from view.page_home.view_page_home import ViewPageHome


class ViewMainWindow:

    def __init__(self):
        self.app = QApplication([])
        self.view_page_home = ViewPageHome()

    def start_window(self):
        self.window = MainWindow(self.view_page_home.get_page())

    def run_window(self):
        self.window.show()
        sys.exit(self.app.exec())

    def stop_window(self):
        self.window.close()

    def get_view_page_home(self):
        return self.view_page_home

