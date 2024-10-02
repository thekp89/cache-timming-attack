import time
import json

# Define the log file
LOG_FILE = "cache_timing_data.log"

def allocate_memory(size):
    return [0] * size

def measure_access_time(arr, index):
    start = time.perf_counter_ns()
    _ = arr[index]
    end = time.perf_counter_ns()
    return end - start

def log_data(cached_time, uncached_time):
    # Get the current timestamp
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    
    # Create a dictionary to store the data
    log_entry = {
        "timestamp": timestamp,
        "cached_time": cached_time,
        "uncached_time": uncached_time
    }
    
    # Append the log entry to the file
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(log_entry) + "\n")

def cache_timing_demo():
    array_size = 10**6
    arr = allocate_memory(array_size)
    cached_index = 0
    uncached_index = len(arr) - 1

    # "Warm up" the cache
    for _ in range(10):
        _ = arr[cached_index]

    while True:
        # Measure cached and uncached access times
        cached_time = measure_access_time(arr, cached_index)
        uncached_time = measure_access_time(arr, uncached_index)

        # Log the data
        log_data(cached_time, uncached_time)

        # Wait for 5 seconds before the next measurement
        time.sleep(5)

if __name__ == "__main__":
    cache_timing_demo()

