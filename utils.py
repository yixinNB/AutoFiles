import os.path


def separate(path):
    driver, tmp = os.path.splitdrive(path)
    dir, tmp = os.path.split(tmp)
    filename, file_ext = os.path.splitext(tmp)
    # return driver, dir, filename, file_ext
    return {
        "driver":driver,
        "dir":dir,
        "filename":filename,
        "file_ext":file_ext
    }


class File:
    def __init__(self, path):
        self.path = path
        # self.driver, self.dir, self.filename, self.file_ext = separate(path) function changed
    def set_name(self,main_category,tags:list,extra_infomation:str):
        """
        eg.main_category/file_name #tag1 #tag2
        eg.tables/score 2023 #college entrance examination# .xlsx
        """
        pass

