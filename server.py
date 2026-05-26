#!/usr/bin/env python3
"""
Polysigma Terminal - Simple HTTP Server
Only serves HTML, API calls go directly to terminal.polysigma.io
"""
import os
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(SCRIPT_DIR, "polysigma_terminal_full.html")


class Handler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass  # silent

    def do_GET(self):
        if self.path == "/" or self.path == "/index.html" or self.path.startswith("/?"):
            try:
                with open(HTML_FILE, "rb") as f:
                    html = f.read()
                self.send_response(200)
                self.send_header('Content-Type', 'text/html; charset=utf-8')
                self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(html)
            except FileNotFoundError:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b"Terminal HTML not found")
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Use / or /index.html")

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.end_headers()


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
    print(f"Polysigma Terminal")
    print(f"URL: http://localhost:{port}/")
    print(f"API:  https://terminal.polysigma.io")
    print(f"HTML: {HTML_FILE}")
    print()
    server = HTTPServer(('0.0.0.0', port), Handler)
    server.serve_forever()