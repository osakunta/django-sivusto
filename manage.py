#!/usr/bin/env python
import os
import sys

# Added to filter out warnings for Django 2.0
import warnings
from django.utils.deprecation import RemovedInDjango110Warning
warnings.filterwarnings('always', category=RemovedInDjango110Warning)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sato.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
