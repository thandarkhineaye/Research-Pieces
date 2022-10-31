from multiprocessing import Process
import os
import time

def square_number():
    for i in range(100):
        i * i
        time.sleep(0.1)

processes = []
num_processes = os.cpu_count()

if __name__ == '__main__':
    for i in range(num_processes):
        p = Process(target=square_number)
        processes.append(p)

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    print('end main')