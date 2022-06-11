# Codigo base en: https://github.com/elementzonline/RaspberryPi-Sample-Codes/blob/master/ngrok_mqtt.py
import os
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

while True:
  time.sleep(1)
  mqttc.publish("ngrok_test",ip_address)                  # Publishing the created URL to "ngrok_test" Topic 
  mqttc.loop(2)
  time.sleep(120)                                         # send mqtt message every 2 minutes