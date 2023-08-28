import { useState } from "react";
import { AutoComplete, AutoCompleteCompleteEvent } from "primereact/autocomplete";

export default function Input_project_name() {
    const [value, setValue] = useState<string>('');
    const [items, setItems] = useState<string[]>([]);

    const search = (event: AutoCompleteCompleteEvent) => {
        setItems([...Array(10).keys()].map(item => event.query + '-' + item));
    }

    return (
        <div className="card flex justify-content-center">
            <span className="p-float-label">
                <AutoComplete inputId="ac" value={value} suggestions={items} completeMethod={search} onChange={(e) => setValue(e.value)} />
                <label htmlFor="ac">Float Label</label>
            </span>
        </div>
    )
}

