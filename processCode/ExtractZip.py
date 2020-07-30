import os
import zipfile
def openZip(path):
    dirs = os.listdir(path)
    for dir in dirs:
        savepath = path + '\\' + dir.split('.')[0]
        os.mkdir(savepath)
        with zipfile.ZipFile(path + '\\' + dir, 'r') as z:
            z.extractall(savepath)
        os.remove(path + '\\' + dir)

