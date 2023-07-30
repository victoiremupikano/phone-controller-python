# on import
# pour la manip des ip v4
from ipaddress import IPv4Address
# Airmore pour la manip de session
from pyairmore.request import AirmoreSession

# Airmore pour la manip du service message
from pyairmore.services.messaging import MessagingService

try:
    ip = IPv4Address("192.168.43.63")
except Exception as e:
    print(e)

# on ouvre une session vers cette ip
session = AirmoreSession(ip)

# on se connecte au service message
service_msg = MessagingService(session)

# recuperation des sms
messages = service_msg.fetch_message_history()
for msg in messages:
    print(f"L'id : {msg.id}")
    print(f"Nom du corresponant : {msg.name}")
    print(f"Numero du corresponant : {msg.phone}")
    print(f"Message : {msg.content}")
    print(f"Date et heure : {msg.datetime}")
    print(f"Type, (recu, envoyer,...) : {msg.type}")
    print(f"Etat de la lecture : {msg.was_read}")
    print(f"Nombre : {msg.count}")

print("Debut du code de chat")
# reuperation d'un chat
message = messages[0]
chats = service_msg.fetch_chat_history(message)
taille = len(chats)
for chat in chats:
    print(f"La taille du chat :{taille}")
    print(f"L'id : {chat.id}")
    print(f"Nom du corresponant : {chat.name}")
    print(f"Numero du corresponant : {chat.phone}")
    print(f"Message : {chat.content}")
    print(f"Date et heure : {chat.datetime}")