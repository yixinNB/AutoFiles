import os

test_path = "D:\Downloads"


def get_subfiles_subfolders(root_path):
    subfiles = []
    subfolders = []
    for file_or_folder in os.listdir(root_path):
        path = os.path.join(root_path, file_or_folder)
        if os.path.isfile(path):
            subfiles.append(path)
        else:
            subfolders.append(path)
    return subfiles, subfolders


if __name__ == "__main__":
    print((get_subfiles_subfolders("d:/")))
