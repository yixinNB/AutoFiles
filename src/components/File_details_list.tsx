import React from 'react';
import interfaces from "interfaces.ts"
interface Dictionary {
    [key: string]: string;
}

interface DictionaryItemProps {
    dictionary: Dictionary;
}

const DictionaryItem: React.FC<DictionaryItemProps> = ({ dictionary }) => {
    return (
        <div className="dictionary-item">
            {Object.entries(dictionary).map(([key, value]) => (
                <div key={key}>
                    <strong>{key}: </strong>
                    {value}
                </div>
            ))}
        </div>
    );
};

function File_details({details_dict}) {
    return(
        <div className="dictionary-item">
            {Object.entries(details_dict).map(([key, value]) => (
                <div key={key}>
                    <strong>{key}: </strong>
                    {value}
                </div>
            ))}
        </div>
    )
}

interface DictionaryListProps {
    dictionaries: Dictionary[];
}

const DictionaryList: React.FC<DictionaryListProps> = ({ dictionaries }) => {
    return (
        <div className="dictionary-list">
            {dictionaries.map((dictionary, index) => (
                <File_details key={index} details_dict={dictionary} />
            ))}
        </div>
    );
};

export default DictionaryList;