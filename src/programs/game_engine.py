if __name__ != "__main__":
    try:
        import time
        import typing
        import math
        import random

        import pygame
        import moderngl
        import moderngl_window
        from moderngl_window.scene.camera import KeyboardCamera
        from moderngl_window import geometry
        import numpy
        import pyrr

        from registry_utils import Registry

        import display_utils
        import sound_utils
        import error_utils
        import shader_utils
        import math_utils
        import camera_utils
        import shadow_mapping_utils
        import path_utils
    except Exception as error:
        from tkinter import messagebox

        messagebox.showerror(
            "Unable to start Pycraft",
            f"A problem occurred whilst trying to start Pycraft (game_engine.py).\nMore Details: {error}")

    TIME_STRETCH_CONSTANT = 190.98593171
    TIME_DISPLACEMENT = math.pi / 2

    class create_game_engine(Registry):
        def __init__(self):
            try:
                Registry.wnd.vsync = False

                pygame.display.flip()

                if Registry.anti_aliasing:
                    samples = Registry.anti_aliasing_quality

                else:
                    samples = 1

                Registry.wnd.samples = samples

                Registry.camera = KeyboardCamera(
                    Registry.wnd.keys,
                    aspect_ratio=Registry.aspect_ratio,
                    far=Registry.render_distance,
                    near=0.1)

                Registry.camera.projection.update(
                    near=1,
                    far=Registry.render_distance,
                    fov=70)

                Registry.wnd.mouse_exclusivity = True

                self.sun_radius = 50

                self.sun = geometry.sphere(
                    radius=self.sun_radius)

                self.moon = geometry.sphere(
                    radius=80)

                cloud_layer_size = [Registry.render_distance*2]*2

                self.cloud_layer = geometry.quad_2d(size=cloud_layer_size)
                self.ocean_layer = geometry.quad_2d(size=cloud_layer_size)

                self.sky_sphere = geometry.sphere(
                    radius=Registry.render_distance)

                self.objects: typing.Dict[
                    str,
                    moderngl.VertexArray] = {}

                map_object_path = f"{Registry.base_path}/src/resources/game engine/map/map.obj"
                map_object_path = path_utils.Path(map_object_path).path

                # Use 'u' to do things with UVs that this really needs
                scene: moderngl_window.scene.Scene = moderngl_window.WindowConfig.load_scene(
                    Registry.wnd,
                    path=map_object_path,
                    cache=True)

                sky_sphere_object_path = f"{Registry.base_path}/src/resources/game engine/sky_sphere/ClearSkyTransition.gif"
                sky_sphere_object_path = path_utils.Path(sky_sphere_object_path).path

                self.skysphere_texture = moderngl_window.WindowConfig.load_texture_array(
                    Registry.wnd,
                    path=sky_sphere_object_path,
                    anisotropy=samples)

                # Programs
                (self.depth_prog,
                    self.shadowmap,
                    self.sun_prog,
                    self.moon_prog,
                    self.sky_sphere_prog,
                    self.clouds_prog,
                    self.ocean_prog) = shader_utils.load_programs().load_program_files()

                self.vao = scene.root_nodes[0].mesh.vao
                self.objects["map"] = self.vao.instance(self.shadowmap)

                self.sky_sphere_prog["texture0"].value = 0
                self.sky_sphere_prog["num_layers"].value = 41.0

                self.shadowmap["u_sampler_shadow"].value = 0
                self.shadowmap["grass_color"].value = 1
                self.shadowmap["rock_color"].value = 2

                self.shadowmap["light_level"] = 0.5

                self.mvp = (self.shadowmap["projection_matrix"], self.shadowmap["matrix"])
                self.mvp_depth = (self.shadowmap["bias_matrix"], self.shadowmap["mvp_light"])

                self.light = self.shadowmap["u_light"]
                self.color = self.shadowmap["u_color"]

                self.mvp_shadow = self.depth_prog["u_mvp"]

                self.sun_prog["color"].value = (1.0, 1.0, 0.0, 1.0)
                self.moon_prog["color"].value = (1.0, 1.0, 1.0, 1.0)

                self.color.value = (1.0, 1.0, 1.0)

                grass_texture_path = f"{Registry.base_path}/src/resources/game engine/map/GrassTexture.png"
                grass_texture_path = path_utils.Path(grass_texture_path).path
                rock_texture_path = f"{Registry.base_path}/src/resources/game engine/map/RockTexture.png"
                rock_texture_path = path_utils.Path(rock_texture_path).path

                tex1 = moderngl_window.WindowConfig.load_texture_2d(
                    Registry.wnd,
                    path=grass_texture_path,
                    mipmap=True,
                    anisotropy=samples)

                tex2 = moderngl_window.WindowConfig.load_texture_2d(
                    Registry.wnd,
                    path=rock_texture_path,
                    mipmap=True,
                    anisotropy=samples)

                tex1.use(location=1)
                tex2.use(location=2)

                SHADOW_SIZE: typing.Final[int] = 2 << 7

                shadow_size = (SHADOW_SIZE,
                               SHADOW_SIZE,)

                self.tex_depth = Registry.ctx.depth_texture(shadow_size)

                self.sampler_depth = Registry.ctx.sampler(
                    filter=(moderngl.LINEAR,
                                moderngl.LINEAR),
                    compare_func=">=",
                    repeat_x=False,
                    repeat_y=False,)

                self.shadowmap["render_fog"] = Registry.render_fog
                self.clouds_prog["render_fog"] = Registry.render_fog
                self.ocean_prog["render_fog"] = Registry.render_fog

                self.on_start = True

                self.time_percent = 0
                self.default_skysphere_color = 1.0

                self.target = numpy.array((0, 0, 0), dtype="f4")

                self.up = numpy.array((0, 0, 1), dtype="f4")

                self.scene_pos = numpy.array((0, -5, -32), dtype="f4")

                self.scene_translation = pyrr.Matrix44.from_translation(
                    (0.0, 0.0, 0.0),
                    dtype="f4")

                self.bias_matrix = (
                    pyrr.Matrix44.from_translation(
                        (0.5, 0.5, 0.5),
                        dtype="f4")
                    *
                    pyrr.Matrix44.from_scale(
                        (0.5, 0.5, 0.5),
                        dtype="f4")
                )

                self.shadowmap["w_max"].value = Registry.render_distance
                self.shadowmap["w_min"].value = 1600

                self.clouds_prog["w_max"].value = Registry.render_distance
                self.clouds_prog["w_min"].value = 1000

                self.ocean_prog["w_max"].value = Registry.render_distance
                self.ocean_prog["w_min"].value = 1600

                self.sky_sphere_prog["transparency"] = 1.0

                self.collision = False
                self.increased_speed = False
                self.modifier = 20
                self.base_camera_velocity = Registry.camera.velocity

                self.projection = math_utils.perspective_fov(
                    70,
                    Registry.aspect_ratio,
                    1,
                    Registry.render_distance)

                Registry.camera.set_position(*Registry.position)
                Registry.camera.set_rotation(*Registry.rotation)

                self.game_starts_running = time.perf_counter()

                self.orbit_start_time = time.perf_counter()

                self.texture2 = Registry.ctx.texture(Registry.display_size, 4)
                depth_attachment = Registry.ctx.depth_renderbuffer(Registry.display_size)
                self.fbo = Registry.ctx.framebuffer(self.texture2, depth_attachment)
                self.camera_up = numpy.array((0, 1, 0), dtype="f4")
                self.cloud_seed = math_utils.getseed(random.randint(0, 999999))
                self.cloud_offset = [0, 0]
                self.matrix = None
                self.jump_timer = 0
                self.jump_starting_y_pos = 0
                self.sun_lightpos = None
                self.moon_lightpos = None
                self.game_run_time = 0
            except Exception as error:
                error_utils.Error(error=error)

        def render_game_engine(self):
            try:
                game_runtime = time.perf_counter() - self.game_starts_running

                self.cloud_offset[0] += math_utils.generate_perlin_noise(
                    game_runtime/500,
                    0,
                    self.cloud_seed)

                self.cloud_offset[1] += math_utils.generate_perlin_noise(
                    0,
                    game_runtime/500,
                    self.cloud_seed)

                Registry.ctx.clear(
                    self.default_skysphere_color,
                    self.default_skysphere_color,
                    self.default_skysphere_color)

                if not Registry.in_hud:
                    if pygame.event.get_grab():
                        mouse_motion = pygame.mouse.get_rel()

                        Registry.camera.rot_state(-mouse_motion[0], -mouse_motion[1])

                if Registry.increase_speed:
                    modifier = self.modifier

                else:
                    modifier = 1

                if Registry.in_hud:
                    if Registry.spin:
                        mouse_motion = 0
                        mouse_motion = [0, 0]

                        Registry.camera.set_position(
                            math.sin(modifier*self.game_run_time/10)*300,
                            50,
                            math.cos(modifier*self.game_run_time/10)*300)

                    self.matrix, self.position = camera_utils.compute_camera.get_camera_values(
                        self.camera_up,
                        point_towards=(0, 0, 0))
                else:
                    self.matrix, self.position = camera_utils.compute_camera.get_camera_values(
                        self.camera_up)

                Registry.camera.velocity = self.base_camera_velocity * modifier

                if Registry.start_jumping and Registry.jump is False:
                    Registry.jump = True
                    self.jump_timer = time.perf_counter()
                    self.jump_starting_y_pos = Registry.camera.position.y

                if Registry.jump:
                    current_time = time.perf_counter()
                    delta = current_time - self.jump_timer
                    offset = delta*180
                    offset_radians = math.radians(offset)

                    if self.increased_speed:
                        calculation = self.jump_starting_y_pos + (math.sin(
                            offset_radians) / (2 / self.modifier))

                    else:
                        calculation = self.jump_starting_y_pos + (math.sin(
                            offset_radians) / 2)

                    Registry.camera.position.y = calculation
                    if delta > 1:
                        Registry.jump = False
                        if self.collision == False:
                            Registry.camera.position.y = self.jump_starting_y_pos

                try:
                    if (pygame.mixer.Channel(2).get_busy() is False and
                            Registry.sound and
                            self.on_start is False):

                        sound_utils.play_sound.play_ambient_sound()

                except Exception as error:
                    error_utils.Error(error=error)

                self.time_percent = ((100/1056)*(Registry.game_time))

                (self.sun_lightpos,
                    self.moon_lightpos) = shadow_mapping_utils.shadowmapping_mathematics.compute_celestial_entities(
                    self.sun_prog,
                    self.moon_prog,
                    self.scene_pos,
                    self.projection,
                    self.matrix,
                    self.position)  # slow

                Registry.ctx.enable(
                    moderngl.DEPTH_TEST |
                    moderngl.CULL_FACE)

                shadow_mapping_utils.shadowmapping_mathematics.compute_shadows(
                    self.mvp,
                    self.light,
                    self.sun_lightpos,
                    self.mvp_depth,
                    self.mvp_shadow,
                    self.bias_matrix,
                    self.projection,
                    self.matrix,
                    self.target,
                    self.up)  # slowest

                # --- PASS 2: Render scene to screen
                Registry.game_engine.fbo.use()
                cam = self.matrix
                cam[3][0] = 0
                cam[3][1] = 0
                cam[3][2] = 0
                self.sky_sphere_prog["m_proj"].write(
                    self.projection)
                self.sky_sphere_prog["m_model"].write(self.scene_translation)
                self.sky_sphere_prog["m_camera"].write(cam)

                if self.time_percent < 40:  # Registry.day
                    self.sky_sphere_prog["time"].value = 0
                    self.default_skysphere_color = 1.0

                elif self.time_percent < 50:  # sunset
                    self.default_skysphere_color = 1 - \
                        ((0.7/10)*(self.time_percent-40))
                    self.sky_sphere_prog["time"].value = (
                        (19/10)*(self.time_percent-40))+1

                elif self.time_percent < 90:  # night
                    self.sky_sphere_prog["time"].value = 21
                    self.default_skysphere_color = 0.3

                else:  # sunrise
                    self.default_skysphere_color = 1 - \
                        ((0.7/10)*(100-self.time_percent))
                    self.sky_sphere_prog["time"].value = 21 - \
                        (((21/10)*(self.time_percent-90)))

                cloud_layer_pos = numpy.array(
                    [0, 200, 0],
                    dtype="f4")

                self.clouds_prog["m_proj"].write(self.projection)
                self.clouds_prog["m_camera"].write(self.matrix)
                self.clouds_prog["m_model"].write(
                    pyrr.Matrix44.from_translation(
                        cloud_layer_pos,
                        dtype="f4"))
                pos = numpy.array([self.camera.position[0], self.camera.position[1]], dtype="f4")
                pos += self.cloud_offset
                self.clouds_prog["camera_pos"].write(pos/25)
                cloud_scale = (1+math_utils.generate_perlin_noise(
                    game_runtime/500,
                    game_runtime/500,
                    self.cloud_seed))*25

                self.clouds_prog["cloud_scale"] = cloud_scale

                #

                ocean_pos = numpy.array(
                    [0, (-Registry.camera.position.y)+math.cos(game_runtime/(TIME_STRETCH_CONSTANT/2))*3, 0],
                    dtype="f4")

                self.ocean_prog["m_proj"].write(self.projection)
                self.ocean_prog["m_camera"].write(self.matrix)
                self.ocean_prog["m_model"].write(
                    pyrr.Matrix44.from_translation(
                        ocean_pos,
                        dtype="f4"))

                Registry.ctx.front_face = "cw"

                self.skysphere_texture.use(location=0)
                self.sky_sphere.render(self.sky_sphere_prog)

                Registry.ctx.front_face = "ccw"

                # pass 5: Render the sun position
                self.moon.render(self.moon_prog)
                self.sun.render(self.sun_prog)
                self.cloud_layer.render(self.clouds_prog)

                Registry.ctx.front_face = "cw"

                self.ocean_layer.render(self.ocean_prog)

                Registry.ctx.blend_func = moderngl.DEFAULT_BLENDING

                # pass 2: render the scene and retro project depth shadow-map
                # counter clock wise -> render front faces

                #self.sampler_depth.use(location=0)
                self.tex_depth.use(location=0)

                Registry.ctx.front_face = "ccw"

                # pass 4: render textured scene with shadow
                self.objects["map"].render()

                if self.on_start:
                    self.on_start = False

                    if not Registry.in_hud:
                        pygame.event.set_grab(True)
                        pygame.mouse.set_visible(False)

                Registry.game_time = Registry.time_offset + time.perf_counter() - self.game_starts_running
            except Exception as error:
                error_utils.Error(error=error)

else:
    print("You need to run this as part of Pycraft")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
