if __name__ != "__main__":
    class Colors:
        def __init__(self) -> None:
            self.color = {
                "red": (255, 0, 0),
                "orange": (255, 165, 0),
                "yellow": (255, 255, 0),
                "green": (59, 131, 53),
                "blue": (29, 73, 153),
                "purple": (134, 85, 214),
                "indigo": (37, 0, 64),
                "violet": (156, 0, 197),
                "black": (0, 0, 0),
                "white": (255, 255, 255)}

else:
    print("You need to run this as part of Pycraft")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
