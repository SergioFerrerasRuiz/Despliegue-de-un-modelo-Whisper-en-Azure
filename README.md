# Despliegue de un modelo Whisper en Azure

## Descripción
En este repositorio se explica de forma detallada cómo desplegar un modelo Whisper en Azure y realizar transcripciones de audio utilizando código en Python.

## Contenido del repositorio

1. **Guía de despliegue:**
   - Instrucciones paso a paso para configurar y desplegar el modelo Whisper en Azure.
   - Configuración del entorno y de los servicios necesarios.

2. **Transcripción de audio:**
   - Código de ejemplo en Python para realizar transcripciones de audio.
   - Ejemplos de entrada y salida del modelo.

## Requisitos previos

- Una cuenta activa de Azure.
- Instalación de las siguientes herramientas:
  - Azure CLI
  - Python 3.8 o superior

## Despliegue del modelo Whisper en Azure

En el siguiente video se explica de manera simple y concisa cómo se realiza el despliegue de un modelo Whisper en Azure:

[![Despliegue de un modelo Whisper en Azure](https://img.youtube.com/vi/fYBEPDGDJyQ/hqdefault.jpg)](https://www.youtube.com/watch?v=fYBEPDGDJyQ)


Tambien, podeis mirar la documentacion oficial de Microsoft:
- [Despliegue de un modelo Whisper en Azure by Microsoft]( https://learn.microsoft.com/es-es/azure/ai-services/openai/how-to/create-resource?pivots=web-portal)



## Ejecucion del programa pyhton:
### Comprobaciones y pasos previos
#### Clonacion del repositorio:
Una vez hallamos desplegado el modelo siguiendo los pasos del video anterior, clonaremos este repositorio en nuestro dispositivo. usando el siguiente comando

```bash
git clone https://github.com/SergioFerrerasRuiz/Despliegue-de-un-modelo-Whisper-en-Azure.git
```
#### Creacion de un archivo ``.env``
Despues de haber clonado el repositorio, crearemos un archivo env, donde almacenaremos la ``Key`` y el ``Endpoint`` de nuestro modelo.

Dentro de nuestro archivo, deberemos de tener el siguiente contenido:
```bash 
AZURE_OPENAI_API_KEY="Sustituye esto por tu key"
AZURE_OPENAI_ENDPOINT="Sustituye esto por tu endpoint"
```
### Ejecucion del programa
#### Accede al entorno y ejecuta el programa
Por ultimo debes de acceder a la terminal y situarte en la ruta donde clonaste el repositorio.
Despues usaras el siguiente comando para acceder al entorno:
```bash 
entorno\Scripts\activate
```

Una vez estemos dentro del entorno, escribiremos el siguiente comando para ejecutar el codigo de python y si todos los pasos se han seguido correctamente, deberia de funcionar.
```bash 
python .\pruebaswishper.py
```

### A tener en cuenta
#### Cambio de ruta
Esto ha sido una pequeña demostracion de como funciona el programa, en caso de querer usar audios propios es tan facil como guardar los audios en nuestro dispositivo y sustituir la ruta actual del codigo con la ruta de nuestro nuevo audio:
```bash 
audio_test_file = "./nuevo_audio.mp4"
```
#### Archivos que soporta 
Los archivos de audio que soporta el modelo Whisper son:

- **MP3**: Popular y comprimido. Ideal por su tamaño reducido.
- **WAV**: Alta calidad sin pérdida (lossless), pero ocupa más espacio.
- **M4A**: Usado en dispositivos Apple y aplicaciones como iTunes.
- **FLAC**: Comprimido sin pérdida, mantiene la calidad original del audio.
- **OGG**: Más comprimido que FLAC, con buena calidad y enfoque en código abierto.


### Alternativas
Este apartado esplica como hacerlo todo un poco mas a fondo por si no funcionara el entorno:
#### Creacion del entorno:
En caso de que el entorno no funcione, tendremos que crear uno nuevo, para ello abriremos la terminal y escribiremos el comando:
```bash 
python -m venv entorno
```
### Instalacion de librerias
Una vez hallamos creado el entorno, ejecutaremos el comando para acceder a el:
```bash 
entorno\Scripts\activate
```
Una vez dentro de el, instalaremos las librerias correspondientes con el comando:
```bash 
pip install openai python-dotenv                                                            
```
Una vez realizado esto, ya podremos ejecutar nuestro programa usando el comando:
```bash 
python .\pruebaswishper.py
```
### Posibles fallos
Es posible que el entorno no pueda descragar las librerias porque dice que no existen, eso puede ser por dos cosas:
1. La version de Python que tenemos instalada es antigua.
2. Se ha rayado el entorno.
Si la version que tenemos es antigua, tendremos que actualizarla, para ello ponemos el comando:
```bash 
winget upgrade python
```
Y si se ha rayado el entorno, borraremos el entorno con el comando:

y volveremos a crearlo siguiendo los pasos anterirores.

Si todo ha salid bien, ejecutaremos el programa y funcionara correctamente.
