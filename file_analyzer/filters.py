import os

def filter_by_extension(file_info, extension): return file_info.get('extension', '') == extension
def filter_by_min_size(file_info, min_size): return file_info.get('size', 0) >= min_size
def filter_by_max_size(file_info, max_size): return file_info.get('size', 0) <= max_size
def filter_by_name(file_info, substring): return substring in os.path.basename(file_info.get('path', ''))

def apply_filters(files, args):
    result = []
    for file in files:
        if (args.ext and not filter_by_extension(file, args.ext)):
            continue
        if (args.min_size > 0 and not filter_by_min_size(file, args.min_size)):
            continue
        if (args.max_size and not filter_by_max_size(file, args.max_size)):
            continue
        if (args.name and not filter_by_name(file, args.name)):
            continue
        result.append(file)
    return result
