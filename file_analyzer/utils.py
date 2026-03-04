from pathlib import Path

def validate_args(args):
    errors = []
    path = Path(args.path)
    
    if not path.exists():
        errors.append(f"Ошибка: путь '{args.path}' не существует")
        return errors
    if not path.is_dir():
        errors.append(f"Ошибка: путь '{args.path}' не является директорией или нет прав на чтение директории")
        return errors
    if args.min_size < 0:
        errors.append(f"Ошибка: минимальный размер не может быть отрицательным ({args.min_size})")
    if args.max_size is not None:
        if args.max_size < 0:
            errors.append(f"Ошибка: максимальный размер не может быть отрицательным ({args.max_size})")
        if args.max_size < args.min_size:
            errors.append(f"Ошибка: максимальный размер ({args.max_size}) меньше минимального ({args.min_size})")
    if args.top <= 0:
        errors.append(f"Ошибка: значение --top должно быть положительным ({args.top})")
    return errors
