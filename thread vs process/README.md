# Threading vs Multiprocessing

Simple code test to compare Threading and Multiprocessing with Python

## Threading:
- A new thread is spawned within the existing process
- Starting a thread is faster than starting a process
- Memory is shared between all threads
- Mutexes often necessary to control access to shared data
- One GIL (Global Interpreter Lock) for all threads

To test:
1. open Task Manager (for ready to check)
2. run thread.py

## Multiprocessing:
- A new process is started independent from the first process
- Starting a process is slower than starting a thread
- Memory is not shared between processes
- Mutexes not necessary (unless threading in the new process)
- One GIL (Global Interpreter Lock) for each process

To test:
1. open Task Manager (for ready to check)
2. run processes.py
