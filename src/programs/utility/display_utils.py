if __name__ != "__main__":
    try:
        import os

        import pygame
        from PIL import Image

        from registry_utils import Registry

        import image_utils
        import path_utils
    except Exception as error:
        from tkinter import messagebox

        messagebox.showerror(
            "Unable to start LAaMES",
            f"A problem occurred whilst trying to start Pycraft (display_utils.py).\nMore Details: {error}")

    class Display(Registry):
        def set_caption(self, string:str) -> None:
            if string == "":
                pygame.display.set_caption("Pycraft")
            else:
                pygame.display.set_caption(f"Pycraft: {string}")

        def clear_display(self) -> None:
            Registry.displays.display.fill(Registry.themes.background_color)

        def toggle_fullscreen(self) -> None:
            Registry.fullscreen = not Registry.fullscreen

            if Registry.fullscreen:
                size = (0, 0)
                flags = self.flags | pygame.FULLSCREEN
            else:
                size = self.size
                flags = self.flags

            self.display = pygame.display.set_mode(
                size,
                flags=flags,
                vsync=int(self.vsync))

            Registry.display_size = pygame.display.get_window_size()
            Registry.aspect_ratio =  Registry.display_size[0] / Registry.display_size[1]

            Registry.hud.resize()

        def __init__(
                self,
                size=(
                    1280,
                    720),
                borderless=False,
                resizable=True,
                vsync=False,
                fullscreen=False,
                title="Pycraft") -> None:

            os.environ['SDL_VIDEO_CENTERED'] = '1'

            image_path = f"{Registry.base_path}/src/resources/general/icon.png"
            image_path = path_utils.Path(image_path).path

            image = Image.open(image_path)
            image = image_utils.Color(image).color_converter(
                (0, 0, 0, 255),
                Registry.themes.shape_color)

            image = image.resize((
                128,
                128))
            self.icon = image_utils.ImageConverter().pil_image_to_pygame_surface(image, alpha=None)

            pygame.display.set_icon(self.icon)
            pygame.display.set_caption(title)

            flags = pygame.OPENGL|pygame.DOUBLEBUF|pygame.HWSURFACE|pygame.HWACCEL
            if borderless:
                flags = flags or pygame.NOFRAME
            if resizable:
                flags = flags or pygame.RESIZABLE
            if fullscreen:
                flags = flags or pygame.FULLSCREEN
                display_size = (0, 0)
            else:
                display_size = size

            self.display = pygame.display.set_mode(
                display_size,
                flags=flags,
                vsync=int(vsync))

            Registry.display_size = pygame.display.get_window_size()
            Registry.aspect_ratio =  Registry.display_size[0] / Registry.display_size[1]
            self.flags = flags
            self.vsync = vsync
            self.size = size

            self.cached_background = None
            self.cached_radius = None

else:
    print("You need to run this as part of Pycraft")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
