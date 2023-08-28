import React, {useState, useRef} from "react";
import {useFormik} from 'formik';
import {Button} from 'primereact/button';
import {classNames} from 'primereact/utils';
import {AutoComplete} from "primereact/autocomplete";
import {Toast} from 'primereact/toast';
import {global_websocket} from "@src/App.tsx";

export default function Input_project_name({file_dir}) {
    const toast = useRef(null);
    const [items, setItems] = useState([]);

    const show = () => {
        toast.current.show({severity: 'success', summary: 'Form Submitted', detail: formik.values.item});//todo var data
    };

    const search = (event) => {
        setItems([...Array(10).keys()].map((item) => event.query + '-' + item));
    };

    const formik = useFormik({
        initialValues: {
            item: ''
        },
        validate: (data) => {
            let errors = {};

            if (!data.item) {
                errors["item"] = 'Value is required.';
            }

            return errors;
        },
        onSubmit: (data) => {
            data.item && show();
            global_websocket.sendMsg({
                "file":file_dir,
                "project_name":formik.values.item
            })
            formik.resetForm();
        }
    });

    const isFormFieldInvalid = (name) => !!(formik.touched[name] && formik.errors[name]);

    const getFormErrorMessage = (name) => {
        return isFormFieldInvalid(name) ? <small className="p-error">{formik.errors[name]}</small> :
            <small className="p-error">&nbsp;</small>;
    };

    return (
        <div className="card flex justify-content-center">
            <form onSubmit={formik.handleSubmit} className="flex flex-column gap-2">
                <label htmlFor="ac_item">project name</label>
                <Toast ref={toast}/>
                <AutoComplete
                    inputId="ac_item"
                    name="item"
                    value={formik.values.item}
                    suggestions={items}
                    completeMethod={search}
                    className={classNames({'p-invalid': isFormFieldInvalid('item')})}
                    onChange={(e) => {
                        formik.setFieldValue('item', e.value);
                    }}
                />
                {getFormErrorMessage('item')}
                <Button type="submit" label="Submit"/>
            </form>
        </div>
    )
}