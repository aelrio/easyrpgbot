from telegram import Update
from telegram.ext import (
    CallbackContext
    , CommandHandler)
from util import *

PATH="data/health.txt"

class HealthObject:

    def __init__(self, LISTA):
        self.profile = str(LISTA[0]).upper()
        self.maxhealth = int(LISTA[1])
        self.health = int(LISTA[2])

    def __str__(self):
        return self.profile + ": " + str(self.health) + "/" + str(self.maxhealth)

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
    return "\n".join([str(i) for i in LISTA])


# RPG - Método para leer la salud de los perfiles
def salud(update: Update, context: CallbackContext):
    if len(context.args) > 20:
        context.bot.sendMessage(chat_id=update.effective_chat.id, text="NO SOPORTADO 20+ ARGUMENTOS")
    elif len(context.args) > 0:
        context.bot.sendMessage(chat_id=update.effective_chat.id, text=healthListMessage([ HEALTHLIST[i] if i in HEALTHLIST.keys() else "*NO-ENCONTRADO*" for i in [x.upper() for x in context.args] ] ))
    else: # LISTAR TODOS
        context.bot.sendMessage(chat_id=update.effective_chat.id, text=healthListMessage(HEALTHLIST.values()))

    

# RPG - Método para restar salud a un perfil
def herir(update: Update, context: CallbackContext):
    # TODO GESTION DEL ERROR SI PASAN ALGO DISTINTO A UN NUMERO?
    valor = gestionarEntrada(context.args[1])

    if len(context.args) < 2:
        context.bot.sendMessage(chat_id=update.effective_chat.id, text="NO SOPORTADO SIN 2 ARGUMENTOS")
    else:
        HEALTHLIST[context.args[0].upper()].health -= int(valor)
        context.bot.sendMessage(chat_id=update.effective_chat.id
        , text=HEALTHLIST[context.args[0].upper()].profile+" recibe "+valor+" heridas.")

# RPG - Método para agnadir salud a un perfil
def curar(update: Update, context: CallbackContext):

    if len(context.args) < 2:
        context.bot.sendMessage(chat_id=update.effective_chat.id, text="NO SOPORTADO SIN 2 ARGUMENTOS")
    else:
        valor = gestionarEntrada(context.args[1])

        HEALTHLIST[context.args[0].upper()].health += int(valor)
        context.bot.sendMessage(chat_id=update.effective_chat.id, text=HEALTHLIST[context.args[0].upper()].profile+" es curado "+valor+" puntos.")

def setMaxHealth(update: Update, context: CallbackContext):

    HEALTHLIST[context.args[0].upper()].maxhealth = int(context.args[1])
    context.bot.sendMessage(chat_id="La salud máxima de "+HEALTHLIST[context.args[0].upper()].profile+" es: "+HEALTHLIST[context.args[0].upper()].maxhealth)

# --------------------------------
def gestionarEntrada(texto):
    if (isDiceText(texto)):
        res = solveDice(texto)
    else:
        res = texto