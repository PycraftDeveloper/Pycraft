if __name__ != "__main__":
    try:
        import pickle

        from registry_utils import Registry

        import error_utils
        import general_utils
        import path_utils
        import logging_utils
    except Exception as error:
        from tkinter import messagebox

        messagebox.showerror(
            "Unable to start LAaMES",
            f"A problem occurred whilst trying to start Pycraft (file_utils.py).\nMore Details: {error}")

    REGISTRY_BLACKLIST = [
        "__module__",
        "__dict__",
        "__weakref__",
        "__doc__",
        "version",
        "base_path",
        "ask_to_update",
        "developer_mode",
        "online_version",
        "window_size",
        "fonts",
        "displays",
        "themes",
        "mouse_pos",
        "display_size",
        "update_graphics",
        "mouse_button_down",
        "splash_process",
        "clock",
        "wnd",
        "ctx",
        "camera",
        "game_engine",
        "hud",
        "main_menu",
        "menu_resources",
        "fonts",
        "loading_menu"
    ]

    class Config(Registry):
        def __init__(
                self) -> None:

            try:
                config_path = f"{Registry.base_path}/setup"
                config_path = f"{config_path}/configuration"
                config_path = f"{config_path}/configuration.conf"
                self.config_path = path_utils.Path(config_path)

                if self.config_path.exists() is False:
                    self.create_config()
            except Exception as error:
                error_utils.Error(error=error)

        def write_config(self) -> None:
            self.create_config()

        def read_config(self) -> None:
            try:
                with open(
                        self.config_path.path,
                        "rb") as file:

                    data = pickle.load(file)
                    if data is not None:
                        for key in data:
                            try:
                                setattr(
                                    Registry,
                                    key,
                                    data[key])
                            except Exception as error:
                                logging_utils.Log().log_warning(error=error)

            except (
                    EOFError,
                    FileNotFoundError):
                self.create_config()
            except Exception as error:
                error_utils.Error(error=error)

        def create_config(self) -> None:
            try:
                with open(
                        self.config_path.path,
                        "wb") as file:

                    registry_attributes = dict(vars(Registry))
                    filtered_attributes = {}
                    for attribute in registry_attributes:
                        if not attribute in REGISTRY_BLACKLIST:
                            filtered_attributes[attribute] = registry_attributes[attribute]

                    pickle.dump(
                        filtered_attributes,
                        file)
            except Exception as error:
                if type(error) == EOFError or type(error) == KeyError:
                    try:
                        logging_utils.Log().log_warning(error=error)
                        open(self.config_path.path, "a").close()
                    except Exception as error:
                        error_utils.Error(error=error)
                else:
                    error_utils.Error(error=error)

else:
    print("You need to run this as part of Pycraft")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
