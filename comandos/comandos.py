from telegram import Update
from telegram.ext import (
    CallbackContext
    , CommandHandler)

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

def loadHandlers(updater):

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", callback=start))
    dispatcher.add_handler(CommandHandler("helloworld", callback=hola_mundo))
    dispatcher.add_handler(CommandHandler("logo", callback=logo))
    dispatcher.add_handler(CommandHandler("caps", callback=caps))



    # Guardas se añaden fuera
    return dispatcher
