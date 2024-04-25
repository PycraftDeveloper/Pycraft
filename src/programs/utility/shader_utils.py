if __name__ != "__main__":
    try:
        import moderngl_window

        from registry_utils import Registry

        import path_utils
    except Exception as error:
        from tkinter import messagebox

        messagebox.showerror(
            "Unable to start Pycraft",
            f"A problem occurred whilst trying to start Pycraft (shader_utils.py).\nMore Details: {error}")

    class load_programs(Registry):
        def load_program_files(self):
            shader_path = f"{Registry.base_path}/src/shaders"

            depth_prog_path = path_utils.Path(f"{shader_path}/raw_depth.glsl").path
            depth_prog = moderngl_window.WindowConfig.load_program(
                Registry.wnd,
                path=depth_prog_path)

            shadowmap_path = path_utils.Path(f"{shader_path}/shadowmap.glsl").path
            shadowmap = moderngl_window.WindowConfig.load_program(
                Registry.wnd,
                path=shadowmap_path)

            sun_prog_path = path_utils.Path(f"{shader_path}/orbital_prog.glsl").path
            sun_prog = moderngl_window.WindowConfig.load_program(
                Registry.wnd,
                path=sun_prog_path)

            moon_prog_path = path_utils.Path(f"{shader_path}/orbital_prog.glsl").path
            moon_prog = moderngl_window.WindowConfig.load_program(
                Registry.wnd,
                path=moon_prog_path)

            skysphere_prog_path = path_utils.Path(f"{shader_path}/skysphere.glsl").path
            skysphere_prog = moderngl_window.WindowConfig.load_program(
                Registry.wnd,
                path=skysphere_prog_path)

            clouds_prog_path = path_utils.Path(f"{shader_path}/cloud_layer.glsl").path
            clouds_prog = moderngl_window.WindowConfig.load_program(
                Registry.wnd,
                path=clouds_prog_path)

            ocean_prog_path = path_utils.Path(f"{shader_path}/ocean.glsl").path
            ocean_prog = moderngl_window.WindowConfig.load_program(
                Registry.wnd,
                path=ocean_prog_path)

            return (depth_prog,
                        shadowmap,
                        sun_prog,
                        moon_prog,
                        skysphere_prog,
                        clouds_prog,
                        ocean_prog)

else:
    print("You need to run this as part of Pycraft")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
