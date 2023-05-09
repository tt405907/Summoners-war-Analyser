from controller.controller_page_home import ControllerPagehome
from model.model import Model
from view.view import View


class Controller:

    def __init__(self):
        self.view = View()
        self.model = Model()
        # Init Pages here
        self.controller_page_home = ControllerPagehome(self.model, self.view)

    def start(self):
        self.view.start_window_main()
        self.view.loading_pages_window_main()
        self.instantiation_of_connections()
        self.view.run_window_main()

    def instantiation_of_connections(self):
        self.controller_page_home.connection_events()


