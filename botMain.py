# Importamos las librerías necesarias
#from telegram.ext import Updater
from telegram.ext import *
from telegram import Update
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

CONST_TOKEN = "***REMOVED***"

# Método que imprimirá por pantalla la información que reciba
def listener_mensajes(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

# Método que utilizaremos para cuando se mande el comando de "start"
def start(update: Update, context: CallbackContext):
    context.bot.sendMessage(chat_id=update.effective_chat.id, text='¡Bienvenido al bot personalizado de Oscoder!')

# Método que mandará el mensaje "¡Hola, lector de Bytelix!"
def hola_mundo(update: Update, context: CallbackContext):
    context.bot.sendMessage(chat_id=update.effective_chat.id, text='¡Hola, Mundo!')

# Método que mandará el logo de la página
def logo(bot, update):
    # Enviamos de vuelta una foto. Primero indicamos el ID del chat a donde
    # enviarla y después llamamos al método open() indicando la dónde se encuentra
    # el archivo y la forma en que queremos abrirlo (rb = read binary)
    bot.sendPhoto(chat_id=update.message.chat_id, photo=open('Icono.png', 'rb'))

def caps(update: Update, context: CallbackContext):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


#Fallback -> si pasan comandos no conocidos
def unknown(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="No he reconocido el comando.")


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