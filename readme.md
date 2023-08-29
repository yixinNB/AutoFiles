# AutoFiles

[Discord](https://discord.gg/jwAJ3YCQJ)  
Automatically archive project or desktop files

[中文chinese](readme_chinese.md)  help me translate  
Since the project has just begun, I'm open to any suggestions you may have.
[Discord](https://discord.gg/jwAJ3YCQJ)

# why AutoFiles

I used to organize my desktop files all the time, but once I moved it, I couldn't find it anymore.  
Then I stopped organizing, and as my desktop got messier and messier, I thought it was time to fix the problem.  
I don't want to move files that are less than a month old because I still need them. I need to group files together that
are created by doing the same thing, and this program will ask you and then move it to a specific location.

# what will it do

The software looks for files on the desktop that are more than 1 month old (default) and reminds the user to organize
them  
Software lets users label each file(set`project_name`)  
The software will move files with the same label to the `$storage_root$/project_name` folder

# how to use it

- download the portable execuation file from github release.
- You can put it anywhere, even if you don't unzip it.
- Do not close the command window while the program is running
- Ensure that the files have been moved correctly and click `del originals` to delete the files on the desktop(
  pre-release version)

### for developers

- The program will occupy port 8765
- Settings and deleting cache files saved in `C:\ProgramData\AutoFiles` (you can modify the time interval before a file
  reminds the user to organize)
- json using json5

# contribution

### structure

backend: python  
frontend: typescript react tauri

### how to run

- generage exe from python using `pyinstaller -F main.py`
- move `main.exe` to ui(another branch)>src-tauri>src>main.exe

### websocket data protocols

dictionary==json5==>string  
every dictionary contains `type`

```
onConnected
{
    "items_waiting_move":refresh_waiting_move()
}

listener
type:listener
listen_key:xxx
value:xxx
```

### strange error

the following means error in onMsg

```
connection handler failed
Traceback (most recent call last):
  File "D:\WorkSpace\python\venv\Lib\site-packages\websockets\legacy\server.py", line 240, in handler
    await self.ws_handler(self)
  File "D:\WorkSpace\AutoFiles\ws_server.py", line 33, in handle_connection
    self.clients.remove(websocket)
KeyError: <websockets.legacy.server.WebSocketServerProtocol object at 0x00000297B63FCC90>
```

















