Piedra papel o tijera:

El propósito de este proyecto es crear una interfaz de juego, basada en las reglas del piedra papel o tijera, donde se involucren estructuras de datos de python como diccionarios y listas. El contenido de estas estructuras será mediado a través de elementos como condicionales, iteradores, contadores, entre otros. Estos elementos, almacenados en funciones, serán distribuidos en diferentes módulos.

En el modulo 'validateUser.py', tendremos las funciones encargadas de añadir jugadores y validar su identidad. Si es la primera vez que se registra un jugador, se creará un usuario para la máquina por defecto. 

En el módulo 'storageJson.py', tendremos todas las funciones que garantizan la creación del archivo Json, su lectura y escritura. Cada vez que se cambie o añada un dato en el programa, el archivo Json se actualizará automaticamente.

EN el módulo 'game.py', se crearon las funciones para que el o los usuarios puedan jugar. Este módulo, además de proveer la interfaz al usuario para que interactue con el juego, es el encargado de editar las estadísticas individuales de cada jugador, localizadas en el diccionario principal . 

Estas estadísticas serán procesadas en el módulo 'estadisticas.py'. allí, se hará la recolección y filtrado necesarios para cumplir con los requerimientos: Mostrar a los 3 jugadores con la puntuación más alta, al jugador con la peor puntuación, a los 3 jugadores que más hayan perdido contra la máquina y el promedio de jugadores que han podido ganarle a la máquina.

Todos estos módulos serán condensados en el módulo 'menus.py'. En este módulo, se creará la interfaz para que el usuario pueda decidir que acción ejecutar (registrarse, jugar o ver estadísticas). 

Para jugar este juego, el usuario debe ejecutar el archivo 'menus.py'. 