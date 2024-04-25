if __name__ != "__main__":
    try:
        import tkinter as tk
        from PIL import Image, ImageTk
        import tkinter.font as font

        from registry_utils import Registry

        import main_menu

        import tkinter_utils
    except Exception as error:
        from tkinter import messagebox

        messagebox.showerror(
            "Unable to start Pycraft Installer",
            f"A problem occurred whilst trying to start Pycraft Installer (pycraft_installer_main.py).\nMore Details: {error}")

    class Core:
        def __init__(self):
            Registry.tkinter_utils = tkinter_utils.TkinterUtils()

            Registry.root = tk.Tk()
            Registry.root.eval('tk::PlaceWindow . center')
            Registry.tkinter_utils.set_size(695, 501)
            Registry.root.title("Pycraft: Installer")
            Registry.root.resizable(width=False, height=False)

            Registry.banner_image = ImageTk.PhotoImage(Image.open(Registry.banner_path))
            Registry.icon_image = ImageTk.PhotoImage(Image.open(Registry.icon_path))

            Registry.tkinter_utils.style("TLabel")
            Registry.tkinter_utils.style("TEntry")
            Registry.tkinter_utils.style("TButton")
            Registry.tkinter_utils.style("TFrame")
            Registry.tkinter_utils.style("Horizontal.TScrollbar")

            Registry.root.wm_iconphoto(False, Registry.icon_image)

            fonts = font.nametofont('TkTextFont').actual()
            Registry.default_font_size = fonts["size"]

            self.main_screen = main_menu.MainMenu()

        def main(self):
            Registry.tkinter_utils.basic_window_configuration()
            self.main_screen.main()

            Registry.root.mainloop()

    def init():
        Core().main()

    def get_version():
        return Registry.version
else:
    MESSAGE = "You need to run this as part of Pycraft's Installer. "
    MESSAGE += "Please run the 'main.py' file."
    print(MESSAGE)
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Fail",
        MESSAGE)
