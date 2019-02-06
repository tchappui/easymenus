from collections import OrderDict

from jinja2 import Environment, FileSystemLoader

class Application:  

    def __init__(self, template_paths=None):
        if template_paths is None:
            template_paths = "./menus"
        self._env = Environment(loader=FileSystemLoader(template_paths))
        self.menus = 




