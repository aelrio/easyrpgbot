from mailbox import NoSuchMailboxError
from posixpath import split
from telegram import Update
from telegram.ext import (
    CallbackContext
    , CommandHandler)

PATH="data\health.txt"

class HealthObject:

    def __init__(self, LISTA):
        self.profile = str(LISTA[0]).upper()
        self.maxhealth = int(LISTA[1])
        self.health = int(LISTA[2])

    def __str__(self):
        return ":".join([self.profile, str(self.maxhealth), str(self.health)])

    def __repr__(self):
        return self.profile
    
    

def load():
    HLIST = None
    try:
        archivo = open(PATH,'r')
        
        # print(archivo)
        HLIST = parsearlineas(archivo)
        print("HEALTH LEIDO")
        archivo.close()
        return HLIST
    except FileNotFoundError:
        print("FILENOTFOUNDERROR")
    except OSError as err:
        print(err)
        archivo.close()
    except Exception as e:
        print(e)
        archivo.close()
    
def parsearlineas(arch):
    # print(arch.readlines()) # Esta se imprime bien
    L = {}
    for ite in arch.readlines():
        o = HealthObject(ite.split(':'))
        L[o.profile] = o
    
    return L

def persist():
    # abrir archivo
    try:
        archivo = open(PATH,'w')
        
        # print(archivo)
        for item in HEALTHLIST:
            
            archivo.write(str(item))
        
        archivo.close()
        print("UPDATED HEALTH")
        
    except FileNotFoundError:
        print("FILENOTFOUNDERROR")
    except OSError as err:
        print(err)
        archivo.close()
    except Exception as e:
        print(e)
        archivo.close()

HEALTHLIST = load()

def healthListMessage(LISTA):
    return "|".join([str(i) for i in LISTA.values()])

# RPG - Método para agnadir un perfil
def salud(update: Update, context: CallbackContext):
    
    context.bot.sendMessage(chat_id=update.effective_chat.id, text=healthListMessage(HEALTHLIST))

    # RPG - Método para restar salud a un perfil
def herir(update: Update, context: CallbackContext):
    # TODO GESTION DEL ERROR SI PASAN ALGO DISTINTO A UN NUMERO?

    HEALTHLIST[context.args[0].upper()].health -= int(context.args[1])
    context.bot.sendMessage(chat_id=update.effective_chat.id
        , text=HEALTHLIST[context.args[0].upper()].profile+" recibe "+context.args[1]+" heridas.")

# RPG - Método para agnadir salud a un perfil
def curar(update: Update, context: CallbackContext):
    

    HEALTHLIST[context.args[0].upper()].health += int(context.args[1])
    context.bot.sendMessage(chat_id=HEALTHLIST[context.args[0].upper()].profile+" es curado "+context.args[1]+" puntos.")

def setMaxHealth(update: Update, context: CallbackContext):

    HEALTHLIST[context.args[0].upper()].maxhealth = int(context.args[1])
    context.bot.sendMessage(chat_id="La salud máxima de "+HEALTHLIST[context.args[0].upper()].profile+" es: "+HEALTHLIST[context.args[0].upper()].maxhealth)
    