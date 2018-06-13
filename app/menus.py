from .formatters import DefaultFormatter

class MenuEntry:
    """Class representing a menu entry."""

    def __init__(self, id, label, handler, menu):
        """Constructor."""
        self.id = id
        self.label = label
        self.handler = handler
        self.menu = menu

class MenuManager:
    """Class responsible for the management of a menu."""

    def __init__(self, menu):
        """Constructor."""
        self.menu = menu

    def _input(self):
        """Asks the user for an input and repeat the request until the
        answer is correct."""
        while True:
            answer = input(self.menu.message).lower().strip()
            if self.menu.is_valid(answer):
                return self.menu.get(answer)

    def ask(self, entries):
        """Prompts the user for an input and execute the correct handler method."""
        menu_entry = self._input()
        entries[menu_entry.menu.name] = menu_entry
        menu_entry.handler(entries)


class Menu:
    """Class reprensenting a menu."""

    def __init__(self, name, title=None, prompt='--> ', formatter=None, manager=None):
        """Constructor."""
        self.name = name
        self.counter = 1
        self.title = title if title else name.title()
        self.prompt = prompt
        self.numeric_entries = {}
        self.keyword_entries = {}
        self.formatter = formatter if formatter else DefaultFormatter()
        self.manager = manager if manager else MenuManager(self)

    def add(self, label, handler, id=None):
        """Appends a new entry to the menu. The new entry is numeric by default."""
        if id is None:
            id = self.counter
            self.counter += 1
            self.numeric_entries[str(id)] = MenuEntry(id, label, handler, self)
        else:
            self.keyword_entries[id] = MenuEntry(id, label, handler, self)

    def get(self, answer):
        """Returns the MenuEntry corresponding to a given answer of the user."""
        return {**self.numeric_entries, **self.keyword_entries}.get(answer, None)

    def is_valid(self, answer):
        """Returns True if the user answer is a valid one."""
        return answer in {**self.numeric_entries, **self.keyword_entries}

    @property
    def message(self):
        """Formats the menu."""
        return self.formatter.format(self)
