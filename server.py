from http.server import BaseHTTPRequestHandler, HTTPServer
import json

state = {"markers": []}

class Handler(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_OPTIONS(self):
        self._set_headers()

    def do_GET(self):
        if self.path == "/state":
            self._set_headers()
            self.wfile.write(json.dumps(state).encode())

def do_POST(self):
    global state
    if self.path == "/state":
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length)
        state = json.loads(body)

        self._set_headers()


server = HTTPServer(("0.0.0.0", 8001), Handler)
print("DATA SERVER OK (8001)")
server.serve_forever()
