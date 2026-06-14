import psutil
import time
import csv
import os
from datetime import datetime

csv_file = "server_logs.csv"

file_exists = os.path.isfile(csv_file)

print("Starting system monitoring... Press Ctrl+C to stop the program.")

try:
    with open(csv_file, mode = 'a', newline = '', encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Timestamp","CPU_Usage_Percent", "RAM_Usage_Percent"])
            file.flush()

        while True:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cpu = psutil.cpu_percent(interval=1)
            ram = psutil.virtual_memory().percent

            print(f"[{current_time}] Data Logged -> CPU: {cpu}% | RAM: {ram}%")

            writer.writerow([current_time,cpu,ram])
            file.flush()

            time.sleep(3)

except KeyboardInterrupt:
    print("\nMonitoring System is successfully stoppped. Data Saved to 'server_logs.csv'.")