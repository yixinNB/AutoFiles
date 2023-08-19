import os
import shutil
import hashlib

def copy2lib(source,driver,project_name,type="projects"):
    lib_dir=driver[:1]+":\AutoFiles_lib"
    destination_folder=lib_dir+f"\\{type}\\{project_name}"
    copy_folder_or_file(source,destination_folder)

def copy_folder_or_file(source, destination):
    if os.path.isfile(source):
        __copy_file(source, destination)
    # 创建目标文件夹
    if not os.path.exists(destination):
        os.makedirs(destination)

    # 遍历源文件夹中的所有文件和子文件夹
    for item in os.listdir(source):
        source_item = os.path.join(source, item)
        destination_item = os.path.join(destination, item)

        # 如果是文件夹，则递归复制
        if os.path.isdir(source_item):
            copy_folder_or_file(source_item, destination_item)
        else:
            __copy_file(source_item, destination_item)


def __copy_file(source_item, destination_item):
    if os.path.exists(destination_item):
        # todo file compare
        return
    # 如果是文件，则复制并比对哈希值
    shutil.copy2(source_item, destination_item)
    # if __compare_hashes(source_item, destination_item):
    #     print(f"哈希值匹配 {source_item}")
    # else:
    #     print(f"error哈希值不匹配 {source_item}")# todo recopy or sth else

def __compare_hashes(file1, file2):
    def calculate_hash(file):
        hasher = hashlib.md5()
        with open(file, 'rb') as f:
            while True:
                buffer = f.read(4096)
                if not buffer:
                    break
                hasher.update(buffer)
        return hasher.hexdigest()
    hash1 = calculate_hash(file1)
    hash2 = calculate_hash(file2)
    return hash1 == hash2


if __name__=="__main__":
    source_folder = "D:\AutoFiles_demo\测试.txt"
    destination_folder = "D:\AutoFiles_lib\projects\测试.txt"
    copy_folder_or_file(source_folder, destination_folder)