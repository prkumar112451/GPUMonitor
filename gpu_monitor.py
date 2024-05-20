import time
import pynvml

def monitor_gpu():
    pynvml.nvmlInit()
    device_count = pynvml.nvmlDeviceGetCount()

    while True:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(f"{timestamp} - ", end="")
        for i in range(device_count):
            handle = pynvml.nvmlDeviceGetHandleByIndex(i)
            mem_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
            utilization = pynvml.nvmlDeviceGetUtilizationRates(handle)

            print(f"GPU {i}: Memory Used: {mem_info.used / 1024**2:.2f} MB Memory Total: {mem_info.total / 1024**2:.2f} MB GPU Utilization: {utilization.gpu}% Memory Utilization: {utilization.memory}% -------------------------------", end="\r")

        time.sleep(2)

if __name__ == "__main__":
    monitor_gpu()
