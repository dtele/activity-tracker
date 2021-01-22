# Installs dependencies listed in requirements.txt
# .txt file used for easier additions.

from subprocess import CalledProcessError, check_call
from sys import executable


modules, bad_modules = [i.strip('\n') for i in open('requirements.txt', 'r').readlines()], []

exit_cond = False

for i in modules:
    try:
        check_call([executable, '-m', 'pip', 'install', i])
    except CalledProcessError:
        pass
    try:
        if i == 'pywin32':
            __import__('win32gui')
        else:
            __import__(i)
    except ModuleNotFoundError:
        exit_cond = True
        bad_modules.append(i)

if exit_cond:
    input(f'\n\n\nError in installing the following modules: {", ".join(bad_modules)}'
          f'\nTry installing manually and/or checking PATH variables. '
          f'Press enter to exit. ')
else:
    input(f'\n\n\nAll modules installed successfully. Press enter to exit. ')
