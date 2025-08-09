from http.server import BaseHTTPRequestHandler, HTTPServer
import mysql.connector
import json

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/items":
            try:
                conn = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='shahil123',
                    database='amazon',
                    port=3306
                )
                cursor = conn.cursor(dictionary=True)
                cursor.execute("SELECT item_name, item_price FROM items")
                result = cursor.fetchall()
                conn.close()

                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(result).encode("utf-8"))

            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(f"Error: {str(e)}".encode("utf-8"))
        elif self.path == "/" or self.path == "/amazon.html":
            with open("amazon.html", "rb") as file:
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(file.read())
        elif self.path == "/script.js":
            with open("script.js", "rb") as file:
                self.send_response(200)
                self.send_header("Content-type", "application/javascript")
                self.end_headers()
                self.wfile.write(file.read())
        elif self.path == "/style.css":
            with open("style.css", "rb") as file:
                self.send_response(200)
                self.send_header("Content-type", "text/css")
                self.end_headers()
                self.wfile.write(file.read())
        elif self.path.endswith((".jpg", ".jpeg", ".png", ".gif", ".webp")):
            filepath = self.path.lstrip("/")  # remove leading /
            with open(filepath, "rb") as file:
                self.send_response(200)
                # Set content type based on file extension
                if filepath.endswith(".jpg") or filepath.endswith(".jpeg"):
                    self.send_header("Content-type", "image/jpeg")
                elif filepath.endswith(".png"):
                    self.send_header("Content-type", "image/png")
                elif filepath.endswith(".gif"):
                    self.send_header("Content-type", "image/gif")
                elif filepath.endswith(".webp"):
                    self.send_header("Content-type", "image/webp")
                self.end_headers()
                self.wfile.write(file.read())
        else:
            self.send_response(404)
            self.end_headers()
                
if __name__ == "__main__":
    server = HTTPServer(("", 8000), MyHandler)
    print("Server running at http://localhost:8000")
    server.serve_forever()
