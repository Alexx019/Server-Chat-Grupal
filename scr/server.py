import socket
import threading

clientes = []
hilos = []

host = ''
port = 3333

def manejar_cliente(c, add):
    print(f"Conexión establecida con {add}")
    while True:
        recibido = c.recv(1024)
        
        if recibido.decode() == "/exit":
            clientes.remove(c)
            hilos.remove(threading.current_thread())
            break
        
        s = f"> {add[0]}: {recibido.decode()}"
        print(s)
        try:
            for cliente in clientes:
                cliente.send(s.encode())
        except Exception as e:
            print(e)
        
    c.close()

# Instanciamos un objeto para trabajar con el socket
ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Puerto y servidor que debe escuchar
ser.bind((host, port))

# Aceptamos conexiones entrantes, indicamos cuántas como parámetro
ser.listen()
print("Esperando conexiones...")

#do:
cli, addr = ser.accept()
clientes.append(cli)
# Iniciamos un nuevo hilo que manejará la conexión con el cliente
hilo_cliente = threading.Thread(target=manejar_cliente, args=(cli, addr))
hilo_cliente.start()
hilos.append(hilo_cliente)

#while clientes is not empty
while len(clientes) != 0:
    cli, addr = ser.accept()
    clientes.append(cli)
    # Iniciamos un nuevo hilo que manejará la conexión con el cliente
    hilo_cliente = threading.Thread(target=manejar_cliente, args=(cli, addr))
    hilo_cliente.start()
    hilos.append(hilo_cliente)
    
# Cerramos la instancia del servidor
ser.close()
print("Servidor cerrado")

# Nota: este script no maneja el cierre del servidor de manera elegante,
# por lo que para este ejemplo, el servidor se deberá cerrar forzosamente.
