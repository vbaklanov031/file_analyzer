import os
from decorators import measure_time, log_call

@measure_time
@log_call
def scan_directory(path):
    for root, _, files in os.walk(path):
        for file in files:
            full_path = os.path.join(root, file)
            size = os.path.getsize(full_path)
            _, ext = os.path.splitext(file)
            yield (full_path, size, ext if ext else "no_extension")

def get_file_info(full_path):
    size = os.path.getsize(full_path)
    file_name = os.path.basename(full_path)
    _, extension = os.path.splitext(file_name)
    
    return {'path': full_path, 'name': file_name, 'extension': extension, 'size': size}
