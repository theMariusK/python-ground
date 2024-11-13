import psutil
import json

def get_cpu_info():
    return {
        "physical_cores": psutil.cpu_count(logical=False),
        "total_cores": psutil.cpu_count(logical=True),
        "cpu_usage_per_core": dict(enumerate(psutil.cpu_percent(percpu=True, interval=1))),
        "total_cpu_usage": psutil.cpu_percent(interval=1)
    }

if __name__ == "__main__":
    data = {
        "cpu_info": get_cpu_info()
    }

    print(json.dumps(data, indent=4))
