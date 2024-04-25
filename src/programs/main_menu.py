if __name__ != "__main__":
    try:
        import time
        import math

        import pygame

        from registry_utils import Registry

        import path_utils
        import sound_utils
    except Exception as error:
        from tkinter import messagebox

        messagebox.showerror(
            "Unable to start Pycraft",
            f"A problem occurred whilst trying to start Pycraft (pycraft_main.py).\nMore Details: {error}")

    class Home(Registry):
        def __init__(self):
            sound_utils.play_sound.play_inventory_sound()
            self.start = time.perf_counter()
            self.alpha = 0

        def draw(self):
            Registry.hud.canvas.fill([255, 0, 255, 0])

            if Registry.in_hud: # temp
                rect = pygame.Rect(25, 25, Registry.display_size[0]-50, Registry.display_size[1]-50)
                pygame.draw.rect(Registry.hud.canvas, (30, 30, 30, 100), rect, border_radius=10)
                pygame.draw.rect(Registry.hud.canvas, (80, 80, 80, 100), rect, width=1, border_radius=10)

                Registry.hud.canvas.blit(
                    Registry.menu_resources.logo,
                    ((Registry.display_size[0]-Registry.menu_resources.logo.get_width())/2,
                        (Registry.display_size[1]-Registry.menu_resources.logo.get_height())/2))

        def main(self):
            run = True
            Registry.displays.set_caption("")
            initial_run = True
            Registry.spin = True
            Registry.in_hud = True
            Registry.update_graphics = True
            while run:
                run_start_time = time.perf_counter()
                (events, run) = Registry.events.handle()
                for event in events:
                    if event.type == pygame.VIDEORESIZE:
                        self.logo = Registry.menu_resources.logo

                Registry.hud.update(self.draw, 255)

                if initial_run:
                    initial_run = False

                pygame.display.flip()
                Registry.clock.tick(Registry.fps)
                if Registry.spin:
                    Registry.game_engine.game_run_time += time.perf_counter() - run_start_time

else:
    MESSAGE = "You need to run this as part of Pycraft, please run the 'main.py' file"
    print(MESSAGE)
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Fail",
        MESSAGE)
