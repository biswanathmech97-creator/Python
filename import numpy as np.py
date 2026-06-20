try:
    import numpy as np
except ImportError:
    import subprocess
    import sys
    print("Error: numpy is not installed. Attempting to install...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "numpy"])
    import numpy as np

# একটি সিম্পল NumPy অ্যারে তৈরি করে দেখা
arr = np.array([1, 2, 3, 4, 5])
print("NumPy successfully installed!")
print("Array:", arr)