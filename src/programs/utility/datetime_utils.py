"""
This program is in charge of formatting datetime
to create new timestamps.
"""
if __name__ != "__main__":
    try:
        import datetime

        import error_utils
    except Exception as error:
        from tkinter import messagebox

        messagebox.showerror(
            "Unable to start Pycraft",
            f"A problem occurred whilst trying to start Pycraft (datetime_utils.py).\nMore Details: {error}")

    def generate_timestamp() -> str:
        """
        This function takes the current time and formats it
        into the standard form supported by LAaMES.

        Returns:
            str: The current timestamp.
        """
        try:
            current_time = datetime.datetime.now()
            string = ""
            string += str(current_time.year)
            string += "-"
            string += str(current_time.month)
            string += "-"
            string += str(current_time.day)
            string += " "
            string += str(current_time.hour)
            string += ":"
            string += str(current_time.minute)
            string += ":"
            string += str(current_time.second)
            string += "."
            string += str(current_time.microsecond)
            return string
        except Exception as error:
            error_utils.Error(error=error)

    def generate_time_code(date_time_stamp=None) -> int:
        """
        This function takes the current time and formats it
        into the standard integer supported by LAaMES for
        comparing tokens

        Returns:
            int: The current time in numeric form.
            (YYYYMMDDHHMMSSUUUUUU) where:
            * Y is the year
            * M is the month
            * D is the day
            * H is the hour
            * M is the minute
            * S is the second
            * U is the microsecond
        """
        try:
            if date_time_stamp is None:
                current_time = datetime.datetime.now()
            else:
                current_time = date_time_stamp
            time_code = ""

            year = str(current_time.year)
            time_code += "0"*(4-len(year)) + year
            del year

            month = str(current_time.month)
            time_code += "0"*(2-len(month)) + month
            del month

            day = str(current_time.day)
            time_code += "0"*(2-len(day)) + day
            del day

            hour = str(current_time.hour)
            time_code += "0"*(2-len(hour)) + hour
            del hour

            minute = str(current_time.minute)
            time_code += "0"*(2-len(minute)) + minute
            del minute

            second = str(current_time.second)
            time_code += "0"*(2-len(second)) + second
            del second

            microsecond = str(current_time.microsecond)
            time_code += "0"*(6-len(microsecond)) + microsecond
            del microsecond
            return int(time_code)
        except Exception as error:
            error_utils.Error(error=error)

else:
    print("You need to run this as part of Pycraft")
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Error",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
