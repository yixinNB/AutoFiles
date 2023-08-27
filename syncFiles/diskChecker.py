import os
import random
import string

import myyaml


def check_driver(driver:str):
    driver=driver[:1]
    libPath=driver+":\AutoFiles_lib"
    metaData_path=libPath+r"\MetaData.yml"

    def get_random_str(length=10):
        a = ""
        for i in range(length):
            a += "".join(random.sample(string.ascii_letters + string.digits, 1))
        return a

    def create_lib():
        os.mkdir(libPath)
        myyaml.save({
            "diskId": get_random_str(),
            "diskType": "main backup" # todo ask user to define
        }, metaData_path)

    if not os.path.exists(metaData_path):
        # metaDate not exist
        create_lib()

    meta=myyaml.load(metaData_path)
    return meta


if __name__=="__main__":
    r=check_driver("d:")