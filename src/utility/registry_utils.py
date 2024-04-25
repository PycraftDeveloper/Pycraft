if __name__ != "__main__":
    try:
        import pathlib

        import path_utils
    except Exception as error:
        from tkinter import messagebox

        messagebox.showerror(
            "Unable to start Pycraft Installer",
            f"A problem occurred whilst trying to start Pycraft Installer (registry_utils.py).\nMore Details: {error}")

    class Registry:
        root = path_utils.Path(__file__)
        for _ in range(3):
            root.up()
        base_path = root.path
        banner_path = path_utils.Path(f"{base_path}/resources/images/banner.png").path
        banner_image = None
        icon_path = path_utils.Path(f"{base_path}/resources/images/icon.png").path
        icon_image = None
        version = "5.2.0"
        DEFAULT_INSTALLER_PATH = path_utils.Path(str(pathlib.Path.home()))
        progressbar = None
        install_directory = DEFAULT_INSTALLER_PATH.path
        install_finished = False
        cancel_install = False
        installer_stopped = False

else:
    MESSAGE = "You need to run this as part of Pycraft's Installer. "
    MESSAGE += "Please run the 'main.py' file."
    print(MESSAGE)
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Fail",
        MESSAGE)
