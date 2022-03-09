#easyserver source code
from http import server#import 1 
from http.server import HTTPServer, CGIHTTPRequestHandler#import 2
ip = input("Enter the server ip! For example: localhost: ")#ip
port = int(input("Enter the port: "))#port
serverdata = (ip, port)#creating tuple with server ip and port

server = HTTPServer(serverdata, CGIHTTPRequestHandler)#creating server
print("Server runned at: " + ip + ":" + str(port))#run info
server.serve_forever()#running
#Version: 1.0
#Author: Abbas Lutvaliyev
#Telegram: @alutvaliyev

