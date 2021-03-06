__author__ = 'Langens Jonathan'

from KnowledgeDomainServer.SocketFileReceiver import send_msg, recv_msg
from KnowledgeDomainServer.KDSQueryParser import ParseQuery
import socket
import sys

HOST = ''   # Symbolic name meaning all available interfaces
PORT = 4578 # Arbitrary non-privileged port
if len(sys.argv) > 1:
    PORT = int(sys.argv[1])



serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#serverSocket.bind((socket.gethostname(), PORT))
serverSocket.bind((HOST, PORT))
serverSocket.listen(5)

while True:
    (client_socket, address) = serverSocket.accept()
    print("connection accepted")
    print("connected to " + str(address))

    query = recv_msg(client_socket)

    print("received following query:\n" + query)

    result = ParseQuery(query)

    send_msg(client_socket, result)

serverSocket.close()
