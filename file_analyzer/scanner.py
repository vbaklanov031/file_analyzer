import os
from decorators import measure_time, log_call

@measure_time
@log_call
def scan_directory(path):
    for root, _, files in os.walk(path):
        for file in files:
            full_path = os.path.join(root, file)
            try:
                size = os.path.getsize(full_path)
                _, ext = os.path.splitext(file)
                yield {
                    'path': full_path,
                    'name': file,
                    'size': size,
                    'extension': ext if ext else "no_extension"
                }
            except (PermissionError, OSError):
                continue  # Пропускаем файлы, к которым нет доступа

def get_file_info(full_path):
    size = os.path.getsize(full_path)
    file_name = os.path.basename(full_path)
    _, extension = os.path.splitext(file_name)
    
    return {'path': full_path, 'name': file_name, 'extension': extension, 'size': size}
