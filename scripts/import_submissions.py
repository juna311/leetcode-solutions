#!/usr/bin/env python3
"""Import saved LeetCode JSON exports; no credentials or network access required."""
import argparse
import ast
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'submissions.json'

def git(*args, **kwargs):
    return subprocess.check_output(['git', '-C', str(ROOT), *args], text=True, **kwargs).strip()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('exports', nargs='+', type=Path)
    parser.add_argument('--author-name', required=True)
    parser.add_argument('--author-email', required=True)
    parser.add_argument('--timezone-offset', default='+0900', help='Git author timezone, e.g. +0900')
    args = parser.parse_args()
    if not re.fullmatch(r'[+-](?:0[0-9]|1[0-4])[0-5][0-9]', args.timezone_offset):
        parser.error('Invalid timezone offset')
    rows = {}
    for path in args.exports:
        payload = json.loads(path.read_text(encoding='utf-8'))
        for row in payload['submissions_dump']:
            if row['status'] != 10:
                continue
            sid = str(row['id'])
            if sid in rows and rows[sid] != row:
                raise ValueError(f'Conflicting export for submission {sid}')
            rows[sid] = row
    records = json.loads(MANIFEST.read_text()) if MANIFEST.exists() else []
    seen = {str(row['submission_id']) for row in records}
    pending = sorted((r for sid, r in rows.items() if sid not in seen),
                     key=lambda r: (int(r['timestamp']), int(r['id'])))
    # Validate the whole batch before creating any commits.
    for row in pending:
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', row['title_slug']):
            raise ValueError('Invalid problem slug')
        if row['lang'] != 'python3':
            raise ValueError(f"Add explicit language support for {row['lang']}")
        if not isinstance(row['code'], str) or not row['code'].strip():
            raise ValueError('Missing submitted code')
        ast.parse(row['code'])
        timestamp = int(row['timestamp'])
        if not 0 < timestamp <= int(datetime.now(timezone.utc).timestamp()):
            raise ValueError('Invalid submission timestamp')
    if not pending:
        print('No new accepted submissions; nothing changed.')
        return
    if git('diff', '--cached', '--name-only'):
        raise RuntimeError('Stage is not empty; finish staged work before importing.')
    for row in pending:
        rel = f"solutions/{row['title_slug']}/solution.py"
        code_path = ROOT / rel
        if code_path.exists() and git('status', '--porcelain', '--', rel):
            raise RuntimeError(f'Uncommitted changes in {rel}')
        if MANIFEST.exists() and git('status', '--porcelain', '--', 'submissions.json'):
            raise RuntimeError('Uncommitted changes in submissions.json')
        timestamp = int(row['timestamp'])
        submitted = datetime.fromtimestamp(timestamp, timezone.utc).isoformat()
        code_path.parent.mkdir(parents=True, exist_ok=True)
        code_path.write_bytes(row['code'].encode('utf-8'))
        records.append({
            'submission_id': str(row['id']),
            'problem': row['title'],
            'slug': row['title_slug'],
            'language': row['lang'],
            'submitted_at': submitted,
            'timestamp': timestamp,
            'problem_url': f"https://leetcode.com/problems/{row['title_slug']}/",
            'submission_url': f"https://leetcode.com/problems/{row['title_slug']}/submissions/{row['id']}/",
            'file': rel,
            'sha256': hashlib.sha256(row['code'].encode('utf-8')).hexdigest(),
        })
        MANIFEST.write_text(json.dumps(records, indent=2, ensure_ascii=False) + '\n')
        git('add', '--', rel, 'submissions.json')
        env = os.environ.copy()
        env.update(GIT_AUTHOR_NAME=args.author_name, GIT_AUTHOR_EMAIL=args.author_email,
                   GIT_AUTHOR_DATE=f'{timestamp} {args.timezone_offset}',
                   GIT_COMMITTER_NAME=args.author_name, GIT_COMMITTER_EMAIL=args.author_email)
        env.pop('GIT_COMMITTER_DATE', None)
        git('-c', 'commit.gpgsign=false', 'commit', '-m',
            f"Solve {row['title']} (LeetCode {row['id']})", '-m',
            f'Imported from an accepted LeetCode submission.\nOriginal submission: {submitted}\nAuthor date preserves submission time; committer date records import time.', env=env)
    print(f'Imported {len(pending)} accepted submissions across {len({r["title_slug"] for r in pending})} problems.')

if __name__ == '__main__':
    main()
