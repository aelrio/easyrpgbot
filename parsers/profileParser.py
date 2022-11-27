from telegram import Update
from telegram.ext import (
    CallbackContext
    , CommandHandler)

PATH="data/profiles.txt"
# RPG - Método para agnadir un perfil
def profileAdd(update: Update, context: CallbackContext):
    try:
        # Logica de creacion/guardado
        # TODO AGNADIR A LOS ARCHIVOS
 
        # TODO MERGEAR INFORMACION EN MEMORIA
        # TODO CARGAR INFORMACION A LA MEMORIA

        # mensaje OK
        context.bot.sendMessage(chat_id=update.effective_chat.id, text="Personaje creado: " + context.args[0].upper())
    except Exception as e:
      # mensaje noOK
        print(e)
        context.bot.sendMessage(chat_id=update.effective_chat.id, text="No se ha podido crear el personaje")

# RPG - Método para devolver los perfiles anotados
def perfiles(update: Update, context: CallbackContext):
    context.bot.sendMessage(chat_id=update.effective_chat.id, text="Personajes:\n" + readPerfiles())



def readPerfiles():
    with open(PATH, 'r') as archivo:
        lineas = archivo.readlines()
    
    if len(lineas) > 0:
        return "".join(lineas).upper()
    else:
        return "No hay personajes declarados"