# AutoFiles

自动归档项目或桌面文件

# 为什么使用AutoFiles

我曾经常整理桌面文件,但一旦我移动它,就找不到了.  
后来我不整理了,随着桌面越来越乱,我想是时候解决这个问题了.  
我不希望移动1个月以内的文件,因为我还需要他们.我需要将做一件事产生的文件归类到一起,这个软件会询问你,然后将它移动到指定的位置.

# what will it do
软件会查找桌面上超过1个月的文件并提醒用户整理  
软件让用户为每个文件打标签(设置`project_name`)  
软件会将标签相同的移动到`$storage_root$/project_name`文件夹下

# how to use it

- download the portable execuation file from github release.
- 你可以将它放在任意地方,哪怕不解压它
- 程序运行时不要关闭命令窗口
- 确保文件被正确移动后点击`del originals`删除桌面上的文件(pre-release version)

### for developers

- 程序会占用8765端口
- 判断时间用的是文件的最后访问时间和最后修改时间
- 设置和删除缓存文件保存在`C:\ProgramData\AutoFiles`(可以修改一个文件在提醒用户整理之前的时间间隔)
- json使用json5

# contribution

### structure

backend: python  
frontend: typescript react tauri

### how to run

- generage exe from python using `pyinstaller -F main.py`
- move `main.exe` to ui(another branch)>src-tauri>src>main.exe

### websocket 数据协议

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

### 奇怪的错误

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

### 规划

- [x] 超过3个月无访问自动复制到指定位置
- [ ] 自动判断是否能直接剪切
- [ ] 支持备份到其他硬盘
- [ ] *UI
- [ ] 用压缩包存档

- [ ] 自动整理桌面
- [ ] 整理的时候需要按照最后编辑时间顺序交给用户打标签
- [ ] 什么时候一个文件夹应该当作一个整理看待













