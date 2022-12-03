from telegram import Update
from telegram.ext import (
    CallbackContext
    , CommandHandler)

CACHE=dict()


def getCache():
    return CACHE

def saveCache(update: Update, context: CallbackContext):
    chatId = update.effective_chat.id
    HEALTHPATH="data/"+ str(chatId) + "/health.txt"
    PROFILESPATH="data/"+ str(chatId) + "/profiles.txt"

    with (open(HEALTHPATH,'w')) as archivo:
        [archivo.write(healthItem.savestring()+ "\n") for healthItem in CACHE[chatId].healthList.values() ]
            

    with (open(PROFILESPATH,'w')) as archivo:
        [archivo.write(profile + "\n") for profile in CACHE[chatId].healthList.keys() ]
    
