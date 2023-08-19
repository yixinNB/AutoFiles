import os
import time

from syncFiles.folder_timeCheck import check_lastReadTime
from syncFiles.moveFiles import copy2lib

project_folder="D:\AutoFiles_demo"
backup_driver="D:"

for subfolder in os.listdir(project_folder):
    subfolder_path=os.path.join(project_folder,subfolder)
    if os.path.isfile(subfolder_path): continue
    delta_seconds = time.time() - check_lastReadTime(subfolder_path)
    print(delta_seconds)
    if delta_seconds>3600*24*31*3: #3 months
    # if delta_seconds >100:
        copy2lib(subfolder_path,backup_driver,subfolder)

