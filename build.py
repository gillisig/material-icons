import os
from shutil import copy2


rootdir = 'svg'
dist = 'dist'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        fileName = file.split('.')
        subSplit = subdir.split('/')

        newFilename = '.'
        seq = (subSplit[1], fileName[1])
        newFilename = newFilename.join(seq)
        # print(newFilename)
        oldPath = os.path.join(subdir, file)
        newPath = os.path.join(dist, fileName[0], newFilename)
        print(oldPath)
        print(newPath)

        if not os.path.exists(os.path.dirname(newPath)):
            try:
                os.makedirs(os.path.dirname(newPath))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

        copy2(oldPath, newPath)
        # print os.path.join(subdir, file)