import json5 from "json5"



/*
notice:
    useEffect(()=>{
        global_websocket.add_listener("waiting_move_data", setData)
    },[])
*/

export abstract class MyWs {
    private socket
    private connected = false;
    private msgCache = []
    private listeners: { [key: string]: Function }={}
    private listened_cache = {}

    constructor(ws_url: string = 'ws://localhost:8765') {
        this.socket = new WebSocket(ws_url);
        this.socket.onopen = () => {
            this.connected = true
            this.msgCache.map((data) => {
                this.sendMsg(data)
            })
        }
        this.socket.onmessage = (event) => {
            const message = event.data
            let data = json5.parse(message)
            if (data["type"] == "listener") {
                let listen_key = data["listen_key"]
                let value = data["value"]
                if (listen_key in this.listeners) {
                    const set_function = this.listeners[listen_key]
                    console.log(this.listened_cache)
                    set_function(value)
                } else {
                    console.log("listener cache add,key:" + listen_key)
                    this.listened_cache[listen_key] = value
                }
                return
            }
            let r = this.onMsg(data)
            if (r) this.sendMsg(r)
        }
        this.socket.onerror = (err) => {
            console.error("myWS error", err)
        }
        this.socket.onclose = () => {
            console.log("myws closed")
        }
    }

    add_listener(listen_key, setValue: Function) {
        // if(listen_key in this.listeners) return
        if (listen_key in this.listened_cache) {
            setValue(this.listened_cache[listen_key])
            delete this.listened_cache[listen_key]
        }
        this.listeners[listen_key]=setValue
    }

    abstract onMsg(data: { [key: string]: any }): void | { [key: string]: any }

    sendMsg(data: { [key: string]: any }) {
        if (this.connected == false) {
            this.msgCache.push(data)
        }
        const message = json5.stringify(data);
        this.socket.send(message);
    }
}


// import {MyWs} from './utils/myWs.tsx'
// class Ws extends MyWs{
//     onMsg(message: { [p: string]: any }): void | { [p: string]: any } {
//         console.log(JSON.stringify(message));
//     }
// }
// let ws= new Ws("ws://localhost:8765")
// ws.sendMsg({"test":1})