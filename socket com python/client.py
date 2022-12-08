import socket, pickle

class ProcessData():
  def __init__(self, num1, num2):
    self.num1 = num1
    self.num2 = num2

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('localhost', 7777))
print ('Cliente conectado.\n')

try:
  data = pickle.dumps(
    ProcessData(
      int(input('Digite o 1º número da soma: ')),
      int(input('Digite o 2º número da soma: '))
    )
  )
  print('Dados enviados!')
  client.send(data)
  result = client.recv(1024).decode()
  print(f'O resultado é: {result}')
except socket.error as e: 
    print ("Socket error: %s" %str(e)) 
except Exception as e: 
    print ("Other exception: %s" %str(e)) 
finally: 
    print ("Conexão encerrada com o servidor!") 
    client.close() 