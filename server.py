import http.server
import socketserver
import os
import json

PORT = int(os.environ.get("PORT", 8000))

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps(77777777).encode())

    def do_POST(self):
        self.do_GET()

with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as server:
    server.serve_forever()