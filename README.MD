# Practicando Bots de telegram

## About

Proyecto para practicar un poco de Python

## Checklist

- Programacion
  - <input type="checkbox" checked> Acceso a ficheros en python
  - <input type="checkbox" > Acceso a base de datos en python
  - <input type="checkbox" checked> Modularidad y arquitectura para un programita
    - He visitado este [blog](https://docs.python-guide.org/writing/structure/) y he empezado a crear una estructura
  - <input type="checkbox"> `/data` que organiza información referente a un mismo chat en el que se encuentre el bot.
- Operacion
  - Procfile perfecto para depliegue en Heroku.
    - Ya no es gratuito. 
  - <input type="checkbox" checked>Despliegue en Google Cloud.
- <input type="checkbox" checked>Librería de dados.
- <input type="checkbox">Funcionalidad de dados
- <input type="checkbox">¡! Gestionar los juegos en memoria. Un diccionario con el numero
- <input type="checkbox">
- <input type="checkbox">

## Estructura de proyecto - curiosidades para el novato de python

- La forma de impportar en la carpeta `tests`.
- Archivo `Makefile` que utiliza requiremets para hacer instalacion con `pip`. En realidad he realizado la ejecución de ese comando a mano:

~~~
pip3 install -r requirements.txt
~~~


--- 

> To keep in line with the style guide, keep module names short, lowercase, and be sure to avoid using special symbols like the dot (.) or question mark (?). A file name like my.spam.py is the one you should avoid! Naming this way will interfere with the way Python looks for modules.

start - comienzo de la funcionalidad
about - mostrar informacion del bot
help - mostrar ayuda sobre el bot
profile - crea un perfil para personaje.
health - mostrar la vida de los personajes
herir - herir a un personaje, hiere a un personaje.
curar - cura a un personaje la cantidad indicada.

## LICENSING

De code on this project is bound to the LICENSE text provided.

The `dice` module that is included comes from  [borntyping python-dice repository](https://github.com/borntyping/python-dice/) comes from code is bound to the MIT license wich is provided inside it's folder (`dice/LICENSE` file).
