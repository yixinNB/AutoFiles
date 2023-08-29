import {useEffect, useRef, useState} from "react";
import DictionaryList from "./components/File_details_list.tsx";
import {MyWs} from './utils/myWs.tsx'
import Location_setting from "@src/components/Location_setting.tsx";
import {Button} from 'primereact/button';
import {Toast} from "primereact/toast";


class Ws extends MyWs {
    private setData

    onMsg(data: { [p: string]: any }): void | { [p: string]: any } {
        console.log(data)
        this.setData(data["items_waiting_move"])
    }

    constructor(ws_url, setData) {
        super(ws_url);
        this.setData = setData
    }
}

// const data: interfaces.Item[] = [
//     {name: 'Alice', age: '25', city: 'New York'},
//     {name: 'Bob', age: '30', city: 'London'},
//     {name: 'Charlie', age: '35', city: 'Paris'},
//     {name: 'Alice', age: '25', city: 'New York'},
//     {name: 'Bob', age: '30', city: 'London'},
// ];
export let global_websocket: Ws
let toastRef
export const global_show = (message) => {
    toastRef.current?.show({severity: 'info', summary: 'Info', detail: message});
};
export default function App() {
    const [data, setData] = useState([])
    toastRef = useRef<Toast>(null)
    useEffect(() => {
        global_websocket = new Ws("ws://localhost:8765", setData)
    }, [])
    return (
        <>
            <Toast ref={toastRef}/>
            <div style={{
                color: "red",
                fontSize: "30",
                border: "1px solid red",
                borderRadius: "6px"
            }}>
                technical testing, NOT indicative of final quality.
            </div>
            storage location
            <Location_setting/>
            <p>
                In alpha version,please click the button below to delete original files AFTER you make sure they have
                been stored correctly.
                <br/>
                <Button label={"del originals"} onClick={() => {
                    global_show("requested")
                    global_websocket.sendMsg({
                        "type": "del originals"
                    })
                }}/>

            </p>

            <DictionaryList dictionaries={data}/>
        </>
    )
}


