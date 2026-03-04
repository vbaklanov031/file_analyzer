import time
import logging
import functools

_exec_times = {'scan': 0.0, 'report': 0.0}

def log_call(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Called {func.__name__} with arguments args={args} and kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper

def measure_time(func):
    total_time = 0
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal total_time
        start = time.perf_counter()
        result = func(*args, **kwargs)
        total_time += (time.perf_counter() - start) * 1000
        name = func.__name__.lower()
        if 'scan' in name:
            _exec_times['scan'] += total_time
        elif 'report' in name:
            _exec_times['report'] += total_time
        return result
    return wrapper

def get_scan_time(): return _exec_times['scan']
def get_report_time(): return _exec_times['report']
