import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import {PrimeReactProvider} from "primereact/api";
//theme
import "primereact/resources/themes/lara-light-indigo/theme.css";
//core
import "primereact/resources/primereact.min.css";


import {MyWs} from "@src/utils/myWs.tsx";

class Ws extends MyWs {
    onMsg(data: { [p: string]: any }): void | { [p: string]: any } {
        console.log(data)
    }
}

export const global_websocket = new Ws("ws://localhost:8765")

ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(
    <React.StrictMode>
        <PrimeReactProvider>
            <App/>
        </PrimeReactProvider>
    </React.StrictMode>,
);


