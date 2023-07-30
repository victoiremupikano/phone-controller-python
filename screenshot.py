# on import
# pour la manip des ip v4
from ipaddress import IPv4Address
# Airmore pour la manip de session
from pyairmore.request import AirmoreSession
# service pur gerer l'apareil
from pyairmore.services.device import DeviceService

try:
    ip = IPv4Address("192.168.43.63")
except Exception as e:
    print(e)

# on ouvre une session vers cette ip
session = AirmoreSession(ip)

     
# on ouvre la session vers notre device
service_dvc = DeviceService(session)

# on peux afficher les info de ntre smartphone
# on prend une capture d'ecran
image = service_dvc.take_screenshot()
image.show()