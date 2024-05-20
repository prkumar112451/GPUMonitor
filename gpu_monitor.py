import time
import pynvml
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def monitor_gpu():
    pynvml.nvmlInit()
    device_count = pynvml.nvmlDeviceGetCount()

    while True:
        for i in range(device_count):
            handle = pynvml.nvmlDeviceGetHandleByIndex(i)
            mem_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
            utilization = pynvml.nvmlDeviceGetUtilizationRates(handle)

            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            logger.info(f"{timestamp} - GPU {i}: Memory Used: {mem_info.used / 1024**2:.2f} MB Memory Total: {mem_info.total / 1024**2:.2f} MB GPU Utilization: {utilization.gpu}% Memory Utilization: {utilization.memory}% -------------------------------")

        time.sleep(2)

if __name__ == "__main__":
    monitor_gpu()
