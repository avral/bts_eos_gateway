import os
import sys


command = sys.argv[1]

if command is 'upgrade':
    os.system('python manage.py migrate')
