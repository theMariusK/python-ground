import os
import json
import time
import psutil

def get_kernel_info():
    return {
        "kernel_version": os.uname().release,
        "system_name": os.uname().sysname,
        "node_name": os.uname().nodename,
        "machine": os.uname().machine
    }

def get_system_uptime():
    boot_time_timestamp = psutil.boot_time()
    current_time_timestamp = time.time()
    uptime_seconds = current_time_timestamp - boot_time_timestamp
    uptime_minutes = uptime_seconds / 60
    uptime_hours = uptime_minutes / 60
    uptime_days = uptime_hours / 24
    uptime = {
        "days": uptime_days,
        "hours": uptime_hours,
        "minutes": uptime_minutes,
        "seconds": uptime_seconds
    }
    return uptime

def get_info():
    data = {
        "kernel_info": get_kernel_info(),
        "system_uptime": get_system_uptime()
    }

    return json.dumps(data, indent=4)

if __name__ == '__main__':
    print(get_info())
