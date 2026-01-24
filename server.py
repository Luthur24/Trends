import http.server
import socketserver
import os
import json

PORT = int(os.environ.get("PORT", 8000))

class Handler(http.server.BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write(json.dumps(9).encode("utf-8"))

    def do_POST(self):
        self._set_headers()
        self.wfile.write(json.dumps(9).encode("utf-8"))

    def do_OPTIONS(self):
        self._set_headers()

with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as server:
    server.serve_forever()