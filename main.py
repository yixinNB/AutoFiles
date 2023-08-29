import datetime
import os
import time

import win32api, win32con

import data_storage
import syncFiles.moveFiles
import time_checker
import findFiles
import ws_server
import data_storage

print("backend server, DO NOT close it")
settings_onStart=data_storage.get_settings()
__time_before_move=datetime.timedelta(days=settings_onStart["time_before_require_move_days"],
                                      minutes=settings_onStart["time_before_require_move_minutes"])

def get_desktop():
    key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,
                              r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders', 0, win32con.KEY_READ)
    return win32api.RegQueryValueEx(key, 'Desktop')[0]

def refresh_waiting_move():
    desktop_dir = get_desktop()
    subfiles, subfolders = findFiles.get_subfiles_subfolders(desktop_dir)

    items_waiting_move = []
    for item in subfiles:
        access, modified, mb = time_checker.get_file_last_access_modified_time_mb(item)
        access_delta_datetime = datetime.datetime.now() - access
        if access_delta_datetime > __time_before_move:
            items_waiting_move.append({
                "dir": item,
                "last access": access,
                "last modified": modified,
                "size": str(mb) + "MB"
            })
    return items_waiting_move


class Ws(ws_server.WsServer):
    def onMsg(self, data):
        print("Server received:", data)
        match data["type"]:
            case "change location":
                temp=data_storage.get_settings()
                temp["storage_location"]=data["data"]
                print(temp)
                data_storage.set_settings(temp)
                yield {
                    "type": "listener",
                    "listen_key": "storage_location",
                    "value": data_storage.get_settings()["storage_location"],
                }
            case "del originals":
                for item in data_storage.get_del_cache():
                    syncFiles.moveFiles.del_files(item)
                if os.path.exists("C:\ProgramData\AutoFiles\del_cache.json"):
                    os.remove("C:\ProgramData\AutoFiles\del_cache.json")
                yield {
                    "type": "listener",
                    "listen_key": "waiting_move_data",
                    "value": refresh_waiting_move(),
                }
            case "set file project":
                file_dir=data["file"]
                project_name=data["project_name"]
                time_checker.set_access_modified_time_2_now(file_dir)
                data_storage.set_del_cache(file_dir)
                syncFiles.moveFiles.beta_copy2lib(file_dir,project_name)

    def onConnected(self):
        yield {
            "type": "listener",
            "listen_key": "waiting_move_data",
            "value": refresh_waiting_move(),
        }
        yield {
            "type": "listener",
            "listen_key": "storage_location",
            "value": data_storage.get_settings()["storage_location"],
        }

ws=Ws()
ws.run_forever()
print("error,press any key to exit")
input()
