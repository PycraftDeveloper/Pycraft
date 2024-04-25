if __name__ != "__main__":
    try:
        import threading
        import os
        import shutil
        from tkinter import messagebox
        import subprocess
        import sys
        import venv
        import requests
        import json
        import platform
        import zipfile

        from registry_utils import Registry

        import path_utils
    except Exception as error:
        from tkinter import messagebox

        messagebox.showerror(
            "Unable to start Pycraft Installer",
            f"A problem occurred whilst trying to start Pycraft Installer (install_coordinator_utils.py).\nMore Details: {error}")

    class thread_with_trace(threading.Thread):
        def __init__(self, *args, **keywords):
            threading.Thread.__init__(self, *args, **keywords)
            self.killed = False

        def start(self):
            self.__run_backup = self.run
            self.run = self.__run
            threading.Thread.start(self)

        def __run(self):
            sys.settrace(self.globaltrace)
            self.__run_backup()
            self.run = self.__run_backup

        def globaltrace(self, frame, event, arg):
            if event == 'call':
                return self.localtrace
            else:
                return None

        def localtrace(self, frame, event, arg):
            if self.killed:
                if event == 'line':
                    raise SystemExit()
            return self.localtrace

        def kill(self):
            self.killed = True
            Registry.installer_stopped = True

    class InstallCoordinator:
        def __init__(self):
            self.main_install_thread = thread_with_trace(target=self.main)
            self.install_directory = Registry.install_directory
            self.temporary_directory = None
            self.src_directory = None
            self.resources_directory = None
            self.component_progress = (1/8)*100

        def start(self):
            self.main_install_thread.start()

        def kill(self):
            self.main_install_thread.kill()

        def main(self):
            self.install_directory = path_utils.Path(f"{Registry.install_directory}/Pycraft").path
            self.temporary_directory = path_utils.Path(f"{self.install_directory}/temporary").path
            self.src_directory = path_utils.Path(f"{self.install_directory}/src").path
            self.resources_directory = path_utils.Path(f"{self.install_directory}/resources").path
            self.environment_directory = path_utils.Path(f"{self.install_directory}/venv").path
            self.pycraft_environment_directory = path_utils.Path(f"{self.install_directory}/venv/pycraft").path
            if platform.system() == "Windows":
                self.activate_environment_directory = path_utils.Path(f"{self.install_directory}/venv/pycraft/Scripts/python.exe").path
            else:
                self.activate_environment_directory = path_utils.Path(f"{self.install_directory}/venv/pycraft/bin/python").path

            self.setup_directories()

            environment_setup_thread = threading.Thread(target=self.setup_venv)
            environment_setup_thread.daemon = True
            environment_setup_thread.start()

            download_source_code_thread = threading.Thread(target=self.download_source_code)
            download_source_code_thread.daemon = True
            download_source_code_thread.start()

            environment_setup_thread.join()
            self.activate_venv("pip install --upgrade pip").communicate()

            download_source_code_thread.join()

            download_resources_thread = threading.Thread(target=self.download_resources)
            download_resources_thread.daemon = True
            download_resources_thread.start()

            extract_source_code_thread = threading.Thread(target=self.extract_source_code)
            extract_source_code_thread.daemon = True
            extract_source_code_thread.start()

            download_resources_thread.join()

            extract_resources_thread = threading.Thread(target=self.extract_resources)
            extract_resources_thread.daemon = True
            extract_resources_thread.start()

            install_dependencies_thread = threading.Thread(target=self.install_dependencies)
            install_dependencies_thread.daemon = True
            install_dependencies_thread.start()

            extract_source_code_thread.join()
            extract_resources_thread.join()
            install_dependencies_thread.join()

            self.clean_up()

            Registry.install_finished = True

        def setup_directories(self): # 1/8 or 12.5
            try:
                os.mkdir(self.install_directory)
            except FileExistsError:
                try:
                    answer = messagebox.askyesno("Pycraft: Installer", "There is already a folder at this location named Pycraft.\nDo you want to overwrite it?")
                    if answer:
                        shutil.rmtree(self.install_directory)
                        os.mkdir(self.install_directory)
                except:
                    messagebox.showerror("Pycraft: Installer", "Pycraft's installation has failed.\nThis is likely because of a file permission error.")
            except:
                messagebox.showerror("Pycraft: Installer", "Pycraft's installation has failed.\nThis is likely because of a file permission error.")

            Registry.progressbar['value'] += self.component_progress/5
            os.mkdir(self.temporary_directory)
            Registry.progressbar['value'] += self.component_progress/5
            os.mkdir(self.environment_directory)
            Registry.progressbar['value'] += self.component_progress/5
            os.mkdir(self.pycraft_environment_directory)
            Registry.progressbar['value'] += self.component_progress/5
            os.mkdir(self.resources_directory)
            Registry.progressbar['value'] += self.component_progress/5

        def setup_venv(self):
            venv.create(self.pycraft_environment_directory, with_pip=True)
            Registry.progressbar['value'] += self.component_progress

        def download_source_code(self):
            online_version = "0.0.0"
            try:
                try:
                    response = requests.get(
                        "https://api.github.com/repos/PycraftDeveloper/Pycraft/tags")
                    response.raise_for_status()
                except requests.exceptions.ConnectionError:
                    messagebox.showerror("Pycraft: Installer", "Pycraft's installation has failed.\nThis is likely because the installer couldn't access the internet.")

                try:
                    laames_tags = json.loads(response.text)
                    result =  laames_tags[0]["name"]
                except (IndexError, UnboundLocalError):
                    pass

                else:
                    online_version = result
            except Exception:
                messagebox.showerror("Pycraft: Installer", "Pycraft's installation has failed.\nUnable to get latest online version from GitHub")

            base_url = "http://api.github.com/repos/PycraftDeveloper/Pycraft/zipball/"
            online_content_url = f"{base_url}{str(online_version)}"

            request = requests.get(online_content_url)
            download_size = len(request.content)

            progress = self.component_progress/download_size

            source_code_download_file = path_utils.Path(f"{self.temporary_directory}/pycraft_sc.zip").path

            with requests.get(
                online_content_url,
                stream=True) as request:

                request.raise_for_status()
                with open(
                        source_code_download_file,
                        'wb') as file:

                    for chunk in request.iter_content(
                            chunk_size=None):
                        Registry.progressbar['value'] += progress*len(chunk)
                        file.write(chunk)

        def extract_source_code(self):
            source_code_download_file = path_utils.Path(f"{self.temporary_directory}/pycraft_sc.zip").path
            extracted_source_code_directory = path_utils.Path(f"{self.temporary_directory}/pycraft_sc").path
            with zipfile.ZipFile(source_code_download_file, "r") as zip_ref:
                zip_ref.extractall(extracted_source_code_directory)

            Registry.progressbar['value'] += self.component_progress/2

            dir_name = os.listdir(extracted_source_code_directory)

            if len(dir_name) > 1:
                raise Exception("More than one directory in zip file")

            source_path = path_utils.Path(f"{extracted_source_code_directory}/{dir_name[0]}").path

            file_names = os.listdir(source_path)

            for file_name in file_names:
                shutil.move(os.path.join(source_path, file_name), self.install_directory)

            Registry.progressbar['value'] += self.component_progress/2

        def activate_venv(self, additional_command):
            command = f"{self.activate_environment_directory} -m {additional_command}"

            return subprocess.Popen([*command.split()])

        def download_resources(self):
            self.activate_venv("pip install mediafiregrabber").communicate()
            Registry.progressbar['value'] += self.component_progress/2

            resource_downloader_file = path_utils.Path(f"{Registry.base_path}/src/utility/resource_downloader.py").path

            resource_downloader_process = subprocess.Popen([self.activate_environment_directory, resource_downloader_file, self.temporary_directory])
            resource_downloader_process.communicate()

            Registry.progressbar['value'] += self.component_progress/2

        def install_dependencies(self):
            requirements_path = path_utils.Path(f"{self.install_directory}/requirements.txt").path
            with open(requirements_path, "r") as file:
                line_data = file.readlines()
                for line in line_data:
                    if line.strip() != "":
                        self.activate_venv(f"pip install {line.strip()}").communicate()
                        Registry.progressbar['value'] += self.component_progress/len(line_data)

            self.activate_venv("pip install pyperclip").communicate()

        def extract_resources(self):
            resources_download_file = path_utils.Path(f"{self.temporary_directory}/pycraft_resources/resources.zip").path
            extracted_resources_directory = path_utils.Path(f"{self.temporary_directory}/pycraft_rs").path
            with zipfile.ZipFile(resources_download_file, "r") as zip_ref:
                zip_ref.extractall(extracted_resources_directory)

            Registry.progressbar['value'] += self.component_progress/2

            source_path = path_utils.Path(f"{extracted_resources_directory}/resources").path
            destination_path = path_utils.Path(f"{self.install_directory}/resources").path

            file_names = os.listdir(source_path)

            for file_name in file_names:
                shutil.move(os.path.join(source_path, file_name), destination_path)

            Registry.progressbar['value'] += self.component_progress/2

        def clean_up(self):
            source_code_download_file = path_utils.Path(f"{self.temporary_directory}/pycraft_sc.zip").path
            os.remove(source_code_download_file)
            Registry.progressbar['value'] += self.component_progress/4

            extracted_source_code_directory = path_utils.Path(f"{self.temporary_directory}/pycraft_sc").path
            shutil.rmtree(extracted_source_code_directory)
            Registry.progressbar['value'] += self.component_progress/4

            resources_download_file = path_utils.Path(f"{self.temporary_directory}/pycraft_resources").path
            shutil.rmtree(resources_download_file)
            Registry.progressbar['value'] += self.component_progress/4

            extracted_resources_directory = path_utils.Path(f"{self.temporary_directory}/pycraft_rs").path
            shutil.rmtree(extracted_resources_directory)
            Registry.progressbar['value'] += self.component_progress/4

else:
    MESSAGE = "You need to run this as part of Pycraft's Installer. "
    MESSAGE += "Please run the 'main.py' file."
    print(MESSAGE)
    from tkinter import messagebox
    messagebox.showerror(
        "Startup Fail",
        MESSAGE)
