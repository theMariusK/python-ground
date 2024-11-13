import os
import psutil
import json
import time

def get_kernel_info():
    return {
        "kernel_version": os.uname().release,
        "system_name": os.uname().sysname,
        "node_name": os.uname().nodename,
        "machine": os.uname().machine
    }

def get_memory_info():
    return {
        "total_memory": psutil.virtual_memory().total / (1024.0 ** 3),
        "available_memory": psutil.virtual_memory().available / (1024.0 ** 3),
        "used_memory": psutil.virtual_memory().used / (1024.0 ** 3),
        "available_memory_percentage": 100 - psutil.virtual_memory().percent
    }

def get_cpu_info():
    return {
        "physical_cores": psutil.cpu_count(logical=False),
        "total_cores": psutil.cpu_count(logical=True),
        "cpu_usage_per_core": dict(enumerate(psutil.cpu_percent(percpu=True, interval=1))),
        "total_cpu_usage": psutil.cpu_percent(interval=1)
    }

def get_disk_info():
    disk_usage = psutil.disk_usage('/')
    disk_info = {
            "disk_total": disk_usage.total / (1024.0 ** 3),
            "disk_used": disk_usage.used / (1024.0 ** 3),
            "disk_free": disk_usage.free / (1024.0 ** 3),
            "disk_used_percent": disk_usage.percent
    }
    return disk_info

def get_network_info():
    net_io_counters = psutil.net_io_counters()
    return {
        "bytes_sent": net_io_counters.bytes_sent,
        "bytes_recv": net_io_counters.bytes_recv
    }

def get_load_average():
    load_avg_1, load_avg_5, load_avg_15 = psutil.getloadavg()
    return {
        "load_average_1": load_avg_1,
        "load_average_5": load_avg_5,
        "load_average_15": load_avg_15
    }
    
def get_system_uptime():
    boot_time_timestamp = psutil.boot_time()
    current_time_timestamp = time.time()
    uptime_seconds = current_time_timestamp - boot_time_timestamp
    uptime_minutes = uptime_seconds // 60
    uptime_hours = uptime_minutes // 60
    uptime_days = uptime_hours // 24
    uptime_str = f"{int(uptime_days)} days, {int(uptime_hours % 24)} hours, {int(uptime_minutes % 60)} minutes, {int(uptime_seconds % 60)} seconds"
    return {"uptime": uptime_str}


if __name__ == '__main__':
    data = {
        "kernel_info": get_kernel_info(),
        "memory_info": get_memory_info(),
        "cpu_info": get_cpu_info(),
        "disk_info": get_disk_info(),
        "network_info": get_network_info(),
        "system_uptime": get_system_uptime(),
        "load_average": get_load_average(),
    }

    print(json.dumps(data, indent=4))
