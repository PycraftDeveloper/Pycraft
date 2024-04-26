try:
    if __name__ == "__main__":
        import platform
        from tkinter import messagebox

        if platform.system() != "Windows" and platform.system() != "Linux":
            answer = messagebox.askyesno(
                "Pycraft Compatibility Checker",
                "We have detected you aren't using an operating system officially supported by the development team yet.\n\nYou can continue with the install by pressing 'yes' or exit by pressing 'no'.\n\nNote that by continuing we cannot guarantee Pycraft will run correctly, however if you encounter an issue and want to help out, drop us a bug report on the official GitHub repository!")

            if not answer:
                exit()

        import __init__
        __init__.start()
except Exception as error:
    from tkinter import messagebox

    messagebox.showerror(
        "Unable to start Pycraft Installer",
        f"A problem occurred whilst trying to start Pycraft Installer (main.py).\nMore Details: {error}")
