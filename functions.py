import os, errno

# --------> get desktop path

currentDirectory = os.getcwd()
# desktopPath = os.path.join(os.environ["HOMEPATH"], "Desktop")
# os.chdir(desktopPath)
try:
    os.mkdir('Gelen_Parser')
except FileExistsError:
    print('------->File alreeady exists')
    pass

gelen_path = os.path.join(currentDirectory, "Gelen_Parser")
# os.chdir(currentDirectory)