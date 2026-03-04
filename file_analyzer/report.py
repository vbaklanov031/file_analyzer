import json
from decorators import measure_time, get_scan_time, get_report_time

def collect_stats(files, top_n=5):
    if not files:
        return {'total': 0, 'size': 0, 'exts': {}, 'top': []}
    
    exts, size = {}, 0
    for f in files:
        size += f['size']
        ext = f.get('extension', '') or '<no extension>'
        exts.setdefault(ext, {'count': 0, 'size': 0})
        exts[ext]['count'] += 1
        exts[ext]['size'] += f['size']
    
    return {'total': len(files), 'size': size, 'exts': exts, 
            'top': sorted(files, key=lambda x: x['size'], reverse=True)[:top_n]}

@measure_time
def make_text_report(files, args):
    stats = collect_stats(files, args.top)
    lines = [
        f"Analysis path: {args.path}",
        f"Total files: {stats['total']}",
        f"Total size: {stats['size']} bytes",
        "",
        "Execution info:",
        f"  Scan time: {get_scan_time()} ms",
        f"  Report generation time: {get_report_time()} ms",
        "",
        "By extension:"
    ]
    
    for ext in sorted(stats['exts']):
        data = stats['exts'][ext]
        lines.append(f"  {ext} — {data['count']} files, {data['size']} bytes")
    
    lines.append("")
    lines.append(f"Top {args.top} largest files:")
    for i, file in enumerate(stats['top'], 1):
        lines.append(f"  {i}. {file['path']} — {file['size']} bytes")
    
    return "\n".join(lines)

@measure_time
def make_json_report(files, args):
    stats = collect_stats(files, args.top)
    return json.dumps({
        "analysis_path": args.path,
        "total_files": stats['total'],
        "total_size": stats['size'],
        "execution_info": {
            "scan_time": round(get_scan_time()),
            "report_generation_time": round(get_report_time())
        },
        "by_extension": stats['exts'],
        "top_files": [{"path": f['path'], "size": f['size']} for f in stats['top']]
    })

def make_report(files, args):
    return make_json_report(files, args) if args.json else make_text_report(files, args)
