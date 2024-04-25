if __name__ != "__main__":
    try:
        import math

        import numpy
        import pyrr

        from registry_utils import Registry

        import math_utils
    except Exception as error:
        from tkinter import messagebox

        messagebox.showerror(
            "Unable to start Pycraft",
            f"A problem occurred whilst trying to start Pycraft (shadow_mapping_utils.py).\nMore Details: {error}")

    TIME_STRETCH_CONSTANT = 190.98593171
    TIME_DISPLACEMENT = math.pi / 2

    class shadowmapping_mathematics(Registry):
        def compute_celestial_entities(
                sun_prog,
                moon_prog,
                scene_pos,
                projection_matrix,
                matrix,
                position):

            stretched_time = Registry.game_time / TIME_STRETCH_CONSTANT

            if Registry.game_time >= 1056:
                Registry.game_time = 0
                Registry.day += 1

            sun_pos = [
                math.sin(stretched_time-TIME_DISPLACEMENT)*Registry.render_distance,
                math.cos(stretched_time-TIME_DISPLACEMENT)*Registry.render_distance
            ]

            sun_lightpos = numpy.array(
                (sun_pos[0] + position.x,
                    sun_pos[1] + position.y,
                    0),
                dtype="f4")

            moon_pos = [
                math.sin(stretched_time+math.pi-TIME_DISPLACEMENT)*Registry.render_distance,
                math.cos(stretched_time+math.pi-TIME_DISPLACEMENT)*Registry.render_distance
            ]

            moon_lightpos = numpy.array(
                (moon_pos[0] + position.x,
                    moon_pos[1] + position.y,
                    0),
                dtype="f4")

            sun_prog["m_proj"].write(projection_matrix)
            sun_prog["m_camera"].write(matrix)
            sun_prog["m_model"].write(
                pyrr.Matrix44.from_translation(
                    sun_lightpos + scene_pos,
                    dtype="f4"))

            moon_prog["m_proj"].write(projection_matrix)
            moon_prog["m_camera"].write(matrix)
            moon_prog["m_model"].write(
                pyrr.Matrix44.from_translation(
                    moon_lightpos + scene_pos,
                    dtype="f4"))

            return sun_lightpos, moon_lightpos

        def compute_shadows(
                mvp,
                light,
                sun_lightpos,
                mvp_depth,
                mvp_shadow,
                bias_matrix,
                projection,
                matrix,
                target,
                up):

            mvp[0].write(projection.astype("f4").tobytes())
            mvp[1].write(matrix.astype("f4").tobytes())

            # build light camera
            light.value = tuple(sun_lightpos)

            sun_light_look_at = math_utils.look_at(
                sun_lightpos,
                target,
                up)

            # light projection matrix (scene dependant)
            light_proj = math_utils.perspective_fov(
                90.0 / 2,
                Registry.aspect_ratio,
                0.01,
                2000.0)

            # light model view projection matrix
            mvp_light = math_utils.multiply(
                light_proj,
                sun_light_look_at)

            # send uniforms to shaders
            mvp_depth[0].write(bias_matrix.astype("f4").tobytes())
            mvp_depth[1].write(mvp_light.astype("f4").tobytes())
            mvp_shadow.write(mvp_light.astype("f4").tobytes())

else:
    print("You need to run this as part of Pycraft")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
