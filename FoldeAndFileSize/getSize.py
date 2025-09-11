#!/usr/bin/env python3
import os
import sys
import platform
import heapq

# ---------- CONFIGURATION ----------
# Hardcoded folders to exclude (case-insensitive on Windows)
EXCLUDED_FOLDERS = [
    "C:\\Windows",         # Example (Windows system folder)
    "/proc",               # Example (Linux virtual FS)
    "/sys",                # Example (Linux virtual FS)
    "/dev"                 # Example (Linux device files)
]
TOP_N = 10
# -----------------------------------

def get_drives():
    """
    Return list of drives to scan.
    Linux/macOS -> just root "/"
    Windows -> all available drives
    """
    system = platform.system().lower()
    if system == "windows":
        import string
        from ctypes import windll

        drives = []
        bitmask = windll.kernel32.GetLogicalDrives()
        for letter in string.ascii_uppercase:
            if bitmask & 1:
                drives.append(f"{letter}:\\")
            bitmask >>= 1
        return drives
    else:
        return ["/"]

def folder_size(path):
    """
    Calculate total size of a folder by summing file sizes.
    Skips excluded folders and inaccessible files.
    """
    total = 0
    for root, dirs, files in os.walk(path, topdown=True, followlinks=False):
        # Apply exclusions
        dirs[:] = [d for d in dirs if not is_excluded(os.path.join(root, d))]
        for f in files:
            try:
                fp = os.path.join(root, f)
                if not os.path.islink(fp):
                    total += os.path.getsize(fp)
            except Exception:
                pass  # ignore permission errors etc.
    return total

def is_excluded(path):
    """
    Check if path should be excluded (case-insensitive on Windows).
    """
    norm_path = os.path.normpath(path)
    system = platform.system().lower()
    if system == "windows":
        norm_path = norm_path.lower()
        return any(norm_path.startswith(os.path.normpath(p).lower()) for p in EXCLUDED_FOLDERS)
    else:
        return any(norm_path.startswith(os.path.normpath(p)) for p in EXCLUDED_FOLDERS)

def scan():
    """
    Scan all drives and find the top N largest folders.
    """
    results = []
    drives = get_drives()
    for drive in drives:
        print(f"Scanning drive {drive} ...")
        for item in os.listdir(drive):
            path = os.path.join(drive, item)
            if os.path.isdir(path) and not is_excluded(path):
                try:
                    size = folder_size(path)
                    results.append((size, path))
                except Exception:
                    pass
    # Get top N
    largest = heapq.nlargest(TOP_N, results, key=lambda x: x[0])
    return largest

def human_readable_size(size_bytes):
    """Convert bytes to human-readable format."""
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.2f} PB"

def main():
    largest = scan()
    print("\nTop {} folders by size:".format(TOP_N))
    for size, path in largest:
        print(f"{human_readable_size(size):>10}  {path}")

if __name__ == "__main__":
    main()
