import socket, pickle

class ProcessData():
  num1 = 0
  num2 = 0

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
server.bind (('localhost', 7777))
print('Aguardando conexões.\n')
server.listen(5)

connection, address = server.accept()
print('Esperando entradas do usuário')
data = connection.recv(1024)
dataReceived = pickle.loads(data)
result = str(dataReceived.num1 + dataReceived.num2)
print('resultado enviado!')
connection.send(result.encode())
connection.close()