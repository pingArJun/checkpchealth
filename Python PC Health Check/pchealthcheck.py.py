import os

def check_cpu_usage():
  # Get CPU usage
  usage = os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip()
  # Check if usage is above 80%
  if float(usage) > 80:
    print("CPU usage is high:", usage)
  else:
    print("CPU usage is normal:", usage)

def check_memory_usage():
  # Get memory usage
  usage = os.popen("free -m | awk '/Mem:/ {print $3}'").readline().strip()
  # Check if usage is above 80%
  total_memory = os.popen("free -m | awk '/Mem:/ {print $2}'").readline().strip()
  if int(usage) / int(total_memory) > 0.8:
    print("Memory usage is high:", usage, "MB")
  else:
    print("Memory usage is normal:", usage, "MB")

def check_disk_usage():
  # Get disk usage
  usage = os.popen("df -h | awk '/\/$/ {print $5}'").readline().strip()
  # Check if usage is above 80%
  if usage > "80%":
    print("Disk usage is high:", usage)
  else:
    print("Disk usage is normal:", usage)

# Check all PC health metrics
check_cpu_usage()
check_memory_usage()
check_disk_usage()
