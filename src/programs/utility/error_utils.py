if __name__ != "__main__":
    try:
        import sys
        import traceback
        from typeguard import Optional
        from tkinter import messagebox, Tk

        from registry_utils import Registry

        import logging_utils
        import general_utils
    except Exception as error:
        from tkinter import messagebox

        messagebox.showerror(
            "Unable to start Pycraft",
            f"A problem occurred whilst trying to start Pycraft (error_utils.py).\nMore Details: {error}")

    class Error(Registry):
        def __init__(
                self,
                string: Optional[str] = None,
                error: Optional[Exception] = None,
                log:bool = True) -> None:

            if log:
                logging_utils.Log().log_error(
                    string=string,
                    error=error)

            if string is None:
                content = str(error)
            else:
                content = string

            if Registry.developer_mode and error is not None:
                content += "\n"
                content += "".join(
                    traceback.format_exception(
                        None,
                        error,
                        error.__traceback__))

            if Registry.developer_mode:
                long_content = content + "\n"
                long_content += "".join(
                    traceback.format_exception(
                        None,
                        error,
                        error.__traceback__))

                print(f"Pycraft has ran into a problem", long_content)
            else:
                print(f"Pycraft has ran into a problem", content)

            try:
                import pygame
                pygame.quit()
            except:
                pass

            Tk().destroy()

            messagebox.showerror(
                f"Pycraft has ran into a problem",
                content)

            sys.exit()

else:
    print("You need to run this as part of Pycraft")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
