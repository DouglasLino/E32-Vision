# Codigo base en: https://github.com/elementzonline/RaspberryPi-Sample-Codes/blob/master/ngrok_mqtt.py
import os
import subprocess

ip_address = os.environ['IP_ADDRESS']
ngrok_token = os.environ['TOKEN']
from pyngrok import ngrok
import paho.mqtt.client as mqtt
import time
mqttc=mqtt.Client()
mqttc.connect("test.mosquitto.org", 1883, 60)             # Mqtt broker
ngrok.set_auth_token(ngrok_token)                         # Enter the registered Auth_Token
public_url = ngrok.connect(ip_address)                    # tunnel to host:port instead of localhost

print(public_url)                                         # Displaying the ngrok_tunnel url 

# obteniendo solo el URL de gnrok
onlyUrl = str(public_url).split()[1]

#------------------------------------- Modificacion del archivo -------------------------------------
localizacion = subprocess.Popen("./whereami", stdout=subprocess.PIPE)
coordenadas = localizacion.stdout.read()
# str(coordenadas)
# print(coordenadas)


characters = "'\LAT:()abcdefghijklmnopqrstubwxyz "
for x in range(len(characters)):
    coordenadas = str(coordenadas).replace(characters[x],"")

size = len(coordenadas)
mod_string = coordenadas[:size - 27]
coordenada_exacta = mod_string[:9] + "," + mod_string[9:]
print(coordenada_exacta)
print("se a modificado el archivo addsource.js")

# Escribir el archivo
f = open ('addsource.js','w')
f.write('map.addSource(\'places\', { \n')
f.write('\'type\': \'geojson\', \n')
f.write('\'data\': { \n')
f.write('\'type\': \'FeatureCollection\',\n')
f.write('\'features\': [\n')
f.write('{\n')
f.write('\'type\': \'Feature\',\n')
f.write('\'properties\': {\n')
f.write('\'description\':\n')
f.write('\'<strong>ATENCION</strong><p>Su camara se encuentra en esta posicion</p><a href='+onlyUrl + ' target="_newblank"> Link </a>\',\n')
f.write('\'icon\': \'attraction-15\',\n')
f.write('},\n')
f.write('\'geometry\': {\n')
f.write('\'type\': \'Point\',\n')
f.write('\'coordinates\':'+" ["+coordenada_exacta+"]"+'\n')
f.write('}\n')
f.write('}\n')
f.write(']\n')
f.write('}\n')
f.write('});\n')

f.close()

# -----------------------------------






while True:
  time.sleep(1)
  mqttc.publish("ngrok_test",ip_address)                  # Publishing the created URL to "ngrok_test" Topic 
  mqttc.loop(2)
  time.sleep(120)                                         # send mqtt message every 2 minutes