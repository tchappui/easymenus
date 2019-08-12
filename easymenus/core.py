from jinja2 import Template


_DEFAULT_TEMPLATE = """
{%- if menu.title -%}
--- {{ menu.title }} ---
{% endif -%}
{% for key, entry in menu -%}
{{ key }} - {{ entry.text }}
{% endfor -%}
{%- if menu.prompt -%}
{{ menu.prompt }}
{%- else -%}
--> {% endif -%}"""


class MenuEntry:
    """Class representing a menu entry."""

    def __init__(self, text, handler, key, menu, **data):
        """Constructor."""
        self.text = text
        self.handler = handler
        self.menu = menu
        self.key = key
        self.data = data

class Menu:
    """Class representing a menu."""

    choices = {}

    def __init__(
        self, 
        name, 
        template=Template(_DEFAULT_TEMPLATE),
        **meta
    ):
        """Constructor."""
        self._counter = 1
        self._entries = {}

        self.name = name
        self.template = template
        self.meta = meta

        self.choices[name] = None

    def add(self, text, handler, key=None, **data):
        """Appends a new entry to the menu. The new entry is numeric by default."""
        if key is None:
            key = self._counter
            self._counter += 1
        key = str(key)
        self._entries[key] = MenuEntry(text, handler, key, self, **data)

    def is_valid(self, answer):
        """Returns True if the user answer is a valid one."""
        return answer in self

    def __call__(self):
        """Asks the user for an input and repeat the request until the
        answer is correct."""
        while True:
            answer = input(self.template.render(menu=self))
            if self.is_valid(answer):
                entry = self.choices[self.name] = self[answer]
                return entry.handler()

    def __getitem__(self, key):
        """Returns the MenuEntry corresponding to a given key."""
        return self._entries.get(str(key))

    def __contains__(self, key):
        """Returns the MenuEntry corresponding to a given key."""
        return str(key) in self._entries

    def __iter__(self):
        return iter(self._entries.items())

    def __getattr__(self, key):
        return self.meta.get(key)

