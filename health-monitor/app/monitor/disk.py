import psutil
import json

def get_disk_info():
    disk_usage = psutil.disk_usage('/')
    disk_info = {
            "disk_total": disk_usage.total / (1024.0 ** 3),
            "disk_used": disk_usage.used / (1024.0 ** 3),
            "disk_free": disk_usage.free / (1024.0 ** 3),
            "disk_used_percent": disk_usage.percent
    }
    return disk_info

if __name__ == "__main__":
    data = {
        "disk_info": get_disk_info()
    }

    print(json.dumps(data, indent=4))
