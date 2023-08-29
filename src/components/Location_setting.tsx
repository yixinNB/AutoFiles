import React, {useRef, useState} from 'react';
import {InputNumber} from 'primereact/inputnumber';
import {InputText} from 'primereact/inputtext';
import {Button} from 'primereact/button';
import {global_show, global_websocket} from "@src/App.tsx";

export default function Location_setting() {
    const [value, setValue] = useState("")
    const inputRef=useRef(null)
    const buttonRef=useRef(null)
    return (
        <div className="card flex flex-wrap justify-content-center gap-3">
            <InputText ref={inputRef}  placeholder="d:\test" value={value} onChange={e=>
                setValue(e.target.value)}/>
            <Button ref={buttonRef} label="change" onClick={(e)=>{
                setValue(value)
                inputRef.current.disabled=true
                buttonRef.current.disabled=true
                global_show("changed")
                global_websocket.sendMsg({
                    "type":"change location",
                    "data":value
                })
            }}/>
        </div>
    )
}