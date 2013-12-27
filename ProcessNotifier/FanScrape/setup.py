import sys
from cx_Freeze import setup, Executable

setup(
	name = "Fan Duel Scraper",
	version = "0.1",
	description = "Scrape fan duel website for data.",
	executables = [Executable("scrape.py", base = "Console")])