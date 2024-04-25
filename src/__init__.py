if __name__ != "__main__":
    try:
        import os
        import sys
        import platform
    except Exception as error:
        from tkinter import messagebox

        messagebox.showerror(
            "Unable to start Pycraft Installer",
            f"A problem occurred whilst trying to start Pycraft Installer (__init__.py).\nMore Details: {error}")

    SEPARATOR = os.sep

    def up(path: str) -> str:
        return path[::-1].split(SEPARATOR, 1)[-1][::-1]

    base_path = up(up(__file__))

    sys.pycache_prefix = base_path + SEPARATOR + "temporary"

    pycraft_installer_src_path = base_path + SEPARATOR + "src"
    pycraft_installer_utility_path = pycraft_installer_src_path + SEPARATOR + "utility"

    sys.path.append(
        pycraft_installer_src_path)

    sys.path.append(
        pycraft_installer_utility_path)

    import pycraft_installer_main

    if platform.system() == "Windows":
        import ctypes
        VERSION = pycraft_installer_main.get_version()
        myappid = f"PycraftDev.Pycraft Installer._.{VERSION}"
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        del myappid
        del ctypes

    del sys
    del platform
    del base_path
    del up
    del SEPARATOR

    def start() -> None:
        pycraft_installer_main.init()

else:
    MESSAGE = "You need to run this as part of Pycraft's Installer. "
    MESSAGE += "Please run the 'main.py' file."
    print(MESSAGE)
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Fail",
        MESSAGE)
