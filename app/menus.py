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

    def ask(self, entries={}):
        """Prompts the user for an input and execute the correct handler method."""
        menu_entry = self._input()
        # The chosen entry is saved
        entries[menu_entry.menu.name] = menu_entry
        # Let's call the handler method for the chosen entry
        menu_entry.handler(entries)


class Menu:
    """Class reprensenting a menu."""

    def __init__(self, name, title=None, prompt='--> ', formatter=None, manager=None):
        """Constructor."""
        self.name = name
        self.counter = 1
        self.title = title if title else name.title()
        self.prompt = prompt
        # Numeric entries are those represented by a numeric choice number that will be 
        # auto-incremented
        self.numeric_entries = {}
        # Keyword entries ate those repesented by an alphabetical letter
        self.keyword_entries = {}
        # formatter and manager can be customized if needed
        self.formatter = formatter if formatter else DefaultFormatter()
        self.manager = manager if manager else MenuManager(self)

    def add(self, label, handler, id=None):
        """Appends a new entry to the menu. The new entry is numeric by default."""
        if id is None:
            # Get the next value and increment the counter
            id = self.counter
            self.counter += 1
            self.numeric_entries[str(id)] = MenuEntry(id, label, handler, self)
        else:
            self.keyword_entries[id] = MenuEntry(id, label, handler, self)

    def get(self, answer):
        """Returns the MenuEntry corresponding to a given answer of the user."""
        return {**self.numeric_entries, **self.keyword_entries}.get(answer, None)

    def is_valid(self, answer):
        """Returns True if the user answer is a valid one.
        
        A valid answer is one the is present either in self.numberic_entries or
        in the self.keyword_entries dictionaries.
        """
        return answer in {**self.numeric_entries, **self.keyword_entries}

    @property
    def message(self):
        """Formats the menu.
        
        The message is prepared by an external formatter that can be replaced by 
        any class implementing the same interface as formatters.DefaultFormatter.
        """
        return self.formatter.format(self)

