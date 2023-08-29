export interface Item {
    [key: string]: string;
}

export interface ItemProps {
    details_dict: Item;
}

export interface ItemListProps {
    dictionaries: Item[];
}
