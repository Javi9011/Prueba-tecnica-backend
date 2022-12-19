# Prueba-tecnica-backend
Servicio de logica-backend de APP-Desarrollado por Nelson Amaya Guerrero
En microservicio esta desarrollado con el IDE de Python(Pycharm), el cual expone servicios para realizar la logica de la BD de la aplicacion 
A continuacion exponemos el paso a paso para el desarrollo del servicio:
1- se realiza analisis de los modelos que va a utilizar, en este caso los siguientes: (puesto de votacion, votante, lider, capitan, municipio, departamento, capitan-municipio, municipio-departamento)
2- Establecer relacion de los modelos, de uno a uno, uno a muchos y muchos a muchos.
3- Se importan todas las librerias que se van a utilizar en el proyecto.
4- Se configura el archivo config.json, el cual nos establece la conexion a la base de datos y nos expone el servicio por una IP y un Puerto.
5- se crean directorios Modelos, Controladores y Repositorios
6- En los Modelos se establecen las tablas u objetos a crear
7- En los repositorios se reedirecciona para crear en BD
8- Controladores llevan la parte logica de los Modelos
9- En el main se exponen los servicios y las rutas.
10- Se realizan pruebas con Postman para alimentar base de datos y gestionar informacion.
11- Se sube microservicio a repositorio GitHub

