import http.server
import socketserver
import urllib.parse
import json

PORT = 8000

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Serve your index.html by default
        if self.path == '/' or self.path == '':
            self.path = '/index.html'
        super().do_GET()  # This serves all static files (HTML, CSS, JS, images)

    def do_POST(self):
        if self.path == '/api/submit':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)

            try:
                data = json.loads(post_data)
                data_type = "JSON"
            except json.JSONDecodeError:
                data = urllib.parse.parse_qs(post_data.decode('utf-8'))
                data_type = "Form"

            response = {
                "message": "Data received on phone server!",
                "received": data,
                "type": data_type
            }

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')  # Optional: for JS fetch
            self.end_headers()
            self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            self.send_error(404, "Not found")

# Important: Bind to 0.0.0.0 so it's accessible from your phone's browser
with socketserver.ThreadingTCPServer(("0.0.0.0", PORT), MyHandler) as httpd:
    print(f"Server running! Open your phone browser and go to:")
    print(f"http://127.0.0.1:{PORT}")
    print(f"Or try your local IP (see below)")
    httpd.serve_forever()