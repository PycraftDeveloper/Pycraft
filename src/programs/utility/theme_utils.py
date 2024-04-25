if __name__ != "__main__":
    try:
        import getostheme

        from registry_utils import Registry

        import logging_utils
    except Exception as error:
        from tkinter import messagebox

        messagebox.showerror(
            "Unable to start Pycraft",
            f"A problem occurred whilst trying to start Pycraft (theme_utils.py).\nMore Details: {error}")

    class Theme(Registry):
        LIGHT = "light"
        DARK = "dark"
        def get_dark_theme(self) -> bool:
            theme = True
            try:
                theme = getostheme.isDarkMode()
            except Exception as error:
                logging_utils.Log().log_error(error=error)

            return theme

        def update_theme(self, theme=None, sys_theme=True):
            try:
                old_theme = self.theme
                if theme is not None and sys_theme is False:
                    self.theme = theme

                elif sys_theme:
                    is_dark_theme = getostheme.isDarkMode()

                    if is_dark_theme:
                        self.theme = self.DARK
                    else:
                        self.theme = self.LIGHT

                if old_theme != self.theme:
                    self.update_colors()
                    Registry.update_graphics = True
            except Exception as error:
                logging_utils.Log().log_error(error=error)

        def __init__(self) -> None:
            self.theme = self.DARK
            self.update_theme()

            self.shape_color = (
                29,
                73,
                153)

            self.secondary_shape_color = (
                49,
                93,
                173)

            self.background_color = (
                30,
                30,
                30)

            self.secondary_background_color = (
                80,
                80,
                80)

            self.tertiary_background_color = (
                100,
                100,
                100)

            self.font_color = (
                255,
                255,
                255)

            self.secondary_font_color = (
                200,
                200,
                200)

            self.update_colors()

        def update_colors(self):
            if self.theme == self.DARK:
                self.secondary_shape_color = (
                    49,
                    93,
                    173)

                self.background_color = (
                    30,
                    30,
                    30)

                self.secondary_background_color = (
                    80,
                    80,
                    80)

                self.tertiary_background_color = (
                    100,
                    100,
                    100)

                self.font_color = (
                    255,
                    255,
                    255)

                self.secondary_font_color = (
                    200,
                    200,
                    200)

            else:
                self.secondary_shape_color = (
                    9,
                    53,
                    133)

                self.background_color = (
                    255,
                    255,
                    255)

                self.secondary_background_color = (
                    205,
                    205,
                    205)

                self.tertiary_background_color = (
                    185,
                    185,
                    185)

                self.font_color = (
                    0,
                    0,
                    0)

                self.secondary_font_color = (
                    55,
                    55,
                    55)

else:
    print("You need to run this as part of Pycraft")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
