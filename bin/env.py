#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import os
import sys

import virtualenv as venv

"""
Colorful output
"""

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = "\033[1m"

def head(msg):
    print(HEADER + msg + ENDC)

def info(msg):
    print(msg)

def infog(msg):
    print(OKGREEN + msg + ENDC)

def infob(msg):
    print(OKBLUE + msg + ENDC)

def warn(msg):
    print(WARNING + msg + ENDC)

def err(msg):
    print(FAIL + msg + ENDC)

"""
Welcome message
"""

head("Welcome!")

"""
Check python version
"""

info("checking python version...")

req_version = (3, 6)
cur_version = sys.version_info

if cur_version < req_version:
    err("Your Python interpreter is too old. Please consider upgrading.")
    sys.exit(-1)

"""
Check virtual enviroment
"""

if not os.path.exists(".py"):
    sys.argv = ['virtualenv', '.py']
    venv.cli_run(['.py'])
