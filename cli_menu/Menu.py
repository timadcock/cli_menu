class MenuItem():
    def __init__(self, option_name, option_icon, function=None):
        self._name = option_name
        self._function = function
        self._icon = option_icon

    def get_name(self):
        return self._name

    def __str__(self):
        return f"{self._name}: {self._icon}"

    def __call__(self, *args, **kwargs):
        return self._function(*args, **kwargs)


class Menu():
    def __init__(self, menu_name="Menu", width=40, length=10):
        self._options = {}
        self._width = width
        self._length = length
        self._menu_name = menu_name

        self._options["q"] = MenuItem("Quit", "q", exit)

    def add_option(self, option_name, function, order=None):

        index = order if order is not None else len(self._options)

        # Wrap index as a string for later calling
        index = str(index)

        self._options[index] = MenuItem(option_name, order if order is not None else len(self._options), function)

    def display_menu(self):
        out = f"{self._menu_name:^{self._width}}\n"
        tmp = "Choose one of the options below"
        out += f"{tmp:^{self._width}}\n\n"
        for option in self._options:

            try:
                if option.lower() == "q":
                    continue
            except AttributeError:
                # We expect this for numerical options
                pass
            out += f"{self._options[option]}\n"

        # Make sure our exit is set
        out += f"{self._options["q"]}\n"

        print(out)

    def run_option(self):
        self.display_menu()



        valid_option = True

        while valid_option:
            try:
                choice = input("Option: ")
                print(f"Selected option {self._options[choice].get_name()}")
                return self._options[choice]()
                valid_option = False

            except KeyError:
                print("Invalid option")