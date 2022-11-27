# from time import *
from telegram import Update
from telegram.ext import (
    CallbackContext
    , CommandHandler)
from oscoderBot import (globalValue)

from parsers.healthParser import *
from parsers.profileParser import *

#
# update.message.text mensaje que recibe el 
#
#
#
#

# Método que imprimirá por pantalla la información que reciba
def listener_mensajes(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

# Método que utilizaremos para cuando se mande el comando de "start"
def start(update: Update, context: CallbackContext):
    context.bot.sendMessage(chat_id=update.effective_chat.id, text='¡Bienvenido al bot personalizado de Oscoder!')





# ---------------------------------------------------------
# Método que mandará el mensaje "¡Hola, lector de Bytelix!"
def about(update: Update, context: CallbackContext):
    context.bot.sendMessage(chat_id=update.effective_chat.id, text='¡TEXTO DE ABOUT!')

# Método que mandará el logo de la página
def help(update: Update, context: CallbackContext):
    # Enviamos de vuelta una foto. Primero indicamos el ID del chat a donde
    # enviarla y después llamamos al método open() indicando la dónde se encuentra
    # el archivo y la forma en que queremos abrirlo (rb = read binary)
    context.bot.sendMessage(chat_id=update.effective_chat.id, text='¡TEXTO DE AYUDA!')
    # bot.sendPhoto(chat_id=update.message.chat_id, photo=open('Icono.png', 'rb'))

def caps(update: Update, context: CallbackContext):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


#Fallback -> si pasan comandos no conocidos
def unknown(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="No he reconocido el comando.")

def loadHandlers(updater):

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", callback=start))
    dispatcher.add_handler(CommandHandler("about", callback=about))
    dispatcher.add_handler(CommandHandler("help", callback=help))
    # dispatcher.add_handler(CommandHandler("caps", callback=caps))
    dispatcher.add_handler(CommandHandler("perfiles", callback=perfiles))
    dispatcher.add_handler(CommandHandler("nuevo", callback=profileAdd))

    dispatcher.add_handler(CommandHandler("salud", callback=salud))
    dispatcher.add_handler(CommandHandler("herir", callback=herir))
    dispatcher.add_handler(CommandHandler("curar", callback=curar))
    

    # Guardas se añaden fuera
    return dispatcher
