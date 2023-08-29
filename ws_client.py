import asyncio
import threading
import time

import json5
import websockets

class WsClient:
    socket = None

    def __init__(self, ws_url="ws://localhost:8765"):
        self.ws_url = ws_url
        threading.Thread(target=self.__connect_wrapper).start()

    def __connect_wrapper(self):
        asyncio.run(self.__connect())

    async def __connect(self):
        self.socket = await websockets.connect(self.ws_url)
        await self.__sendMsg({
            "message":"test"
        })
        await self.__receive_listener()

    def __receive_listener_wrapper(self):
        asyncio.run(self.__receive_listener())

    async def __receive_listener(self):
        async for message in self.socket:
            data=json5.loads(message)
            r=self.onMsg(data)
            if r is not None:
                await self.__sendMsg(r)

    def onMsg(self, data):
        print("onmsg", data)

    def sendMsg(self, data:dict):
        asyncio.run(self.__sendMsg(data))

    async def __sendMsg(self, data:dict):
        assert type(data) == dict
        message=json5.dumps(data)
        await self.socket.send(message)


if __name__ == "__main__":
    ws = WsClient()
