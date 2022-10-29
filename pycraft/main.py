print("Loaded <Pycraft_main>")
class Startup:
    def __init__(Class_Startup_variables):
        try:
            # [Class_Startup_variables]
            # mod
            # (module)
            # (module name)
            # (subsection of module)
            # (name references)
            import tkinter as tk
            Class_Startup_variables.mod_Tkinter__tk = tk
            from tkinter import messagebox
            Class_Startup_variables.mod_Tkinter_messagebox_ = messagebox
            from PIL import Image, ImageFilter
            Class_Startup_variables.mod_PIL_Image_ = Image
            Class_Startup_variables.mod_PIL_ImageFilter_ = ImageFilter
            import pygame
            Class_Startup_variables.mod_Pygame__ = pygame
            import numpy
            Class_Startup_variables.mod_Numpy__ = numpy
            import os
            Class_Startup_variables.mod_OS__ = os
            import sys
            Class_Startup_variables.mod_Sys__ = sys
            import random
            Class_Startup_variables.mod_Random__ = random
            import time
            Class_Startup_variables.mod_Time__ = time
            import platform
            Class_Startup_variables.mod_Platform__ = platform
            import moderngl
            Class_Startup_variables.mod_ModernGL__ = moderngl
            import moderngl_window
            Class_Startup_variables.mod_ModernGL_window_ = moderngl_window
            import moderngl_window.geometry as geometry
            Class_Startup_variables.mod_ModernGL_window_Geometry = geometry
            import moderngl_window.screenshot as screenshot
            Class_Startup_variables.mod_ModernGL_window_Screenshot = screenshot
            from moderngl_window.scene.camera import KeyboardCamera
            Class_Startup_variables.mod_ModernGL_window_KeyboardCamera = KeyboardCamera
            import pyautogui
            Class_Startup_variables.mod_Pyautogui__ = pyautogui
            import psutil
            Class_Startup_variables.mod_Psutil__ = psutil
            import timeit
            Class_Startup_variables.mod_Timeit__ = timeit
            import subprocess
            Class_Startup_variables.mod_Subprocess__ = subprocess
            import traceback
            Class_Startup_variables.mod_Traceback__ = traceback
            import datetime
            Class_Startup_variables.mod_Datetime__ = datetime
            import ctypes
            Class_Startup_variables.mod_Ctypes__ = ctypes
            import json
            Class_Startup_variables.mod_JSON__ = json
            import threading
            Class_Startup_variables.mod_Threading__ = threading
            import cpuinfo
            Class_Startup_variables.mod_CPUinfo__ = cpuinfo
            import GPUtil
            Class_Startup_variables.mod_GPUtil__ = GPUtil
            from pyrr import Matrix44, Vector3, matrix44
            Class_Startup_variables.mod_Pyrr_Matrix44_ = Matrix44
            Class_Startup_variables.mod_Pyrr_matrix44_ = matrix44
            Class_Startup_variables.mod_Pyrr_Vector3_ = Vector3
            Class_Startup_variables.mod_urllib_request_ = None
            from pyjoystick.sdl2 import run_event_loop
            Class_Startup_variables.mod_pyjoystick_run_event_loop_ = run_event_loop
            import pyjoystick
            Class_Startup_variables.mod_pyjoystick__ = pyjoystick
            from typing import Final
            Class_Startup_variables.mod_Typing_Final = Final
            import typing
            Class_Startup_variables.mod_Typing__ = typing
            import math
            Class_Startup_variables.mod_Math__ = math

            try:
                import noise
                Class_Startup_variables.mod_Noise__= noise

            except Exception as Message:
                print(Message)
                Class_Startup_variables.AddedPerlin = False

            else:
                Class_Startup_variables.AddedPerlin = True

            import numpy
            Class_Startup_variables.mod_Numpy__ = numpy
            from matplotlib import cm
            Class_Startup_variables.mod_Matplotlib_cm_ = cm

            moderngl.create_standalone_context()

            os.environ["SDL_VIDEO_CENTERED"] = "1"

            Class_Startup_variables.mod_Pygame__.init()

            Class_Startup_variables.base_folder = os.path.dirname(__file__)

            ImportPackagesAsUsual = True

            if ("site-packages" in Class_Startup_variables.base_folder or
                    "dist-packages" in Class_Startup_variables.base_folder):
                ImportPackagesAsUsual = False

            if ImportPackagesAsUsual:
                import main
                import PycraftStartupTest
                import StartupAnimation
                import DisplayUtils
                import GetSavedData
                import ThemeUtils
                import HomeScreen
                import SoundUtils
                import DrawingUtils
                import CaptionUtils
                import Credits
                import TkinterUtils
                import Achievements
                import CharacterDesigner
                import Settings
                import Benchmark
                import ExBenchmark
                import GLWindowUtils
                import ShareDataUtils
                import TextUtils
                import Inventory
                import ImageUtils
                import MapGUI
                import ThreadingUtils
                import IntegratedInstaller
                import ErrorUtils
                import Installer_main
                import JoystickUtils
                import GameEngineUtils

            else:
                from pycraft import main
                from pycraft import PycraftStartupTest
                from pycraft import StartupAnimation
                from pycraft import DisplayUtils
                from pycraft import GetSavedData
                from pycraft import ThemeUtils
                from pycraft import HomeScreen
                from pycraft import SoundUtils
                from pycraft import DrawingUtils
                from pycraft import CaptionUtils
                from pycraft import Credits
                from pycraft import TkinterUtils
                from pycraft import Achievements
                from pycraft import CharacterDesigner
                from pycraft import Settings
                from pycraft import Benchmark
                from pycraft import ExBenchmark
                from pycraft import GLWindowUtils
                from pycraft import ShareDataUtils
                from pycraft import TextUtils
                from pycraft import Inventory
                from pycraft import ImageUtils
                from pycraft import MapGUI
                from pycraft import ThreadingUtils
                from pycraft import IntegratedInstaller
                from pycraft import ErrorUtils
                from pycraft import Installer_main
                from pycraft import JoystickUtils
                from pycraft import GameEngineUtils

            Class_Startup_variables.mod_Main__ = main
            Class_Startup_variables.mod_PycraftStartupTest__ = PycraftStartupTest
            Class_Startup_variables.mod_StartupAnimation__ = StartupAnimation
            Class_Startup_variables.mod_DisplayUtils__ = DisplayUtils
            Class_Startup_variables.mod_GetSavedData__ = GetSavedData
            Class_Startup_variables.mod_ThemeUtils__ = ThemeUtils
            Class_Startup_variables.mod_HomeScreen__ = HomeScreen
            Class_Startup_variables.mod_SoundUtils__ = SoundUtils
            Class_Startup_variables.mod_DrawingUtils__ = DrawingUtils
            Class_Startup_variables.mod_CaptionUtils__ = CaptionUtils
            Class_Startup_variables.mod_Credits__ = Credits
            Class_Startup_variables.mod_TkinterUtils__ = TkinterUtils
            Class_Startup_variables.mod_Achievements__ = Achievements
            Class_Startup_variables.mod_CharacterDesigner__ = CharacterDesigner
            Class_Startup_variables.mod_Settings__ = Settings
            Class_Startup_variables.mod_Benchmark__ = Benchmark
            Class_Startup_variables.mod_ExBenchmark__ = ExBenchmark
            Class_Startup_variables.mod_Base__ = GLWindowUtils
            Class_Startup_variables.mod_Globals__ = ShareDataUtils
            Class_Startup_variables.mod_TextUtils__ = TextUtils
            Class_Startup_variables.mod_Inventory__ = Inventory
            Class_Startup_variables.mod_ImageUtils__ = ImageUtils
            Class_Startup_variables.mod_MapGUI__ = MapGUI
            Class_Startup_variables.mod_ThreadingUtil__ = ThreadingUtils
            Class_Startup_variables.mod_IntegInstaller__ = IntegratedInstaller
            Class_Startup_variables.mod_ErrorUtils__ = ErrorUtils
            Class_Startup_variables.mod_Installer__ = Installer_main
            Class_Startup_variables.mod_JoystickUtil__ = JoystickUtils
            Class_Startup_variables.mod_GameEngineUtils__ = GameEngineUtils

            Class_Startup_variables.aa = True
            Class_Startup_variables.AccentCol = (237, 125, 49)
            Class_Startup_variables.AnimateLogo = False
            Class_Startup_variables.aFPS = 0
            Class_Startup_variables.BackgroundCol = [30, 30, 30]
            Class_Startup_variables.camera = None
            Class_Startup_variables.camera_enabled = True
            Class_Startup_variables.cameraANGspeed = 3.5
            Class_Startup_variables.clock = pygame.time.Clock()
            Class_Startup_variables.ctx = 0
            Class_Startup_variables.Command = None
            Class_Startup_variables.ConnectionPermission = None
            Class_Startup_variables.ConnectionStatus = False
            Class_Startup_variables.crash = False

            CurrentTime = Class_Startup_variables.mod_Datetime__.datetime.now()
            Class_Startup_variables.current_time = CurrentTime
            Class_Startup_variables.currentDate = "".join((f"{CurrentTime.day}/",
                                                           f"{CurrentTime.month}/",
                                                           f"{CurrentTime.year}"))

            Class_Startup_variables.CurrentlyDisplayingMessage = False
            Class_Startup_variables.CurrentMemoryUsage = 0
            Class_Startup_variables.CurrentlyPlaying = None
            Class_Startup_variables.CurrentResourceCheckTime = 0

            Class_Startup_variables.Data_aFPS = []
            Class_Startup_variables.Data_aFPS_Max = 1

            Class_Startup_variables.Data_CPUUsE = []
            Class_Startup_variables.Data_CPUUsE_Max = 1

            Class_Startup_variables.Data_eFPS = []
            Class_Startup_variables.Data_eFPS_Max = 1

            Class_Startup_variables.Data_MemUsE = []
            Class_Startup_variables.Data_MemUsE_Max = 1

            Class_Startup_variables.Devmode = 0
            Class_Startup_variables.Pygame_DeviceRemoved_Update = False
            Class_Startup_variables.Pygame_DeviceAdded_Update = False
            Class_Startup_variables.Display = 0
            Class_Startup_variables.DeviceConnected = False
            Class_Startup_variables.DeviceConnected_Update = False
            Class_Startup_variables.eFPS = 60
            Class_Startup_variables.ErrorMessage = None
            Class_Startup_variables.ErrorMessage_detailed = None
            Class_Startup_variables.FancyGraphics = True
            Class_Startup_variables.FanPart = True
            Class_Startup_variables.FontCol = (255, 255, 255)
            Class_Startup_variables.FOV = 70
            Class_Startup_variables.FromPlay = False
            Class_Startup_variables.FromGameGUI = False
            Class_Startup_variables.Fullscreen = False
            Class_Startup_variables.FPS = 60
            Class_Startup_variables.FullscreenX = pyautogui.size()[0]
            Class_Startup_variables.FullscreenY = pyautogui.size()[1]
            Class_Startup_variables.GameEngine_Control = [[False, False],
                                                          [False, False],
                                                          [False, False],
                                                          [False, False]]
            Class_Startup_variables.Game_Engine_variables = None
            Class_Startup_variables.GameError = None
            Class_Startup_variables.GetOutdated = [False, False]
            Class_Startup_variables.GoTo = None
            Class_Startup_variables.Iteration = 1
            Class_Startup_variables.JoystickHatPressed = False
            Class_Startup_variables.InstallLocation = None
            Class_Startup_variables.JoystickConfirm = False
            Class_Startup_variables.JoystickConnected = False
            Class_Startup_variables.JoystickConfirm_toggle = False
            Class_Startup_variables.JoystickExit = False
            Class_Startup_variables.JoystickMouse = [0, 0]
            Class_Startup_variables.JoystickReset = False
            Class_Startup_variables.JoystickZoom = None
            Class_Startup_variables.lastRun = "29/09/2021"
            Class_Startup_variables.Load3D = True
            Class_Startup_variables.LoadMusic = True
            Class_Startup_variables.LoadTime = [0, 1]
            Class_Startup_variables.mousebuttondown = False
            Class_Startup_variables.MovementSpeed = 1
            Class_Startup_variables.music = True
            Class_Startup_variables.musicVOL = 5
            Class_Startup_variables.Mx = 0
            Class_Startup_variables.My = 0
            Class_Startup_variables.Outdated = False
            Class_Startup_variables.FPS_Overclock = False
            # Will remove all FPS limits in game, no way to set to 'True' in game for now.
            # False by default!

            if Class_Startup_variables.FPS_Overclock:
                input("".join(("You are entering an unlimited FPS mode; ",
                               "press enter to continue at your own risk.")))

            Class_Startup_variables.platform = Class_Startup_variables.mod_Platform__.system()
            Class_Startup_variables.PlayTime = 0
            Class_Startup_variables.Project_Sleeping = False
            Class_Startup_variables.Progress_Line = []
            Class_Startup_variables.ProgressMessageText = "Initiating"
            Class_Startup_variables.realHeight = 720
            Class_Startup_variables.realWidth = 1280
            Class_Startup_variables.RecommendedFPS = 60
            Class_Startup_variables.RenderFOG = True
            Class_Startup_variables.RunFullStartup = False
            Class_Startup_variables.RunTimer = 0
            Class_Startup_variables.ResourceCheckTime = [0, 0]
            Class_Startup_variables.StartAnimation = True
            Class_Startup_variables.SecondFontCol = (100, 100, 100)
            Class_Startup_variables.SavedWidth = 1280
            Class_Startup_variables.SavedHeight = 720
            Class_Startup_variables.ShapeCol = (80, 80, 80)
            Class_Startup_variables.ShowMessage = True
            Class_Startup_variables.ShowLightning = False
            Class_Startup_variables.sound = True
            Class_Startup_variables.soundVOL = 75

            EventThread = Class_Startup_variables.mod_Threading__.Event()
            Class_Startup_variables.Stop_Thread_Event = EventThread

            Class_Startup_variables.SettingsPreference = "Medium"
            Class_Startup_variables.theme = False
            Class_Startup_variables.Timer = 0

            if Class_Startup_variables.platform == "Linux":
                Class_Startup_variables.TitleFont = Class_Startup_variables.mod_Pygame__.font.Font(
                    Class_Startup_variables.mod_OS__.path.join(
                        Class_Startup_variables.base_folder,
                        ("Fonts//Book Antiqua.ttf")), 60)

                Class_Startup_variables.WindowIcon = Class_Startup_variables.mod_Pygame__.image.load(
                    Class_Startup_variables.mod_OS__.path.join(
                        Class_Startup_variables.base_folder,
                        ("Resources//General_Resources//Icon.png")))

            else:
                Class_Startup_variables.WindowIcon = Class_Startup_variables.mod_Pygame__.image.load(
                    Class_Startup_variables.mod_OS__.path.join(
                        Class_Startup_variables.base_folder,
                        ("Resources\\General_Resources\\Icon.png")))

                Class_Startup_variables.TitleFont = Class_Startup_variables.mod_Pygame__.font.Font(
                    Class_Startup_variables.mod_OS__.path.join(
                        Class_Startup_variables.base_folder,
                        ("Fonts\\Book Antiqua.ttf")), 60)

            Class_Startup_variables.TotalNumUpdate = 0
            Class_Startup_variables.Total_move_x = 0
            Class_Startup_variables.Total_move_y = 0
            Class_Startup_variables.Total_move_z = 0
            Class_Startup_variables.Total_Vertices = 0
            Class_Startup_variables.UseMouseInput = True
            Class_Startup_variables.wnd = None
            Class_Startup_variables.Updated = False
            Class_Startup_variables.version = "9.5.0"
            Class_Startup_variables.X = 0
            Class_Startup_variables.Y = 0
            Class_Startup_variables.Z = 0

            LongThreadTarget = Class_Startup_variables.mod_ThreadingUtil__.ThreadingUtils.StartVariableChecking
            Class_Startup_variables.Thread_StartLongThread = Class_Startup_variables.mod_Threading__.Thread(
                target=LongThreadTarget,
                args=(Class_Startup_variables,))
            Class_Startup_variables.Thread_StartLongThread.daemon = True
            Class_Startup_variables.Thread_StartLongThread.start()
            Class_Startup_variables.Thread_StartLongThread.name = "Thread_VariableControl"

            CPUloggingTarget = Class_Startup_variables.mod_ThreadingUtil__.ThreadingUtils.StartCPUlogging
            Class_Startup_variables.Thread_GetCPUMetrics = Class_Startup_variables.mod_Threading__.Thread(
                target=CPUloggingTarget,
                args=(Class_Startup_variables,))
            Class_Startup_variables.Thread_GetCPUMetrics.daemon = True
            Class_Startup_variables.Thread_GetCPUMetrics.start()
            Class_Startup_variables.Thread_GetCPUMetrics.name = "Thread_GetCPUMetrics"

            AdaptiveTarget = Class_Startup_variables.mod_ThreadingUtil__.ThreadingUtils.AdaptiveMode
            Class_Startup_variables.Thread_AdaptiveMode = Class_Startup_variables.mod_Threading__.Thread(
                target=AdaptiveTarget,
                args=(Class_Startup_variables,))
            Class_Startup_variables.Thread_AdaptiveMode.daemon = True
            Class_Startup_variables.Thread_AdaptiveMode.start()
            Class_Startup_variables.Thread_AdaptiveMode.name = "Thread_AdaptiveMode"

            JoystickEventTarget = Class_Startup_variables.mod_JoystickUtil__.EstablishJoystickConnection.JoystickEvents
            Class_Startup_variables.Thread_JoystickEvents = Class_Startup_variables.mod_Threading__.Thread(
                target=JoystickEventTarget,
                args=(Class_Startup_variables,))
            Class_Startup_variables.Thread_JoystickEvents.daemon = True
            Class_Startup_variables.Thread_JoystickEvents.start()
            Class_Startup_variables.Thread_JoystickEvents.name = "Thread_JoystickEvents"

            JoystickIOtarget = Class_Startup_variables.mod_JoystickUtil__.EstablishJoystickRemoved.JoystickRemoved
            Class_Startup_variables.Thread_JoystickRemoved = Class_Startup_variables.mod_Threading__.Thread(
                target=JoystickIOtarget,
                args=(Class_Startup_variables,))
            Class_Startup_variables.Thread_JoystickRemoved.daemon = True
            Class_Startup_variables.Thread_JoystickRemoved.start()
            Class_Startup_variables.Thread_JoystickRemoved.name = "Thread_JoystickRemoved"

            Class_Startup_variables.mod_Globals__.Share.initialize(Class_Startup_variables)

            Class_Startup_variables.mod_Globals__.Share.initialize_controller_game(
                Class_Startup_variables)

            if ("site-packages" in Class_Startup_variables.base_folder or
                    "dist-packages" in Class_Startup_variables.base_folder):
                try:
                    from pycraft import GameEngine
                    Class_Startup_variables.mod_MainGameEngine__ = GameEngine
                except:
                    import GameEngine
                    Class_Startup_variables.mod_MainGameEngine__ = GameEngine
            else:
                import GameEngine
                Class_Startup_variables.mod_MainGameEngine__ = GameEngine
        except Exception as Message:
            try:
                import tkinter as tk
                import sys
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
    def MenuSelector(Class_Startup_variables):
        try:
            if Class_Startup_variables.SharedData.FromPlay:
                Class_Startup_variables = Class_Startup_variables.SharedData
                Class_Startup_variables.mod_Pygame__.display.quit()
                Class_Startup_variables.mod_Pygame__.display.init()
                Class_Startup_variables.mod_DisplayUtils__.DisplayUtils.SetDisplay(
                    Class_Startup_variables)
        except:
            pass

        while True:
            if Class_Startup_variables.mod_Pygame__.mixer.Channel(1).get_busy() == 1:
                Class_Startup_variables.mod_Pygame__.mixer.Channel(1).stop()
            if Class_Startup_variables.mod_Pygame__.mixer.Channel(2).get_busy() == 1:
                Class_Startup_variables.mod_Pygame__.mixer.Channel(2).stop()
            if Class_Startup_variables.mod_Pygame__.mixer.Channel(3).get_busy() == 1:
                Class_Startup_variables.mod_Pygame__.mixer.Channel(3).stop()
            if Class_Startup_variables.mod_Pygame__.mixer.Channel(4).get_busy() == 1:
                Class_Startup_variables.mod_Pygame__.mixer.Channel(4).stop()
            if Class_Startup_variables.mod_Pygame__.mixer.music.get_busy() == 0:
                Class_Startup_variables.mod_Pygame__.mixer.music.unpause()

            Class_Startup_variables.Mx = Class_Startup_variables.realWidth/2
            Class_Startup_variables.My = Class_Startup_variables.realHeight/2
            Class_Startup_variables.StartAnimation = True
            Class_Startup_variables.RunTimer = 0
            Class_Startup_variables.GoTo = None
            Class_Startup_variables.mousebuttondown = False

            if Class_Startup_variables.Command == "saveANDexit":
                Class_Startup_variables.mod_GetSavedData__.LoadSaveFiles.SaveTOconfigFILE(
                    Class_Startup_variables)
                if Class_Startup_variables.ErrorMessage is not None:
                    Class_Startup_variables.mod_ErrorUtils__.GenerateErrorScreen.ErrorScreen(
                        Class_Startup_variables)

                Class_Startup_variables.mod_Pygame__.quit()
                Class_Startup_variables.mod_Sys__.exit()

                continue

            elif Class_Startup_variables.Command == "Credits":
                Class_Startup_variables.mod_Credits__.GenerateCredits.Credits(
                    Class_Startup_variables)
                Class_Startup_variables.Command = "Undefined"
                continue

            elif Class_Startup_variables.Command == "Achievements":
                Class_Startup_variables.mod_Achievements__.GenerateAchievements.Achievements(
                    Class_Startup_variables)
                Class_Startup_variables.Command = "Undefined"

            elif Class_Startup_variables.Command == "CharacterDesigner":
                Class_Startup_variables.mod_CharacterDesigner__.GenerateCharacterDesigner.CharacterDesigner(
                    Class_Startup_variables)
                Class_Startup_variables.Command = "Undefined"
                continue

            elif Class_Startup_variables.Command == "Settings":
                Class_Startup_variables.mod_Settings__.GenerateSettings.settings(
                    Class_Startup_variables)
                Class_Startup_variables.Command = "Undefined"
                continue

            elif Class_Startup_variables.Command == "Benchmark":
                Class_Startup_variables.mod_Benchmark__.GenerateBenchmarkMenu.Benchmark(
                    Class_Startup_variables)
                Class_Startup_variables.Command = "Undefined"
                continue

            elif Class_Startup_variables.Command == "Play":
                Class_Startup_variables.mod_Pygame__.mixer.music.pause()
                Class_Startup_variables.mod_MainGameEngine__.CreateEngine.Play(
                    Class_Startup_variables)
                continue

            elif Class_Startup_variables.Command == "Inventory":
                Class_Startup_variables.mod_Inventory__.GenerateInventory.Inventory(
                    Class_Startup_variables)
                Class_Startup_variables.Command = "Play"
                continue

            elif Class_Startup_variables.Command == "MapGUI":
                Class_Startup_variables.mod_MapGUI__.GenerateMapGUI.MapGUI(
                    Class_Startup_variables)
                Class_Startup_variables.Command = "Play"
                continue

            elif Class_Startup_variables.Command == "Installer":
                Class_Startup_variables.mod_Pygame__.display.quit()
                Class_Startup_variables.mod_Installer__.RunInstaller.Initialize()
                Class_Startup_variables.mod_Sys__.exit()


            elif Class_Startup_variables.ErrorMessage is not None:
                Class_Startup_variables.mod_ErrorUtils__.GenerateErrorScreen.ErrorScreen(
                    Class_Startup_variables)
                continue

            else:
                Class_Startup_variables.Command = "Undefined"
                Class_Startup_variables.Command = Class_Startup_variables.mod_HomeScreen__.GenerateHomeScreen.Home_Screen(
                    Class_Startup_variables)
                continue


    def Start():
        global Class_Startup_variables
        Class_Startup_variables = Startup()
        try:
            Class_Startup_variables.mod_GetSavedData__.LoadSaveFiles.ReadMainSave(
                Class_Startup_variables)
        except Exception as Message:
            Class_Startup_variables.mod_GetSavedData__.LoadSaveFiles.RepairLostSave(
                Class_Startup_variables)
            ErrorString = "".join(("Unable to access saved data, we have attempted ",
                                   f"to repair the missing data, please try again\n\n{Message}"))
            Class_Startup_variables.ErrorMessage = f"main: {ErrorString}"
            Class_Startup_variables.mod_ErrorUtils__.GenerateErrorScreen.ErrorScreen(
                Class_Startup_variables)

        Class_Startup_variables.mod_GetSavedData__.FixInstaller.GetInstallLocation(
            Class_Startup_variables)
        if Class_Startup_variables.InstallLocation is None:
            Class_Startup_variables.mod_GetSavedData__.FixInstaller.SetInstallLocation(
                Class_Startup_variables)

        if Class_Startup_variables.ConnectionPermission is None:
            Class_Startup_variables.mod_TkinterUtils__.TkinterInfo.GetPermissions(
                Class_Startup_variables)

        if (Class_Startup_variables.currentDate != Class_Startup_variables.lastRun or
                Class_Startup_variables.crash):
            Class_Startup_variables.GetOutdated = [False, True]
            if Class_Startup_variables.ConnectionPermission:
                import urllib.request
                Class_Startup_variables.mod_urllib_request_ = urllib.request
                Class_Startup_variables.ConnectionStatus = Class_Startup_variables.mod_IntegInstaller__.CheckConnection.test(
                    Class_Startup_variables)

                if Class_Startup_variables.ConnectionStatus:
                    Class_Startup_variables.Thread_Get_Outdated = Class_Startup_variables.mod_Threading__.Thread(
                        target=Class_Startup_variables.mod_IntegInstaller__.IntegInstaller.CheckVersions,
                        args=(Class_Startup_variables,))

                    Class_Startup_variables.Thread_Get_Outdated.daemon = True
                    Class_Startup_variables.Thread_Get_Outdated.start()
                    Class_Startup_variables.Thread_Get_Outdated.name = "Thread_Get_Outdated"

        Class_Startup_variables.mod_DisplayUtils__.DisplayUtils.SetDisplay(
            Class_Startup_variables)
        if Class_Startup_variables.ErrorMessage is not None:
            Class_Startup_variables.mod_ErrorUtils__.GenerateErrorScreen.ErrorScreen(
                Class_Startup_variables)

        Class_Startup_variables.mod_PycraftStartupTest__.StartupTest.PycraftSelfTest(
            Class_Startup_variables)
        if Class_Startup_variables.ErrorMessage is not None:
            Class_Startup_variables.mod_ErrorUtils__.GenerateErrorScreen.ErrorScreen(
                Class_Startup_variables)

        if Class_Startup_variables.theme is False:
            Class_Startup_variables.mod_ThemeUtils__.DetermineThemeColours.GetThemeGUI(
                Class_Startup_variables)
            if Class_Startup_variables.ErrorMessage is not None:
                Class_Startup_variables.mod_ErrorUtils__.GenerateErrorScreen.ErrorScreen(
                    Class_Startup_variables)

        Class_Startup_variables.mod_ThemeUtils__.DetermineThemeColours.GetColours(
            Class_Startup_variables)
        if Class_Startup_variables.ErrorMessage is not None:
            Class_Startup_variables.mod_ErrorUtils__.GenerateErrorScreen.ErrorScreen(
                Class_Startup_variables)

        Class_Startup_variables.mod_Pygame__.mouse.set_visible(False)
        Class_Startup_variables.mod_StartupAnimation__.GenerateStartupScreen.Start(
            Class_Startup_variables)
        Class_Startup_variables.mod_Pygame__.mouse.set_visible(True)

        if Class_Startup_variables.ErrorMessage is not None:
            Class_Startup_variables.mod_ErrorUtils__.GenerateErrorScreen.ErrorScreen(
                Class_Startup_variables)

        Initialize.MenuSelector(Class_Startup_variables)

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
                if proc.info["name"] == "Pycraft.exe":
                    counter += 1

            if counter >= 3:
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
    return "pycraft v9.5.0"

def start():
    print("Started <Pycraft_main>")
    Initialize.Start()
