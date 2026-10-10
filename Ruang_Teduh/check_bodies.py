import sys

sys.stdout.reconfigure(encoding='utf-8')

for fname in [
    'landing.html',
    'login.html',
    'index.html',
    'calendar.html',
    'mood-summary.html',
    'family-link.html'
]:
    with open(fname, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()

    print(f"=== {fname} ({len(lines)} lines) ===")

    body_start = -1
    body_end = -1

    for i, line in enumerate(lines):
        if '<body' in line:
            body_start = i

        if '</body>' in line:
            body_end = i

    print(f"  Body from line {body_start + 1} to {body_end + 1}")