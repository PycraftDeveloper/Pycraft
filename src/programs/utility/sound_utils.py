if __name__ != "__main__":
    try:
        import random

        import pygame

        from registry_utils import Registry

        import path_utils
    except Exception as error:
        from tkinter import messagebox

        messagebox.showerror(
            "Unable to start Pycraft",
            f"A problem occurred whilst trying to start Pycraft (sound_utils.py).\nMore Details: {error}")

    class play_sound(Registry):
        def play_inventory_sound():
            audio_path = f"{Registry.base_path}/src/resources/general/473545__erokia__ambient-wave-compilation-by-erokia.ogg"
            audio_path = path_utils.Path(audio_path).path

            pygame.mixer.music.load(audio_path)

            pygame.mixer.music.set_volume((Registry.music_volume/100)-0.75)
            pygame.mixer.music.play(loops=-1, fade_ms=1500)

        def play_click_sound():
            channel0 = pygame.mixer.Channel(0)
            audio_path = f"{Registry.base_path}/src/resources/general/Click.ogg"
            audio_path = path_utils.Path(audio_path).path

            clickMUSIC = pygame.mixer.Sound(audio_path)

            channel0.set_volume(Registry.sound_volume/100)
            channel0.play(clickMUSIC)
            pygame.time.wait(40)

        def play_footsteps_sound():
            channel1 = pygame.mixer.Channel(1)
            RandomNum = random.randint(0, 5)

            audio_path = f"{Registry.base_path}/src/resources/game engine/GameSounds/footstep/footsteps{RandomNum}.wav"
            audio_path = path_utils.Path(audio_path).path

            Footsteps = pygame.mixer.Sound(audio_path)

            channel1.set_volume(Registry.sound_volume/100)
            channel1.play(Footsteps)

        def play_ambient_sound():
            channel2 = pygame.mixer.Channel(2)
            audio_path = f"{Registry.base_path}/src/resources/game engine/GameSounds/FieldAmb.ogg"
            audio_path = path_utils.Path(audio_path).path

            LoadAmb = pygame.mixer.Sound(audio_path)

            channel2.set_volume(Registry.sound_volume/100)
            channel2.play(LoadAmb)

        def play_thunder_sound():
            channel3 = pygame.mixer.Channel(3)
            RandomNum = random.randint(0, 10)

            audio_path = f"{Registry.base_path}/src/resources/game engine/GameSounds/thunder/thunder{RandomNum}.ogg"
            audio_path = path_utils.Path(audio_path).path

            Thunder = pygame.mixer.Sound(audio_path)

            channel3.set_volume(Registry.sound_volume/100)
            channel3.play(Thunder)

        def play_rain_sound():
            channel4 = pygame.mixer.Channel(4)
            audio_path = f"{Registry.base_path}/src/resources/game engine/GameSounds/rain.ogg"
            audio_path = path_utils.Path(audio_path).path

            Rain = pygame.mixer.Sound(audio_path)

            channel4.set_volume(Registry.sound_volume/100)
            channel4.play(Rain)

else:
    print("You need to run this as part of Pycraft")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
