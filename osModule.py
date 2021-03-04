import os
from datetime import datetime

# it shows attributes and methods that we have
# access to within this module
# print(dir(os))

print(os.getcwd())

# os.chdir('/home/divi/Documents/')
# print(os.getcwd())
# print(os.listdir())

# os.mkdir('osDemo')
# os.makedirs('osDemo/demo2')

# os.rmdir('osDemo')
# os.removedirs('osDemo/demo2')

# os.rename('test.txt', 'text.txt')

# print(os.stat('strings.py'))

modtime = os.stat('strings.py').st_mtime
print(f"strings.py-- {datetime.fromtimestamp(modtime)}")

# see entire directory tree use os.walk()

# for dirpath, dirnames, filenames in os.walk('/home/'):
#     print(f"Current path: {dirpath}")
#     print(f"Directories: {dirnames}")
#     print(f"Files: {filenames}")
#     print()

print(os.environ.get('HOME'))
