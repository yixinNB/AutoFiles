import os
import utils


def detect_folder_type(dir):
    file_count, total_score = __detect_folder_type(dir)
    print(total_score,"  ",file_count)
    return total_score / file_count


def __detect_folder_type(dir):
    file_count = 0
    total_score = 0
    for item in os.listdir(dir):
        item_dir = os.path.join(dir, item)

        if os.path.isdir(item_dir):
            a, b = __detect_folder_type(item_dir)
            file_count += a
            total_score += b
        else:
            r = __detect_file_type(item_dir)
            total_score += r
            file_count += 1
    return file_count, total_score


def __detect_file_type(dir):
    ext = utils.separate(dir)["file_ext"]
    if ext[1:]=="":return 0
    if ext[1:].lower() in project_files:
        return 1
    if ext in not_project_files:
        return -1
    else:
        return 0

'''
软件安装目录
部分图库
'''
project_files = [
    "php",
    "py",
    "txt",
    "html",
    "css",
    "md",
    "js",
    "h",
    "ico",
    

    "exe",
    "msix",
    "bat",
    "jar",
    "vbs",
    "sh",
    "vmoptions",
    "conf",
    "inf",
    "sys",
    "dll",
    "dat",
    "bin",
    "pak",
    "json",
]

'''
存图片 pdf的文件夹
'''
not_project_files = [
    "png",
    "mp4",
    "mp3",

    "zip",
    "rar",
    "iso",
    "img",

    "xlsx",
    "csv",
    "doc",
    "docx",
    "pdf",
]


if __name__=="__main__":
    while 1:
        r=detect_folder_type(input())
        print(r)