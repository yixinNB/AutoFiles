import asyncio
import threading
import time
from abc import ABC, abstractmethod

import json5
import websockets


class WsServer(ABC):
    clients = set()

    def __init__(self, port=8765):
        self.port = port
        threading.Thread(target=self.__start_wrapper).start()

    async def handle_connection(self, websocket):
        self.clients.add(websocket)
        r=self.onConnected()
        if r is not None:
            for data in r:
                assert type(data)==dict
                await self.__sendData(websocket, data)

        try:
            await self.wait_request(websocket)
        except websockets.exceptions.ConnectionClosedError as e:
            print(e)
            self.clients.remove(websocket)
        except Exception as e:
            print(e)
            self.clients.remove(websocket)
        finally:
            self.clients.remove(websocket)

    async def wait_request(self, websocket):
        async for message in websocket:
            data = json5.loads(message)
            r = self.onMsg(data)
            if r is not None:
                for data in r:
                    assert type(data) == dict
                    await self.__sendData(websocket, data)

    @abstractmethod
    def onMsg(self, data):
        print("Server received:", data)
        new = "hello " + str(data)
        yield {
            "message": new
        }

    def onConnected(self):
        # yield {}
        pass

    def __start_wrapper(self):
        asyncio.run(self.__start())

    async def __start(self):
        async with websockets.serve(self.handle_connection, "localhost", self.port):
            await asyncio.Future()  # run forever

    def sendData(self, websocket, data: dict):
        asyncio.run(self.__sendData(websocket, data))

    async def __sendData(self, websocket, data: dict):
        assert (type(data) == dict or print("assert err",type(data)))
        data_str = json5.dumps(data,default=str)
        await websocket.send(data_str)

    def broadcast(self, data):
        asyncio.run(self.__broadcast(data))

    async def __broadcast(self, data):
        await asyncio.gather(*[self.__sendData(client, data) for client in self.clients])

    def __len__(self):
        return len(self.clients)

    async def close_all_clients(self):
        for client in self.clients:
            await client.close()


if __name__ == "__main__":
    ws = WsServer()
