# main.py
import routes
from http.server import HTTPServer, BaseHTTPRequestHandler
from router import ROUTES
from config import FILE_DIR
import mimetypes
import os
import time


HOST = "192.168.0.124"
PORT = 8999

class SidhHTTP(BaseHTTPRequestHandler):
    def do_GET(self):
        print(ROUTES)
        if self.path in ROUTES:
            # Call the matching route function
            status, content_type, body = ROUTES[self.path](self)

            self.send_response(status)
            self.send_header("Content-type", content_type)
            self.end_headers()

            # Write response (binary-safe)
            if isinstance(body, str):
                self.wfile.write(body.encode())
            else:
                self.wfile.write(body)
        else:
            self.send_error(404, "Page Not Found")

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.wfile.write(bytes(f'{{"time": "{date}"}}', "utf-8"))

# Start the server
server = HTTPServer((HOST, PORT), SidhHTTP)
print("server running...")
server.serve_forever()
server.server_close()
print("server closed...")
