# on import
# pour la manip des ip v4
from ipaddress import IPv4Address
# Airmore pour la manip de session
from pyairmore.request import AirmoreSession

# Airmore pour la manip du service message
from pyairmore.services.messaging import MessagingService

try:
    ip = IPv4Address("192.168.0.100")
except Exception as e:
    print(e)

# on ouvre une session vers cette ip
session = AirmoreSession(ip)

# on se connecte au service message
service_msg = MessagingService(session)

# on envoie un sms
number = "0975036272"
message = "Message envoyer depuis un script python"

try:
    service_msg.send_message(number, message)
    print("Message envoyer avec succès")
except Exception as e:
    print(e)