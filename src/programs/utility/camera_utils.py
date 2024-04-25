if __name__ != "__main__":
    try:
        import time

        import numpy

        from registry_utils import Registry

        import math_utils
    except Exception as error:
        from tkinter import messagebox

        messagebox.showerror(
            "Unable to start Pycraft",
            f"A problem occurred whilst trying to start Pycraft (camera_utils.py).\nMore Details: {error}")

    class compute_camera(Registry):
        def camera_move_state(
                direction,
                activate):

            if direction == Registry.RIGHT:
                Registry.camera._xdir = Registry.POSITIVE if activate else Registry.STILL
            if direction == Registry.LEFT:
                Registry.camera._xdir = Registry.NEGATIVE if activate else Registry.STILL
            if direction == Registry.FORWARD:
                Registry.camera._zdir = Registry.NEGATIVE if activate else Registry.STILL
            if direction == Registry.BACKWARD:
                Registry.camera._zdir = Registry.POSITIVE if activate else Registry.STILL
            if direction == Registry.UP:
                Registry.camera._ydir = Registry.POSITIVE if activate else Registry.STILL
            if direction == Registry.DOWN:
                Registry.camera._ydir = Registry.NEGATIVE if activate else Registry.STILL

        def get_camera_values(
                camera_up,
                point_towards=None):

            position = Registry.camera.position

            compute_camera.compute_camera_dir()

            if point_towards is not None:
                cam_matrix = math_utils.gl_look_at(
                    position, numpy.array([*point_towards]), camera_up)
            else:
                cam_matrix = math_utils.gl_look_at(
                    position, position + Registry.camera.dir, camera_up)

            return cam_matrix, position

        def compute_camera_dir():
            # Use separate time in camera so we can move it when paused
            now = time.time()
            # If the camera has been inactive for a while, a large time delta
            # can suddenly move the camera far away from the scene
            t = max(now - Registry.camera._last_time, 0)
            Registry.camera._last_time = now

            # X Movement
            if Registry.camera._xdir == Registry.POSITIVE:
                Registry.camera.position += Registry.camera.right * Registry.camera._velocity * t
            elif Registry.camera._xdir == Registry.NEGATIVE:
                Registry.camera.position -= Registry.camera.right * Registry.camera._velocity * t

            # Z Movement
            if Registry.camera._zdir == Registry.NEGATIVE:
                Registry.camera.position += Registry.camera.dir * Registry.camera._velocity * t
            elif Registry.camera._zdir == Registry.POSITIVE:
                Registry.camera.position -= Registry.camera.dir * Registry.camera._velocity * t

            # Y Movement
            if Registry.camera._ydir == Registry.POSITIVE:
                Registry.camera.position += Registry.camera.up * Registry.camera._velocity * t
            elif Registry.camera._ydir == Registry.NEGATIVE:
                Registry.camera.position -= Registry.camera.up * Registry.camera._velocity * t

else:
    print("You need to run this as part of Pycraft")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
