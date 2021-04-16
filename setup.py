#!/usr/bin/python
#coding:utf-8
import sys, os
from cx_Freeze import setup, Executable

path = sys.path
includefiles = []
includes = []
excludes = []
packages = ["modules/crypt", "modules/network", "modules/rights"]

options = {"path": path,
           "include_files": includefiles,
           "includes": includes,
           "excludes": excludes,
           "packages": packages
           }

base = None
if (sys.platform == "win32"):
    base = "Win32GUI"
setup(
	name = "TrackManiaHack",
	version = "1.4",
	options = {"build_exe": options},
    description = "FREE TRACKMANIA - Here is the last version of the famous game TrackMania for free"
	executables = [Executable("main.py", base=base)]
)
