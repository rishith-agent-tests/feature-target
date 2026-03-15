from . import start_time

def producer(val):
    print(f"producer started at {start_time}")
    return val
