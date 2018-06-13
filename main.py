from app.menus import Menu

# Fake database results
data = {
    'A': ["A1", "A2", "A3", "A4"],
    'B': ["B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8"],
    'C': ["C1", "C2", "C3", "C4", "C6"],
}

class Application:
    """Represents the demo application."""
    
    def start(self):
        """Main entry point of the demo application.
        
        The main menu is handled by self.handle_start_menu.
        """
        self.handle_start_menu()

    def handle_start_menu(self, entries={}):
        """Handler method for the main menu.
        
        1. Create the menu
        2. Add menu entries
        3. Display the menu to the user
        """
        menu = Menu('start', title='Start menu', prompt='What do you want to do? ')
        menu.add('Choose a A', self.handle_a_menu, 'a')
        menu.add('Quit', self.handle_quit, 'q')
        menu.manager.ask(entries)

    def handle_a_menu(self, entries={}):
        """Handler method for the A menu.
        
        1. Create the menu
        2. Add numeric menu entries from the 'pseudo-database'
        2. Add keyword menu entries to quit the app and to return to the previous menu
        3. Display the menu to the user
        """
        menu = Menu('a', title="Menu A", prompt='What do you want to do? ')
        for a in data['A']:
            menu.add(a, self.handle_b_menu)
        menu.add('Quit', self.handle_quit, 'q')
        menu.add("Return to start menu", self.handle_start_menu, 'a')
        menu.manager.ask(entries)

    def handle_b_menu(self, entries={}):
        """Handler method for the B menu.
        
        1. Create the menu
        2. Add numeric menu entries from the 'pseudo-database'
        2. Add keyword menu entries to quit, return to the main menu or return to the previous menu.
        3. Display the menu to the user
        """
        menu = Menu('b', title="Menu B", prompt='What do you want to do? ')
        for b in data['B']:
            menu.add(b, self.handle_c_menu)
        menu.add('Quit', self.handle_quit, 'q')
        menu.add("Return to start menu", self.handle_start_menu, 'a')
        menu.add("Return to previous menu", self.handle_a_menu, 'b')
        menu.manager.ask(entries)

    def handle_c_menu(self, entries={}):
        """Handler method for the C menu.
        
        1. Create the menu
        2. Add numeric menu entries from the 'pseudo-database'
        2. Add keyword menu entries to quit, return to the main menu or return to the previous menu.
        3. Display the menu to the user
        """
        menu = Menu('c', title="Menu C", prompt='Quelle entrée choisissez-vous? ')
        for c in data['C']:
            menu.add(c, self.handle_final_print)
        menu.add('Quit', self.handle_quit, 'q')
        menu.add("Return to start menu", self.handle_start_menu, 'a')
        menu.add("Return to previous menu", self.handle_a_menu, 'b')
        menu.manager.ask(entries)

    def handle_final_print(self, entries={}):
        """Handler method for the final task, then returns to the main menu."""
        print(
            "Vous avez sélectionné:\n"
            f"- {entries['start'].label} ({entries['start'].id})\n"
            f"-- {entries['a'].label} ({entries['a'].id})\n"
            f"--- {entries['b'].label} ({entries['b'].id})\n"
            f"---- {entries['c'].label} ({entries['c'].id})\n"
        )
        # Retour au point de départ
        self.handle_start_menu(entries)

    def handle_quit(self, entries):
        """Handler method for the quit choice."""
        print("Bye, bye!")
        
def main():
    """Main entry point of the application."""
    app = Application()
    app.start()

if __name__ == "__main__":
    main()
    
