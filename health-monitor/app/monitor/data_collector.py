import machine
import cpu
import network
import disk
import json

class DataCollector:
    def __init__(self):
        pass

    def get_machine(self):
        return machine.get_info()

    def get_cpu(self):
        return cpu.get_info()

    def get_network(self):
        return network.get_info()

    def get_disk(self):
        return disk.get_info()

    def get_all_info(self):
        return json.dumps({
            **json.loads(self.get_machine()),
            **json.loads(self.get_cpu()),
            **json.loads(self.get_network()),
            **json.loads(self.get_disk())
        })

if __name__ == "__main__":
    dc = DataCollector()
    print(dc.get_all_info())
