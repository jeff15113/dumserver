import os
import time

while 1:
    os.system("python dumserver.py")
    print("Restarting...")
    time.sleep(0.2)  # 200ms to CTR+C twice
