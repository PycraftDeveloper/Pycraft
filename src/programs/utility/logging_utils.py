if __name__ != "__main__":
    try:
        import traceback
        from typeguard import Optional

        from registry_utils import Registry

        import datetime_utils
        import error_utils
        import path_utils
    except Exception as error:
        from tkinter import messagebox

        messagebox.showerror(
            "Unable to start Pycraft",
            f"A problem occurred whilst trying to start Pycraft (logging_utils.py).\nMore Details: {error}")

    class Log(Registry):
        def __init__(self) -> None:
            try:
                log_file_path = f"{Registry.base_path}/setup/log.txt"
                self.log_file_path = path_utils.Path(log_file_path)
                if self.log_file_path.exists() is False:
                    self.create_log()
            except Exception as error:
                error_utils.Error(error=error)

        def update_log(
                self,
                string:str) -> None:
            try:
                if self.log_file_path.exists() is False:
                    self.create_log()

                with open(
                        self.log_file_path.path,
                        "a",
                        encoding="utf-8") as file:

                    file.write(string)
            except Exception as error:
                error_utils.Error(error=error)

        def log_information(
                self,
                string: Optional[str] = None,
                error: Optional[Exception] = None) -> None:
            try:
                timestamp = datetime_utils.generate_timestamp()
                content = f"In Pycraft. Information: {string} @ {timestamp}"
                if Registry.developer_mode and error is not None:
                    content += "\n"
                    detailed_error = "".join(
                        traceback.format_exception(
                            None,
                            error,
                            error.__traceback__))

                    content += detailed_error

                self.update_log(content)
            except Exception as error:
                error_utils.Error(error=error)

        def log_warning(
                self,
                string: Optional[str] = None,
                error: Optional[Exception] = None) -> None:
            try:
                timestamp = datetime_utils.generate_timestamp()
                content = "\n"
                content += "-"*16
                content += f"\nIn Pycraft. Warning: {string} @ {timestamp}\n"
                if Registry.developer_mode and error is not None:
                    detailed_error = "".join(
                        traceback.format_exception(
                            None,
                            error,
                            error.__traceback__))

                    content += detailed_error

                content += "-"*16

                self.update_log(content)
            except Exception as error:
                error_utils.Error(error=error)

        def log_error(
                self,
                string: Optional[str] = None,
                error: Optional[Exception] = None) -> None:
            try:
                timestamp = datetime_utils.generate_timestamp()
                content = "\n"
                content += "#"*16
                content += f"\nIn Pycraft. Error: {string} @ {timestamp}\n"
                if Registry.developer_mode and error is not None:
                    detailed_error = "".join(
                        traceback.format_exception(
                            None,
                            error,
                            error.__traceback__))

                    content += detailed_error
                content += "#"*16

                self.update_log(content)
            except Exception as error:
                error_utils.Error(
                    error=error,
                    log=False)

        def create_log(self) -> None:
            try:
                with open(
                        self.log_file_path.path,
                        "w",
                        encoding="utf-8") as file:

                    timestamp = datetime_utils.generate_timestamp()
                    string = f"Created log @ {timestamp}"
                    file.write(string)
            except Exception as error:
                error_utils.Error(error=error)

else:
    print("You need to run this as part of Pycraft")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
