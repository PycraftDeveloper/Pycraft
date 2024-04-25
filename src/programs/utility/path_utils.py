if __name__ != "__main__":
    try:
        import os
    except Exception as error:
        from tkinter import messagebox

        messagebox.showerror(
            "Unable to start LAaMES",
            f"A problem occurred whilst trying to start LAaMES.\nMore Details: {error}")

    SEPARATOR = os.sep

    class Path:
        def __init__(self, path) -> None:
            self.path = path.replace("/", SEPARATOR)

        def is_file(self):
            return "." in self.path

        def is_dir(self):
            return SEPARATOR in self.path and not self.is_file()

        def exists(self, path=None):
            if path is None:
                path = self.path
            return os.path.exists(path) or os.path.isfile(path)

        def up(self):
            self.path = self.path[::-1].split(SEPARATOR, 1)[-1][::-1]

        def mkdir(self):
            path = ""
            for folder in self.path.split(SEPARATOR):
                path += folder
                if not self.exists(path=path):
                    os.mkdir(path)
                path += SEPARATOR

else:
    print("You need to run this as part of Pycraft")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
