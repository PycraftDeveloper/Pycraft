if __name__ != "__main__":
    try:
        import time
        import math
        import random

        import pygame
        import moderngl_window

        from registry_utils import Registry

        import path_utils
        import sound_utils
        import text_utils
    except Exception as error:
        from tkinter import messagebox

        messagebox.showerror(
            "Unable to start Pycraft",
            f"A problem occurred whilst trying to start Pycraft (pycraft_main.py).\nMore Details: {error}")

    class LoadingMenu(Registry):
        def __init__(self):
            self.splash_text_path = f"{Registry.base_path}/src/data files/splash_text.txt"
            self.splash_text_path = path_utils.Path(self.splash_text_path).path

            with open(
                    self.splash_text_path,
                    "r",
                    encoding="utf-8") as file:

                self.splash_text = file.readlines()

            self.splash = self.splash_text[random.randint(0, len(self.splash_text)-1)].strip()

            self.splash_text_size = Registry.fonts.get_text_size(self.splash, 30)

            image_path = path_utils.Path(
                f"{Registry.base_path}/temporary/last_scene.png").path

            try:
                self.tex2 = moderngl_window.WindowConfig.load_texture_2d(
                    Registry.wnd,
                    path=image_path,
                    mipmap=True)
            except:
                self.tex2 = False

        def draw(self):
            Registry.hud.canvas.fill([255, 0, 255, 0])

            rect = pygame.Rect(25, 25, Registry.display_size[0]-50, Registry.display_size[1]-50)
            pygame.draw.rect(Registry.hud.canvas, (30, 30, 30, 100), rect, border_radius=10)
            pygame.draw.rect(Registry.hud.canvas, (80, 80, 80, 100), rect, width=1, border_radius=10)

            content_y_position = (Registry.display_size[1]-Registry.menu_resources.logo.get_height())/2

            Registry.hud.canvas.blit(
                Registry.menu_resources.logo,
                ((Registry.display_size[0]-Registry.menu_resources.logo.get_width())/2,
                    (Registry.display_size[1]-Registry.menu_resources.logo.get_height())/2))

            content_y_position += Registry.menu_resources.logo.get_height()

            content_y_position += self.splash_text_size[1]

            Registry.fonts.render_text(
                self.splash,
                30,
                fg_color=Registry.themes.font_color,
                position=[text_utils.CENTERED, content_y_position],
                wrap=False,
                surface=Registry.hud.canvas)

else:
    MESSAGE = "You need to run this as part of Pycraft, please run the 'main.py' file"
    print(MESSAGE)
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Fail",
        MESSAGE)
