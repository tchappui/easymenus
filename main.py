from menus import Menu

data = {
    'A': ["A1", "A2", "A3", "A4"],
    'B': ["B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8"],
    'C': ["C1", "C2", "C3", "C4", "C6"],
}

class App:
    def start(self):
        self.handle_start_menu()

    def handle_start_menu(self, entries={}):
        menu = Menu('accueil', title='Accueil', prompt='Quelle entrée choisissez-vous? ')
        menu.add('Choisir un A', self.handle_a_menu, 'a')
        menu.add('Quitter', self.handle_quit, 'q')
        menu.manager.ask(entries)

    def handle_a_menu(self, entries={}):
        menu = Menu('a', title="Menu A", prompt='Quelle entrée choisissez-vous? ')
        for a in data['A']:
            menu.add(a, self.handle_b_menu)
        menu.add('Quitter', self.handle_quit, 'q')
        menu.add("Revenir à l'accueil", self.handle_start_menu, 'a')
        menu.manager.ask(entries)

    def handle_b_menu(self, entries={}):
        menu = Menu('b', title="Menu B", prompt='Quelle entrée choisissez-vous? ')
        for b in data['B']:
            menu.add(b, self.handle_c_menu)
        menu.add('Quitter', self.handle_quit, 'q')
        menu.add("Revenir à l'accueil", self.handle_start_menu, 'a')
        menu.add("Revenir en arrière", self.handle_a_menu, 'b')
        menu.manager.ask(entries)

    def handle_c_menu(self, entries={}):
        menu = Menu('c', title="Menu C", prompt='Quelle entrée choisissez-vous? ')
        for c in data['C']:
            menu.add(c, self.handle_final_print)
        menu.add('Quitter', self.handle_quit, 'q')
        menu.add("Revenir à l'accueil", self.handle_start_menu, 'a')
        menu.add("Revenir en arrière", self.handle_a_menu, 'b')
        menu.manager.ask(entries)

    def handle_final_print(self, entries={}):
        print(
            "Vous avez sélectionné:\n"
            f"- {entries['accueil'].label} ({entries['accueil'].id})\n"
            f"-- {entries['a'].label} ({entries['a'].id})\n"
            f"--- {entries['b'].label} ({entries['b'].id})\n"
            f"---- {entries['c'].label} ({entries['c'].id})\n"
        )
        # Retour au point de départ
        self.handle_start_menu(entries)

    def handle_quit(self, entries):
        print("Bye, bye!")

if __name__ == "__main__":
    app = App()
    app.start()
