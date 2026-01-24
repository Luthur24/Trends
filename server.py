import http.server
import socketserver
import os
import Modules as M

PORT = int(os.environ.get("PORT", 8000))

class Handler(http.server.BaseHTTPRequestHandler):

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_POST(self):
        # Read incoming data
        content_length = int(self.headers.get("Content-Length", 0))
        frontenddata = self.rfile.read(content_length).decode("utf-8")

        # Call your module function
        try:
            response_text = M.frontend_request_protocol(frontenddata)
        except Exception as e:
            response_text = f"SERVER ERROR: {e}"

        # Send response
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(response_text.encode("utf-8"))

    def do_GET(self):
        # Optional: basic health check
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(b"Backend running")

with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as server:
    server.serve_forever()