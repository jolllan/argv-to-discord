# VARIABLE A DEFINIR :

TOKEN: str = "TOKEN"
            # Token du bot discord

###   -----------------------------------------------------------------------------------   ###
import sys
import discord
from discord.ext import commands


# Gestion des erreur :
import asyncio
import selectors
selector = selectors.SelectSelector()
loop = asyncio.SelectorEventLoop(selector)
asyncio.set_event_loop(loop)

class DevNull:
    def write(self, msg):
        pass


sys.stderr = DevNull()

#-----------------------------------#

#Récupère tout les arguments !
all_argv = sys.argv

#vérification si l'id est bien formaté 
argv_id = int(sys.argv[1])
if len(str(argv_id)) == 18:
    pass
else:
    print("Veuillez bien rentrez l'id du salon en premier argument")
    sys.exit()
    

#enlève le premier élément de liste

# le chemin d'exécution
all_argv.pop(0)
#l' id du channel
all_argv.pop(0)

#Convertir la liste en string
all_argv_str = ' '.join(all_argv)


# Définition des intents
intents = discord.Intents.default()
intents.members = True
intents.guilds = True
intents.messages = True
intents.guild_messages = False

# Lancement de l'instance
client = commands.Bot(intents=intents)

@client.event
async def on_ready():
    # Savoir si le bot a accès au channel
    channel = client.get_channel(argv_id)
    if channel is not None:
        await channel.send(all_argv_str)
    else:
        print("Le bot n'a pas accès au canal spécifié")
    #await client.close()
    sys.exit()

client.run(TOKEN)