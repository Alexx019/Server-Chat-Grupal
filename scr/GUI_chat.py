import tkinter as tk
import socket
import threading

def enviar_mensaje(event=None, mensaje=None):
    if mensaje is None:
        mensaje = campo_texto.get()
    if mensaje:  # Verificar si se proporcionó un mensaje directamente o si el campo de texto no está vacío
        try:
            sk.send(mensaje.encode())  # Enviar mensaje al servidor
            if mensaje == "/exit":
                sk.close()
                ventana.quit()
            else:
                campo_texto.delete(0, tk.END)  # Limpiar el campo de texto después de enviar
        except Exception as e:
            area_mensajes.config(state=tk.NORMAL)
            area_mensajes.insert(tk.END, f"Error al enviar mensaje: {e}\n")
            area_mensajes.config(state=tk.DISABLED)
        area_mensajes.see(tk.END)  # Autoscroll al final


def recibir_mensaje():
    while True:
        try:
            recibido = sk.recv(1024).decode()
            area_mensajes.config(state=tk.NORMAL)
            area_mensajes.insert(tk.END, recibido + "\n")  # Mostrar mensaje recibido
            area_mensajes.config(state=tk.DISABLED)
            area_mensajes.see(tk.END)  # Autoscroll al final
        except OSError:  # Posiblemente el socket se ha cerrado
            break

def on_cerrar():
    enviar_mensaje(None, "/exit")

# Configuración del socket
host = '192.168.169.50'
port = 3333
sk = socket.socket()
sk.connect((host, port))

# Creación de la ventana de la GUI
ventana = tk.Tk()
ventana.title("Cliente Chat")

# Ajustes generales de la ventana
ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(0, weight=1)
ventana.configure(padx=10, pady=10)  # Agregar un poco de espacio alrededor de los widgets

# Configuración del área de mensajes recibidos
area_mensajes = tk.Text(ventana, height=20, width=50, state=tk.DISABLED, font=('Helvetica', 12))
area_mensajes.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)

# Scrollbar para el área de mensajes
scrollbar = tk.Scrollbar(ventana, orient="vertical", command=area_mensajes.yview)
scrollbar.grid(row=0, column=2, sticky="ns")
area_mensajes['yscrollcommand'] = scrollbar.set

# Configuración del campo de texto para escribir mensajes
campo_texto = tk.Entry(ventana, font=('Helvetica', 12))
campo_texto.grid(row=1, column=0, sticky="ew", padx=5)
campo_texto.bind("<Return>", enviar_mensaje)

# Configuración del botón de enviar
boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_mensaje, font=('Helvetica', 12))
boton_enviar.grid(row=1, column=1, padx=5)

# Iniciar hilo para recibir mensajes
hilo_receptor = threading.Thread(target=recibir_mensaje, daemon=True)
hilo_receptor.start()

# Configuración de la ventana para manejar el cierre con la cruz roja
ventana.protocol("WM_DELETE_WINDOW", on_cerrar)

# Iniciar la GUI
ventana.mainloop()




