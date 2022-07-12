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
coordenadas = subprocess.Popen("curl ipinfo.io/loc", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]

characters = "'\Labcdefghijklmnopqrstubwxyz "
for x in range(len(characters)):
    coordenadas = str(coordenadas).replace(characters[x],"")
coordenadas = coordenadas[8:] +","+ coordenadas[:7]
print(coordenadas)

# Escribir el archivo
f = open ('index.html','w')
f.write('<!DOCTYPE html>   \n' )
f.write('<head>  \n' )
f.write('<meta charset="UTF-8" />  \n' )
f.write('<meta name="viewport" content="width=device-width, initial-scale=1.0" />  \n' )
f.write('<title> Ubicacion de camara</title>  \n' )
f.write('<script src=\'https://api.mapbox.com/mapbox-gl-js/v2.9.1/mapbox-gl.js\'></script>   \n' )
f.write('<link href=\'https://api.mapbox.com/mapbox-gl-js/v2.9.1/mapbox-gl.css\' rel="stylesheet" />   \n' )
f.write('</head>   \n' )
f.write('<div id=\'map\' style=\'width: 100vw; height: 100vh;\'></div>   \n' )
f.write('<script>  \n' )
f.write('mapboxgl.accessToken = \'pk.eyJ1IjoibGlua2VyYiIsImEiOiJjbDVlbXhvenMxMzVyM2NtcDhicGUwY3U1In0.ks_OTnhUiLxDW1rKI8RTmg\';  \n' )
f.write('const map = new mapboxgl.Map({  \n' )
f.write('container: \'map\',  \n' )
f.write('style: \'mapbox://styles/mapbox/streets-v11\',  \n' )
f.write('center: [-89.1872,13.6893],  \n' )
f.write('zoom: 12  \n' )
f.write('});  \n' )
f.write('map.on(\'load\', () => {   \n' )
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
f.write('\'coordinates\':'+" ["+str(coordenadas)+"]"+'\n')
f.write('}\n')
f.write('}\n')
f.write(']\n')
f.write('}\n')
f.write('});\n')
f.write('map.addLayer({ \n' )
f.write('\'id\': \'places\', \n' )
f.write('\'type\': \'symbol\', \n' )
f.write('\'source\': \'places\', \n' )
f.write('\'layout\': { \n' )
f.write('\'icon-image\': \'{icon}\', \n' )
f.write('\'icon-size\': 2.5, \n' )
f.write('\'icon-allow-overlap\': true  \n' )
f.write('}\n')
f.write('});\n')
f.write('map.on(\'click\', \'places\', (e) => {')
f.write('const coordinates = e.features[0].geometry.coordinates.slice();\n')
f.write('const description = e.features[0].properties.description;\n')
f.write('while (Math.abs(e.lngLat.lng - coordinates[0]) > 180) { \n')
f.write('coordinates[0] += e.lngLat.lng > coordinates[0] ? 360 : -360;\n')
f.write('}\n')
f.write('new mapboxgl.Popup()\n')
f.write('.setLngLat(coordinates)')
f.write('.setHTML(description)\n')
f.write('.addTo(map);\n')
f.write('});\n')
f.write('map.on(\'mouseenter\', \'places\', () => {\n')
f.write('map.getCanvas().style.cursor = \'pointer\';\n')
f.write('});\n')
f.write('map.on(\'mouseleave\', \'places\', () => {\n')
f.write('map.getCanvas().style.cursor = \'\';\n')
f.write('});\n')
f.write('});\n')
f.write('</script>\n')
f.write('</body>\n')
f.close()
print("se a modificado el archivo addsource.js")
os.system("cp /app/index.html /var/www/html/index.html")
os.system("/etc/init.d/apache2 restart")
# -----------------------------------






while True:
  time.sleep(1)
  mqttc.publish("ngrok_test",ip_address)                  # Publishing the created URL to "ngrok_test" Topic 
  mqttc.loop(2)
  time.sleep(120)                                         # send mqtt message every 2 minutes