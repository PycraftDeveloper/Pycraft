if __name__ != "__main__":
    try:
        import tkinter as tk
        from tkinter import ttk
        from tkinter import messagebox

        from registry_utils import Registry
    except Exception as error:
        from tkinter import messagebox

        messagebox.showerror(
            "Unable to start Pycraft Installer",
            f"A problem occurred whilst trying to start Pycraft Installer (tkinter_utils.py).\nMore Details: {error}")

    class TkinterUtils:
        def style(self, widget):
            style = ttk.Style()
            style.configure(
                widget,
                background="white",
                foreground="black",
                borderwidth=1,
                focusthickness=3,
                focuscolor="none")

            style.map(
                widget,
                background=[
                    ("active", "white")])

        def get_display_size(self):
            try:
                root = tk.Tk()

                screen_size_x = root.winfo_screenwidth()
                screen_size_y = root.winfo_screenheight()
                root.destroy()

                return (
                    screen_size_x,
                    screen_size_y)
            except:
                return (0, 0)

        def set_size(self, x, y):
            screen_size = self.get_display_size()
            window_size = (x, y)
            centred_x_position = int((screen_size[0]-window_size[0])/2)
            centred_y_position = int((screen_size[1]-window_size[1])/2)

            Registry.root.geometry(f"{window_size[0]}x{window_size[1]}+{centred_x_position}+{centred_y_position}")

        def basic_window_configuration(self):
            Registry.root.configure(background="white")
            panel = tk.Label(Registry.root, image=Registry.banner_image, highlightthickness=0, borderwidth=0)
            panel.pack(side=tk.LEFT)
else:
    MESSAGE = "You need to run this as part of Pycraft's Installer. "
    MESSAGE += "Please run the 'main.py' file."
    print(MESSAGE)
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Fail",
        MESSAGE)
