# gpu_monitor.py
import time
import pynvml

def monitor_gpu():
    pynvml.nvmlInit()
    device_count = pynvml.nvmlDeviceGetCount()

    while True:
        for i in range(device_count):
            handle = pynvml.nvmlDeviceGetHandleByIndex(i)
            mem_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
            utilization = pynvml.nvmlDeviceGetUtilizationRates(handle)

            print(f"GPU {i}:")
            print(f"  Memory Used: {mem_info.used / 1024**2:.2f} MB")
            print(f"  Memory Total: {mem_info.total / 1024**2:.2f} MB")
            print(f"  GPU Utilization: {utilization.gpu}%")
            print(f"  Memory Utilization: {utilization.memory}%")
            print("-------------------------------")

        time.sleep(2)

if __name__ == "__main__":
    monitor_gpu()
