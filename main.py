import win32con
import win32gui
import ctypes
from os import listdir
from os.path import isfile, join

cursor_map = {
    "normal": 32512,
    "select": 32513,
    "busy": 32514,
    "pressel": 32515,
    "altsel": 32516,
    "diagresize1": 32642,
    "diagresize2": 32643,
    "horizresize": 32644,
    "vertresize": 32645,
    "move": 32646,
    "no": 32648,
    "link": 32649,
    "workinbg": 32650
}

dirname = "valentine"
filenames = [f for f in listdir(dirname) if isfile(join(dirname, f))]

for file in filenames:
    filen = file.split(".")[0]
    path_to_file = join(dirname, file)
    if filen in file:
        print("Path "+path_to_file)
        try:
            cursor = win32gui.LoadImage(0, path_to_file, win32con.IMAGE_CURSOR,
                                        0, 0, win32con.LR_LOADFROMFILE)
            ctypes.windll.user32.SetSystemCursor(cursor, cursor_map[filen])
            ctypes.windll.user32.DestroyCursor(cursor)
        except:
            print("No such file")
input()