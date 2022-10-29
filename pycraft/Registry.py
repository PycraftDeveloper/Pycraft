if __name__ != "__main__":
    print("Started <Pycraft_Registry>")

    class generate_registry:
        def __init__(self):
            pass

        def registry(self):
            CurrentTime = self.mod_datetime__.datetime.now()
            
            self.FOV = 70
            self.FPS = 60
            self.FPS_overclock = False
            self.aFPS = 0
            self.aa = True
            self.accent_color = (237, 125, 49)
            self.background_color = [30, 30, 30]
            self.camera = None
            self.camera_angle_speed = 3.5
            self.camera_enabled = True
            self.clock = self.mod_pygame__.time.Clock()
            self.command = None
            self.connection_permission = None
            self.connection_status = False
            self.crash = False
            self.ctx = 0
            self.current_date = "".join((f"{CurrentTime.day}/",
                                         f"{CurrentTime.month}/",
                                         f"{CurrentTime.year}"))
            self.current_memory_usage = 0
            self.current_time = CurrentTime
            self.currently_displaying_message = False
            self.data_CPU_usage = []
            self.data_CPU_usage_Max = 1
            self.data_aFPS = []
            self.data_aFPS_Max = 1
            self.data_eFPS = []
            self.data_eFPS_Max = 1
            self.data_memory_usage = []
            self.data_memory_usage_Max = 1
            self.device_connected = False
            self.device_connected_update = False
            self.devmode = 0
            self.display = 0
            self.eFPS = 60
            self.error_message = None
            self.error_message_detailed = None
            self.fancy_graphics = True
            self.fancy_particles = True
            self.font_color = (255, 255, 255)
            self.from_game_GUI = False
            self.from_play = False
            self.fullscreen = False
            self.fullscreen_x = self.mod_pyautogui__.size()[0]
            self.fullscreen_y = self.mod_pyautogui__.size()[1]
            self.game_engine_control = [[False, False],
                                        [False, False],
                                        [False, False],
                                        [False, False]]
            self.get_outdated = [False, False]
            self.go_to = None
            self.install_location = None
            self.iteration = 1
            self.joystick_confirm = False
            self.joystick_confirm_toggle = False
            self.joystick_connected = False
            self.joystick_exit = False
            self.joystick_hat_pressed = False
            self.joystick_mouse = [0, 0]
            self.joystick_reset = False
            self.joystick_zoom = None
            self.save_keys = {"theme": False,
                               "settings_preference": "Medium",
                               "devmode": 0,
                               "AdaptiveFPS": 60,
                               "FPS": 60,
                               "aFPS": 60,
                               "iteration": 1,
                               "FOV": 75,
                               "camera_angle_speed": 3,
                               "aa": True,
                               "render_fog": True,
                               "fancy_graphics": True,
                               "fancy_particles": True,
                               "sound": True,
                               "sound_volume": 75,
                               "music": True,
                               "music_volume": 50,
                               "x": 0,
                               "y": 0,
                               "z": 0,
                               "last_run": "29/09/2021",
                               "run_full_startup": True,
                               "crash": False,
                               "saved_window_width": 1280,
                               "saved_window_height": 720,
                               "fullscreen": True,
                               "connection_permission": None,
                               "updated": True,
                               "load_time": [0, 1],
                               "show_message": False,
                               "show_lightning": False}
            
            self.last_run = "29/09/2021"
            self.load_3D = True
            self.load_music = True
            self.load_time = [0, 1]
            self.mouse_button_down = False
            self.mouse_x = 0
            self.mouse_y = 0
            self.music = True
            self.music_volume = 5
            self.outdated = False
            self.platform = self.mod_platform__.system()
            self.play_time = 0
            self.progress_line = []
            self.progress_message_text = "Initiating"
            self.project_sleeping = False
            self.pygame_device_added_update = False
            self.pygame_device_removed_update = False
            self.real_window_height = 720
            self.real_window_width = 1280
            self.recommended_FPS = 60
            self.render_fog = True
            self.run_full_startup = False
            self.run_timer = 0
            self.saved_window_height = 720
            self.saved_window_width = 1280
            self.secondary_font_color = (100, 100, 100)
            self.settings_preference = "Medium"
            self.shape_color = (80, 80, 80)
            self.show_lightning = False
            self.show_message = True
            self.sound = True
            self.sound_volume = 75
            self.startup_animation = True
            self.theme = False
            self.timer = 0
            self.total_move_x = 0
            self.total_move_y = 0
            self.total_move_z = 0
            self.total_number_of_updates = 0
            self.updated = False
            self.use_mouse_input = True
            self.version = "9.5.2"
            self.window_in_focus = True
            self.wnd = None
            self.x = 0
            self.y = 0
            self.z = 0


else:
    print("You need to run this as part of Pycraft")
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror(
        "Startup Fail",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
