import time
def program_time(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"\nProgram execution time {(end - start):4f}s ")
    return wrapper



