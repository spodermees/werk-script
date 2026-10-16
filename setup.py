from cx_Freeze import setup, Executable

setup(
    name="AutoClicker",
    version="1.0",
    description="Automatische clicker applicatie",
    executables=[Executable("main.py")],
    options={
        "build_exe": {
            "packages": ["tkinter", "pyautogui", "pynput"],
            "include_files": ["requirements.txt"],
        }
    }
)
