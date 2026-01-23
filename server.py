import http.server
import socketserver
import json
import os

PORT = int(os.environ.get("PORT", 8000))

class MyHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/' or self.path == '':
            self.path = '/index.html'
        super().do_GET()

    def do_POST(self):
        if self.path == '/api/submit':
            # Read incoming data (even if we won't use it)
            content_length = int(self.headers.get('Content-Length', 0))
            _ = self.rfile.read(content_length)

            # Response
            response = {"message": 9}

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()

            self.wfile.write(json.dumps(response).encode('utf-8'))

        else:
            self.send_error(404, "Not found")


with socketserver.ThreadingTCPServer(("0.0.0.0", PORT), MyHandler) as httpd:
    print(f"Server running on port {PORT}")
    httpd.serve_forever()