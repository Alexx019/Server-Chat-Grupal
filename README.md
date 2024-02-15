# Server y Chat Grupal

## Descripción del Proyecto

El proyecto "Server y Chat Grupal" es una aplicación de chat en tiempo real que permite a múltiples usuarios conectarse a un servidor centralizado y participar en un chat grupal. La aplicación se destaca por su interfaz de usuario gráfica (GUI), desarrollada con Tkinter, que ofrece una experiencia de usuario interactiva y amigable. Utilizando sockets para la comunicación de red y threading para manejar múltiples conexiones simultáneamente, este proyecto proporciona una plataforma robusta para la comunicación en línea.

## Características Principales

- **Conexión en Tiempo Real**: Utiliza sockets para establecer conexiones de red entre el servidor y varios clientes, permitiendo la comunicación en tiempo real.
- **Chat Grupal**: Los usuarios pueden enviar y recibir mensajes en un entorno grupal, viendo las contribuciones de todos los participantes en tiempo real.
- **Interfaz Gráfica de Usuario**: Incorpora una GUI desarrollada con Tkinter, mejorando la interactividad y la facilidad de uso del chat.
- **Manejo de Múltiples Clientes**: Implementa threading para gestionar múltiples usuarios conectados al servidor simultáneamente, asegurando un rendimiento fluido y eficiente.

## Tecnologías Utilizadas

- **Python**: Lenguaje de programación principal para el desarrollo del servidor y la interfaz de usuario.
- **Sockets**: Para la creación de conexiones de red y la comunicación entre el servidor y los clientes.
- **Threading**: Utilizado para manejar múltiples conexiones de clientes al mismo tiempo, permitiendo que cada uno opere de manera independiente sin bloquear a los demás.
- **Tkinter**: Para el desarrollo de la interfaz gráfica de usuario, proporcionando una experiencia de usuario más rica y amigable.

## Cómo Empezar

Para ejecutar el "Server y Chat Grupal" en tu máquina local, sigue estos pasos:

1. Clona el repositorio en tu máquina local usando `git clone [URL del Repositorio]`.
2. Asegúrate de tener Python instalado en tu sistema. Este proyecto ha sido desarrollado con Python 3.11
3. Navega hasta la carpeta `dist` del proyecto y ejecuta `server.exe` para iniciar el servidor.
4. Abre otra terminal y ejecuta `GUI_chat.exe` para iniciar la interfaz de usuario del cliente y conectarte al servidor. Puedes iniciar tantos clientes como desees de la misma manera.
5. Una vez conectado, puedes comenzar a enviar y recibir mensajes en el chat grupal.

Si quieres hacer pruebas desde la terminal, en vez de `GUI_chat`, podeis ejecutar `cliente_emisor.py` para solo enviar al server o `cliente_receptor.py` que solo recibe lo que cualquier otro envía.

## Contribuciones

Si tienes alguna sugerencia para mejorar este proyecto o deseas contribuir, no dudes en hacer un fork del repositorio y enviar una pull request con tus cambios. Las contribuciones son siempre bienvenidas!

## Contacto

Si tienes alguna pregunta o deseas discutir más sobre este proyecto, no dudes en contactarme:

- **Email**: [ariassoutoalex@gmail.com](mailto:ariassoutoalex@gmail.com)

¡Espero que disfrutes usando el "Server y Chat Grupal" tanto como yo disfruté desarrollándolo!
