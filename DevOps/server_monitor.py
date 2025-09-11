#!/usr/bin/env python3
import subprocess
import platform
import sys
import time
from datetime import datetime

# ---------- CONFIGURATION ----------
IP_LIST = [
    "8.8.8.8",      # Google DNS
    "1.1.1.1",      # Cloudflare DNS
    "192.168.1.120"   # Example local server
]
INTERVAL = 600  # 10 minutes in seconds
LOG_FILE = "server_monitor.log"
# -----------------------------------

def log(message, is_error=False):
    """
    Log message to stdout or stderr and append to file.
    """
    stream = sys.stderr if is_error else sys.stdout
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted = f"[{timestamp}] {message}"
    print(formatted, file=stream)
    with open(LOG_FILE, "a") as f:
        f.write(formatted + "\n")

def ping_host(host: str, count: int = 2, timeout: int = 2) -> bool:
    """
    Check if host is reachable via ICMP ping.
    Works on Windows, Linux, macOS.
    """
    param = "-n" if platform.system().lower() == "windows" else "-c"
    timeout_param = "-w" if platform.system().lower() == "windows" else "-W"
    try:
        result = subprocess.run(
            ["ping", param, str(count), timeout_param, str(timeout), host],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return result.returncode == 0
    except Exception:
        return False

def check_server(host: str):
    """
    Check one server and log its status.
    """
    if ping_host(host):
        log(f"[OK] {host} is reachable.")
    else:
        log(f"[ERROR] {host} is unreachable!", is_error=True)

def main():
    while True:
        log("Starting server check cycle...")
        for ip in IP_LIST:
            check_server(ip)
        log(f"Cycle completed. Waiting {INTERVAL // 60} minutes...\n")
        time.sleep(INTERVAL)

if __name__ == "__main__":
    main()
