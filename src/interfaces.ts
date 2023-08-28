export interface Item {
    [key: string]: string;
}

export interface ItemListProps {
    dictionaries: Item[];
}

export interface ItemProps {
    dictionary: Item;
}