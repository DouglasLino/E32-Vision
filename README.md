<p align="center">
  <img src="https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fk68EIVrPdLCVPu4257mG%2Fuploads%2Fp7VuXDdA1Ua04wq6q6iE%2Fproyectofinal.gif?alt=media&token=fc0bed23-3c4a-4a0a-96dc-2cb3e9b76131" width="500" title="e32-vision">
    <br/>
    <span>
      <img alt="" src="https://img.shields.io/github/license/DouglasLino/E32-Vision">
    </span>
</p>




# Tecnologías
- [Arduino](https://www.arduino.cc/ "Arduino"): Las tecnologías a usar sería primeramente la parte de Arduino ,siendo la parte principal.
- [Arduino-cli](https://www.arduino.cc/pro/cli "Arduino-cli"): Herramienta de línea de comandos que contiene todo lo necesario para el ecosistema Arduino, con la finalidad de instalar automaticamente el codigo al ESP32-CAM
- C++: El lenguaje de programación sería C++ que es el por defecto de arduino
- [Ngrok](https://ngrok.com/ "Ngrok"): Una herramienta de proxy inverso que abre diferentes túneles “seguros” generando una URL pública a un host local el cual cuenta con su propia librería pyngrok.
- JavaScript: El lenguaje utilizado para renderizar el mapa con la ubicacion de la camara
- Python: para elaborar una mini aplicación que obtenga la dirección IP y un token para exponerlo al internet mediante un broker.
- [mosquitto](https://test.mosquitto.org/ "mosquitto"): Es un servidor web que aloja un “broker” que funciona con el protocolo MQTT que es utilizado para la publicación/suscripción de mensajes.
- Librerías:
	- Librería de la cámara [OV2640](https://github.com/espressif/esp32-camera "OV2640")
	- Librería [WiFi](https://www.arduino.cc/reference/en/libraries/wifi/ "WiFi")
	- Libreria [WebServer](https://www.arduino.cc/reference/en/libraries/wifi/ "WebServer") para el servidor web
	- Librería [WiFiClient](https://www.arduino.cc/reference/en/libraries/wifi/ "WiFiClient") para el cliente
  - Mapbox[MapProvider](https://www.mapbox.com/) Proveedor de mapas en linea para mostrar la ubicacion de la camara
	- [pyngrok](https://pypi.org/project/pyngrok/ "pyngrok") para un mejor manejo de la herramienta ngrok
	- [paho-mqtt](https://pypi.org/project/paho-mqtt/ "paho-mqtt"): proporciona un cliente para mosquitto.


# Documentación
Toda la documentación relacionada al proyecto la puedes encontrar [aqui](https://00018318.gitbook.io/e32-vision/ "aqui"):

<p align="center">
      <a href="https://00018318.gitbook.io/e32-vision/" target="_blank"><img src="https://www.freelogovectors.net/svg10/gitbook_logo-freelogovectors.net_.svg" width="500" alt="e32-vision" /></a>
</p>
