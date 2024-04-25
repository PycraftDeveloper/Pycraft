if __name__ != "__main__":
    try:
        from os import makedirs, sep
        from os import path as os_path
    except Exception as error:
        from tkinter import messagebox

        messagebox.showerror(
            "Unable to start Pycraft Installer",
            f"A problem occurred whilst trying to start Pycraft Installer (path_utils.py).\nMore Details: {error}")

    SEPARATOR = sep

    class Path:
        def __init__(self, path):
            self.path = path.replace("/", SEPARATOR)

        def is_file(self):
            return "." in self.path

        def is_dir(self):
            return SEPARATOR in self.path and not self.is_file()

        def exists(self, path=None):
            if path is None:
                path = self.path
            return os_path.exists(path) or os_path.isfile(path)

        def up(self):
            self.path = self.path[::-1].split(SEPARATOR, 1)[-1][::-1]

        def mkdir(self):
            makedirs(self.path)

else:
    MESSAGE = "You need to run this as part of Pycraft's Installer. "
    MESSAGE += "Please run the 'main.py' file."
    print(MESSAGE)
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Fail",
        MESSAGE)
