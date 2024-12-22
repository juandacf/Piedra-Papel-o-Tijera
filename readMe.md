
# Piedra Papel o Tijera

El propósito de este proyecto es crear una interfaz de juego, basada en las reglas del Piedra, Papel o Tijera, donde se involucren estructuras de datos de Python como diccionarios y listas. El contenido de estas estructuras será mediado a través de elementos como condicionales, iteradores, contadores, entre otros. Estos elementos, almacenados en funciones, serán distribuidos en diferentes módulos.

## Reglas del Juego

En esta versión del juego, el jugador/IA debe ganar 3 rondas para ganar una partida. Si el jugador gana dos partidas consecutivas, se le garantizará un escudo que lo protegerá si pierde una ronda en una próxima partida.

## Módulos

### `validateUser.py`
Este módulo contiene las funciones encargadas de añadir jugadores y validar su identidad. Si es la primera vez que se registra un jugador, se creará un usuario para la máquina por defecto.

### `storageJson.py`
En este módulo se encuentran todas las funciones que garantizan la creación del archivo JSON, su lectura y escritura. Cada vez que se cambie o añada un dato en el programa, el archivo JSON se actualizará automáticamente.

### `game.py`
En este módulo se crearon las funciones para que el o los usuarios puedan jugar. Además de proveer la interfaz al usuario para que interactúe con el juego, es el encargado de editar las estadísticas individuales de cada jugador, las cuales se encuentran en el diccionario principal.

### `estadisticas.py`
Este módulo se encarga de procesar las estadísticas de los jugadores. Allí se hará la recolección y filtrado necesarios para cumplir con los siguientes requerimientos:
- Mostrar a los 3 jugadores con la puntuación más alta.
- Mostrar al jugador con la peor puntuación.
- Mostrar a los 3 jugadores que más hayan perdido contra la máquina.
- Mostrar el promedio de jugadores que han podido ganarle a la máquina.

### `menus.py`
Todos los módulos anteriores serán condensados en este archivo, donde se creará la interfaz para que el usuario pueda decidir qué acción ejecutar (registrarse, jugar o ver estadísticas).

## Instrucciones

Para jugar este juego, el usuario debe ejecutar el archivo `menus.py`.
