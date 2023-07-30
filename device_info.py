# on import
# pour la manip des ip v4
from ipaddress import IPv4Address
# Airmore pour la manip de session
from pyairmore.request import AirmoreSession
# service pur gerer l'apareil
from pyairmore.services.device import DeviceService

try:
    ip = IPv4Address("192.168.137.36")
except Exception as e:
    print(e)

# on ouvre une session vers cette ip
session = AirmoreSession(ip)

     
# on ouvre la session vers notre device
service_dvc = DeviceService(session)

# on peux afficher les info de ntre smartphone
# on le selectionne tous d'abord
details = service_dvc.fetch_device_details()
print(f"Votre smartphone est de la marque : {details.brand}")
print(f"Votre energie est à : {details.power} en %")
print(f"Votre model : {details.model}")
print(f"Nom de l'appareil : {details.device_name}")
print(f"Numero du smartphone : {details.phone_number}")
print(f"Code IMEI: {details.imei}")
print(f"Code IMSI : {details.imsi}")
print(f"Adresse MAC: {details.mac_address}")
print(f"Numero de serie : {details.serial_number}")
print(f"Numero de serie de l'appareil : {details.device_serial_number}")
print(f"Resolution de l'appareil : {details.resolution}")
print(f"Rooter, true ou false : {details.is_root}")
print(f"Id de la version du SDK: {details.sdk_version_id}")
print(f"Nom de la version du SDK : {details.sdk_version_name}")
print(f"Plateforme : {details.platform}")
print(f"Code l'app : {details.app_version_code}")
print(f"Non du code de l'app : {details.app_version_name}")
print(f"Etat du wifi : {details.is_wifi_on}")
print(f"Taille de la carte sd : {details.external_sd_total_size}")
print(f"Etat de la carte sd : {details.external_sd_available_size}")
print(f"Taille de la memoire interne: {details.internal_sd_total_size}")
print(f"Etat de la memoire interne : {details.internal_sdv_available_size}")
print(f"Taille total de tous la memoire : {details.memory_total_size}")
print(f"Etat de tout la memoire : {details.memory_available_size}")
print(f"Nombre d'historique des appels : {details.call_history_count}")
print(f"Nombre des contacts : {details.contacts_count}")
print(f"Nombre des SMS : {details.messages_count}")
print(f"Nombre des photos : {details.pictures_count}")
print(f"Taille des photos : {details.pictures_total_size}")
print(f"Nombre des musics : {details.songs_count}")
print(f"Taille des musiques : {details.songs_total_size}")
print(f"Nombre des videos : {details.videos_count}")
print(f"Taille des videos : {details.videos_total_size}")
print(f"apjs_total_size : {details.apks_total_size}")
print(f"system_apks_count : {details.system_apks_count}")
print(f"user_apks_count : {details.user_apks_count}")