print("Loaded <Pycraft_main>")


class Startup:
    def __init__(self):
        try:
            # [self]
            # mod
            # (module)
            # (module name)
            # (subsection of module)
            # (name references)
            from PIL import Image
            self.mod_PIL_Image_ = Image
            from PIL import ImageFilter
            self.mod_PIL_ImageFilter_ = ImageFilter
            from moderngl_window.scene.camera import KeyboardCamera
            self.mod_ModernGL_window_keyboard_camera = KeyboardCamera
            from matplotlib import cm
            self.mod_matplotlib_cm_ = cm
            from pyjoystick.sdl2 import run_event_loop
            self.mod_pyjoystick_run_event_loop_ = run_event_loop
            from pyrr import Matrix44, Vector3, matrix44
            self.mod_pyrr_Matrix44_ = Matrix44
            self.mod_pyrr_Vector3_ = Vector3
            self.mod_pyrr_matrix44_ = matrix44
            from tkinter import messagebox
            self.mod_tkinter_messagebox_ = messagebox
            from typing import Final
            
            import GPUtil
            self.mod_GPUtil__ = GPUtil
            import cpuinfo
            self.mod_cpuinfo__ = cpuinfo
            import ctypes
            self.mod_ctypes__ = ctypes
            import datetime
            self.mod_datetime__ = datetime
            import json
            self.mod_json__ = json
            import math
            self.mod_math__ = math
            import moderngl
            self.mod_ModernGL__ = moderngl
            import moderngl_window
            self.mod_ModernGL_window_ = moderngl_window
            import moderngl_window.geometry as geometry
            self.mod_ModernGL_window_geometry = geometry
            import moderngl_window.screenshot as screenshot
            self.mod_ModernGL_window_screenshot = screenshot
            import numpy
            self.mod_numpy__ = numpy
            import os
            self.mod_OS__ = os
            import platform
            self.mod_platform__ = platform
            import psutil
            self.mod_psutil__ = psutil
            import pyautogui
            self.mod_pyautogui__ = pyautogui
            import pygame
            self.mod_pygame__ = pygame
            import pyjoystick
            self.mod_pyjoystick__ = pyjoystick
            import random
            self.mod_random__ = random
            import subprocess
            self.mod_subprocess__ = subprocess
            import sys
            self.mod_sys__ = sys
            import threading
            self.mod_threading__ = threading
            import time
            self.mod_time__ = time
            import timeit
            self.mod_timeit__ = timeit
            import tkinter as tk
            self.mod_tkinter__tk = tk
            import traceback
            self.mod_traceback__ = traceback
            import typing
            self.mod_typing_Final = Final
            self.mod_typing__ = typing

            self.mod_urllib_request_ = None

            moderngl.create_standalone_context()

            os.environ["SDL_VIDEO_CENTERED"] = "1"

            self.mod_pygame__.init()

            self.base_folder = os.path.dirname(__file__)

            ImportPackagesAsUsual = True

            if ("site-packages" in self.base_folder or
                    "dist-packages" in self.base_folder):
                ImportPackagesAsUsual = False

            if ImportPackagesAsUsual:
                import Achievements
                import Benchmark
                import CaptionUtils
                import CharacterDesigner
                import Credits
                import DisplayUtils
                import DrawingUtils
                import ErrorUtils
                import ExtendedBenchmark
                import FileUtils
                import GameEngineUtils
                import GLWindowUtils
                import HomeScreen
                import ImageUtils
                import Installer_main
                import IntegratedInstaller
                import Inventory
                import JoystickUtils
                import main
                import MapGUI
                import PycraftStartupTest
                import Settings
                import ShareDataUtils
                import SoundUtils
                import StartupAnimation
                import TextUtils
                import ThemeUtils
                import ThreadingUtils
                import TkinterUtils

            else:
                from pycraft import Achievements
                from pycraft import Benchmark
                from pycraft import CaptionUtils
                from pycraft import CharacterDesigner
                from pycraft import Credits
                from pycraft import DisplayUtils
                from pycraft import DrawingUtils
                from pycraft import ErrorUtils
                from pycraft import ExtendedBenchmark
                from pycraft import FileUtils
                from pycraft import GameEngineUtils
                from pycraft import GLWindowUtils
                from pycraft import HomeScreen
                from pycraft import ImageUtils
                from pycraft import Installer_main
                from pycraft import IntegratedInstaller
                from pycraft import Inventory
                from pycraft import JoystickUtils
                from pycraft import main
                from pycraft import MapGUI
                from pycraft import PycraftStartupTest
                from pycraft import Settings
                from pycraft import ShareDataUtils
                from pycraft import SoundUtils
                from pycraft import StartupAnimation
                from pycraft import TextUtils
                from pycraft import ThemeUtils
                from pycraft import ThreadingUtils
                from pycraft import TkinterUtils

            self.mod_achievements__ = Achievements
            self.mod_base__ = GLWindowUtils
            self.mod_benchmark__ = Benchmark
            self.mod_caption_utils__ = CaptionUtils
            self.mod_character_designer__ = CharacterDesigner
            self.mod_credits__ = Credits
            self.mod_display_utils__ = DisplayUtils
            self.mod_drawing_utils__ = DrawingUtils
            self.mod_error_utils__ = ErrorUtils
            self.mod_extended_benchmark__ = ExtendedBenchmark
            self.mod_file_utils__ = FileUtils
            self.mod_game_engine_utils__ = GameEngineUtils
            self.mod_globals__ = ShareDataUtils
            self.mod_home_screen__ = HomeScreen
            self.mod_image_utils__ = ImageUtils
            self.mod_installer__ = Installer_main
            self.mod_integrated_installer__ = IntegratedInstaller
            self.mod_inventory__ = Inventory
            self.mod_joystick_utils__ = JoystickUtils
            self.mod_main__ = main
            self.mod_map_GUI__ = MapGUI
            self.mod_pycraft_startup_test__ = PycraftStartupTest
            self.mod_settings__ = Settings
            self.mod_sound_utils__ = SoundUtils
            self.mod_startup_animation__ = StartupAnimation
            self.mod_text_utils__ = TextUtils
            self.mod_theme_utils__ = ThemeUtils
            self.mod_threading_utils__ = ThreadingUtils
            self.mod_tkinter_utils__ = TkinterUtils

            CurrentTime = self.mod_datetime__.datetime.now()
            EventThread = self.mod_threading__.Event()
            
            self.FOV = 70
            self.FPS = 60
            self.FPS_overclock = False
            self.aFPS = 0
            self.aa = True
            self.accent_color = (237, 125, 49)
            self.animate_logo = False
            self.background_color = [30, 30, 30]
            self.camera = None
            self.camera_angle_speed = 3.5
            self.camera_enabled = True
            self.clock = pygame.time.Clock()
            self.command = None
            self.connection_permission = None
            self.connection_status = False
            self.crash = False
            self.ctx = 0
            self.current_date = "".join((f"{CurrentTime.day}/",
                                         f"{CurrentTime.month}/",
                                         f"{CurrentTime.year}"))
            self.current_memory_usage = 0
            self.current_resource_check_time = 0
            self.current_time = CurrentTime
            self.currently_displaying_message = False
            self.currently_playing = None#
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
            self.fullscreen_x = pyautogui.size()[0]
            self.fullscreen_y = pyautogui.size()[1]
            self.game_engine_control = [[False, False],
                                        [False, False],
                                        [False, False],
                                        [False, False]]
            self.game_engine_variables = None
            self.game_error = None
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
            self.last_run = "29/09/2021"
            self.load_3D = True
            self.load_music = True
            self.load_time = [0, 1]
            self.mouse_button_down = False
            self.mouse_x = 0
            self.mouse_y = 0
            self.movement_speed = 1
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
            self.resource_check_time = [0, 0]
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
            self.stop_thread_event = EventThread
            self.theme = False
            self.timer = 0
            self.total_move_x = 0
            self.total_move_y = 0
            self.total_move_z = 0
            self.total_number_of_updates = 0
            self.total_vertices = 0
            self.updated = False
            self.use_mouse_input = True
            self.version = "9.5.1"
            self.wnd = None
            self.x = 0
            self.y = 0
            self.z = 0

            if self.platform == "Linux":
                self.title_font = self.mod_pygame__.font.Font(
                    self.mod_OS__.path.join(
                        self.base_folder,
                        ("fonts//Book Antiqua.ttf")), 60)

                self.window_icon = self.mod_pygame__.image.load(
                    self.mod_OS__.path.join(
                        self.base_folder,
                        ("resources//general resources//Icon.png")))

            else:
                self.window_icon = self.mod_pygame__.image.load(
                    self.mod_OS__.path.join(
                        self.base_folder,
                        ("resources\\general resources\\Icon.png")))

                self.title_font = self.mod_pygame__.font.Font(
                    self.mod_OS__.path.join(
                        self.base_folder,
                        ("fonts\\Book Antiqua.ttf")), 60)

            # Will remove all FPS limits in game, no way to set to 'True' in game for now.
            # False by default!

            if self.FPS_overclock:
                input("".join(("You are entering an unlimited FPS mode; ",
                               "press enter to continue at your own risk.")))

            LongThreadTarget = self.mod_threading_utils__.ThreadingUtils.StartVariableChecking
            self.thread_start_long_thread = self.mod_threading__.Thread(
                target=LongThreadTarget,
                args=(self,))
            self.thread_start_long_thread.daemon = True
            self.thread_start_long_thread.start()
            self.thread_start_long_thread.name = "Thread_VariableControl"

            CPUloggingTarget = self.mod_threading_utils__.ThreadingUtils.StartCPUlogging
            self.thread_get_CPU_metrics = self.mod_threading__.Thread(
                target=CPUloggingTarget,
                args=(self,))
            self.thread_get_CPU_metrics.daemon = True
            self.thread_get_CPU_metrics.start()
            self.thread_get_CPU_metrics.name = "thread_get_CPU_metrics"

            AdaptiveTarget = self.mod_threading_utils__.ThreadingUtils.AdaptiveMode
            self.thread_adaptive_mode = self.mod_threading__.Thread(
                target=AdaptiveTarget,
                args=(self,))
            self.thread_adaptive_mode.daemon = True
            self.thread_adaptive_mode.start()
            self.thread_adaptive_mode.name = "thread_adaptive_mode"

            JoystickEventTarget = self.mod_joystick_utils__.EstablishJoystickConnection.JoystickEvents
            self.thread_joystick_events = self.mod_threading__.Thread(
                target=JoystickEventTarget,
                args=(self,))
            self.thread_joystick_events.daemon = True
            self.thread_joystick_events.start()
            self.thread_joystick_events.name = "thread_joystick_events"

            JoystickIOtarget = self.mod_joystick_utils__.EstablishJoystickRemoved.JoystickRemoved
            self.thread_joystick_removed = self.mod_threading__.Thread(
                target=JoystickIOtarget,
                args=(self,))
            self.thread_joystick_removed.daemon = True
            self.thread_joystick_removed.start()
            self.thread_joystick_removed.name = "thread_joystick_removed"

            self.mod_globals__.Share.initialize(self)

            self.mod_globals__.Share.initialize_controller_game(
                self)

            if ("site-packages" in self.base_folder or
                    "dist-packages" in self.base_folder):
                try:
                    from pycraft import GameEngine
                    self.mod_game_engine__ = GameEngine
                except:
                    import GameEngine
                    self.mod_game_engine__ = GameEngine
            else:
                import GameEngine
                self.mod_game_engine__ = GameEngine
        except Exception as Message:
            try:
                import sys
                import tkinter as tk
                from tkinter import messagebox
                root = tk.Tk()
                root.withdraw()
                messagebox.showerror(
                    "Startup Fail",
                    str(Message))
                sys.exit()
            except Exception as Message:
                print(Message)
                sys.exit()


class Initialize:
    def MenuSelector(self):
        try:
            if self.SharedData.from_play:
                self = self.SharedData
                self.mod_pygame__.display.quit()
                self.mod_pygame__.display.init()
                self.mod_display_utils__.displayUtils.set_display(
                    self)
        except:
            pass

        try:
            while True:
                if self.mod_pygame__.mixer.Channel(1).get_busy() == 1:
                    self.mod_pygame__.mixer.Channel(1).stop()
                if self.mod_pygame__.mixer.Channel(2).get_busy() == 1:
                    self.mod_pygame__.mixer.Channel(2).stop()
                if self.mod_pygame__.mixer.Channel(3).get_busy() == 1:
                    self.mod_pygame__.mixer.Channel(3).stop()
                if self.mod_pygame__.mixer.Channel(4).get_busy() == 1:
                    self.mod_pygame__.mixer.Channel(4).stop()
                if self.mod_pygame__.mixer.music.get_busy() == 0:
                    self.mod_pygame__.mixer.music.unpause()

                self.mouse_x = self.real_window_width/2
                self.mouse_y = self.real_window_height/2
                self.startup_animation = True
                self.run_timer = 0
                self.go_to = None
                self.mouse_button_down = False

                if self.command == "saveANDexit":
                    self.mod_file_utils__.LoadSaveFiles.SaveTOconfigFILE(
                        self)
                    if self.error_message is not None:
                        self.mod_error_utils__.GenerateErrorScreen.ErrorScreen(
                            self)

                    self.mod_pygame__.quit()
                    self.mod_sys__.exit()

                    continue

                elif self.command == "Credits":
                    self.mod_credits__.GenerateCredits.Credits(
                        self)
                    self.command = "Undefined"
                    continue

                elif self.command == "Achievements":
                    self.mod_achievements__.GenerateAchievements.Achievements(
                        self)
                    self.command = "Undefined"

                elif self.command == "CharacterDesigner":
                    self.mod_character_designer__.GenerateCharacterDesigner.CharacterDesigner(
                        self)
                    self.command = "Undefined"
                    continue

                elif self.command == "Settings":
                    self.mod_settings__.GenerateSettings.settings(
                        self)
                    self.command = "Undefined"
                    continue

                elif self.command == "Benchmark":
                    self.mod_benchmark__.GenerateBenchmarkMenu.Benchmark(
                        self)
                    self.command = "Undefined"
                    continue

                elif self.command == "Play":
                    self.mod_pygame__.mixer.music.pause()
                    self.mod_game_engine__.CreateEngine.Play(
                        self)
                    continue

                elif self.command == "Inventory":
                    self.mod_inventory__.GenerateInventory.Inventory(
                        self)
                    self.command = "Play"
                    continue

                elif self.command == "MapGUI":
                    self.mod_map_GUI__.GenerateMapGUI.MapGUI(
                        self)
                    self.command = "Play"
                    continue

                elif self.command == "Installer":
                    self.mod_pygame__.display.quit()
                    self.mod_installer__.RunInstaller.Initialize()
                    self.mod_sys__.exit()

                elif self.error_message is not None:
                    self.mod_error_utils__.GenerateErrorScreen.ErrorScreen(
                        self)
                    continue

                else:
                    self.command = "Undefined"
                    self.command = self.mod_home_screen__.GenerateHomeScreen.Home_Screen(
                        self)
                    continue
        except Exception as Message:
            self.error_message = "".join(("main > Initialize > ",
                                         f"MenuSelector: {str(Message)}"))

            self.error_message_detailed = "".join(
                self.mod_traceback__.format_exception(
                    None,
                    Message,
                    Message.__traceback__))

            self.mod_error_utils__.GenerateErrorScreen.ErrorScreen(
                self)

    def Start():
        global self
        self = Startup()
        try:
            self.mod_file_utils__.LoadSaveFiles.ReadMainSave(
                self)
        except Exception as Message:
            self.mod_file_utils__.LoadSaveFiles.RepairLostSave(
                self)
            ErrorString = "".join(("Unable to access saved data, we have attempted ",
                                   f"to repair the missing data, please try again\n\n{Message}"))
            self.error_message = f"main: {ErrorString}"
            self.mod_error_utils__.GenerateErrorScreen.ErrorScreen(
                self)

        self.mod_file_utils__.FixInstaller.Getinstall_location(
            self)
        if self.install_location is None:
            self.mod_file_utils__.FixInstaller.Setinstall_location(
                self)

        if self.connection_permission is None:
            self.mod_tkinter_utils__.TkinterInfo.GetPermissions(
                self)

        if (self.current_date != self.last_run or
                self.crash):
            self.get_outdated = [False, True]
            if self.connection_permission:
                import urllib.request
                self.mod_urllib_request_ = urllib.request
                self.connection_status = self.mod_integrated_installer__.CheckConnection.test(
                    self)

                if self.connection_status:
                    self.Thread_Get_outdated = self.mod_threading__.Thread(
                        target=self.mod_integrated_installer__.IntegInstaller.CheckVersions,
                        args=(self,))

                    self.Thread_Get_outdated.daemon = True
                    self.Thread_Get_outdated.start()
                    self.Thread_Get_outdated.name = "Thread_Get_outdated"

        self.mod_display_utils__.displayUtils.set_display(
            self)
        if self.error_message is not None:
            self.mod_error_utils__.GenerateErrorScreen.ErrorScreen(
                self)

        self.mod_pycraft_startup_test__.StartupTest.PycraftSelfTest(
            self)
        if self.error_message is not None:
            self.mod_error_utils__.GenerateErrorScreen.ErrorScreen(
                self)

        if self.theme is False:
            self.mod_theme_utils__.DetermineThemeColours.GetThemeGUI(
                self)
            if self.error_message is not None:
                self.mod_error_utils__.GenerateErrorScreen.ErrorScreen(
                    self)

        self.mod_theme_utils__.DetermineThemeColours.GetColours(
            self)
        if self.error_message is not None:
            self.mod_error_utils__.GenerateErrorScreen.ErrorScreen(
                self)

        self.mod_pygame__.mouse.set_visible(False)
        self.mod_startup_animation__.GenerateStartupScreen.Start(
            self)
        self.mod_pygame__.mouse.set_visible(True)

        if self.error_message is not None:
            self.mod_error_utils__.GenerateErrorScreen.ErrorScreen(
                self)

        Initialize.MenuSelector(self)


if __name__ == "__main__":
    print("Started <Pycraft_main>")

    import sys
    try:
        import psutil
    except Exception as Message:
        import tkinter as tk
        from tkinter import messagebox
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror(
            "Startup Fail",
            str(Message))

        sys.exit()
    else:
        try:
            counter = 0
            for proc in psutil.process_iter(["pid", "name", "username"]):
                if "pycraft.exe" in str(proc.info["name"]).lower():
                    counter += 1

            if counter >= 2:
                sys.exit()

            Initialize.Start()
        except Exception as Message:
            import tkinter as tk
            from tkinter import messagebox
            root = tk.Tk()
            root.withdraw()
            messagebox.showerror(
                "Startup Fail",
                str(Message))

            sys.exit()


def QueryVersion():
    return "pycraft v9.5.1"


def start():
    print("Started <Pycraft_main>")
    Initialize.Start()
