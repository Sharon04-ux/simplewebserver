from http.server import HTTPServer, BaseHTTPRequestHandler

content = '''
<!doctype html>
<html>
    <head>
        <body bgcolor="cyan">
            <table border="1" align="center" bgcolor ="orange" cellpadding="10">
            <caption><h1>List of protocols</h1></caption>
            <tr><th>S.No.</th><th>Name of the layers</th>
                <th>Name of the protocols</th>
            </tr>
            <tr>
                <td>1</td><td>Aplplication Layer</td><td>HTTP, FTP</td>
            </tr>
            <tr>
                <td>2</td><td>Transport Layer</td><td>TCP & UDP</td>
            </tr>
            <tr>
                <td>3</td><td>Network Layer</td><td>ip</td>
            </tr>
            </table>
        </body>
    </head>
</html>'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()