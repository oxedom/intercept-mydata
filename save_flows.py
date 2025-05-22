from mitmproxy import http
from pathlib import Path
from datetime import datetime

log_file = Path('mitm_logs.ndjson')  # Each line = JSON per flow

def response(flow: http.HTTPFlow):
    ts = datetime.utcnow().isoformat()
    record = {
        'timestamp': ts,
        'request': {
            'method': flow.request.method,
            'url': flow.request.pretty_url,
            'headers': dict(flow.request.headers),
            'body': flow.request.get_text()
        },
        'response': {
            'status_code': flow.response.status_code,
            'headers': dict(flow.response.headers),
            'body': flow.response.get_text()
        }
    }
    with log_file.open('a', encoding='utf-8') as f:
        f.write(f'{record}\n')
