import React, {useEffect, useRef, useState} from 'react';
import {InputNumber} from 'primereact/inputnumber';
import {InputText} from 'primereact/inputtext';
import {Button} from 'primereact/button';
import {global_show} from "@src/App.tsx";
import {global_websocket} from "@src/main.tsx";

export default function Location_setting() {
    const [value, setValue] = useState("")
    const[storage_location,set_storage_location]=useState("loading")
    const inputRef=useRef(null)
    const buttonRef=useRef(null)
    useEffect(()=>{
        global_websocket.add_listener("storage_location",set_storage_location)
    },[])
    return (
        <div className="card flex flex-wrap justify-content-center gap-3">
            <InputText ref={inputRef}  placeholder={storage_location} value={value} onChange={e=>
                setValue(e.target.value)}/>
            <Button ref={buttonRef} label="change" onClick={(e)=>{
                global_show("changed")
                global_websocket.sendMsg({
                    "type":"change location",
                    "data":value
                })
            }}/>
        </div>
    )
}