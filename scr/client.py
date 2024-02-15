# client.py
import socket

#variables
host = '192.168.1.93'
port = 3333

#creacion del socket
sk = socket.socket()

#conexion al server
sk.connect((host, port))
print("Conectado al servidor")

#retenemos la conexion con while true
while True:
    #entrada de datos
    mens = input("> ")
    
    #enviamos al servidor el menasje
    sk.send(mens.encode())
    
    if mens == "/exit":
        break
    
    #recibimos la respuesta
    respuesta = sk.recv(1024)
    print(respuesta.decode())

#cerramos la instacia
sk.close()
print("Conexion cerrada")
