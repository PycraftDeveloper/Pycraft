if __name__ != "__main__":
    try:
        from registry_utils import Registry

        import error_utils
        import path_utils
    except Exception as error:
        from tkinter import messagebox

        messagebox.showerror(
            "Unable to start Pycraft",
            f"A problem occurred whilst trying to start Pycraft (directory_utils.py).\nMore Details: {error}")

    class Check(Registry):
        def __init__(
            self) -> None:

            try:
                paths = [
                    path_utils.Path(f"{Registry.base_path}/temporary"),
                    path_utils.Path(f"{Registry.base_path}/setup"),
                    path_utils.Path(f"{Registry.base_path}/setup/configuration")
                ]

                for path in paths:
                    if path.exists() is False:
                        path.mkdir()

            except Exception as error:
                error_utils.Error(error=error)

else:
    print("You need to run this as part of Pycraft")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
