import sys
from cx_Freeze import setup, Executable

setup(
	name = "Process Notifier",
	version = "0.1",
	description = "small utility to monitor a process' ram/CPU usage and report it.",
	executables = [Executable("main.py", base = "Console")])