if __name__ != "__main__":
    try:
        import threading
        import time

        import pygame
        from PIL import Image, ImageFilter, ImageOps
        import numpy

        from registry_utils import Registry
    except Exception as error:
        from tkinter import messagebox

        messagebox.showerror(
            "Unable to start Pycraft",
            f"A problem occurred whilst trying to start Pycraft (image_utils.py).\nMore Details: {error}")

    IMAGE_SIZE = 30

    class BlurredImage(Registry):
        def blur_function(self, radius, image_filtered_blur=ImageFilter.GaussianBlur):
            blurred = self.image.filter(
                image_filtered_blur(
                    radius=radius*2))

            self.blurred_images[radius] = ImageConverter(
            ).pil_image_to_pygame_surface(blurred)

        def __init__(self, surface):
            image_converter = ImageConverter()
            self.image = image_converter.pygame_surface_to_pil_image(
                surface,
                mode="RGB")

            self.image_filtered_blur = ImageFilter.GaussianBlur
            self.blurred_images = {}

            start = time.perf_counter()
            self.blur_function(
                11,
                self.image_filtered_blur)

            end = time.perf_counter()
            if 11*(end-start) > 0.8:
                self.image_filtered_blur = ImageFilter.BoxBlur

            self.blurred_images = {}
            self.blur_threads = []
            for i in range(11):
                blur_thread = threading.Thread(
                    target=self.blur_function,
                    args=(
                        i,
                        self.image_filtered_blur))
                blur_thread.start()
                self.blur_threads.append(blur_thread)

            for thread in self.blur_threads:
                thread.join()

        def blur(self, radius):
            return self.blurred_images[radius]

    class Icon:
        def square_icon(self, path):
            self.image = Image.open(path)
            converter = Color(self.image)
            self.image = converter.color_converter(
                (0,0,0,255),
                Registry.themes.secondary_font_color)
            self.icon = self.image.resize((
                IMAGE_SIZE,
                IMAGE_SIZE))

            self.icon_surface = ImageConverter(
            ).pil_image_to_pygame_surface(
                self.icon)

        def pycraft_icon(self, path):
            image = Image.open(path)
            width, height = image.size
            new_width  = (680/1280)*Registry.display_size[0]
            new_height = new_width * height / width
            image = image.resize((int(new_width), int(new_height)))
            return ImageConverter().pil_image_to_pygame_surface(image)

    class Color:
        def make_gradient(self, size, color1, color2):
            gradient = numpy.linspace(
                color1,
                color2,
                size[1],
                True).astype(numpy.uint8)

            gradient = numpy.tile(
                gradient,
                [2 * size[1], 1, 1])

            gradient = Image.fromarray(gradient)
            gradient = gradient.transpose(Image.TRANSPOSE)

            self.gradient = gradient.resize(
                (518, 125)).convert("RGBA")

        def color_converter(self, old_color, new_color):
            new_image_data = []
            for color in self.image.getdata():
                if color == old_color:
                    new_image_data.append(new_color)
                else:
                    new_image_data.append(color)

            new_image = Image.new(
                self.image.mode,
                self.image.size)

            new_image.putdata(new_image_data)
            return new_image

        def __init__(self, image):
            self.image = image

    class ImageConverter:
        def display_to_string(self, surface, mode:str="RGBA"):
            surface_image = pygame.image.tostring(
                    surface,
                    mode)

            return surface_image

        def ctx_texture_to_pil_image(self, texture, mode:str="RGBA", frombgr=False):
            sub = Image.frombytes(mode, (1280,720), texture.read(), 'raw')
            if frombgr:
                sub = sub.convert(mode)
                data = numpy.array(sub)
                red, green, blue, alpha = data.T
                data = numpy.array([blue, green, red, alpha])
                data = data.transpose()
                sub = Image.fromarray(data)
            sub = ImageOps.flip(sub)
            return sub

        def pygame_surface_to_pil_image(self, surface, mode:str="RGBA"):
            return Image.frombytes(
                mode,
                surface.get_size(),
                self.display_to_string(surface, mode=mode),
                "raw")

        def pil_image_to_pygame_surface(self, image, alpha=True):
            surface = pygame.image.fromstring(
                image.tobytes(),
                image.size,
                image.mode)
            if alpha:
                surface.convert_alpha()
            if alpha is False:
                surface.convert()
            return surface

else:
    print("You need to run this as part of Pycraft")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
