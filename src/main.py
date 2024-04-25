try:
    if __name__ == "__main__":
        import __init__
        __init__.start()
except Exception as error:
    from tkinter import messagebox

    messagebox.showerror(
        "Unable to start Pycraft",
        f"A problem occurred whilst trying to start Pycraft (main.py).\nMore Details: {error}")
