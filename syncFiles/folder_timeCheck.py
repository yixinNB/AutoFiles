import os
import time

def check_lastReadTime(path,last_time=0):
    if os.path.isfile(path):
        last_access_time = os.path.getatime(path)  # 获取文件的最后读取时间
        return max(last_access_time,last_time)
    else:
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            r=check_lastReadTime(item_path,last_time)
            last_time=max(last_time,r)
        return last_time

# r=check_lastReadTime("D:\AutoFiles_demo",1)
# formatted_time = time.ctime(r)# 将时间戳转换为可读格式
# print(f"最后读取时间是: {formatted_time}")