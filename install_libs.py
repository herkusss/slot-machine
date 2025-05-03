import subprocess
import sys

def install_requirements():
    """Install requirements from requirements.txt."""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("All requirements installed successfully!")
    except subprocess.CalledProcessError:
        print("An error occurred while installing the requirements.")

if __name__ == "__main__":
    install_requirements()
