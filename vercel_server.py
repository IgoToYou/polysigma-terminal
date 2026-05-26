"""
Polysigma Terminal - Vercel Python Handler
Serves the trading terminal HTML, API calls go directly to terminal.polysigma.io
"""

import os

HTML_PATH = os.path.join(os.path.dirname(__file__), 'polysigma_terminal_full.html')

def handler(event, context):
    """Vercel Python entry point"""
    
    path = event.get('path', '/')
    headers = event.get('headers', {})
    
    # Serve main page
    if path in ['/', '/index.html'] or not path.startswith('/api'):
        try:
            with open(HTML_PATH, 'r', encoding='utf-8') as f:
                html = f.read()
        except FileNotFoundError:
            return {
                'statusCode': 404,
                'body': 'Terminal HTML not found. Deploy the full backup.'
            }
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'text/html; charset=utf-8',
                'Cache-Control': 'public, max-age=0, must-revalidate',
                'Access-Control-Allow-Origin': '*'
            },
            'body': html
        }
    
    # API paths - redirect to terminal
    if path.startswith('/api/'):
        return {
            'statusCode': 302,
            'headers': {
                'Location': f'https://terminal.polysigma.io{path}',
                'Cache-Control': 'no-cache'
            },
            'body': ''
        }
    
    # Static assets
    return {
        'statusCode': 404,
        'body': 'Not found'
    }