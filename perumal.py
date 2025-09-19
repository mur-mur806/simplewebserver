from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
    <head>
        <title>device</title>
    </head>
    <body>
        <h1 align="center">Device specification-25016127</h1>
        <br>
        <center>
        <table border="3" cellspacing="5" callpadding="10" width="400" height="300">
        </center>
            <tr>
                <th>s.no.</th>
                <th>Device specification</th>
                <th>Description</th>
            </tr>
            <tr>
                <td>1</td>
                <td>storage</td>
                <td>1 TB</td>
            </tr>
            <tr>
                <td>2</td>
                <td>Ram</td>
                <td>16</td>
            </tr>
            <tr>
                <td>3</td>
                <td>processer</td>
                <td>intel core i5 ultra</td>
            </tr>
            <tr>
                <td>4</td>
                <td>graphics card</td>
                <td>intel graphics</td>
            </tr>
            <tr>
                <td>5</td>
                <td>device name</td>
                <td>acer</td>
            </tr>
        </table>
    </body>
</html>
            
            


"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()