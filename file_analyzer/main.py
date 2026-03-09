import argparse
import sys
from scanner import scan_directory
from filters import apply_filters
from report import make_report
from utils import validate_args

def parse_args():
    parser = argparse.ArgumentParser(
        prog="file_analyzer",
        description="Анализатор файлов: собирает статистику о файлах в указанном каталоге"
    )
    
    parser.add_argument("path", type=str, help="Путь к анализируемому каталогу")
    parser.add_argument("--ext", type=str, default=None, help="Фильтрация по расширению файла")
    parser.add_argument("--min-size", type=int, default=0, help="Минимальный размер файла в байтах (по умолчанию: 0)")
    parser.add_argument("--max-size", type=int, default=None, help="Максимальный размер файла в байтах")
    parser.add_argument("--name", type=str, default=None, help="Подстрока в имени файла")
    parser.add_argument("--top", type=int, default=5, help="Количество самых больших файлов в отчёте (по умолчанию: 5)")
    parser.add_argument("--output", type=str, default=None, help="Путь для сохранения отчёта в файл")
    parser.add_argument("--json", action="store_true", default=False, help="Формировать отчёт в формате JSON вместо текстового")
    
    return parser.parse_args()

def main():
    try:
        args = parse_args()
        errors = validate_args(args)
        
        if errors:
            print("Обнаружены ошибки\n" + "\n".join(errors))
            sys.exit(1)
             
        files = scan_directory(args.path)
        filtered = apply_filters(files, args)
        report = make_report(filtered, args)
    
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(report)
        else:
            print(report)      
                
    except Exception as e:
        print(f"Ошибка: {e}")
        sys.exit(1)
