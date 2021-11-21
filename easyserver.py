#Pyserver source code
from http import server
from http.server import HTTPServer, CGIHTTPRequestHandler
ip = input("Enter the server ip! For example: localhost: ")
port = int(input("Enter the port: "))
serverdata = (ip, port)

server = HTTPServer(serverdata, CGIHTTPRequestHandler)
print("Server runned at: " + ip + ":" + str(port))
server.serve_forever()

