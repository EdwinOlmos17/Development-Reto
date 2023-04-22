# Autor:Edwin Olmos

# Contenido
# 1. Descripcion Reto Tecnico.
# 2. Tecnologías.
# 3. Estado del Proyecto.
# 4. Instalación de la libreria scheduler.
# 5. Propuesta de solución


# 1.- Descripcion Reto Tecnico 
	El proyecto se trata de incorporar a los modelos predictivos ya existentes los datos del web service que
	proporciona la institucion de conagua, este webservice es: : https://smn.conagua.gob.mx/es/web-service-api

# 2.- Tecnologías
	Lenguaje de programación python
	Sistema Operativo : Linux, Windows
	IDE: Spyder, sublime_text

# 3.- Estado del proyecto.
	En Desarrollo

# 4.- Instalación de la libreria scheduler
	pip install schedule

# 5.- Propuesta de solucion y funcionalidad.
	Para este proyecto se escriben las siguientes funciones en el archivo task.py, se anexa diagrama de flujo de las tareas.

# Tarea 1: 
	1.1 Consumir servicio.
	1.2 Obtiene el archivo generado por el webservice y lo convierte en tipO JSON
	1.3 Convierte en dataframe el archivo JSON.
	1.4 Agrega el campo calculado "Promedio Temp"
	1.5 Se hace la conversion a DataFrame

# Tarea 2: 
	2.1 Ubica el ultimo archivo mas reciente del directorio data_municipos.
	2.2 Lo convierte en DataFrame 

# Tarea 3: 
	3.1 Union de los DataFrame

# Task 4: 
	4.1 Obtener tabla con la union de DataFrames en tipo .csv
	4.2 Copia del archivo .csv

# Task 5: 
	5.- Ejecucion por hora de la funcion read_webservice.

# Nota:
Las rutas que contiene el archivo tasks.py se crean si es que se va a probar código.

# Puntos Fuertes y Debiles
Considero que un proyecto será tan fuerte o débil, dependiendo de la experiencia que tenga en el tema que se vaya a tratar y compromiso
que uno tenga con el desarrollo del mismo.
En este caso un punto fuerte que tiene este desarrollo es el compromiso, la planificacion ,el esfuerzo y el tiempo de entrega que se hizo para obtener esta primer version, puede que ser que no sea el mejor camino para obtener la solucion, pero trate de abarcar todos los requerimientos solicitados.
Sin embargo, creo que tambien esta solucion tiene un punto debil que la parte de la automatizacion de las tareas. Otro punto débil que considero importante es la falta de testing a mi codigo.






