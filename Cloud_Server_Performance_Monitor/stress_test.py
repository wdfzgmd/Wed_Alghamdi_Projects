import time
import multiprocessing
from datetime import datetime

def generate_cpu_load():
    print(f"[{datetime.now().strftime('%H:%M:%S')}] CPU Stress worker started...")
    while True:
        _ = 12345 * 67890
if __name__ == "__main__":
    print("==================================================")
    print("WARNING: Starting Server Stress Test Simulation...")
    print("This will simulate a heavy user load or a system spike.")
    print("Press Ctrl+C at any time to STOP the stress test.")
    print("==================================================")

    processes = []

    num_cores = multiprocessing.cpu_count()

    try:
        cores_to_stress = max(1, num_cores // 2)
        print(f"Spawning {cores_to_stress} stress workers to simulate high traffic...")

        for _ in range(cores_to_stress):
            p = multiprocessing.Process(target= generate_cpu_load)
            p.start()
            processes.append(p)
        time.sleep(30)
        print("\nTime's up! Stopping the stress test naturally...")

    except KeyboardInterrupt:
           print("\nInterrupted by user. Stopping the stress test safely...")
    finally:
         for p in processes:
              p.terminate()
         print("System load returned to normal. Stress test complete.")
