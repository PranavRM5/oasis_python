import time, socket, sys
print('Setup Server...')
time.sleep(1)
soc = socket.socket()
host_name = socket.gethostname()
ip = socket.gethostbyname(host_name)
port = 1234
soc.bind((host_name, port))
print(host_name, '({})'.format(ip))
name = input('Enter your name: ')
soc.listen(1) 
print('Waiting for  connections......')
connection, addr = soc.accept()
print("Received connection from ", addr[0], "(", addr[1], ")\n")
print('Connection Established. Connected From: {}, ({})'.format(addr[0], addr[0]))
#get a connection from client side
client_name = connection.recv(1024)
client_name = client_name.decode()
print(client_name + ' has connected.')
print('Enter bye to end the chat')
connection.send(name.encode())
while True:
    message = input('Me > ')
    if message == 'bye':
        message = 'bye :)'
        connection.send(message.encode())
        print("\n")
        break
    connection.send(message.encode())
    message = connection.recv(1024)
    message = message.decode()
    print(client_name, '>', message)
