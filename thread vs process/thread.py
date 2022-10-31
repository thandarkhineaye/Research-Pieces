from threading import Thread
import os
import math
import time

def square_number():
    for i in range(100):
        i * i
        time.sleep(0.1)

threads = []
num_threads=10 

for i in range(num_threads):
    t = Thread(target=square_number)
	# print('registering thread %d' % t)
    threads.append(t)

for thread in threads:
	thread.start()

for thread in threads:
	thread.join()

print('end main')