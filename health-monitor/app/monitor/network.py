import psutil
import json

def get_network_info():
    net_io_counters = psutil.net_io_counters()
    return {
        "bytes_sent": net_io_counters.bytes_sent,
        "bytes_recv": net_io_counters.bytes_recv
    }

def get_info():
    data = {
        "network_info": get_network_info()
    }

    return json.dumps(data, indent=4)

if __name__ == "__main__":
    print(get_info())
