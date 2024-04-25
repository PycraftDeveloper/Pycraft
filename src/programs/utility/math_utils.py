if __name__ != "__main__":
    try:
        import math
        from math import floor
        from ctypes import c_int64

        import pyrr
        import numpy
        import numba

        from registry_utils import Registry
    except Exception as error:
        from tkinter import messagebox

        messagebox.showerror(
            "Unable to start Pycraft",
            f"A problem occurred whilst trying to start Pycraft (math_utils.py).\nMore Details: {error}")

    GRADIENTS2 = numpy.array([
        5, 2, 2, 5,
        -5, 2, -2, 5,
        5, -2, 2, -5,
        -5, -2, -2, -5,
    ], dtype=numpy.int64)

    GRADIENTS3 = numpy.array([
        -11, 4, 4, -4, 11, 4, -4, 4, 11,
        11, 4, 4, 4, 11, 4, 4, 4, 11,
        -11, -4, 4, -4, -11, 4, -4, -4, 11,
        11, -4, 4, 4, -11, 4, 4, -4, 11,
        -11, 4, -4, -4, 11, -4, -4, 4, -11,
        11, 4, -4, 4, 11, -4, 4, 4, -11,
        -11, -4, -4, -4, -11, -4, -4, -4, -11,
        11, -4, -4, 4, -11, -4, 4, -4, -11,
    ], dtype=numpy.int64)

    GRADIENTS4 = numpy.array([
        3, 1, 1, 1, 1, 3, 1, 1, 1, 1, 3, 1, 1, 1, 1, 3,
        -3, 1, 1, 1, -1, 3, 1, 1, -1, 1, 3, 1, -1, 1, 1, 3,
        3, -1, 1, 1, 1, -3, 1, 1, 1, -1, 3, 1, 1, -1, 1, 3,
        -3, -1, 1, 1, -1, -3, 1, 1, -1, -1, 3, 1, -1, -1, 1, 3,
        3, 1, -1, 1, 1, 3, -1, 1, 1, 1, -3, 1, 1, 1, -1, 3,
        -3, 1, -1, 1, -1, 3, -1, 1, -1, 1, -3, 1, -1, 1, -1, 3,
        3, -1, -1, 1, 1, -3, -1, 1, 1, -1, -3, 1, 1, -1, -1, 3,
        -3, -1, -1, 1, -1, -3, -1, 1, -1, -1, -3, 1, -1, -1, -1, 3,
        3, 1, 1, -1, 1, 3, 1, -1, 1, 1, 3, -1, 1, 1, 1, -3,
        -3, 1, 1, -1, -1, 3, 1, -1, -1, 1, 3, -1, -1, 1, 1, -3,
        3, -1, 1, -1, 1, -3, 1, -1, 1, -1, 3, -1, 1, -1, 1, -3,
        -3, -1, 1, -1, -1, -3, 1, -1, -1, -1, 3, -1, -1, -1, 1, -3,
        3, 1, -1, -1, 1, 3, -1, -1, 1, 1, -3, -1, 1, 1, -1, -3,
        -3, 1, -1, -1, -1, 3, -1, -1, -1, 1, -3, -1, -1, 1, -1, -3,
        3, -1, -1, -1, 1, -3, -1, -1, 1, -1, -3, -1, 1, -1, -1, -3,
        -3, -1, -1, -1, -1, -3, -1, -1, -1, -1, -3, -1, -1, -1, -1, -3,
    ], dtype=numpy.int64)

    STRETCH_CONSTANT2 = -0.211324865405187
    SQUISH_CONSTANT2 = 0.366025403784439
    STRETCH_CONSTANT3 = -1.0 / 6
    SQUISH_CONSTANT3 = 1.0 / 3
    STRETCH_CONSTANT4 = -0.138196601125011
    SQUISH_CONSTANT4 = 0.309016994374947

    NORM_CONSTANT2 = 47
    NORM_CONSTANT3 = 103
    NORM_CONSTANT4 = 30

    @numba.njit(fastmath=True, cache=True)
    def extrapolate2(perm, xsb, ysb, dx, dy):
        index = perm[(perm[xsb & 0xFF] + ysb) & 0xFF] & 0x0E
        g1, g2 = GRADIENTS2[index : index + 2]
        return g1 * dx + g2 * dy

    @numba.njit(fastmath=True, cache=True)
    def generate_perlin_noise(x, y, perm):
        stretch_offset = (x + y) * STRETCH_CONSTANT2

        xs = x + stretch_offset
        ys = y + stretch_offset

        xsb = floor(xs)
        ysb = floor(ys)

        squish_offset = (xsb + ysb) * SQUISH_CONSTANT2
        xb = xsb + squish_offset
        yb = ysb + squish_offset

        xins = xs - xsb
        yins = ys - ysb

        in_sum = xins + yins

        dx0 = x - xb
        dy0 = y - yb

        value = 0

        dx1 = dx0 - 1 - SQUISH_CONSTANT2
        dy1 = dy0 - 0 - SQUISH_CONSTANT2
        attn1 = 2 - dx1 * dx1 - dy1 * dy1
        if attn1 > 0:
            attn1 *= attn1
            value += attn1 * attn1 * extrapolate2(perm, xsb + 1, ysb + 0, dx1, dy1)

        dx2 = dx0 - 0 - SQUISH_CONSTANT2
        dy2 = dy0 - 1 - SQUISH_CONSTANT2
        attn2 = 2 - dx2 * dx2 - dy2 * dy2
        if attn2 > 0:
            attn2 *= attn2
            value += attn2 * attn2 * extrapolate2(perm, xsb + 0, ysb + 1, dx2, dy2)

        if in_sum <= 1:
            zins = 1 - in_sum
            if zins > xins or zins > yins:
                if xins > yins:
                    xsv_ext = xsb + 1
                    ysv_ext = ysb - 1
                    dx_ext = dx0 - 1
                    dy_ext = dy0 + 1
                else:
                    xsv_ext = xsb - 1
                    ysv_ext = ysb + 1
                    dx_ext = dx0 + 1
                    dy_ext = dy0 - 1
            else:
                xsv_ext = xsb + 1
                ysv_ext = ysb + 1
                dx_ext = dx0 - 1 - 2 * SQUISH_CONSTANT2
                dy_ext = dy0 - 1 - 2 * SQUISH_CONSTANT2
        else:
            zins = 2 - in_sum
            if zins < xins or zins < yins:
                if xins > yins:
                    xsv_ext = xsb + 2
                    ysv_ext = ysb + 0
                    dx_ext = dx0 - 2 - 2 * SQUISH_CONSTANT2
                    dy_ext = dy0 + 0 - 2 * SQUISH_CONSTANT2
                else:
                    xsv_ext = xsb + 0
                    ysv_ext = ysb + 2
                    dx_ext = dx0 + 0 - 2 * SQUISH_CONSTANT2
                    dy_ext = dy0 - 2 - 2 * SQUISH_CONSTANT2
            else:
                dx_ext = dx0
                dy_ext = dy0
                xsv_ext = xsb
                ysv_ext = ysb
            xsb += 1
            ysb += 1
            dx0 = dx0 - 1 - 2 * SQUISH_CONSTANT2
            dy0 = dy0 - 1 - 2 * SQUISH_CONSTANT2

        attn0 = 2 - dx0 * dx0 - dy0 * dy0
        if attn0 > 0:
            attn0 *= attn0
            value += attn0 * attn0 * extrapolate2(perm, xsb, ysb, dx0, dy0)

        attn_ext = 2 - dx_ext * dx_ext - dy_ext * dy_ext
        if attn_ext > 0:
            attn_ext *= attn_ext
            value += attn_ext * attn_ext * extrapolate2(perm, xsv_ext, ysv_ext, dx_ext, dy_ext)

        return value / NORM_CONSTANT2

    def overflow(x):
        return c_int64(x).value

    def getseed(seed):
        perm = numpy.zeros(256, dtype=numpy.int64)
        perm_grad_index3 = numpy.zeros(256, dtype=numpy.int64)
        source = numpy.arange(256)

        seed = overflow(seed * 6364136223846793005 + 1442695040888963407)
        seed = overflow(seed * 6364136223846793005 + 1442695040888963407)
        seed = overflow(seed * 6364136223846793005 + 1442695040888963407)
        for i in range(255, -1, -1):
            seed = overflow(seed * 6364136223846793005 + 1442695040888963407)
            r = int((seed + 31) % (i + 1))
            if r < 0:
                r += i + 1
            perm[i] = source[r]
            perm_grad_index3[i] = int((perm[i] % (len(GRADIENTS3) / 3)) * 3)
            source[r] = source[i]

        return perm

    def gl_look_at(pos, target, up):
        x, y, z = compute_position(
            pos, target, up)

        translate = pyrr.Matrix44.identity(dtype="f4")
        translate[3][0] = -pos.x
        translate[3][1] = -pos.y
        translate[3][2] = -pos.z

        rotate = pyrr.Matrix44.identity(dtype="f4")
        rotate[0][0] = x[0]  # -- X
        rotate[1][0] = x[1]
        rotate[2][0] = x[2]
        rotate[0][1] = y[0]  # -- Y
        rotate[1][1] = y[1]
        rotate[2][1] = y[2]
        rotate[0][2] = z[0]  # -- Z
        rotate[1][2] = z[1]
        rotate[2][2] = z[2]

        return rotate * translate[:, numpy.newaxis]

    @numba.njit(fastmath=True, cache=True)
    def compute_position(pos, target, up):
        def normalize(v):
            norm = numpy.linalg.norm(v)
            if norm == 0:
                return v
            return v / norm

        z = normalize(pos - target)
        x = normalize(numpy.cross(normalize(up), z))
        y = numpy.cross(z, x)
        return x, y, z

    @numba.njit(fastmath=True, cache=True)
    def perspective_fov(fov, aspect_ratio, near_plane, far_plane):
        num = 1.0 / math.tan(fov / 2.0)
        num9 = num / aspect_ratio
        return numpy.array([
            [num9, 0.0, 0.0, 0.0],
            [0.0, num, 0.0, 0.0],
            [0.0, 0.0, far_plane / (near_plane - far_plane), -1.0],
            [0.0, 0.0, (near_plane * far_plane) /
                (near_plane - far_plane), 0.0]
        ], dtype="f4")

    @numba.njit(fastmath=True, cache=True)
    def look_at(camera_position, camera_target, up_vector):
        vector = camera_target - camera_position

        x = numpy.linalg.norm(vector)
        vector = vector / x

        vector2 = numpy.cross(up_vector, vector)
        vector2 /= numpy.linalg.norm(vector2)

        vector3 = numpy.cross(vector, vector2)
        return numpy.array([
            [vector2[0], vector3[0], vector[0], 0.0],
            [vector2[1], vector3[1], vector[1], 0.0],
            [vector2[2], vector3[2], vector[2], 0.0],
            [-numpy.dot(vector2, camera_position), -numpy.dot(
                vector3, camera_position), numpy.dot(vector, camera_position), 1.0]
        ], dtype="f4")

    @numba.njit(fastmath=True, cache=True)
    def multiply(light_proj, sun_light_look_at):
        return light_proj * sun_light_look_at

else:
    print("You need to run this as part of Pycraft")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
