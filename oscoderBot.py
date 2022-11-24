# ------------------------------------------------------------------- #
# oscoderBot - Bot de utilidades personales                           #
#    Copyright (C) <2022>  <***REMOVED*** ***REMOVED***>  #
# A LICENSE file should have been provided with this program.         #
#                                                                     #
# GNU GENERAL PUBLIC LICENSE - Version 3, 29 June 2007                #
# Source code provided without guarantee.                             #
# ------------------------------------------------------------------- #


# Importamos las librerías necesarias
# from telegram.ext import Updater
from telegram.ext import *
from telegram import Update
import logging
from comandos.comandos import *
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

CONST_TOKEN = "***REMOVED***"



def main():
    # Creamos el Updater, objeto que se encargará de mandarnos las peticiones del bot
    # Por supuesto no os olvidéis de cambiar donde pone "TOKEN" por el token que os ha dado BotFather
    updater = Updater(token=CONST_TOKEN, use_context=True)

    # Cogemos el Dispatcher, en el cual registraremos los comandos del bot y su funcionalidad
    dispatcher = updater.dispatcher

    # Registramos el método que hemos definido antes como listener para que muestre la información de cada mensaje
    #listener_handler = MessageHandler(Filters.text, listener)
   # dispatcher.add_handler(listener_handler)

    # Ahora registramos cada método a los comandos necesarios
    
    dispatcher.add_handler(CommandHandler("start", callback=start))
    dispatcher.add_handler(CommandHandler("helloworld", callback=hola_mundo))
    dispatcher.add_handler(CommandHandler("logo", callback=logo))
    dispatcher.add_handler(CommandHandler("caps", callback=caps))


    dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command(False)), listener_mensajes)) #Textos y no comandos (excepto inline)
    
    dispatcher.add_handler(MessageHandler(Filters.command(True), unknown)) # Debe ir detrás de los comandos definidos. (Comandos no reconocidos, incluso inline)
    
    
    # Y comenzamos la ejecución del bot a las peticiones
    updater.start_polling()
    updater.idle()

# Llamamos al método main para ejecutar lo anterior
if __name__ == '__main__':
    main()