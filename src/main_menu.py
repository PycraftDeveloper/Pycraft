if __name__ != "__main__":
    try:
        import sys
        import tkinter as tk
        import tkinter.font as font
        import tkinter.filedialog as filedialog
        from tkinter import ttk
        import shutil
        from tkinter import messagebox

        from registry_utils import Registry

        import install_menu

        import path_utils
    except Exception as error:
        from tkinter import messagebox

        messagebox.showerror(
            "Unable to start Pycraft Installer",
            f"A problem occurred whilst trying to start Pycraft Installer (main_menu.py).\nMore Details: {error}")

    class MainMenu:
        def bytes_to_gigabytes(self, size):
            return size / 1e+9

        def is_installable(self, directory):
            try:
                file_stats = shutil.disk_usage(directory)

                installable = self.bytes_to_gigabytes(file_stats.free) > 5
            except:
                installable = False

            if not installable:
                messagebox.showerror("Pycraft's Installation Assistant", "A minimum of 5 GB of free space is required to install Pycraft.\nUnfortunately, that means it wont be possible to install Pycraft here.")

            return installable

        def browse_directories(self):
            filename = filedialog.askdirectory()

            if filename == "":
                return

            filename = path_utils.Path(filename).path
            self.selected_file_path_entry.config(state='normal')
            self.selected_file_path_entry.delete(0, tk.END)
            self.selected_file_path_entry.insert(tk.END, filename)
            self.selected_file_path_entry.config(state='readonly')
            Registry.install_directory = filename

            self.install_button['state'] = tk.NORMAL if self.is_installable(filename) else tk.DISABLED

        def __init__(self):
            self.main_menu_frame = ttk.Frame(Registry.root)

            title_font = font.Font(self.main_menu_frame, size=Registry.default_font_size+7)
            content_font = font.Font(self.main_menu_frame, size=Registry.default_font_size)

            self.title_label = ttk.Label(self.main_menu_frame, text="Pycraft's Installation Assistant", font=title_font)

            self.size_label = ttk.Label(self.main_menu_frame, text="A minimum of 5 GB of free space is required")

            self.content_text = tk.Text(self.main_menu_frame, wrap="word", relief=tk.FLAT, height=5)
            self.content_text.configure(font=content_font)
            self.content_text.insert(
                tk.INSERT,
                "Welcome to Pycraft's Installation Assistant! You can use this to install Pycraft onto your system. \
Please select an install location with at least 5 GB of available space, then click 'install' to \
begin the install process.\nNote that Pycraft is portable and can be installed on removable media.")
            self.content_text.config(state=tk.DISABLED)
            self.content_text.config(highlightthickness = 0, borderwidth=0)

            self.entry_frame = ttk.Frame(self.main_menu_frame)

            self.button_frame = ttk.Frame(self.main_menu_frame)

            self.cancel_button = ttk.Button(self.button_frame, text="Cancel", command=sys.exit)

            self.install_screen = install_menu.InstallMenu()
            self.install_button = ttk.Button(self.button_frame, text="Install", command= lambda: [self.main_menu_frame.destroy(), self.install_screen.main()])
            self.install_button['state'] = tk.NORMAL if self.is_installable(Registry.DEFAULT_INSTALLER_PATH.path) else tk.DISABLED

            self.install_button.pack(side=tk.RIGHT, padx=5, pady=5)
            self.cancel_button.pack(side=tk.RIGHT, padx=5, pady=5)

            select_button = ttk.Button(self.entry_frame, text="Select", command=self.browse_directories)
            select_button.pack(side=tk.LEFT, padx=5)

            horizontal_scrollbar = ttk.Scrollbar(self.entry_frame, orient="horizontal")
            horizontal_scrollbar.pack(side=tk.BOTTOM, fill=tk.X, padx=5)

            self.selected_file_path_entry = ttk.Entry(self.entry_frame, xscrollcommand=horizontal_scrollbar.set)
            self.selected_file_path_entry.config(state='normal')
            self.selected_file_path_entry.insert(0, Registry.DEFAULT_INSTALLER_PATH.path)
            self.selected_file_path_entry.config(state='readonly')
            self.selected_file_path_entry.pack(side=tk.TOP, fill=tk.X, expand=True, padx=5)

            horizontal_scrollbar.config(command=self.selected_file_path_entry.xview)

            ###

            self.title_label.pack()
            self.content_text.pack(fill=tk.X)

            self.entry_frame.pack(fill=tk.X)

            self.button_frame.pack(side=tk.BOTTOM, fill=tk.X)

        def main(self):
            self.main_menu_frame.pack(fill=tk.BOTH, expand=True)

else:
    MESSAGE = "You need to run this as part of Pycraft's Installer. "
    MESSAGE += "Please run the 'main.py' file."
    print(MESSAGE)
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Fail",
        MESSAGE)
