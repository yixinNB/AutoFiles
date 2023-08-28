import {useState} from "react";
import reactLogo from "./assets/react.svg";
import {invoke} from "@tauri-apps/api/tauri";
import Input_project_name from "./components/Input_project_name.tsx"
import File_details from "./components/File_details_list.tsx";
import {MyWs} from './utils/myWs.tsx'
import DictionaryList from "./components/File_details_list.tsx";
import * as interfaces from "@src/interfaces.ts"


// class Ws extends MyWs {
//     onMsg(message: { [p: string]: any }): void | { [p: string]: any } {
//         console.log(JSON.stringify(message));
//     }
// }
// let ws = new Ws("ws://localhost:8765")
// export default function App() {
//     const [fileData, serFileDate] = useState([])
//     let filedetails=fileData.map((item)=>{
//         return(
//             <File_details data={item} />
//         )
//     })
//     return (
//         {...filedetails}
//     )
// }

const dictionaries: interfaces.Item[] = [
    {name: 'Alice', age: '25', city: 'New York'},
    {name: 'Bob', age: '30', city: 'London'},
    {name: 'Charlie', age: '35', city: 'Paris'},
];

export default function () {
    return (
        <>
            <DictionaryList dictionaries={dictionaries}/>
        </>
    )
}


