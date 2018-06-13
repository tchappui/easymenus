
class DefaultFormatter:
    """Class responsible for the formatting of the menus."""

    def format(self, menu):
        """Formats a menu."""
        lines = [f'--- {menu.title} ---']
        lines.extend(f'{k} - {v.label}' for k, v in sorted(menu.numeric_entries.items()))
        lines.extend(f'{k} - {v.label}' for k, v in sorted(menu.keyword_entries.items()))
        lines.append(menu.prompt)
        return '\n'.join(lines)
