#!/usr/bin/env python
import os
import sys

os.environ.setdefault("PYTHONIOENCODING","utf-8")

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sato.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
