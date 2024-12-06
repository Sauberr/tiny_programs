import openai
import requests
import json

function_signature = {
    "name": "get_cryptocurrency_current_price",
    "description": "Get current price of cryptocurrency",
    "parameters": {
        "type": "object",
        "properties": {
            "currency": {
                "type": "string",
                "description": "Cryptocurrency name starting with lowercase letter",
            },
        },
        "required": ["currency"]
    }
}


def get_cryptocurrency_current_price(currency: str) -> float:

    response = requests.get(
        f'https://api.coingecko.com/api/v3/simple/price?ids={currency}&vs_currencies=usd'
    )

    result = str(response.json().get(currency, {}).get('usd', 0)) + '$'

    return result


functions = {
    'get_cryptocurrency_current_price': get_cryptocurrency_current_price,
}


client = openai.Client()

messages = [
    {
        'role': 'user',
        'content': 'What is the price of Bitcoin?',
    },
]

response = client.chat.completions.create(
    messages=messages,
    model='gpt-3.5-turbo',
    functions=[function_signature],
)

function_call = response.choices[0].message.function_call
messages.append({
    'role': 'assistant',
    'content': None,
    'function_call': function_call,
})


if function_call:
    function_name = function_call.name
    kwargs = json.loads(function_call.arguments)
    functions = functions.get(function_name)
    result = functions(**kwargs)
    print(result)
    messages.append({
        'role': 'function',
        'name': function_name,
        'content': str(result),
    })

    new_response = openai.chat.completions.create(
        messages=messages,
        model='gpt-3.5-turbo',
        functions=[
            function_signature
        ],
    )

    print(new_response.choices[0].message.content)
