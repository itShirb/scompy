import os
import time
import subprocess

subprocess.call(['premake/premake5', 'gmake2'])
try:
    subprocess.call(['make'])
except:
    subprocess.call(['mingw32-make'])

directories = ['src', 'include']
mod='./tools/mod'
open(mod, 'w').close()
modf = open(mod, 'a')

for dir in range(0, 1):
    for dirname, subdir, files in os.walk(directories[dir]):
        for filename in files:
            filename_without_extension, extension = os.path.splitext(filename)
            if extension=='.cpp' or '.c' or '.h' or '.hpp':
                path=os.path.join(dirname, filename)
                mtime = os.path.getmtime(path)
                modf.write(path+':'+str(mtime)+'\n')
