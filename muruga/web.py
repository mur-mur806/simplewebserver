from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
    <head>
        <title>device</title>
    </head>
    <body>
        <h1 >Device specification<br>MURUGA PERUMAL P (25016797)</h1>
        <br>
        
        <table border="10"  width="600" height="400" </table>
        
            <tr>
                <th bgcolor="blue" >s.no.</th>
                <th bgcolor="blue">Device specification</th>
                <th bgcolor="blue">Description</th>
            </tr>
           
            <tr>
                <td>1</td>
                <td>Ram</td>
                <td>16</td>
            </tr>
           
            <tr>
                <td>2</td>
                <td>Name of Device</td>
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