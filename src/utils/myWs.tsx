import json5 from "json5"
export abstract class MyWs {
    private socket
    private connected=false;
    private msgCache=[]
    constructor(ws_url: string='ws://localhost:8765') {
        this.socket = new WebSocket(ws_url);
        this.socket.onopen=()=>{
            this.connected=true
            this.msgCache.map((data)=>{
                this.sendMsg(data)
            })
        }
        this.socket.onmessage=(event)=>{
            const message=event.data
            let message_dict = json5.parse(message)
            let r = this.onMsg(message_dict)
            if (r) this.sendMsg(r)
        }
        this.socket.onerror=(err)=>{
            console.error("myWS error",err)
        }
        this.socket.onclose=()=>{
            console.log("myws closed")
        }
    }

    abstract onMsg(data: { [key: string]: any }): void | { [key: string]: any }

    sendMsg(data: { [key: string]: any }) {
        if(this.connected==false){
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
//     a=21
// }
// let ws= new Ws("ws://localhost:8765")
// ws.sendMsg({"test":1})