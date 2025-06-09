# import socket module
from socket import *
# In order to terminate the program
import sys

def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # Prepare a server socket
    serverSocket.bind(("", port))
    serverSocket.listen(1)

    while True:
        # Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()

        try:
            message = connectionSocket.recv(1024).decode()
            filename = message.split()[1]

            f = open(filename[1:], 'rb')
            content = f.read()
            f.close()

            header = "HTTP/1.1 200 OK\r\n"
            header += "Content-Type: text/html; charset=UTF-8\r\n"
            header += "Server: MySimpleServer/0.1\r\n"
            header += "Connection: close\r\n\r\n"

            response = header.encode() + content
            connectionSocket.send(response)
            connectionSocket.close()

        except Exception:
            error_header = "HTTP/1.1 404 Not Found\r\n"
            error_header += "Content-Type: text/html; charset=UTF-8\r\n"
            error_header += "Server: MySimpleServer/0.1\r\n"
            error_header += "Connection: close\r\n\r\n"
            error_body = "<html><body><h1>404 Not Found</h1></body></html>"

            full_response = error_header + error_body
            connectionSocket.send(full_response.encode())
            connectionSocket.close()

if __name__ == "__main__":
    webServer(13331)
