from cx_Freeze import setup, Executable
import sys

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": ["pygame"],
    "include_files": ["images/", "earVisuals/", "Comic Sans MS.ttf"],
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Use this to hide console window

setup(
    name="MyScreenIsNowConfetti",
    version="0.1",
    description="Screen Confetti Game",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)],
)
