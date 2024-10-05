import time
import numpy as np

# Log file setup
log_file = "/app/cache_timing_data.log"

# Start time
start_time = time.time()

# Set duration to run (20 seconds)
run_duration = 20

with open(log_file, "w") as log:
    while time.time() - start_time < run_duration:
        # Simulate cache timing data generation
        timing_data = np.random.random(100)  # Replace with actual cache timing data
        
        # Write data to log
        log.write(f"Timing data: {timing_data.tolist()}\n")
        log.flush()

        # Add delay (5 seconds between each entry)
        time.sleep(5)

print("Data collection finished.")

