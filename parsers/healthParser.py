from telegram import Update
from telegram.ext import (
    CallbackContext
    , CommandHandler)
from util import *
from persistence.cacheHolder import getCache

CACHE=getCache()


class HealthObject:

    def __init__(self, LISTA):
        self.profile = str(LISTA[0]).upper()
        self.maxhealth = int(LISTA[1])
        self.health = int(LISTA[2])

    def __str__(self):
        return self.profile + ": " + str(self.health) + "/" + str(self.maxhealth)

    def __repr__(self):
        return self.profile
    
    

def loadHealth(chatId):
    global CACHE
    CACHE[chatId] = RpgCache()

    HLIST = None
    try:
        archivo = open(healthPath(chatId),'r')
        
        # print(archivo)
        HLIST = parsearlineas(archivo)
        print("HEALTH LEIDO")
        archivo.close()
        CACHE[chatId].healthList = HLIST
        CACHE[chatId].profiles = HLIST.keys()
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

def persist(chatId):
    # abrir archivo
    try:
        #archivo = open(healthPath(chatId),'w')
        
        # print(archivo)
        #for item in HEALTHLIST:
            
         #   archivo.write(str(item))
        
        #archivo.close()
        print("UPDATED HEALTH")
        
    except FileNotFoundError:
        print("FILENOTFOUNDERROR")
    except OSError as err:
        print(err)
        #archivo.close()
    except Exception as e:
        print(e)
        #archivo.close()



def healthListMessage(LISTA):
    return "\n".join([str(i) for i in LISTA])


# RPG - Método para leer la salud de los perfiles
def salud(update: Update, context: CallbackContext):
    global CACHE
    hl = CACHE[update.effective_chat.id].healthList
    
    if len(context.args) > 20:
        context.bot.sendMessage(chat_id=update.effective_chat.id, text="NO SOPORTADO 20+ ARGUMENTOS")
    elif len(context.args) > 0:
        context.bot.sendMessage(chat_id=update.effective_chat.id, text=healthListMessage([ hl[i] if i in hl.keys() else "*NO-ENCONTRADO*" for i in [x.upper() for x in context.args] ] ))
    else: # LISTAR TODOS
        context.bot.sendMessage(chat_id=update.effective_chat.id, text=healthListMessage(hl.values()))

    

# RPG - Método para restar salud a un perfil
def herir(update: Update, context: CallbackContext):
    global CACHE
    hl = CACHE[update.effective_chat.id].healthList

    # TODO GESTION DEL ERROR SI PASAN ALGO DISTINTO A UN NUMERO?
    valor = gestionarEntrada(context.args[1])

    if len(context.args) < 2:
        context.bot.sendMessage(chat_id=update.effective_chat.id, text="NO SOPORTADO SIN 2 ARGUMENTOS")
    else:
        hl[context.args[0].upper()].health -= int(valor)
        context.bot.sendMessage(chat_id=update.effective_chat.id
        , text=hl[context.args[0].upper()].profile+" recibe "+valor+" heridas.")
    if (hl[context.args[0].upper()].health <= 0):
        context.bot.sendMessage(chat_id=update.effective_chat.id
        , text=hl[context.args[0].upper()].profile + " no tiene buen aspecto.")

# RPG - Método para agnadir salud a un perfil
def curar(update: Update, context: CallbackContext):
    global CACHE
    hl = CACHE[update.effective_chat.id].healthList

    if len(context.args) < 2:
        context.bot.sendMessage(chat_id=update.effective_chat.id, text="NO SOPORTADO SIN 2 ARGUMENTOS")
    else:
        valor = gestionarEntrada(context.args[1])

        hl[context.args[0].upper()].health += int(valor)
        context.bot.sendMessage(chat_id=update.effective_chat.id, text=hl[context.args[0].upper()].profile+" es curado "+valor+" puntos.")

def setMaxHealth(update: Update, context: CallbackContext):
    global CACHE
    hl = CACHE[update.effective_chat.id].healthList

    hl[context.args[0].upper()].maxhealth = int(context.args[1])
    context.bot.sendMessage(chat_id="La salud máxima de "+hl[context.args[0].upper()].profile+" es: "+hl[context.args[0].upper()].maxhealth)

# --------------------------------
def gestionarEntrada(texto):
    if (isDiceText(texto)):
        return solveDice(texto)
    else:
        return texto

def healthPath(chatId):
    return "data/"+ str(chatId) +"/health.txt"