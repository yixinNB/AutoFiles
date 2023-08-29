import os
import json5

if not os.path.exists("C:\ProgramData/AutoFiles"):
    os.mkdir("C:\ProgramData/AutoFiles")

__settings_dir = "C:\ProgramData/AutoFiles/data.json"
__default_settings = {
    "storage_location": "d:/AutoFiles_storage",
    "time_before_require_move_days": 30,
    "time_before_require_move_minutes": 0,
}


def get_settings():
    if not os.path.exists(__settings_dir):
        set_settings(__default_settings)
    with open(__settings_dir) as f:
        return json5.load(f)


def set_settings(settings):
    with open(__settings_dir, "w") as f:
        json5.dump(settings, f)


__del_cache_dir = "C:\ProgramData/AutoFiles/del_cache.json"


def get_del_cache():
    try:
        with open(__del_cache_dir) as f:
            return json5.load(f)
    except:
        return []


def set_del_cache(dir):
    try:
        with open(__del_cache_dir) as f:
            data = json5.load(f)
    except:
        data = []
    print(data)
    data.append(dir)
    data = list(set(data))
    with open(__del_cache_dir, "w") as f:
        json5.dump(data, f)


if __name__ == "__main__":
    r = get_del_cache()
    set_del_cache("fff")
