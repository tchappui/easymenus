import itertools
from collections import OrderedDict

class MenuEntry:
    """Class representing a menu entry."""

    def __init__(self, menu, id, label, handler):
        """Constructor."""
        self.menu = menu
        self.id = id
        self.label = label
        self.handler = handler

class MenuManager:
    """Class responsible for the management of a menu."""

    def __init__(self, menu):
        """Constructor."""
        self.menu = menu

    def _input(self):
        """Asks the user for an input and repeat the request until the
        answer is correct."""
        while True:
            answer = input(self.menu.message).strip()
            if answer in self.menu.entries:
                return self.menu.get(answer)

    def render(self, entries={}):
        """Prompts the user for an input and execute the correct handler method."""
        menu_entry = self._input()
        # The chosen entry is saved
        entries[menu_entry.menu.name] = menu_entry
        # Let's call the handler method for the chosen entry
        menu_entry.handler(entries)

class MenuEntryCollection:
    """Class representing a collection of menu entries accessible by order of addition and id type."""

    def __init__(self):
        self.numeric = OrderedDict()
        self.alpha = OrderedDict()
        self.alnum = OrderedDict()

    @property
    def all(self):
        """Generator allowing iteration over all available entries."""
        return (entry for entry in self.alnum.values())

    def add(self, entry):
        """Adds a new entry to the collection."""
        self.all.append(entry)
        self.alnum[str(entry.id)] = entry
        if isinstance(entry.id, int):
            self.numeric[entry.id] = entry
        else:
            self.alpha[str(entry.id)] = entry

    def __iadd__(self, entry):
        """Implements the += operator as a synonyme of add."""
        self.add(entry)

    def __getitem__(self, key):
        return self.alnum.get(str(key), self.alnum.get(str(key).lower())) 

    def __contains__(self, value):
        """Returns True if value is a valid choice in the MenuEntryCollection."""
        return str(value) in self.alnum or str(value).lower() in self.alnum


class Menu:
    """Class reprensenting a menu."""

    def __init__(self, name, manager=None):
        """Constructor."""
        self.name = name
        self.entries = MenuEntryCollection()
        self.manager = manager if manager else MenuManager(self)   
        self._counter = itertools.count(start=1)   

    def add(self, entry_text, handler, id=None):
        """Appends a new entry to the menu. The new entry is numeric by default."""
        if id is None:
            id = next(self._counter)
        self.entries += MenuEntry(self, id, entry_text, handler)

    def add_multiple(self, entries, handler):
        """Appends a new entries to the menu in a list or a dictionary."""
        if isinstance(entries, list):
            for entry_text in entries:
                id = next(self._counter)
                self.entries += MenuEntry(self, id, entry_text, handler)
        elif isinstance(entries, dict):
            for id, entry_text in entries.items():
                self.entries += MenuEntry(self, id, entry_text, handler)


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

