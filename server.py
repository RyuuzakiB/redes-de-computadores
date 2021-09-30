import socket
import sys
serverPort = int(sys.argv[1])
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind(('', serverPort))
    server_socket.listen(1)
    while True:
      print("aguardando conexão...")
      connection_socket, address = server_socket.accept()
      print("conectou")
      with connection_socket:
        while True:
          num_bytes_received = len(connection_socket.recv(1000000))
          if num_bytes_received == 0: break
connection_socket.close()
