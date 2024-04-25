if __name__ != "__main__":
    try:
        import time
        import math
        import random

        import pygame

        from registry_utils import Registry

        import path_utils
        import sound_utils
        import text_utils
        import image_utils
    except Exception as error:
        from tkinter import messagebox

        messagebox.showerror(
            "Unable to start Pycraft",
            f"A problem occurred whilst trying to start Pycraft (pycraft_main.py).\nMore Details: {error}")

    class MenuResources(Registry):
        def __init__(self):
            logo_path = f"{Registry.base_path}/src/resources"
            logo_path = f"{logo_path}/general"
            logo_path = f"{logo_path}/pycraft_logo.png"
            self.logo_path = path_utils.Path(logo_path).path
            self.logo = image_utils.Icon().pycraft_icon(self.logo_path)

else:
    MESSAGE = "You need to run this as part of Pycraft, please run the 'main.py' file"
    print(MESSAGE)
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Fail",
        MESSAGE)
