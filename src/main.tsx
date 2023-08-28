import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import {PrimeReactProvider} from "primereact/api";
//theme
import "primereact/resources/themes/lara-light-indigo/theme.css";
//core
import "primereact/resources/primereact.min.css";

ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(
  <React.StrictMode>
      <PrimeReactProvider>
          <App/>
      </PrimeReactProvider>
  </React.StrictMode>,
);


