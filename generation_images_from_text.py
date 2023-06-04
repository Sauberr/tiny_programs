import openai
import json
from base64 import b64decode
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

prompt = input('The prompt: ')
number = int(input('Number max 4: '))
size = str(input('Size 256x256, 512x512 or 1024x1024 : '))
openai.api_key = OPENAI_API_KEY

response = openai.Image.create(
    prompt=prompt,
    n=number,
    size=size,
    response_format='b64_json',
)
for i in range(number):
    with open('data.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

for i, data in enumerate(response['data']):
    image_data = b64decode(data['b64_json'])
    file_name = f"{prompt}+{i + 1}.png"

    with open(f'{file_name}.png', 'wb') as file:
        file.write(image_data)

