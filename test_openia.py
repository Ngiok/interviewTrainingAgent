import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("No se encontró OPENAI_API_KEY en el .env")
    exit(1)

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": ""},
        {"role": "user", "content": ""}
    ]
)

print("Respuesta recibida:\n")
#print(response.choices[0].message.content)
print("Respuestas: ", response)
