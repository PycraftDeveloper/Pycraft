if __name__ != "__main__":
    try:
        import pygame
        import moderngl
        import moderngl_window
        from moderngl_window import geometry

        from registry_utils import Registry

        import error_utils
        import path_utils
    except Exception as error:
        from tkinter import messagebox

        messagebox.showerror(
            "Unable to start Pycraft",
            f"A problem occurred whilst trying to start Pycraft (hud_utils.py).\nMore Details: {error}")

    class HUD(moderngl_window.WindowConfig):
        def __init__(self):
            self.pg_texture = Registry.ctx.texture(Registry.display_size, 4)

            texture_shader_path = f"{Registry.base_path}/src/shaders/texture.glsl"
            texture_shader_path = path_utils.Path(texture_shader_path).path
            self.texture_program = self.load_program(texture_shader_path)
            self.quad_fs = geometry.quad_fs()
            self.canvas = pygame.Surface(Registry.display_size, flags=pygame.SRCALPHA)

        def resize(self):
            Registry.display_size = pygame.display.get_window_size()
            Registry.ctx.viewport = (0, 0, *pygame.display.get_window_size())
            self.pg_texture = Registry.ctx.texture(Registry.display_size, 4)
            self.canvas = pygame.Surface(Registry.display_size, flags=pygame.SRCALPHA)

        def update_helper(self, render):
            if Registry.update_graphics:
                Registry.update_graphics = False
                render()
                texture_data = self.canvas.get_view('1')
                self.pg_texture.write(texture_data)

        def update(self, render, alpha, colorkey=(1, 0, 1), render_game_engine=True, background=None):
            if background is None:
                background = Registry.game_engine.texture2
            if background is False:
                do_textured_rendering = False
            else:
                do_textured_rendering = True

            if render_game_engine:
                Registry.game_engine.fbo.clear(1.0, 1.0, 0.0)
            if alpha > 1:
                alpha = alpha/255
            #Registry.ctx.viewport = (0, 0, *pygame.display.get_window_size())
            #Registry.ctx.clear(0, 0, 0)

            #Registry.ctx.front_face = "ccw"

            Registry.ctx.enable(moderngl.BLEND)
            #Registry.ctx.disable(moderngl.DEPTH_TEST)

            # Render background graphics
            self.texture_program['texture0'].value = 3
            self.texture_program['texture1'].value = 4
            self.texture_program["screen_size"].value = Registry.display_size
            self.texture_program["Directions"].value = 16
            self.texture_program["Quality"].value = 4
            self.quad_fs.render(self.texture_program)

            # Render foreground objects
            if render_game_engine:
                Registry.game_engine.render_game_engine()
            Registry.ctx.front_face = "ccw"

            self.pg_texture.use(location=3)
            self.update_helper(render)
            if do_textured_rendering:
                background.use(location=4)
            Registry.ctx.screen.use()
            Registry.ctx.clear(0, 0, 0)
            self.quad_fs.render(self.texture_program)

            Registry.ctx.disable(moderngl.BLEND)

else:
    print("You need to run this as part of Pycraft")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
