import {useEffect, useState} from "react";
import DictionaryList from "./components/File_details_list.tsx";
import {MyWs} from './utils/myWs.tsx'


class Ws extends MyWs {
    private setData
    onMsg(data: { [p: string]: any }): void | { [p: string]: any } {
        console.log(data)
        this.setData(data["items_waiting_move"])
    }
    constructor(ws_url,setData) {
        super(ws_url);
        this.setData=setData
    }
}

// const data: interfaces.Item[] = [
//     {name: 'Alice', age: '25', city: 'New York'},
//     {name: 'Bob', age: '30', city: 'London'},
//     {name: 'Charlie', age: '35', city: 'Paris'},
//     {name: 'Alice', age: '25', city: 'New York'},
//     {name: 'Bob', age: '30', city: 'London'},
// ];
export let global_websocket:Ws

export default function () {
    const [data,setData]=useState([])
    useEffect(()=>{
        global_websocket=new Ws("ws://localhost:8765", setData)
    },[])
    return (
        <>
            <div style={{
                color:"red",
                fontSize:"30",
                border:"1px solid red",
                borderRadius:"6px"
            }}>
                technical testing, NOT indicative of final quality.
            </div>

            <DictionaryList dictionaries={data}/>
        </>
    )
}


