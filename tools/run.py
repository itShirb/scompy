import os
import time
import subprocess

directories = ['src', 'include']
mod='./tools/mod'

def modcheck():
    for dir in range(0, 1):
        for dirname, subdir, files in os.walk(directories[dir]):
            for filename in files:
                filename_without_extension, extension = os.path.splitext(filename)
                if extension=='.cpp' or '.c' or '.h' or '.hpp':
                    path = os.path.join(dirname, filename)
                    with open(mod) as modf:
                        for line in modf:
                            parts = line.split(':')
                            if parts[0] == path:
                                if parts[1].rstrip('\n') != str(os.path.getmtime(path)):
                                    subprocess.call(["python", "tools/build.py"])
                                    return

modcheck()
f = open("./tools/binpath", "r")
path = f.read()
fpath = ""
if path.startswith("./"):
    fpath = path
elif path.startswith("/"):
    fpath = "."+path
else:
    fpath = "./"+path
try:
    subprocess.call([fpath])
except:
    fpath.replace('/', '\\')
    subprocess.call([fpath])
f.close()
