import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = ["icon.ico"]

# TARGET
target = Executable(script="smart_attendance_system.py", base="Win32GUI", icon="icon.ico", shortcutName="Smart Attendance", shortcutDir="DesktopFolder")

# SETUP CX FREEZE
setup(
    name="SmartAttendanceSystem",
    version="1.0",
    description="An application to use face recognition to manage student attendance",
    author="Anil Kumar",
    options={"build_exe": {"include_files": files}},
    executables=[target],
)
