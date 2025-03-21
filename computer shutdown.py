import os
import platform

def shutdown():
    """Shuts down the operating system."""
    system = platform.system()
    if system == "Windows":
        os.system("shutdown /s /t 1")
    else:
        print("Unsupported operating system.")

if __name__ == "__main__":
    shutdown()