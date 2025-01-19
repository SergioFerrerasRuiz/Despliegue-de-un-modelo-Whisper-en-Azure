import os
from dotenv import load_dotenv
from openai import AzureOpenAI

# Cargar las variables de entorno del archivo .env
load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
    api_version="2024-02-01",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

deployment_id = "WhisperTest"  # Este es el nombre personalizado de tu despliegue.
audio_test_file = "./prueba.ogg"

result = client.audio.transcriptions.create(
    file=open(audio_test_file, "rb"),            
    model=deployment_id,
    language="es"
)

print("El texto transcrito es: "+str(result.text))

