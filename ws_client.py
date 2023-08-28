import asyncio
import threading
import time

import websockets


async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        name = "test"
        await websocket.send(name)
        print(f">>> {name}")

        greeting = await websocket.recv()
        print(f"<<< {greeting}")


class WsClient:
    socket = None

    def __init__(self, ws_url="ws://localhost:8765"):
        self.ws_url = ws_url
        threading.Thread(target=self.__connect_wrapper).start()

    def __connect_wrapper(self):
        asyncio.run(self.__connect())

    async def __connect(self):
        self.socket = await websockets.connect(self.ws_url)
        await self.socket.send("test")
        await self.__receive_listener()

    def __receive_listener_wrapper(self):
        asyncio.run(self.__receive_listener())

    async def __receive_listener(self):
        async for message in self.socket:
            r=self.onMsg(message)
            if r is not None:
                await self.__sendMsg(r)

    def onMsg(self, data):
        print("onmsg", data)
        time.sleep(1)
        return "reveived"

    def sendMsg(self, data):
        asyncio.run(self.__sendMsg(data))

    async def __sendMsg(self, data):
        await self.socket.send(data)


if __name__ == "__main__":
    ws = WsClient()
