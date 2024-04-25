if __name__ != "__main__":
    try:
        import multiprocessing
        import sys
        import threading

        import pygame
        import moderngl
        import moderngl_window
        from moderngl_window import geometry

        import main_menu

        from registry_utils import Registry

        import game_engine
        import loading_menu

        import file_utils
        import error_utils
        import directory_utils
        import general_utils
        import text_utils
        import display_utils
        import theme_utils
        import hud_utils
        import event_utils
        import menu_utils
    except Exception as error:
        from tkinter import messagebox

        messagebox.showerror(
            "Unable to start Pycraft",
            f"A problem occurred whilst trying to start Pycraft (pycraft_main.py).\nMore Details: {error}")

    class Startup(Registry):
        def setup(self):
            Registry.ctx = moderngl.create_context(standalone=False)

            Registry.wnd = moderngl_window.get_local_window_cls("pygame2")

            moderngl_window.activate_context(Registry.wnd, Registry.ctx)

        def __init__(self) -> None:
            try:
                pygame.init()

                directory_utils.Check()

                file_utils.Config().read_config()

                Registry.window_size = general_utils.get_window_size()

                Registry.themes = theme_utils.Theme()

                Registry.fonts = text_utils.TextRenderer()
                Registry.events = event_utils.EventsManager()
                Registry.displays = display_utils.Display(fullscreen=Registry.fullscreen)
                Registry.displays.set_caption("Initializing")
                Registry.clock = pygame.time.Clock()
                self.setup()

                '''from line_profiler import LineProfiler
                lp = LineProfiler()
                lp_wrapper = lp(game_engine.create_game_engine().temp)
                lp_wrapper()
                lp.print_stats()'''

                Registry.menu_resources = menu_utils.MenuResources()
                Registry.loading_menu = loading_menu.LoadingMenu()

                Registry.hud = hud_utils.HUD()

                Registry.hud.update(Registry.loading_menu.draw, 255, render_game_engine=False, background=Registry.loading_menu.tex2)

                Registry.game_engine = game_engine.create_game_engine()

                Registry.main_menu = main_menu.Home()
                Registry.main_menu.main()

                general_utils.close()
            except Exception as error:
                error_utils.Error(error=error)

    def init() -> None:
        try:
            Startup()
        except Exception as error:
            error_utils.Error(error=error)

    def get_version() -> str:
        return Registry.version

else:
    MESSAGE = "You need to run this as part of Pycraft, please run the 'main.py' file"
    print(MESSAGE)
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Fail",
        MESSAGE)
