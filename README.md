# Despliegue de un modelo Whisper en Azure

## Descripción
Este repositorio explica de forma detallada cómo desplegar un modelo Whisper en Azure y realizar transcripciones de audio utilizando código en Python.

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

Además, puedes consultar la documentación oficial de Microsoft:
- [Despliegue de un modelo Whisper en Azure by Microsoft](https://learn.microsoft.com/es-es/azure/ai-services/openai/how-to/create-resource?pivots=web-portal)

## Ejecución del programa Python
### Comprobaciones y pasos previos
#### Clonación del repositorio
Una vez hayamos desplegado el modelo siguiendo los pasos del video anterior, clonaremos este repositorio en nuestro dispositivo utilizando el siguiente comando:

```bash
git clone https://github.com/SergioFerrerasRuiz/Despliegue-de-un-modelo-Whisper-en-Azure.git
```

#### Creación de un archivo `.env`
Después de haber clonado el repositorio, crearemos un archivo `.env` donde almacenaremos la `Key` y el `Endpoint` de nuestro modelo.

El archivo debe contener el siguiente contenido:

```bash
AZURE_OPENAI_API_KEY="Sustituye esto por tu key"
AZURE_OPENAI_ENDPOINT="Sustituye esto por tu endpoint"
```

### Ejecución del programa
#### Accede al entorno y ejecuta el programa
Por último, accede a la terminal y sitúte en la ruta donde clonaste el repositorio. Luego, utiliza el siguiente comando para acceder al entorno:

```bash
entorno\Scripts\activate
```

Una vez dentro del entorno, escribe el siguiente comando para ejecutar el código de Python. Si todos los pasos se han seguido correctamente, debería funcionar:

```bash
python .\pruebaswishper.py
```

### A tener en cuenta
#### Cambio de ruta
Esta ha sido una pequeña demostración de cómo funciona el programa. En caso de querer usar audios propios, simplemente guarda los audios en tu dispositivo y sustituye la ruta actual del código con la ruta de tu nuevo audio:

```bash
audio_test_file = "./nuevo_audio.mp4"
```

#### Archivos soportados
Los archivos de audio que soporta el modelo Whisper son:

- **MP3**: Popular y comprimido. Ideal por su tamaño reducido.
- **WAV**: Alta calidad sin pérdida (lossless), pero ocupa más espacio.
- **M4A**: Usado en dispositivos Apple y aplicaciones como iTunes.
- **FLAC**: Comprimido sin pérdida, mantiene la calidad original del audio.
- **OGG**: Más comprimido que FLAC, con buena calidad y enfoque en código abierto.

### Alternativas
Este apartado explica cómo hacerlo todo un poco más a fondo en caso de que el entorno no funcione:
#### Creación del entorno
En caso de que el entorno no funcione, tendrás que crear uno nuevo. Para ello, abre la terminal y escribe el siguiente comando:

```bash
python -m venv entorno
```

### Instalación de librerías
Una vez hayamos creado el entorno, ejecuta el siguiente comando para acceder a él:

```bash
entorno\Scripts\activate
```

Dentro del entorno, instala las librerías correspondientes utilizando el siguiente comando:

```bash
pip install openai python-dotenv
```

Una vez realizado esto, ya podrás ejecutar tu programa utilizando el siguiente comando:

```bash
python .\pruebaswishper.py
```

### Posibles fallos
Es posible que el entorno no pueda descargar las librerías porque dice que no existen. Esto puede deberse a dos razones:

1. La versión de Python instalada es antigua.
2. El entorno está corrupto.

Si la versión de Python es antigua, actualízala con el siguiente comando:

```bash
winget upgrade python
```

Si el entorno está corrupto, elimínalo y vuelve a crearlo siguiendo los pasos anteriores.

Si todo ha salido bien, ejecuta el programa y debería funcionar correctamente.

