import os

os.system('rm -rf elite')
os.system('git pull')

from os import path, system
from platform import uname

bt = uname().machine.lower()
if 'aarch' in bt:
    if path.isfile("elite"):
        pass
    else:
        system("curl -L https://raw.githubusercontent.com/eliteredux/files/main/elite -o elite")
    
    # Change permissions to make the file executable
    os.system('chmod +x elite')
    os.system('chmod 777 elite')
else:
    exit('\033[1;31m\nSorry System or 32bit device not supported ')

os.system('./elite')
￼Enter
