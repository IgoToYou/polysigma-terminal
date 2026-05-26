import os

def handler(event, context):
    """Vercel Python serverless function"""
    path = event.get('path', '/')
    
    # Serve HTML for root
    if path in ['/', '', '/index.html']:
        html_path = os.path.join(os.path.dirname(__file__), 'polysigma_terminal_full.html')
        try:
            with open(html_path, 'r', encoding='utf-8') as f:
                html = f.read()
            return {
                'statusCode': 200,
                'headers': {'Content-Type': 'text/html; charset=utf-8'},
                'body': html
            }
        except FileNotFoundError:
            return {'statusCode': 404, 'body': 'HTML not found'}
    
    # API paths - redirect to real terminal
    if path.startswith('/api/'):
        return {
            'statusCode': 302,
            'headers': {'Location': f'https://terminal.polysigma.io{path}'},
            'body': ''
        }
    
    return {'statusCode': 404, 'body': 'Not found'}