# AutoFiles

自动归档项目文件

# 为什么使用AutoFiles
我经常不整理桌面,因为一旦移动了,文件就找不到了.随着桌面越来越乱,我觉得是时候整理一下了.  
我不希望移动3个月以内的文件,因为我还需要他们.我需要将做一件事产生的文件归类到一起,这个软件会询问你,然后将它移动到指定的位置.

# 宏伟的目标

# 规划

- [x] 超过3个月无访问自动复制到指定位置
- [ ] 自动判断是否能直接剪切
- [ ] 支持备份到其他硬盘
- [ ] *UI
- [ ] 用压缩包存档

- [ ] 自动整理桌面
- [ ] 整理的时候需要按照最后编辑时间顺序交给用户打标签
- [ ] 什么时候一个文件夹应该当作一个整理看待

# websocket 传输协议

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


# 奇怪的错误
```
onMsg 中的错误
connection handler failed
Traceback (most recent call last):
  File "D:\WorkSpace\python\venv\Lib\site-packages\websockets\legacy\server.py", line 240, in handler
    await self.ws_handler(self)
  File "D:\WorkSpace\AutoFiles\ws_server.py", line 33, in handle_connection
    self.clients.remove(websocket)
KeyError: <websockets.legacy.server.WebSocketServerProtocol object at 0x00000297B63FCC90>
```














