import psutil
import time

def monitor_resources():
    while True:
        cpu_usage = psutil.cpu_percent(interval=5)
        memory_usage = psutil.virtual_memory().percent
        print(f"CPU Usage: {cpu_usage}% | Memory Usage: {memory_usage}%")
        time.sleep(30)

monitor_resources()
