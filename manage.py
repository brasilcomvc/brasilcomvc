#!/usr/bin/env python
import os
import sys


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'brasilcomvc.settings')
    if 'test' in sys.argv:
        os.environ.setdefault('SECRET_KEY', 'dummy_secret_key')

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
