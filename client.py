import socket
import sys
import time
server_name = sys.argv[1]
server_port = int(sys.argv[2])
tamanho = 1000000
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((server_name, server_port))
    total_bytes_sent = 0
    tempo1 = time.perf_counter()
    while True:
      total_bytes_sent += client_socket.send(bytearray(tamanho))
      tempo2 = time.perf_counter()
      tempo3 =tempo2-tempo1
      if tempo3 >= 1:
        log = (total_bytes_sent*8)/tempo3
        total_bytes_sent = 0
        tempo1 = tempo2
        print("log de média de tráfego = {:,} bits/s".format(log))
