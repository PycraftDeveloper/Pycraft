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
                import Registry
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
                from pycraft import Registry
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
            self.mod_registry__ = Registry
            self.mod_settings__ = Settings
            self.mod_sound_utils__ = SoundUtils
            self.mod_startup_animation__ = StartupAnimation
            self.mod_text_utils__ = TextUtils
            self.mod_theme_utils__ = ThemeUtils
            self.mod_threading_utils__ = ThreadingUtils
            self.mod_tkinter_utils__ = TkinterUtils

            self.mod_registry__.generate_registry.registry(self)

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

            general_thread = self.mod_threading_utils__.ThreadingUtils.general_threading_utility
            self.thread_pycraft_general = self.mod_threading__.Thread(
                target=general_thread,
                args=(self,))
            self.thread_pycraft_general.daemon = True
            self.thread_pycraft_general.start()
            self.thread_pycraft_general.name = "thread_pycraft_general"

            JoystickEventTarget = self.mod_joystick_utils__.establish_joystick_connection.joystick_events
            self.thread_joystick_events = self.mod_threading__.Thread(
                target=JoystickEventTarget,
                args=(self,))
            self.thread_joystick_events.daemon = True
            self.thread_joystick_events.start()
            self.thread_joystick_events.name = "thread_joystick_events"

            JoystickIOtarget = self.mod_joystick_utils__.establish_joystick_removed.JoystickRemoved
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
    def menu_selector(self):
        try:
            if self.shared_data.from_play:
                self = self.shared_data
                self.mod_pygame__.display.quit()
                self.mod_pygame__.display.init()
                self.mod_display_utils__.display_utils.set_display(
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
                        self.mod_error_utils__.generate_error_screen.error_screen(
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
                    self.mod_achievements__.generate_achievements.Achievements(
                        self)
                    self.command = "Undefined"

                elif self.command == "CharacterDesigner":
                    self.mod_character_designer__.GenerateCharacterDesigner.CharacterDesigner(
                        self)
                    self.command = "Undefined"
                    continue

                elif self.command == "Settings":
                    self.mod_settings__.GenerateSettings.Settings(
                        self)
                    self.command = "Undefined"
                    continue

                elif self.command == "Benchmark":
                    self.mod_benchmark__.generate_benchmark.Benchmark(
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
                    self.mod_error_utils__.generate_error_screen.error_screen(
                        self)
                    continue

                else:
                    self.command = "Undefined"
                    self.command = self.mod_home_screen__.GenerateHomeScreen.Home_Screen(
                        self)
                    continue
        except Exception as Message:
            self.error_message = "".join(("main > Initialize > ",
                                         f"menu_selector: {str(Message)}"))

            self.error_message_detailed = "".join(
                self.mod_traceback__.format_exception(
                    None,
                    Message,
                    Message.__traceback__))

            self.mod_error_utils__.generate_error_screen.error_screen(
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
            self.mod_error_utils__.generate_error_screen.error_screen(
                self)

        self.mod_file_utils__.FixInstaller.Getinstall_location(
            self)
        if self.install_location is None:
            self.mod_file_utils__.FixInstaller.Setinstall_location(
                self)

        AdaptiveTarget = self.mod_threading_utils__.ThreadingUtils.AdaptiveMode
        self.thread_adaptive_mode = self.mod_threading__.Thread(
            target=AdaptiveTarget,
            args=(self,))
        self.thread_adaptive_mode.daemon = True
        self.thread_adaptive_mode.start()
        self.thread_adaptive_mode.name = "thread_adaptive_mode"

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

        self.mod_display_utils__.display_utils.set_display(
            self)
        if self.error_message is not None:
            self.mod_error_utils__.generate_error_screen.error_screen(
                self)

        self.mod_pycraft_startup_test__.StartupTest.PycraftSelfTest(
            self)
        if self.error_message is not None:
            self.mod_error_utils__.generate_error_screen.error_screen(
                self)

        self.mod_pygame__.mouse.set_visible(False)
        self.mod_startup_animation__.GenerateStartupScreen.Start(
            self)
        self.mod_pygame__.mouse.set_visible(True)

        if self.error_message is not None:
            self.mod_error_utils__.generate_error_screen.error_screen(
                self)

        if self.theme is False:
            self.mod_theme_utils__.determine_theme_colours.get_theme_GUI(
                self)
            if self.error_message is not None:
                self.mod_error_utils__.generate_error_screen.error_screen(
                    self)

        self.mod_theme_utils__.determine_theme_colours.get_colors(
            self)
        if self.error_message is not None:
            self.mod_error_utils__.generate_error_screen.error_screen(
                self)

        Initialize.menu_selector(self)


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
    return "pycraft v9.5.3"


def start():
    print("Started <Pycraft_main>")
    Initialize.Start()
