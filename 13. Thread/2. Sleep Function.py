import threading
import time

def sleepy_man(secs):
    print("Starting to sleep inside")
    time.sleep(secs)
    print("Woke up inside")

x=threading.Thread(target=sleepy_man,args=(4,))
x.start()

print(threading.active_count())
time.sleep(1.2)
print("done")

print()