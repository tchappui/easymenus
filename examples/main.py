from easymenus import Menu

# Fake database results
data = {
    'A': ["A1", "A2", "A3", "A4"],
    'B': ["B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8"],
    'C': ["C1", "C2", "C3", "C4", "C6"],
}

class Application:
    """Represents the demo application."""
    
    def start(self):
        """Main entry point of the demo application."""
        menu = Menu('start', title='Start Menu', prompt='What do you want to do ? ')
        menu.add('Choose a A', self.handle_a_menu, 'a')
        menu.add('Quit', self.handle_quit, 'q')
        menu()

    def handle_a_menu(self):
        """Handler method for the A menu."""
        menu = Menu('a', title="Menu A", prompt='What do you want to do ? ')
        for a in data['A']:
            menu.add(a, self.handle_b_menu)
        menu.add("Return to start menu", self.start, 'm')
        menu.add('Quit', self.handle_quit, 'q')
        menu()

    def handle_b_menu(self):
        """Handler method for the B menu."""
        menu = Menu('b', title="Menu B", prompt='What do you want to do ? ')
        for b in data['B']:
            menu.add(b, self.handle_c_menu)
        menu.add('Quit', self.handle_quit, 'q')
        menu.add("Return to start menu", self.start, 'a')
        menu.add("Return to previous menu", self.handle_a_menu, 'b')
        menu()

    def handle_c_menu(self):
        """Handler method for the C menu."""
        menu = Menu('c', title="Menu C", prompt='Quelle entrée choisissez-vous ? ')
        for c in data['C']:
            menu.add(c, self.handle_final_print)
        menu.add('Quit', self.handle_quit, 'q')
        menu.add("Return to start menu", self.start, 'a')
        menu.add("Return to previous menu", self.handle_a_menu, 'b')
        menu()

    def handle_final_print(self):
        """Handler method for the final task, then returns to the main menu."""
        print(
            "Vous avez sélectionné:\n"
            f"- {Menu.choices['start'].text} ({Menu.choices['start'].key})\n"
            f"-- {Menu.choices['a'].text} ({Menu.choices['a'].key})\n"
            f"--- {Menu.choices['b'].text} ({Menu.choices['b'].key})\n"
            f"---- {Menu.choices['c'].text} ({Menu.choices['c'].key})\n"
        )
        menu = Menu('last', title='', prompt='What do you what to do ? ')
        menu.add('Return to the start menu', self.start, 'h')
        menu.add('Quit', self.handle_quit, 'q')
        menu()
        

    def handle_quit(self):
        """Handler method for the quit choice."""
        print("Bye, bye!")
        
def main():
    """Main entry point of the application."""
    app = Application()
    app.start()

if __name__ == "__main__":
    main()
    
