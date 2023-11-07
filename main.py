import os


class GnomeGlobalThemeChanger:
    def __init__(self):
        self.theme_list = os.listdir(os.path.expanduser('~/.themes'))

    def create_profile_file(self):
        profile_path = os.path.expanduser("~/.profile")

        if not os.path.exists(profile_path):
            with open(profile_path, 'w') as profile_file:
                pass

        return profile_path

    def display_theme_list(self):
        for i, theme in enumerate(self.theme_list, start=1):
            print(f"{i}: {theme}")

    def input_theme(self):
        try:
            choice = int(
                input("Inserisci il numero del risultato desiderato: "))

            if 1 <= choice <= len(self.theme_list):
                selected_theme = self.theme_list[choice - 1]
                print(f"Cambiamento tema globale: {selected_theme}")

                return selected_theme
            else:
                print("Numero non valido.")

        except ValueError:
            print("Inserisci un numero valido.")

    def set_gtk_theme(self):
        selected_theme = self.input_theme()
        profile_path = self.create_profile_file()

        with open(profile_path, 'r') as profile_file:
            lines = profile_file.readlines()

        for i in range(len(lines)):
            if lines[i].startswith("export GTK_THEME="):
                lines[i] = f"export GTK_THEME={selected_theme}"
                break
        else:
            lines.append(f"export GTK_THEME={selected_theme}")

        with open(profile_path, 'w') as profile_file:
            profile_file.writelines(lines)


if __name__ == "__main__":
    theme_changer = GnomeGlobalThemeChanger()
    theme_changer.display_theme_list()
    theme_changer.set_gtk_theme()
