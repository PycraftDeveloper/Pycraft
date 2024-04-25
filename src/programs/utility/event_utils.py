if __name__ != "__main__":
    try:
        import pygame

        from registry_utils import Registry

        import logging_utils
        import camera_utils
        import menu_utils
    except Exception as error:
        from tkinter import messagebox

        messagebox.showerror(
            "Unable to start Pycraft",
            f"A problem occurred whilst trying to start Pycraft (event_utils.py).\nMore Details: {error}")

    class EventsManager(Registry):
        def __init__(self) -> None:
            self.control_pressed = False

        def handle(self) -> list[list, bool]:
            Registry.display_size = pygame.display.get_window_size()
            Registry.ctx.viewport = (0, 0, *pygame.display.get_window_size())
            events = pygame.event.get()
            close = False

            if Registry.in_hud is False:
                Registry.spin = False

            for event in events:
                if event.type == pygame.QUIT:
                    close = True

                elif event.type == pygame.KEYDOWN:
                    if event.key == Registry.input_configuration["keyboard"]["back"]:
                        close = True

                    if event.key == Registry.input_configuration["keyboard"]["toggle full-screen"]:
                        Registry.update_graphics = True
                        Registry.displays.toggle_fullscreen()
                        Registry.ctx.viewport = (0, 0, *pygame.display.get_window_size())

                    if (event.key == Registry.input_configuration["keyboard"]["skip time"] and
                            Registry.developer_mode):

                        Registry.time_offset += 30

                    if (event.key == Registry.input_configuration["keyboard"]["increase speed"] and
                            Registry.developer_mode):

                        Registry.increase_speed = not Registry.increase_speed

                    if Registry.in_hud:
                        if event.key == Registry.input_configuration["keyboard"]["toggle rotation"]:
                            Registry.spin = not Registry.spin

                    else:
                        if event.key == Registry.input_configuration["keyboard"]["walk forwards"]:
                            camera_utils.compute_camera.camera_move_state(
                                Registry.FORWARD,
                                True)

                        if event.key == Registry.input_configuration["keyboard"]["walk backwards"]:
                            camera_utils.compute_camera.camera_move_state(
                                Registry.BACKWARD,
                                True)

                        if event.key == Registry.input_configuration["keyboard"]["walk left"]:
                            camera_utils.compute_camera.camera_move_state(
                                Registry.LEFT,
                                True)

                        if event.key == Registry.input_configuration["keyboard"]["walk right"]:
                            camera_utils.compute_camera.camera_move_state(
                                Registry.RIGHT,
                                True)

                        if event.key == Registry.input_configuration["keyboard"]["unlock mouse"]:
                            pygame.event.set_grab(not pygame.event.get_grab())
                            pygame.mouse.set_visible(not pygame.event.get_grab())

                        if event.key == Registry.input_configuration["keyboard"]["pause music"]:
                            if pygame.mixer.music.get_busy():
                                pygame.mixer.music.pause()
                            else:
                                pygame.mixer.music.unpause()

                        if (event.key == Registry.input_configuration["keyboard"]["jump"] and
                            Registry.jump is False):

                            Registry.start_jumping = True

                elif event.type == pygame.KEYUP:
                    if not Registry.in_hud:
                        if event.key == Registry.input_configuration["keyboard"]["walk forwards"]:
                            camera_utils.compute_camera.camera_move_state(
                                Registry.FORWARD,
                                False)

                        if event.key == Registry.input_configuration["keyboard"]["walk backwards"]:
                            camera_utils.compute_camera.camera_move_state(
                                Registry.BACKWARD,
                                False)

                        if event.key == Registry.input_configuration["keyboard"]["walk left"]:
                            camera_utils.compute_camera.camera_move_state(
                                Registry.LEFT,
                                False)

                        if event.key == Registry.input_configuration["keyboard"]["walk right"]:
                            camera_utils.compute_camera.camera_move_state(
                                Registry.RIGHT,
                                False)

                        if event.key == Registry.input_configuration["keyboard"]["jump"]:
                            Registry.start_jumping = False

                elif event.type == pygame.MOUSEMOTION:
                    Registry.mouse_pos = pygame.mouse.get_pos()
                    Registry.update_graphics = True

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    Registry.mouse_button_down = True

                elif event.type == pygame.MOUSEBUTTONUP:
                    Registry.mouse_button_down = False

                elif event.type == pygame.VIDEORESIZE:
                    Registry.menu_resources = menu_utils.MenuResources()
                    Registry.update_graphics = True

            return events, not close

else:
    print("You need to run this as part of Pycraft")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
