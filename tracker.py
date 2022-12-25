import time
import psutil

def get_internet_time():
    # Get a list of all running processes
    processes = psutil.process_iter()
    internet_time = 0
    # Iterate through the processes
    for process in processes:
        # Check if the process is a web browser
        if process.name() in ['chrome.exe', 'firefox.exe', 'edge.exe']:
            # Check if the process is active (the user is using it)
            if process.status() == 'running':
                # Get the start time of the process
                start_time = process.create_time()
                # Calculate the elapsed time
                elapsed_time = time.time() - start_time
                # Add the elapsed time to the total internet time
                internet_time += elapsed_time
    # Return the total internet time in minutes
    return int(internet_time / 60)

# Print the total internet time in minutes
print(get_internet_time())
