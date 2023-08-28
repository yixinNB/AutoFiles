import React from 'react';
import * as interfaces from "@src/interfaces.ts"

import {Divider} from 'primereact/divider';
import Input_project_name from "@src/components/Input_project_name.tsx";


function File_details({details_dict}) {
    return(
        <div className="dictionary-item">
            {Object.entries(details_dict).map(([key, value]) => (
                <div key={key}>
                    <strong>{key}: </strong>
                    {value as string}
                </div>
            ))}
        </div>
    )
}

const DictionaryList: React.FC<interfaces.ItemListProps> = ({ dictionaries }) => {
    return (
        <div className="dictionary-list">
            {dictionaries.map((dictionary, index) => (
                <>
                    <File_details key={index} details_dict={dictionary} />
                    <Input_project_name file_dir={dictionary["dir"]}/>
                    <Divider/>
                </>

            ))}
        </div>
    );
};

export default DictionaryList;