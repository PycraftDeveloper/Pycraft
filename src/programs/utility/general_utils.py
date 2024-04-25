if __name__ != "__main__":
    try:
        import sys
        import tkinter
        import traceback

        import pygame
        from PIL import Image

        from registry_utils import Registry

        import file_utils
        import error_utils
        import logging_utils
        import image_utils
        import path_utils
    except Exception as error:
        from tkinter import messagebox

        messagebox.showerror(
            "Unable to start Pycraft",
            f"A problem occurred whilst trying to start Pycraft (general_utils.py).\nMore Details: {error}")

    def close(
            write_config:bool=True) -> None:

        print("Shutting down. Please wait...")

        try:
            image_converter = image_utils.ImageConverter()
            image = image_converter.ctx_texture_to_pil_image(
                Registry.game_engine.texture2)
            image_path = path_utils.Path(
                f"{Registry.base_path}/temporary/last_scene.png").path
            image.save(image_path)

            if write_config:
                file_utils.Config().write_config()

            pygame.quit()
            print("Done, thanks for using Pycraft!")
            sys.exit(0)
        except Exception as error:
            logging_utils.Log().log_error(error=error)
            content = str(error)

            if Registry.developer_mode:
                content += "\n"
                content += "".join(
                    traceback.format_exception(
                        None,
                        error,
                        error.__traceback__))

            messagebox.showerror(
                "Pycraft has ran into a problem",
                content)

            pygame.quit()
            sys.exit(0)

    def get_window_size() -> tuple[
            int,
            int]:
        try:
            root = tkinter.Tk()
            screen_size_x = root.winfo_screenwidth()
            screen_size_y = root.winfo_screenheight()
            root.destroy()
            return (
                screen_size_x,
                screen_size_y)
        except Exception as error:
            error_utils.Error(error=error)

    def style(widget: str) -> None:
        """
        This procedure is in charge of correctly formatting the TTK
        UI elements, and is mainly used as a way of removing the off-
        white background to elements.
        See here: https://www.pythontutorial.net/tkinter/ttk-style/
        for more information on supported TTK elements and their
        references.

        Args:
            widget (str): The name (as determined by Tkinter) of the
            display element to format.
        """
        try:
            style = tkinter.ttk.Style()
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
        except Exception as error:
            error_utils.Error(error=error)

else:
    print("You need to run this as part of Pycraft")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
