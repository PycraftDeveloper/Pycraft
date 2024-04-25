if __name__ != "__main__":
    try:
        import sys
        import tkinter as tk
        import tkinter.font as font
        from tkinter import ttk
        from tkinter import messagebox
        import platform
        import subprocess

        from registry_utils import Registry

        import path_utils
    except Exception as error:
        from tkinter import messagebox

        messagebox.showerror(
            "Unable to start Pycraft Installer",
            f"A problem occurred whilst trying to start Pycraft Installer (finish_menu.py).\nMore Details: {error}")

    class FinishMenu:
        def close(self):
            sys.exit()

        def copy(self):
            try:
                clipboard_manager_path = path_utils.Path(f"{Registry.base_path}/src/utility/clipboard_manager.py").path

                subprocess.Popen([self.activate_environment_directory, clipboard_manager_path, self.run_command])
            except:
                messagebox.showerror(
                    "Pycraft Installer",
                    "Unfortunately it hasn't been possible to copy this to your clipboard, this is likely due to the configuration of your system.")

        def __init__(self):
            self.finish_menu_frame = ttk.Frame(Registry.root)

            title_font = font.Font(self.finish_menu_frame, size=Registry.default_font_size+7)
            content_font = font.Font(self.finish_menu_frame, size=Registry.default_font_size)

            self.title_label = ttk.Label(self.finish_menu_frame, text="Pycraft's Installation Assistant", font=title_font)

            self.install_directory = path_utils.Path(f"{Registry.install_directory}/Pycraft").path
            self.main_directory = path_utils.Path(f"{self.install_directory}/src/main.py").path
            if platform.system() == "Windows":
                self.activate_environment_directory = path_utils.Path(f"{self.install_directory}/venv/pycraft/Scripts/python.exe").path
            else:
                self.activate_environment_directory = path_utils.Path(f"{self.install_directory}/venv/pycraft/bin/python").path

            self.run_command = f"{self.activate_environment_directory} {self.main_directory}"
            newline = "\n"

            self.content_text = tk.Text(self.finish_menu_frame, wrap="word", relief=tk.FLAT, height=10)
            self.content_text.configure(font=content_font)
            self.content_text.insert(
                tk.INSERT,
                f"Pycraft has been successfully installed onto your system!{newline}\
In order to run the application, please use the following command:{newline}{newline}{self.run_command}{newline}{newline}\
Note that this can be copied using the button below, and we also recommend making a \
shortcut to this location on your system for easier access.")
            self.content_text.config(state=tk.DISABLED)
            self.content_text.config(highlightthickness = 0, borderwidth=0)

            self.button_frame = ttk.Frame(self.finish_menu_frame)

            self.copy_button = ttk.Button(self.button_frame, text="Copy", command=self.copy)

            self.close_button = ttk.Button(self.button_frame, text="Close", command=self.close)

            self.close_button.pack(side=tk.RIGHT, padx=5, pady=5)
            self.copy_button.pack(side=tk.RIGHT, padx=5, pady=5)

            ###

            self.title_label.pack()

            self.content_text.pack(fill=tk.X)

            self.button_frame.pack(side=tk.BOTTOM, fill=tk.X)

        def main(self):
            self.finish_menu_frame.pack(fill=tk.BOTH, expand=True)

else:
    MESSAGE = "You need to run this as part of Pycraft's Installer. "
    MESSAGE += "Please run the 'main.py' file."
    print(MESSAGE)
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Fail",
        MESSAGE)
