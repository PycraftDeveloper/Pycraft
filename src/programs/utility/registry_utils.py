if __name__ != "__main__":
    try:
        import pygame

        import path_utils
    except Exception as error:
        from tkinter import messagebox

        messagebox.showerror(
            "Unable to start Pycraft",
            f"A problem occurred whilst trying to start Pycraft (registry_utils.py).\nMore Details: {error}")

    class Registry:
        # Direction Definitions
        RIGHT = 1
        LEFT = 2
        FORWARD = 3
        BACKWARD = 4
        UP = 5
        DOWN = 6

        # Movement Definitions
        STILL = 0
        POSITIVE = 1
        NEGATIVE = 2

        ask_to_update = True
        anti_aliasing = True
        anti_aliasing_quality = 2
        aspect_ratio = 16/9
        auto_save_frequency = 999999
        root = path_utils.Path(__file__)
        for _ in range(4):
            root.up()
        base_path = root.path
        blurred_background = None
        camera = None
        clock = None
        developer_mode = True
        day = 0
        display_size = [0, 0]
        displays = None
        fancy_particles = True
        fonts = None
        fps = 60
        fullscreen = False
        game_time = 0
        in_hud = True
        increase_speed = False
        input_configuration = {
            "keyboard": {
                "back": pygame.K_ESCAPE,
                "walk forwards": pygame.K_w,
                "walk backwards": pygame.K_s,
                "walk left": pygame.K_a,
                "walk right": pygame.K_d,
                "unlock mouse": pygame.K_l,
                "toggle full-screen": pygame.K_F11,
                "jump": pygame.K_SPACE,
                "skip time": pygame.K_k,
                "increase speed": pygame.K_j,
                "toggle rotation": pygame.K_SPACE,
                "pause music": pygame.K_m
            }
        }
        jump = False
        mouse_button_down = False
        mouse_pos = [640, 360]
        music = True
        music_volume = 100
        online_version = None
        play_time = 0
        position = [0, 0, 0]
        update_graphics = True
        render_distance = 2000
        render_fog = True
        reset_configuration = False
        rotation = [0, 0]
        skip_time = True
        sound = True
        sound_volume = 100
        spin = True
        splash_process = None
        start_jumping = False
        themes = None
        time_offset = 0
        version = "0.0.0"
        weather = "sunny"
        window_size = None
        x = 0
        y = 0
        z = 0

else:
    print("You need to run this as part of Pycraft")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
