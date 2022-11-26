from time import CLOCK_THREAD_CPUTIME_ID
from telegram import Update
from telegram.ext import (
    CallbackContext
    , CommandHandler)

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

# RPG - Método para agnadir un perfil
def profileAdd(update: Update, context: CallbackContext):
    try:
        # Logica de creacion/guardado

        # mensaje OK
        context.bot.sendMessage(chat_id=update.effective_chat.id, text="Personaje creado: " + context.args[0].upper())
    except Exception as e:
      # mensaje noOK
        print(e)
        context.bot.sendMessage(chat_id=update.effective_chat.id, text="No se ha podido crear el personaje")

# RPG - Método para agnadir un perfil
def salud(update: Update, context: CallbackContext):
    context.bot.sendMessage(chat_id=update.effective_chat.id, text='¡TEXTO DE SALUD!')

# RPG - Método para restar salud a un perfil
def herir(update: Update, context: CallbackContext):
    context.bot.sendMessage(chat_id=update.effective_chat.id, text='¡TEXTO DE HERIR!')

# RPG - Método para agnadir salud a un perfil
def curar(update: Update, context: CallbackContext):
    context.bot.sendMessage(chat_id=update.effective_chat.id, text='¡TEXTO DE CURAR!')
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
    dispatcher.add_handler(CommandHandler("profile", callback=profileAdd))
    dispatcher.add_handler(CommandHandler("salud", callback=salud))
    dispatcher.add_handler(CommandHandler("herir", callback=herir))
    dispatcher.add_handler(CommandHandler("curar", callback=curar))

    # Guardas se añaden fuera
    return dispatcher
