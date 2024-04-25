if __name__ != "__main__":
    try:
        import sys
        import tkinter as tk
        import tkinter.font as font
        from tkinter import ttk
        import shutil
        from tkinter import messagebox
        import time
        import threading

        from registry_utils import Registry

        import finish_menu

        import install_coordinator_utils
    except Exception as error:
        from tkinter import messagebox

        messagebox.showerror(
            "Unable to start Pycraft Installer",
            f"A problem occurred whilst trying to start Pycraft Installer (install_menu.py).\nMore Details: {error}")

    class InstallMenu:
        def label_updater(self):
            while Registry.install_finished is False:
                value = int(Registry.progressbar['value'])
                if value > 100:
                    value = 100
                elif value < 0:
                    value = 0

                self.written_install_progress.set(f"Install progress: {value}%")
                time.sleep(1/30)

            self.written_install_progress.set("Install progress: 100% - Complete!")
            self.finish_button['state'] = tk.NORMAL

            countdown = 5
            for count in range(countdown, -1, -1):
                time.sleep(1)
                self.finish_button.configure(text=f"Finish ({count})")

            self.finish()

        def finish(self):
            self.install_menu_frame.destroy()
            self.finish_menu.main()

        def exit(self):
            do_cancel = messagebox.askyesno("Pycraft Installer", "Are you sure you want to cancel the installation?\n\nIf you do, bear with us as we terminate the installation process.")

            if do_cancel:
                self.coordinator.kill()
                while Registry.installer_stopped is False:
                    time.sleep(1/30)
                clean_up = messagebox.askyesno("Pycraft Installer", "Do you want us to try and remove any progress made?")
                if clean_up:
                    try:
                        shutil.rmtree(Registry.install_directory)
                    except:
                        messagebox.showinfo("Pycraft Installer", f"Not all files could be removed, please remove those manually from: {Registry.install_directory}")
                sys.exit()

        def __init__(self):
            self.install_menu_frame = ttk.Frame(Registry.root)

            title_font = font.Font(self.install_menu_frame, size=Registry.default_font_size+7)
            content_font = font.Font(self.install_menu_frame, size=Registry.default_font_size)

            self.title_label = ttk.Label(self.install_menu_frame, text="Pycraft's Installation Assistant", font=title_font)

            self.content_text = tk.Text(self.install_menu_frame, wrap="word", relief=tk.FLAT, height=3)
            self.content_text.configure(font=content_font)
            self.content_text.insert(
                tk.INSERT,
                "We are currently in the process of installing Pycraft onto your system.\n\
This may take a few minutes, we will let you know when it's finished!")
            self.content_text.config(state=tk.DISABLED)
            self.content_text.config(highlightthickness = 0, borderwidth=0)

            self.written_install_progress = tk.StringVar()
            self.written_install_progress.set("Install progress: 0%")

            self.progress_label = ttk.Label(self.install_menu_frame, textvariable=self.written_install_progress)

            Registry.progressbar = ttk.Progressbar(self.install_menu_frame)

            self.coordinator = install_coordinator_utils.InstallCoordinator()
            self.label_updater_thread = threading.Thread(target=self.label_updater)
            self.label_updater_thread.daemon = True

            self.button_frame = ttk.Frame(self.install_menu_frame)

            self.cancel_button = ttk.Button(self.button_frame, text="Cancel", command=self.exit)

            self.finish_menu = finish_menu.FinishMenu()
            self.finish_button = ttk.Button(self.button_frame, text="Finish", command=self.finish)
            self.finish_button['state'] = tk.DISABLED

            self.finish_button.pack(side=tk.RIGHT, padx=5, pady=5)
            self.cancel_button.pack(side=tk.RIGHT, padx=5, pady=5)

            ###

            self.title_label.pack()

            self.content_text.pack(fill=tk.X)

            self.progress_label.pack()

            Registry.progressbar.pack(fill=tk.X, padx=5)

            self.button_frame.pack(side=tk.BOTTOM, fill=tk.X)

        def main(self):
            self.label_updater_thread.start()
            self.coordinator.start()
            self.install_menu_frame.pack(fill=tk.BOTH, expand=True)

else:
    MESSAGE = "You need to run this as part of Pycraft's Installer. "
    MESSAGE += "Please run the 'main.py' file."
    print(MESSAGE)
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Fail",
        MESSAGE)
